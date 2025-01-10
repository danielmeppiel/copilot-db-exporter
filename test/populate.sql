-- Insert data into authors
INSERT INTO authors (author_id, first_name, last_name, birthdate) VALUES
(1, 'John', 'Doe', '1970-01-01'),
(2, 'Jane', 'Smith', '1980-02-02'),
(3, 'Emily', 'Johnson', '1990-03-03'),
(4, 'Michael', 'Brown', '1965-04-04'),
(5, 'Sarah', 'Davis', '1975-05-05');

-- Insert data into genres
INSERT INTO genres (genre_id, genre_name) VALUES
(1, 'Fiction'),
(2, 'Non-Fiction'),
(3, 'Science Fiction'),
(4, 'Fantasy'),
(5, 'Mystery');

-- Insert data into books
INSERT INTO books (book_id, title, author_id, genre_id, price, publication_date) VALUES
(1, 'Book One', 1, 1, 19.99, '2020-01-01'),
(2, 'Book Two', 2, 2, 29.99, '2021-02-02'),
(3, 'Book Three', 3, 3, 39.99, '2022-03-03'),
(4, 'Book Four', 4, 4, 24.99, '2020-04-04'),
(5, 'Book Five', 5, 5, 34.99, '2021-05-05'),
(6, 'Book Six', 1, 1, 19.99, '2020-06-06'),
(7, 'Book Seven', 2, 2, 29.99, '2021-07-07'),
(8, 'Book Eight', 3, 3, 39.99, '2022-08-08'),
(9, 'Book Nine', 4, 4, 24.99, '2020-09-09'),
(10, 'Book Ten', 5, 5, 34.99, '2021-10-10');

-- Insert data into customers
INSERT INTO customers (customer_id, first_name, last_name, email, phone, address) VALUES
(1, 'Alice', 'Brown', 'alice@example.com', '123-456-7890', '123 Main St'),
(2, 'Bob', 'Davis', 'bob@example.com', '234-567-8901', '456 Elm St'),
(3, 'Charlie', 'Evans', 'charlie@example.com', '345-678-9012', '789 Oak St'),
(4, 'David', 'Wilson', 'david@example.com', '456-789-0123', '101 Pine St'),
(5, 'Eve', 'Taylor', 'eve@example.com', '567-890-1234', '202 Maple St');

-- Insert data into orders
INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(1, 1, '2023-01-01', 49.98),
(2, 2, '2023-02-02', 29.99),
(3, 3, '2023-03-03', 39.99),
(4, 4, '2023-04-04', 24.99),
(5, 5, '2023-05-05', 34.99),
(6, 1, '2023-06-06', 19.99),
(7, 2, '2023-07-07', 29.99),
(8, 3, '2023-08-08', 39.99),
(9, 4, '2023-09-09', 24.99),
(10, 5, '2023-10-10', 34.99);

-- Insert data into order_items
INSERT INTO order_items (order_item_id, order_id, book_id, quantity, price) VALUES
(1, 1, 1, 2, 19.99),
(2, 2, 2, 1, 29.99),
(3, 3, 3, 1, 39.99),
(4, 4, 4, 1, 24.99),
(5, 5, 5, 1, 34.99),
(6, 6, 6, 1, 19.99),
(7, 7, 7, 1, 29.99),
(8, 8, 8, 1, 39.99),
(9, 9, 9, 1, 24.99),
(10, 10, 10, 1, 34.99);

-- Insert data into suppliers
INSERT INTO suppliers (supplier_id, supplier_name, contact_name, contact_email, contact_phone) VALUES
(1, 'Supplier One', 'Contact One', 'contact1@example.com', '123-456-7890'),
(2, 'Supplier Two', 'Contact Two', 'contact2@example.com', '234-567-8901'),
(3, 'Supplier Three', 'Contact Three', 'contact3@example.com', '345-678-9012'),
(4, 'Supplier Four', 'Contact Four', 'contact4@example.com', '456-789-0123'),
(5, 'Supplier Five', 'Contact Five', 'contact5@example.com', '567-890-1234');

-- Insert data into inventory
INSERT INTO inventory (inventory_id, book_id, supplier_id, quantity) VALUES
(1, 1, 1, 100),
(2, 2, 2, 200),
(3, 3, 3, 300),
(4, 4, 4, 400),
(5, 5, 5, 500),
(6, 6, 1, 150),
(7, 7, 2, 250),
(8, 8, 3, 350),
(9, 9, 4, 450),
(10, 10, 5, 550);