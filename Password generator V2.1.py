from tkinter import *
import tkinter as tk
import string
import random
from tkinter import messagebox
import pyperclip

#Words stores all saved passwords including existing saved passwords
#Passlist stores the 3 most recent passwords
#Passwords will only be added to words if they arent empty and don't already exist
#Passwords will only be added to Passlist if they arent empty and don't already exist
#Passwords from passlist will also only be added to words if they arent empty and don't already exist

class GUI:   
    def __init__(self):
        global passList
        #Placeholder dots which can be used for validation
        passList = ["","",""]
        
        #Read everything in the passwords file (Or create one if doesnt exist)
        self.read()

        self.window = tk.Tk()
        self.window.geometry("700x400")
        self.window.title("Password generator v2.1")

        #Specify grid layout (2x7)
        Grid.rowconfigure(self.window,0,weight=1)
        Grid.rowconfigure(self.window,1,weight=1)
        Grid.rowconfigure(self.window,2,weight=1)
        Grid.rowconfigure(self.window,3,weight=1)
        Grid.rowconfigure(self.window,4,weight=1)
        Grid.rowconfigure(self.window,5,weight=1)
        Grid.rowconfigure(self.window,6,weight=1)
        Grid.columnconfigure(self.window,0,weight=1)
        Grid.columnconfigure(self.window,1,weight=1)

        #check the variables within the checkbuttons to know if they are ticked
        self.checkstate1 = tk.IntVar()
        self.checkstate2 = tk.IntVar()

        #Column 1
        self.label = tk.Label(self.window, text="Password generator v2.1", font= ('Arial, 18'))
        self.horizontal = Scale(self.window, from_=1, to=30, orient=HORIZONTAL, command=self.fix)
        self.capitals = tk.Checkbutton(self.window, text="Capital letters", variable = self.checkstate1)
        self.specials = tk.Checkbutton(self.window, text="Special characters", variable = self.checkstate2)
        self.button = tk.Button(self.window, text = "Generate new password", command=self.generate)
        self.label2 = tk.Label(self.window, text = "")
        self.button2 = tk.Button(self.window, text = "Copy password to clipboard", command=self.clipboard)

        #Column 2
        self.label3 = tk.Label(self.window, text = "Password history", font= ('Arial, 18'))
        self.button3 = tk.Button(self.window, text = "Save password to file", command=self.save1)
        self.button4 = tk.Button(self.window, text = "Save all recent passwords to file", command=self.save2)

        #Place everything on the grid (Column 1)
        self.label.grid(row=0,column=0, sticky="nsew")
        self.horizontal.grid(row=1,column=0, padx = 50, sticky="nsew")
        self.capitals.grid(row=2,column=0, sticky="nsew")
        self.specials.grid(row=3,column=0, sticky="new")
        self.button.grid(row=4,column=0, padx = 50, sticky="new")
        self.label2.grid(row=5,column=0,sticky="new")
        self.button2.grid(row=6,column=0, padx = 50, sticky="new")

        #Place everything on the grid (Column 2)
        self.label3.grid(row=0,column=1,sticky="nsew")
        self.button3.grid(row=2,column=1, padx = 50, sticky="new")
        self.button4.grid(row=6,column=1, padx = 50, sticky="new")
        
        self.window.mainloop()

    def fix(self, ok):
        self.generate()

    def clipboard(self):
        #Check if pyperclip is installed and if password is empty
        try:
            pyperclip.copy(password)
        except NameError:
            pass
        except:
            messagebox.showinfo(title = "Error", message="Pyperclip is not installed! At the command prompt type: pip install pyperclip")
        finally:
            if password != passList[0]:
                self.history()

    def read(self):
        global words
        words = []
        try:
            filer = open("Password history.txt", 'r')
            for item in filer:
                words.append(item.strip('\n'))
        #Make the file if it doesnt exist
        except:
            filew = open("Password history.txt", 'w')
            filew.close()

    #Save only 1 password
    def save1(self): 
        #Ensure that password variable isn't empty with try/except
        try:
            #Ensure password isn't already in passlist
            if passList[0] != password:    
                #Add to the passlist
                self.history()
                #Add to words
                words.insert(0, password)
        except:
            pass

        filew = open("Password history.txt", 'w')
        for item in words:
            filew.write(item + "\n")
        filew.close()
        return

    #Save all recent passwords
    def save2(self): 
        for item in passList[::-1]:
            #Esnure items in passlist aren't empty and aren't in words already
            if item and item not in words:
                #Add to words
                words.insert(0, item)

        filew = open("Password history.txt", 'w')
        for item in words:
            filew.write(item + "\n")
        filew.close()
        return
    
#Password generation and display is done here
    def generate(self):
        global password
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

        self.label2 = tk.Label(self.window, text = password ,font= ('Arial', '10'))
        self.label2.grid(row=5,column=0,sticky="NEW")

        self.passHistory1 = tk.Label(self.window, text = password ,font= ('Arial, 10'))
        self.passHistory1.grid(row=1,column=1,sticky="nsew")

    def history(self):
         #---------------------------Password history---------------------------#
        #Move the old password down
        passList[2] = passList[1]
        passList[1] = passList[0]
        passList[0] = password

        #Define labels to show the password history
        self.passHistory2 = tk.Label(self.window, text = passList[0] ,font= ('Arial, 10'))
        self.passHistory3 = tk.Label(self.window, text = passList[1] ,font= ('Arial, 10'))
        self.passHistory4 = tk.Label(self.window, text = passList[2] ,font= ('Arial, 10'))

        self.passHistory2.grid(row=3,column=1,sticky="NEW")
        self.passHistory3.grid(row=4,column=1,sticky="NEW")
        self.passHistory4.grid(row=5,column=1,sticky="NEW")
        
GUI()                                             
