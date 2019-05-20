
INSERT INTO
       Car
       (ID,VIN,Manufacturer,Model,Year,Color,Purchase_price,Sale_price,idStore,idItem,Purchase_Currency,Sale_Currency)
       VALUES
       ('0','3K096I98581DHSNUP','Volkswagen','Tiguan','2019','Blue','10000','20000',1,1,'EURO','EURO'),
       ('1','ZM8G7BEUQZ97IH46V','Peugeot','Rifter','2019','Red','10000','20000',1,1,'EURO','EURO'),
       ('2','RKXVNNIHLVVZOUB4M','Ford ','Fusion','2018 ','White','10000','20000',2,3,'EURO','EURO'),
       ('3','HKNDGS7CU31E9Z7JW','Toyota','RAV4','2018','Silver','10000','20000',2,3,'EURO','EURO'),
       ('4','DAM41UDN3CHU2WVF6','Volvo','V60','2019','Gray','10000','20000',3,2,'EURO','EURO'),
       ('5','DAM41UDN3CHU2WXF6','Volvo','V60 Cross Country','2019','Gray','10000','20000',3,2,'EURO','EURO')

       ;
--He modificado un VIN porque al establecer está columna como clave primaria no me permitía que tuviera duplicados.

INSERT INTO Store
       (ID,idStore,Address,City,State)
       VALUES
       (1,1,'Calle Golondrina,5','Madrid','España'),
       (2,2,'Zamunda Strasse,25','Berlin','Alemania'),
       (3,3,'High rock street,1554','Atlanta','USA');

insert into Item
       (ID,idItem,Quantity,idCar,idInvoices,Promotion)
       VALUES
       (1,1,1,1,852399038,0),
       (2,2,1,2,852399038,0),
       (3,3,1,3,731166526,0),
       (4,4,2,4,731166526,0.25),
       (5,5,1,5,271135104,0);


insert into Invoice
       (ID,idInvoices,Date,idSalesPerson,idCustomer)
       values
       (0,852399038,'2018-08-22',0,1),
       (1,731166526,'2018-12-31',3,0),
       (2,271135104,'2019-01-22',2,2);  
       
INSERT INTO  customer 
       (ID,idCustomer,Name,Phone_Number,Email,Address,City,State,Country,Zip_Code)
       VALUES
       (0,10001,'Pablo Picasso','+34 636 17 63 82','-','Paseo de la Chopera 14','Madrid','Madrid','Spain','28045'),
       (1,20001,'Abraham Lincoln','+1 305 907 7086','-','120 SW 8th St','Miami','Florida','United States','33130'),
       (2,30001,'Napoléon Bonaparte','+33 1 79 75 40 00','-','40 Rue du Colisée','Paris','Île-de-France','France','775008')
       
       ;



