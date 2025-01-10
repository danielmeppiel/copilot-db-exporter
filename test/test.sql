SELECT 
    o.order_id,
    o.order_date,
    c.first_name + ' ' + c.last_name AS customer_name,
    SUM(oi.quantity) AS total_books_ordered,
    o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY 
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    o.total_amount
ORDER BY 
    total_books_ordered DESC;