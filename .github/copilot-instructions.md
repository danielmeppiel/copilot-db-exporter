
### Application Database

Please consider that the application under development uses a database in PostgreSQL with the schema below.
Leverage this schema when generating any SQL queries, code or answers relative to interaction with the database. 

Respect these rules when doing so:

- Never refer to a table or column that does not appear in the list below. 
- Stick to the available tables and columns only. 
- Do not violate existing table relationships: always respect them. 

## Database schema in YAML format
```yaml
authors:
  columns:
  - name: author_id
    type: integer
  - name: first_name
    type: character varying
  - name: last_name
    type: character varying
  - name: birthdate
    type: date
  relationships: []
books:
  columns:
  - name: book_id
    type: integer
  - name: title
    type: character varying
  - name: author_id
    type: integer
  - name: genre_id
    type: integer
  - name: price
    type: numeric
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
    type: integer
  - name: first_name
    type: character varying
  - name: last_name
    type: character varying
  - name: email
    type: character varying
  - name: phone
    type: character varying
  - name: address
    type: character varying
  relationships: []
genres:
  columns:
  - name: genre_id
    type: integer
  - name: genre_name
    type: character varying
  relationships: []
inventory:
  columns:
  - name: inventory_id
    type: integer
  - name: book_id
    type: integer
  - name: supplier_id
    type: integer
  - name: quantity
    type: integer
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
    type: integer
  - name: order_id
    type: integer
  - name: book_id
    type: integer
  - name: quantity
    type: integer
  - name: price
    type: numeric
  relationships:
  - from_column: order_id
    to_column: order_id
    to_table: orders
  - from_column: book_id
    to_column: book_id
    to_table: books
orders:
  columns:
  - name: order_id
    type: integer
  - name: customer_id
    type: integer
  - name: order_date
    type: date
  - name: total_amount
    type: numeric
  relationships:
  - from_column: customer_id
    to_column: customer_id
    to_table: customers
suppliers:
  columns:
  - name: supplier_id
    type: integer
  - name: supplier_name
    type: character varying
  - name: contact_name
    type: character varying
  - name: contact_email
    type: character varying
  - name: contact_phone
    type: character varying
  relationships: []
```
