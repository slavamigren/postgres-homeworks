-- SQL-команды для создания таблиц
psql
create database north;


CREATE TABLE customers_data
(
customers_id varchar(5) PRIMARY KEY,
company_name varchar(100) NOT NULL,
contact_name varchar(50) NOT NULL
);

CREATE TABLE employees_data
(
employee_id smallint PRIMARY KEY,
first_name varchar(30) NOT NULL,
last_name varchar(30) NOT NULL,
title text NOT NULL,
birth_date date NOT NULL,
notes text
);

CREATE TABLE orders_data
(
order_id int PRIMARY KEY,
customer_id varchar(5) REFERENCES customers_data(customers_id) NOT NULL,
employee_id smallint REFERENCES employees_data(employee_id) NOT NULL,
order_date date NOT NULL,
ship_city varchar(30) NOT NULL
)