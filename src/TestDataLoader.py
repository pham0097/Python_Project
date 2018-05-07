###########################################################
# CST8333 2018W Assignment3                               #
#                                                         #
#Feb 17 2018                                              #
# This class to write a file for testing DataLoader       #
#                                                         #
# Created by Phuong Pham- 040853073                       #
#                                                         #
###########################################################

#Python unit test for read and update data.csv file 
#Import data from DataLoader.py file
# created on Feb 17, 2018 @author: Phuong Pham
import DataLoader
import unittest # import unittest


#Create a class TestMethods
# created on Feb 17, 2018 @author: Phuong Pham
class TestMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestMethods, self).__init__(*args, **kwargs)
        self.data = DataLoader.getData()  # input data from DataLoader.py file
        
# Test case for reading records from the dataset
# created on Feb 17, 2018 @author: Phuong Pham
    def test_read(self):
        print("This program created by Phuong Pham to test a read dataset ")
        record = DataLoader.readRecord(self.data, 1) # test the first  record from the dataset
        self.assertEqual(record['Ref_Date'], 'Jan-90') # test for field 'Ref_Date'
 
# Test case for updating  records from the dataset
# created on Feb 17, 2018 @author: Phuong Pham
    def test_update(self):
        print("This program created by Phuong Pham to test an update dataset ")
        record = DataLoader.readRecord(self.data, 1)    # test the first  record from the dataset
        DataLoader.updateRecord(record, "Value", 100)    # update new value equal 100 for field 'Value' 
        self.assertEqual(record['Value'], 10)    # test for field 'Value'

if __name__ == '__main__':
    unittest.main()            #run the test