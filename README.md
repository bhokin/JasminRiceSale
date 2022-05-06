# JasminRiceSale

This application is allowed the user to buy jasmine rice and shows the sales list of jasmine rice.

## Create database from schema and import data

**Using SQLite and the sqlite3 command line utility**:  

- Create "database.db" using schema commands in a file.  
  (If it's show the message: ***"sqlite3 The '<' operator is reserved for future use."*** use `-init` instead of `<`)
``` 
sqlite3 database.db < database.schema 
or
sqlite3 database.db -init database.schema 
```

- Open a database file using ```sqlite3 database.db```.  


- Import the data from `.csv` file into a particular table in database.
```
sqlite> .mode csv
sqlite> .import data/customers.csv customers
sqlite> .import data/jasmine_rice_sale_list_in_a_day.csv jasmine_rice_sale 
```

## Configure and Run the application  

 - Use `python main.py` to run the application.  


## Project Documents

[Domain model](../../wiki/Domain%20model)  
[UML class diagram](../../wiki/UML%20class%20diagram)  
[Package diagram](../../wiki/Package%20diagram)  
[Web Service API](../../Web%20Service%20API)
