CREATE schema lab_mysql;
USE lab_mysql;

CREATE TABLE IF NOT EXISTS `Car` (
  `ID` INT NOT NULL,
  `VIN` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Year` INT(4) NULL,
  `Color` VARCHAR(45) NOT NULL,
  `Purchase_Price` INT NOT NULL,
  `Sale_price` INT NULL,
  `idStore` INT NULL,
  `idItem` INT NULL,
  `Purchase_Currency` VARCHAR(45) NOT NULL,
  `Sale_Currency` VARCHAR(45) NULL,
  PRIMARY KEY (`idCar`)
  );

CREATE TABLE IF NOT EXISTS `Store` (
  `ID` INT NOT NULL,
  `idStore` INT NOT NULL,
  `Address` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State` VARCHAR(45) NULL,
  PRIMARY KEY (`idStore`));

CREATE TABLE IF NOT EXISTS `Item` (
  `ID` INT NOT NULL,
  `idItem` INT NOT NULL,
  `Quantity` INT NOT NULL,
  `idCar` VARCHAR(20) NOT NULL,
  `idInvoices` INT NOT NULL,
  `Promotion` FLOAT NULL,
  PRIMARY KEY (`idItem`, `idInvoices`, `idCar`)
  );

CREATE TABLE IF NOT EXISTS `Invoice` (
  `ID` INT NOT NULL,
  `idInvoices` INT NOT NULL,
  `Date` DATE NOT NULL,
  `idSalesPerson` INT NOT NULL,
  `idCustomer` INT NOT NULL,
  PRIMARY KEY (`idInvoices`, `idSalesPerson`, `idCustomer`)
  );

CREATE TABLE IF NOT EXISTS `Customer` (
  `ID` INT NOT NULL ,
  `idCustomer` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone_Number` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State` VARCHAR(45) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Zip_Code` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idCustomer`));

CREATE TABLE IF NOT EXISTS `SalesPerson` (
  `ID` INT NOT NULL,
  `idSalesPerson` VARCHAR(10) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Store` VARCHAR(20) NOT NULL,
  `Email` VARCHAR(100) NULL,
  PRIMARY KEY (`idSalesPerson`));


