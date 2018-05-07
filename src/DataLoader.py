##########################################################
# CST8333 2018W Assignment3                              #
#                                                        #
# Feb 17 2018                                            #
# Python coding to create, update, read, and             #
# view records from the data.csv file                    #
#                                                        #
# Created by Phuong Pham- 040853073                      #
#                                                        #
##########################################################


# import statements:csv, random. 
# created on Feb 17, 2018 @author: Phuong Pham
import csv 
import random 

             
# Function to create records from data.csv file
# created on Feb 17, 2018 @author: Phuong Pham
def getData():
    data = []
# Add information for rows in data set
    try:
        csvfile = open('data.csv', newline='')      # open data file
        reader = csv.reader(csvfile)                
        for row in reader:
            record = {
                'Ref_Date': row[0],                 # create row Red_Date
                'GEO': row[1],                      # create row GEO
                'COMMOD': row[2],                   # create row COMMOD
                'Coordinate': row[3],               # create row Coordinate
                'Value': row[4]                     # create row Value
            }
            data.append(record)
    except IOError:
        print('cannot open the file')               # IOError will not open data set
    
    return data

# Function to read records from data.csv file
# created on Feb 17, 2018 @author: Phuong Pham
def readRecord(data, row_num):
    if row_num >=0 and row_num< len(data): # set records range from 1 to length of data file
        return data[row_num]
    else:
        return False
# print the records from data.csv file
# created on Feb 17, 2018 @author: Phuong Pham
def printRecord(record):
    print("Record info:")
    print("Ref_Date      : %40s" % record['Ref_Date']) 
    print("GEO           : %40s" % record['GEO']) 
    print("Commodity     : %40s" % record['COMMOD']) 
    print("Coordinate    : %40s" % record['Coordinate']) 
    print("Value         : %40s" % record['Value']) 
    
# Function to update records from data.csv file
# created on Feb 17, 2018 @author: Phuong Pham
def updateRecord(record, field, new_val):
    fields = ['Red_Date', 'GEO', 'Commodity', 'Coordinate', 'Value'] # set field to choose when updating records
    if not field in fields: # fail result if fields not in data set
        return False
    else:
        record[field] = new_val # add new value for field in data set
        return True
    
# Function to print random records from data.csv file
# created on Feb 17, 2018 @author: Phuong Pham
def getRandomRecord(data):
    return data[random.randint(0, len(data))] 
    
# main of the program
# created on Feb 17, 2018 @author: Phuong Pham
def main():
    print("This program created by Phuong Pham to view dataset")
    data = getData()
    row = int(input("Please enter a row number: "))
    print('Data at row %d is: ' % row)
    printRecord(data[row])                # view records from data.csv file
    # update for field
    print("This program created by Phuong Pham to update the dataset")
    field = input("Enter a field to update: ") 
    new_val = input("Enter a new value: ")      # update new value for field which chose
    if updateRecord(data[row], field, new_val):
        printRecord(data[row])
    else:
        print("Fail to update")
    
    # Print random record from data.csv file
    print("This program created by Phuong Pham to get the random the dataset")
    input("Press Enter")
    print("Test random record")
    printRecord(getRandomRecord(data))

        
if __name__ == '__main__':  
   main()                     #run the program