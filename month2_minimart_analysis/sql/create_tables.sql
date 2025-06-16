-- SQL script to create necessary tables
CREATE TABLE customers(
customer_id serial PRIMARY key,
name varchar(50),
email varchar(50),
join_date date
);

CREATE TABLE products(
product_id serial PRIMARY key,
product_name varchar (100),
category varchar (100),
price int 
);

CREATE TABLE orders(
order_id serial PRIMARY key,
customer_id int,
product_id int,
quantity int,
order_date date,

FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
);

