
INSERT INTO
       Car
       (ID,idCar,Manufacturer,Model,Year,Color,Purchase_price,Sale_price,idStore,idItem,Purchase_Currency,Sale_Currency)
       VALUES
       (1,'C0001','FORD','Mustang Shelby','1970','Red','150000','200000',1,1,'US-D','EURO'),
       (2,'C0002','FORD','Capri','1980','White','6000','10000',1,2,'US-D','EURO'),
       (3,'C0003','FORD','T','1910','White','500000','1000000',1,3,'US-D','EURO'),
       (4,'C0004','SEAT','Ibiza','1995','Green','6000','10000',2,4,'EURO','EURO'),
       (5,'C0005','VOLKSWAGEN','Golf','1995','White','10000','15000',2,5,'EURO','EURO');
       ;

INSERT INTO Store
       (ID,idStore,Address,City,State)
       VALUES
       (1,1,'Calle Golondrina,5','Madrid','España'),
       (2,2,'Zamunda Strasse,25','Berlin','Alemania'),
       (3,3,'High rock street,1554','Atlanta','USA');

insert into Item
       (ID,idItem,Quantity,idCar,idInvoices,Promotion)
       VALUES
       (1,1,1,1,1,0),
       (2,2,1,2,1,0),
       (3,3,1,3,1,0),
       (4,4,2,4,2,0.25),
       (5,5,1,5,2,0);

insert into Invoice
       (ID,idInvoices,Date,idSalesPerson,idCustomer)
       values
       (1,1,curdate(),1,1),
       (2,2,curdate(),2,2);
       

insert into Customer
       (ID,idCustomer,Name,Phone_Number,E-mail,Address,City,State,Country,Zip_Code)
       VALUES

(0,10001,Pablo Picasso,+34 636 17 63 82,-,Paseo de la Chopera 14,Madrid,Madrid,Spain,28045),
(1,20001,Abraham Lincoln,+1 305 907 7086,-,120 SW 8th St,Miami,Florida,United States,33130)
(2,30001,Napoléon Bonaparte,+33 1 79 75 40 00,-,40 Rue du Colisée,Paris,Île-de-France,France,775008)
