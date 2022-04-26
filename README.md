# JasminRiceSale

This application is allowed the user to buy jasmine rice and shows the sales list of jasmine rice.

## Create database from schema and import data

**Using SQLite and the sqlite3 command line utility**:  

- create "database.db" using schema commands in a file  
```
sqlite3 database.db -init database.schema 
```

- import the data from `.csv` file.
```
sqlite> .mode csv
sqlite> .import data/customers.csv customers
sqlite> .import data/jasmine_rice_sale_list_in_a_day.csv jasmine_rice_sale 
```
 
