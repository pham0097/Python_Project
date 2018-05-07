###########################################################
# CST8333 2018W Assignment4                               #
#                                                         #
# Mar 21 2018                                             #
# Python unit Test for multithreading to write a text file#
#                                                         #
# Created by Phuong Pham- 040853073                       #
#                                                         #
###########################################################


# import statements: unit TestDataLoader, Multithreadwritefile file
# created on Mar 21 2018  @author: Phuong Pham
import Multithreadwritefile
import unittest 

# Class of unit TestMultithreadwritefile
# created on Mar 21 2018  @author: Phuong Pham
class TestMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestMethods, self).__init__(*args, **kwargs)

# Test case for write file in valid message in text file 
# created on Mar 21 2018  @author: Phuong Pham      
    def test_write_file_valid(self):
        print("This program created by Phuong Pham to test a write file in valid message in text file ")
        Multithreadwritefile.writeFile("Hello", "out.txt")#TestDataLoader for writing message ='Hello' in out.txt file
        with open("out.txt", "r") as f:
            message = f.read()
        self.assertEqual(message, "Hello")

# Test case 2 for write file in valid message in text file 
# created on Mar 21 2018  @author: Phuong Pham         
    def test_write_file_valid_2(self):
        print("This program created by Phuong Pham to test a write file in valid message in text file ")
        result = Multithreadwritefile.writeFile("Hello World", "out.txt")
        with open("out.txt", "r") as f:
            message = f.read()
        self.assertEqual(message, "Hello World")

# Test case for file valid when writing a message
# created on Mar 21 2018  @author: Phuong Pham
    def test_thread_write_file_valid(self):
        print("This program created by Phuong Pham to test case for file valid when writing a message ")
        result = Multithreadwritefile.threadWriteFile("Hello", "out.txt")
        self.assertEqual(result, True)
        with open("out.txt", "r") as f:
            message = f.read()
        self.assertEqual(message, "Hello")
# Test case for file invalid when writing a message and return false
# created on Mar 21 2018  @author: Phuong Pham
    def test_thread_write_file_invalid(self):
        print("This program created by Phuong Pham to test case for file invalid when writing a message and return false ")
        result = Multithreadwritefile.threadWriteFile("Hello", "invalidfile.txt")
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()            #run the TestDataLoader