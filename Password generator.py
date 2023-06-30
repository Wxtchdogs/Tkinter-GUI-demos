from tkinter import *
import tkinter as tk
import string
import random

class GUI:
    def __init__(self):
        #Generate window
        self.window = tk.Tk()
        self.window.geometry("1200x900")
        self.window.title("Password generator v1")

        self.label = tk.Label(self.window, text="Password generator v1", font= ('Arial, 18'))
        self.label.pack(padx=20, pady =10)

        #Length slider
        self.horizontal = Scale(self.window, from_=8, to=50, orient=HORIZONTAL)
        self.horizontal.pack()

        #check the variables within the checkboxes to know if they are ticked
        self.checkstate1 = tk.IntVar()
        self.checkstate2 = tk.IntVar()

        self.capitals = tk.Checkbutton(self.window, text="Capital letters", variable = self.checkstate1)
        self.capitals.pack()

        self.specials = tk.Checkbutton(self.window, text="Special characters", variable = self.checkstate2)
        self.specials.pack()

        #Button which passes the generate function
        self.button = tk.Button(self.window, text = "Generate password", command=self.generate)
        self.button.pack(pady=10)
        
        self.label2 = tk.Label(self.window, text = "")
        self.label2.pack(padx=20, pady =30)    

        self.window.mainloop()

#Password creation is done here
    def generate(self):
        #Delete the old password whenever this function is passed again
        self.label2.destroy()

        randLower = string.ascii_lowercase
        randCaptial = string.ascii_uppercase
        randSpecial = string.punctuation

        password = ""
        temp = []

        #Get the settings the user input
        length = self.horizontal.get()
        capital = self.checkstate1.get()
        special = self.checkstate2.get()
        
        #Create password based on settings
        if capital == 1 and special == 1:
            while length > len(temp):
                temp.append(random.choice(random.choice(randLower) + random.choice(randCaptial) + random.choice(randSpecial)))       
        elif capital == 1 and special == 0:
            while length > len(temp):
                temp.append(random.choice(random.choice(randLower) + random.choice(randCaptial)))   
        elif capital == 0 and special == 1:
            while length > len(temp):
                temp.append(random.choice(random.choice(randLower) + random.choice(randSpecial)))   
        else:
            while length > len(temp):
                temp.append(random.choice(randLower))   

        #Change password from list to string
        password = password.join(temp)

        #Print the password
        self.label2 = tk.Label(self.window, text = password ,font= ('Arial, 18'))
        self.label2.pack(padx=20, pady =30)    
         
GUI()                                                                                                                                                                                                                                                           