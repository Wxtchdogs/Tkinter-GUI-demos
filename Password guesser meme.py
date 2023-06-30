import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1200x900")
        self.window.title("Password guesser v1")

        self.label = tk.Label(self.window, text="Enter your password", font= ('Arial, 18'))
        self.label.pack(padx=20, pady =30)

        self.textbox = tk.Text(self.window, height = 3, font= ('Arial, 10'))
        self.textbox.pack(padx=300)

        self.checkstate = tk.IntVar()
        self.check = tk.Checkbutton(self.window, text="Magic checkbox", variable = self.checkstate)
        self.check.pack()

        self.button = tk.Button(self.window, text = "Find your password", command=self.show_message)
        self.button.pack(pady=10)
        self.window.mainloop()

    def show_message(self):
        print(self.textbox.get('1.0', tk.END))
        if self.checkstate.get() != 0:
            messagebox.showinfo(title = "Password guesser v1", message="Your password is "+self.textbox.get('1.0', tk.END))
        else: 
            "nil"
         
GUI()                                                                                                                                                                                                                                                           