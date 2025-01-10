# db-schema-generator

This tool will make GitHub Copilot more accurately generate SQL code and Database related code via Chat and Inline Chat (Code Autocompletion is not yet using the Copilot Instructions file).

## Overview
The db-schema-generator project is a command-line tool that connects to a MySQL / PostgreSQL / Microsoft SQL Server database, retrieves the schema information, and generates a YAML representation of the database schema. The generated schema is appended to the file `.github/copilot-instructions.md`. 

## Features
- Prompts for database connection details.
- Establishes a secure connection to the Database.
- Retrieves database schema information.
- Converts schema information to YAML format.
- Appends the YAML schema to `.github/copilot-instructions.md`.

## Requirements
You can install the required dependencies by running:

```
pipenv install
```

In MacOS, you may need to install unixodbc to make MS SQL driver work.

```
brew install unixodbc
```

## Usage
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the script using Python:

```
pipenv shell
python src/generate_schema.py
```

4. Follow the prompts to enter your database connection details.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.