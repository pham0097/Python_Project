##########################################################
# CST8333 2018W Assignment4                              #
# Mar 21 2018                                            #
# Python coding to create, update, read, and             #
# insert database to MySQL                               #
#                                                        #
# Created by Phuong Pham- 040853073                      #
#                                                        #
##########################################################


# import statement: MySQLdb. 
#Created on Mar 21, 2018 @author: Phuong Pham
import MySQLdb

# Open database connection
#Created on Mar 21, 2018 @author: Phuong Pham
db = MySQLdb.connect(user='root', password='password',
                              host='127.0.0.1', )

# prepare a cursor object using cursor() method
#Created on Mar 21, 2018 @author: Phuong Pham
cursor = db.cursor()

# create schema in Mysql with name python
#Created on Mar 21, 2018 @author: Phuong Pham
cursor.execute("CREATE DATABASE Data")
cursor.execute("USE data")

# For creating create database
# Below line  is hide your warning 
#Created on Mar 21, 2018 @author: Phuong Pham
cursor.execute("SET sql_notes = 0; ")
# create db here....
cursor.execute("create database IF NOT EXISTS data")

# create table dataset in schema data
#Created on Mar 21, 2018 @author: Phuong Pham
cursor.execute("SET sql_notes = 0; ")
cursor.execute("""CREATE TABLE if not exists dataset (
    ID int NOT NULL AUTO_INCREMENT,
    Ref_Date date NOT NULL,
    GEO varchar(25),
    COMMOD varchar(83),
    Vector varchar(20) ,
    Coordinate float,
    Value float,
    PRIMARY KEY (ID)
    ); """)  # create the table dataset
cursor.execute("SET sql_notes = 1; ")

# print this row if creating table successful
#Created on Mar 21, 2018 @author: Phuong Pham
print("Phuong Pham created dataset table successful")

#insert data in dataset table
#Created on Mar 21, 2018 @author: Phuong Pham
cursor.execute("""insert into dataset  (ID, Ref_Date, GEO, COMMOD, Vector,Coordinate,  Value  ) 
                                values(01,'2018-08-10', 'Canada', 'Cigarettes','v1574785', 1.217, 252.3)""")
cursor.execute("""insert into dataset  (ID, Ref_Date, GEO, COMMOD, Vector,Coordinate,  Value  ) 
                                values(02,'2018-09-10', 'USA', 'Ale, lager, stout and porter','v1574772', 1.204, 100)""")
cursor.execute("""insert into dataset  (ID, Ref_Date, GEO, COMMOD, Vector,Coordinate,  Value  ) 
                                values(03,'2018-10-10', 'Canada', ' sugar ','v1574728', 1.16, 100)""")
cursor.execute("""insert into dataset  (ID, Ref_Date, GEO, COMMOD, Vector,Coordinate,  Value  ) 
                                values(04,'2018-11-10', 'USA', 'Corn starch','v1574703', 1.135, 80)""")
cursor.execute("""insert into dataset  (ID, Ref_Date, GEO, COMMOD, Vector,Coordinate,  Value  ) 
                                values(05,'2018-12-10', 'Canada', 'Soybean oil cake and meals','v1574682', 1.114, 200)""")

# print this row if insert data in dataset table successful
#Created on Mar 21, 2018 @author: Phuong Pham
print("Phuong Pham insert data in dataset table successful")

#delete data with ID=01 in dataset table
#Created on Mar 21, 2018 @author: Phuong Pham
cursor.execute("""delete from dataset
                       where ID= 01""")
# print this row if delete data in dataset table successful
#Created on Mar 21, 2018 @author: Phuong Pham
print("Phuong Pham delete row 1 in dataset table successful")

# print this row if read data in dataset table successful
#Created on Mar 21, 2018 @author: Phuong Pham
cursor.execute("SELECT * FROM dataset")

for i in range(cursor.rowcount):
        
        row = cursor.fetchone()
        print (row[0], row[1], row[3], row[4],row[5])# print rows in dataset table after deleting

# Commit your changes in the database
#Created on Mar 21, 2018 @author: Phuong Pham
db.commit()

# disconnect from server
#Created on Mar 21, 2018 @author: Phuong Pham
db.close()
