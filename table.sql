CREATE table if not exists Customers (
	PersonID int auto_increment,
	Last varchar(255),
	First varchar(255),
	Address varchar(255),
	Username varchar(255),
	Password varchar(255),
    primary key (PersonID)
);

create table if not exists Employee (
	EmployeeID int auto_increment,
    Last varchar(255),
    First varchar(255),
    Password varchar(255),
    StoreNum int,
    Level varchar(255),
    primary key (EmployeeID)
);

create table if not exists Bricks (
	BrickNum int auto_increment,
    Name varchar(255),
    Price decimal(65,2),
    Quantity int,
    Description varchar(255),
    primary key (BrickNum)
);

create table if not exists Sets (
	SetNum int auto_increment,
    Name varchar(255),
    Price decimal(30,2),
    Quantity int,
    Description varchar(255),
    primary key (SetNum)
);

create table if not exists Stores (
	StoreNum int auto_increment,
	primary key (StoreNum)
);
    