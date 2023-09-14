INSERT INTO Customers (Last, First, Address, Username, Password)
VALUES ('Jones', 'Nick', '201 Inman Street', 'ncj', 'Fireforce'),
('Black', 'Jack', '222 Nacho Drive', 'jackblack', 'Nacho');

insert into Bricks (BrickNum, Name, Price, Quantity, Description)
Values (1,'Red rectangle brick', 0.99, 100, 'Standard red rectanglular brick'),
(2,'Yellow wheel', 0.99, 100, 'Yellow rotating wheel. When attached to spoke, is able to spin.'),
(3,'Black tire', 1.00, 400, 'Black tire piece. Usually goes around yellow rotating wheel');

insert into Employee (EmployeeID, Last, First, Password, StoreNum, Level)
Values (1000, 'Jones', 'Nicholas', 'Fireforce8', 36, 'admin');
insert into Employee (Last, First, Password, StoreNum, Level)
Values('Jones', 'Chris', 'Keyblade97', 45, 'worker');