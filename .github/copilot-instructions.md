### Application Database

Please consider that the application under development uses a database in MS SQL Server with the schema below.
Leverage this schema when generating any SQL queries, code or answers relative to interaction with the database. 

Respect these rules when doing so:

- Never refer to a table or column that does not appear in the list below. 
- Stick to the available tables and columns only. 
- Do not violate existing table relationships: always respect them. 
- Only use syntax that is available in MS SQL Server

## Database schema in YAML format
```yaml
authors:
  columns:
  - name: author_id
    type: int
  - name: first_name
    type: varchar
  - name: last_name
    type: varchar
  - name: birthdate
    type: date
  relationships: []
books:
  columns:
  - name: book_id
    type: int
  - name: title
    type: varchar
  - name: author_id
    type: int
  - name: genre_id
    type: int
  - name: price
    type: decimal
  - name: publication_date
    type: date
  relationships:
  - from_column: author_id
    to_column: author_id
    to_table: authors
  - from_column: genre_id
    to_column: genre_id
    to_table: genres
customers:
  columns:
  - name: customer_id
    type: int
  - name: first_name
    type: varchar
  - name: last_name
    type: varchar
  - name: email
    type: varchar
  - name: phone
    type: varchar
  - name: address
    type: varchar
  relationships: []
genres:
  columns:
  - name: genre_id
    type: int
  - name: genre_name
    type: varchar
  relationships: []
inventory:
  columns:
  - name: inventory_id
    type: int
  - name: book_id
    type: int
  - name: supplier_id
    type: int
  - name: quantity
    type: int
  relationships:
  - from_column: book_id
    to_column: book_id
    to_table: books
  - from_column: supplier_id
    to_column: supplier_id
    to_table: suppliers
order_items:
  columns:
  - name: order_item_id
    type: int
  - name: order_id
    type: int
  - name: book_id
    type: int
  - name: quantity
    type: int
  - name: price
    type: decimal
  relationships:
  - from_column: book_id
    to_column: book_id
    to_table: books
  - from_column: order_id
    to_column: order_id
    to_table: orders
orders:
  columns:
  - name: order_id
    type: int
  - name: customer_id
    type: int
  - name: order_date
    type: date
  - name: total_amount
    type: decimal
  relationships:
  - from_column: customer_id
    to_column: customer_id
    to_table: customers
suppliers:
  columns:
  - name: supplier_id
    type: int
  - name: supplier_name
    type: varchar
  - name: contact_name
    type: varchar
  - name: contact_email
    type: varchar
  - name: contact_phone
    type: varchar
  relationships: []
```
