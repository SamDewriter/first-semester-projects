-- SQL script to insert sample data
insert into customers(name, email, join_date)
values
('julius akande', 'julius_idowu@minimart.com', '2020-06-07'),
('samuel chimenla', 'samuel_chimenla@minimart.com', '2021-05-06'),
('eder millito', 'eder_millito@minimart.com', '2022-04-05'),
('bala ahmed', 'bala_ahmed@minimart.com','2020-03-04'),
('shehu benigo', 'sheu_benigo@minimart.com', '2023-02-03'),
('ayomide adeyeye', 'ayomide_adeyeye@minimart.com', '2024-01-02'),
('samuel chimenla', 'samuel_chimenla@minimart.com', '2024-12-11');


insert into products(product_name, category, price)
values
('cornflakes', 'cereal', 300),
('touchlight', 'utilities', 2500),
('banana', 'fruits', 1000),
('toiletpaper', 'toiletries', 1500),
('originbitters', 'alcoholics', 2500),
('ribena', 'drink', 2000),
('goldenmorn', 'cereal', 400);


TRUNCATE TABLE products, orders, customers RESTART IDENTITY;

select * from customers;

select * from products;

select * from orders;



insert into orders(customer_id, product_id, quantity, order_date)
values
(1,1,4,'2025-06-09'),
(2,2,17,'2025-05-20'),
(3,3,4,'2025-06-10'),
(4,4,29,'2025-04-30'),
(5,5,7,'2025-03-05'),
(6,2,9,'2025-02-05'),
(2,4,9, '2025-03-07'),
(1,1,6, '2025-05-02'),
(5,6,13, '2025-01-17'),
(7,1,4, '2025-02-09'),
(3,5,18, '2025-01-03'),
(7,2,6, '2025-06-02'),
(6,2,15, '2025-04-02'),
(7,4,3, '2025-03-01');