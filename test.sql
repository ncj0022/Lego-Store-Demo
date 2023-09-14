CREATE TABLE People (
	PersonID int auto_increment,
	Last varchar(255),
	First varchar(255),
	Address varchar(255),
	City varchar(255),
	Username varchar(255),
	Password varchar(255),
	primary key (PersonID)
);

CREATE TABLE Pets (
	PetID int auto_increment,
	Type varchar(255),
	Name varchar(255),
	Owner varchar(255),
	primary key (PetID)
);
	


