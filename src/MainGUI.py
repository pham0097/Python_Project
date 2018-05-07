###########################################################
# CST8333 2018W Assignment4                               #
#                                                         #
# Mar 21 2018                                             #
# Open a file dialog window in tkinter using the          #
# filedialog method                                       #
#                                                         #
# Created by Phuong Pham- 040853073                       #
#                                                         #
###########################################################

#Open a file dialog window in tkinter using the filedialog method.
#Tkinter has a prebuilt dialog window to access files. 
#This example is designed to show how you might use a file dialog askopenfilename
#and use it in a program.


# import statements. 
#Created on Mar 21, 2018 @author: Phuong Pham
from tkinter import * # import the tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename #import askopenfilename

root = Tk(  )# assigne the root tkinter object.

#This is where we lauch the file manager bar.
#Created on Mar 21, 2018 @author: Phuong Pham
def OpenFile():# create the method openfile
    name = askopenfilename(initialdir="C:/Users/user/Documents/level 4/cst8333/assignment 4/",
                           filetypes =(("Text File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )# open the data.csv file
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")
        
#Create the title for GUI
#Created on Mar 21, 2018 @author: Phuong Pham
Title = root.title( "CST8333_Assignment4_PhuongPham")  #Set the title for the GUI
root.geometry("680x550")  #Set the size for the GUI

# Create a text label button to show welcome message  
#Created on Mar 21, 2018 @author: Phuong Pham       
label = Label(root, text="Welcome to File Open CSV! Create by PhuongPham", fg='red', 
                           background='blue', font=(30), width=100, height=4)
label.pack()
label = ttk.Label(root, text ="I'm Phuong!!!",foreground="red",font=("Helvetica", 16))
label.pack()

# Create space between buttons
#Created on Mar 21, 2018 @author: Phuong Pham
label = Label(root, text=" ",width=50, height=1)
label.pack() # pack the label

#Create Menu
#Created on Mar 21, 2018 @author: Phuong Pham
menu = Menu(root)
root.config(menu=menu)

#Create a File Menu with 2 labels:Open and Exit
#Created on Mar 21, 2018 @author: Phuong Pham
file = Menu(menu)
file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())
menu.add_cascade(label = 'File', menu = file)

#Create a Help Menu 
#Created on Mar 21, 2018 @author: Phuong Pham 
help = Menu(menu)
help.add_command(label="""This is CST8333 Final Project Python HELP GUI.The program is to display the dataSet. 
        Author: Phuong Pham-040853073
        Date: 2018-04-15
        """)   # put the help information in string""" 
        
menu.add_cascade(label="Help", menu=help)  

#Calling GUI
#Created on Mar 21, 2018 @author: Phuong Pham
root.mainloop()
    
    
    
