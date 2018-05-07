###########################################################
# CST8333 2018W Assignment4                               #
#                                                         #
# Mar 21 2018                                             #
# This class to write a file through multithreading       #
#                                                         #
# Created by Phuong Pham- 040853073                       #
#                                                         #
###########################################################

# import threading. 
# created on Mar 21, 2018 @author: Phuong Pham
import threading

# Function to write a message in text file
# created on Mar 21, 2018 @author: Phuong Pham
def writeFile(message, file):
    with open(file, "w") as f:# Open a file
        f.write(message)
    print('done!!!')

# Function for thread to write a message in text file
# created on Mar 21, 2018 @author: Phuong Pham
def threadWriteFile(message, file):
    try:
        open(file, "r") # open file
    except IOError:#If no file selected, return false
        return False

    t = threading.Thread(target=writeFile(message, file))
    t.start() # thread start
    print("waiting")
    t.join()
    print("done!")
    return True

# Main of the program
# created on Mar 21, 2018 @author: Phuong Pham
def main():
    print("This program created by Phuong Pham to write a file through multithreading")
    message = input("Enter a message to write into the file: ")# add a message
    filename = input("Enter a file name: ")                     # add name of file
    
    if (threadWriteFile(message, filename)):    # if the same name of text file, return success
        print("Success!")
    else:
        print("failed!")# if the different name of text file, return failed
    
if __name__ == '__main__':
    main()  #run the program
        