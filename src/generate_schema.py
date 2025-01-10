import pyodbc
import psycopg2
import mysql.connector
import yaml
import os

def get_db_connection(db_type, server, database, username, password):
    if db_type == 'mssql':
        connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        return pyodbc.connect(connection_string)
    elif db_type == 'postgresql':
        return psycopg2.connect(host=server, database=database, user=username, password=password)
    elif db_type == 'mysql':
        return mysql.connector.connect(host=server, database=database, user=username, password=password)

def fetch_schema(connection):
    cursor = connection.cursor()
    
    # Fetch columns
    if isinstance(connection, psycopg2.extensions.connection):
        cursor.execute("""
            SELECT 
                TABLE_NAME, COLUMN_NAME, DATA_TYPE 
            FROM 
                INFORMATION_SCHEMA.COLUMNS
            WHERE 
                TABLE_SCHEMA = 'public'
            ORDER BY 
                TABLE_NAME, ORDINAL_POSITION
        """)
    elif isinstance(connection, mysql.connector.connection_cext.CMySQLConnection):
        cursor.execute("""
            SELECT 
                TABLE_NAME, COLUMN_NAME, COLUMN_TYPE
            FROM 
                INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = DATABASE()
            ORDER BY 
                TABLE_NAME, ORDINAL_POSITION
        """)
    else:  # MS SQL Server
        cursor.execute("""
            SELECT 
                TABLE_NAME, COLUMN_NAME, DATA_TYPE 
            FROM 
                INFORMATION_SCHEMA.COLUMNS
            WHERE 
                TABLE_SCHEMA = 'dbo'
            ORDER BY 
                TABLE_NAME, ORDINAL_POSITION
        """)
    
    schema = {}
    for table_name, column_name, data_type in cursor.fetchall():
        if table_name not in schema:
            schema[table_name] = {
                'columns': [],
                'relationships': []
            }
        schema[table_name]['columns'].append({'name': column_name, 'type': data_type})
    
    # Fetch relationships
    if isinstance(connection, psycopg2.extensions.connection):
        cursor.execute("""
            SELECT
                tc.table_name AS from_table,
                kcu.column_name AS from_column,
                ccu.table_name AS to_table,
                ccu.column_name AS to_column
            FROM information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
            JOIN information_schema.constraint_column_usage AS ccu
                ON ccu.constraint_name = tc.constraint_name
                AND ccu.table_schema = tc.table_schema
            WHERE tc.constraint_type = 'FOREIGN KEY'
            AND tc.table_schema = 'public'
        """)
    elif isinstance(connection, mysql.connector.connection_cext.CMySQLConnection):
        cursor.execute("""
            SELECT
                TABLE_NAME AS from_table,
                COLUMN_NAME AS from_column,
                REFERENCED_TABLE_NAME AS to_table,
                REFERENCED_COLUMN_NAME AS to_column
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE REFERENCED_TABLE_NAME IS NOT NULL
            AND TABLE_SCHEMA = DATABASE()
        """)
    else:  # MS SQL
        cursor.execute("""
            SELECT 
                FK.TABLE_NAME AS from_table,
                CU.COLUMN_NAME AS from_column,
                PK.TABLE_NAME AS to_table,
                PT.COLUMN_NAME AS to_column
            FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS RC
            JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS FK 
                ON RC.CONSTRAINT_NAME = FK.CONSTRAINT_NAME
            JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS PK 
                ON RC.UNIQUE_CONSTRAINT_NAME = PK.CONSTRAINT_NAME
            JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE CU 
                ON FK.CONSTRAINT_NAME = CU.CONSTRAINT_NAME
            JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE PT 
                ON PK.CONSTRAINT_NAME = PT.CONSTRAINT_NAME
                AND CU.ORDINAL_POSITION = PT.ORDINAL_POSITION
            WHERE FK.TABLE_SCHEMA = 'dbo'
        """)
    
    for from_table, from_column, to_table, to_column in cursor.fetchall():
        schema[from_table]['relationships'].append({
            'from_column': from_column,
            'to_table': to_table,
            'to_column': to_column
        })
    
    return schema

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        yaml.dump(content, file)

def main():
    db_type = input("Select database type (mssql, postgresql, mysql): ").lower()
    server = input("Enter server host: ")
    database = input("Enter database name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    connection = get_db_connection(db_type, server, database, username, password)
    schema = fetch_schema(connection)
    
    output_file = '.github/copilot-instructions.md'
    if not os.path.exists(output_file):
        with open(output_file, 'w') as file:
            file.write("")

    with open(output_file, 'a') as file:
        db_type_display = {
            'mssql': 'MS SQL Server',
            'postgresql': 'PostgreSQL',
            'mysql': 'MySQL'
        }
        file.write(f'''\n### Application Database

Please consider that the application under development uses a database in {db_type_display[db_type]} with the schema below.
Leverage this schema when generating any SQL queries, code or answers relative to interaction with the database. 

Respect these rules when doing so:

- Never refer to a table or column that does not appear in the list below. 
- Stick to the available tables and columns only. 
- Do not violate existing table relationships: always respect them. 

## Database schema in YAML format\n''')
        
        yaml.dump(schema, file)
    print(f"Schema has been appended to {output_file}")

if __name__ == "__main__":
    main()