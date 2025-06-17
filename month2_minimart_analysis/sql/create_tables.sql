-- SQL script to create necessary tables
create table customers(
customer_id serial primary key,
name varchar(100) not null,
email varchar(100) unique,
join_date date default current_date
);
alter table customers add column phone VARCHAR(11);
--alter table customers to add phone number

create table products(
product_id serial primary key,
product_name VARCHAR(100) not null,
category VARCHAR(50) not null,
price decimal(10,2) not null check(price > 0)
);

create table orders(
order_id serial primary key,
customer_id int not null,
product_id int not null,
quantity int not null,
order_date date not null,
foreign key(customer_id) references customers(customer_id)on delete restrict,
foreign key(product_id) references products(product_id)on delete restrict
);
