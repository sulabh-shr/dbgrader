DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS busEntities;
DROP TABLE IF EXISTS billOfMaterials;
DROP TABLE IF EXISTS supplierDiscounts;
DROP TABLE IF EXISTS supplyUnitPricing;
DROP TABLE IF EXISTS manufDiscounts;
DROP TABLE IF EXISTS manufUnitPricing;
DROP TABLE IF EXISTS shippingPricing;
DROP TABLE IF EXISTS customerDemand;
DROP TABLE IF EXISTS supplyOrders;
DROP TABLE IF EXISTS manufOrders;
DROP TABLE IF EXISTS shipOrders;

--Random Comment
create table items (
   item varchar(25),
   unitWeight float,
   primary key(item) 
); 

create table busEntities (
   entity varchar(25),
   shipLoc varchar(25),
   address varchar(25),
   web varchar(100),
   contact integer,
   primary key(entity)
); 

create table billOfMaterials(
prodItem varchar(25), 
matItem varchar(25), 
QtyMatPerItem int,
primary key(prodItem, matItem),
foreign key(prodItem) references items(item),
foreign key(matItem) references items(item)
);

create table supplierDiscounts(
supplier varchar(25), 
amt1 float,
disc1 float,
amt2 float,
disc2 float,
primary key(supplier));

create table supplyUnitPricing(
supplier varchar(25), 
item varchar(25), 
ppu float,
primary key(supplier,item),
foreign key(item) references items(item));

create table manufDiscounts(
manuf varchar(25), 
amt1 float,
disc1 float,
primary key(manuf));

create table manufUnitPricing(
manuf varchar(25), 
prodItem varchar(25), 
setUpCost float,
prodCostPerUnit float,
primary key(manuf,prodItem),
foreign key(prodItem) references items(item)
);

create table shippingPricing(
shipper varchar(25), 
fromLoc  varchar(25), 
toLoc varchar(25), 
minPackagePrice float,
pricePerLb float,
amt1 float,
disc1 float,
amt2 float,
disc2 float,
primary key (shipper, fromLoc, toLoc));

create table customerDemand(
customer varchar(25), 
item varchar(25), 
qty float,
primary key(customer, item),
foreign key(item) references items(item),
foreign key(customer) references busEntities(entity)
 );

create table supplyOrders(
item varchar(25), 
supplier varchar(25), 
qty float,
primary key(item, supplier),
foreign key(item) references items(item),
foreign key(supplier) references busEntities(entity)
);

create table manufOrders(
item varchar(25), 
manuf varchar(25), 
qty float,
primary key(item, manuf),
foreign key(item) references items(item),
foreign key(manuf) references busEntities(entity));
 

create table shipOrders(
item varchar(25), 
shipper varchar(25), 
sender varchar(25), 
recipient varchar(25), 
qty float,
primary key(item, shipper, sender, recipient),
foreign key(shipper) REFERENCES busEntities(entity),
foreign key(item) REFERENCES items(item),
foreign key(sender) REFERENCES busEntities(entity),
foreign key(recipient) REFERENCES busEntities(entity));
