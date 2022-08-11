
## Getting Started:

The goal is wrangle through some data, and test your basic knowledge of data engineering.
For this project, we will we using  the public *randomuser.me* API. 
This [API Endpoint](https://randomuser.me/api/?results=500) should be used for all the tasks

## Tasks:

1. Using the json response from the endpoint. Model, and design the database table/tables.
	-	You can use [dbdiagram](https://dbdiagram.io/d) to generate the ERD
	-	_Deliverable_: Export of ERD

2. Build an end to end process in Python3, that generates a csv file for each of the tables you have designed
	-  The JSON results must be flatten
	-  The column names must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_)
	-  _Deliverable_: The python code, that can generate the csv files. 

3. Now imagine this is a production ETL process. How would you design it? What tests would you put in place?
  - _Deliverable_: Any diagrams/text files that can show us your design. 

## Steps to run the project

Linux
```
. ./run.sh
```

Otherwise, install the requirements 
1. pandas==1.4.3
2. requests==2.28.1
3. pydantic==1.9.1
And run
```
./get_data_and_transform_script.py
```

## Files included 
* run.sh - runs requirments.txt, create a data folder to store csv files and get_data_and_transform_script.py
	* Sets up environment and create csv files 
  
* get_data_and_transform_script.py
	  * collect data from [API Endpoint](https://randomuser.me/api/?results=500), create table and save them as csv files
* ERD.pdf
	  * ERD (Entity Relationship Diagram)
* Data folder
	  * files containing table data 

## Production ETL Process
![Production ELT] (link)

* Tests to put in place?
        * Request fail and request status test and logging
        * Unique (Primary key) test to make sure when adding the raw data it doesn't duplicate primary keys
        * Not null test for columns like login_username and password
        * Data integrity and anomalies test


