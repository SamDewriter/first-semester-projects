-- SQL queries for retrieving insights

--Basic queries
select * from customers;
select * from products where category = 'Dairy';
select * from orders order by order_date desc;

--Aggregation
select count(*) as Total_Orders from orders;

--Using SUM() to calculate revenue per product (price × quantity)
select p.product_id,p.product_name,sum (p.price * o.quantity) 
as  product_revenue
from products p join orders o on p.product_id = o.product_id
group by p.product_id
order by product_revenue desc;

--Using AVG() to find the average product price
select avg(price) as average_product_price from products;

--Joins
--Using INNER JOIN to get detailed order information (with customer and product details).
select o.order_id, c.name as Customer_name,email,p.product_name,price,quantity, (p.price*o.quantity) as Total, order_date
from customers c
inner join orders o on c.customer_id = o.customer_id
inner join products p on p.product_id = o.product_id
order by order_date desc;

--Using LEFT JOIN to list all customers and include their orders (if any)
select c.customer_id,name,email,o.order_id,quantity, order_date
from customers c
left join orders o on c.customer_id = o.customer_id
order by name desc;

--Using LEFT JOIN to show products even if they haven’t been ordered.
select p.product_id,p.product_name
from products p 
left join orders o on p.product_id = o.product_id;