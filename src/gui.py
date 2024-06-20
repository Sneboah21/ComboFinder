import tkinter as tk
from tkinter import *
from tkinter import filedialog
from utils.readfile import read_file
from combofind import result


class ComboFinder:
  #constructor
  def __init__(self,master): #master is the root
    self.master = master
    self.file_path = ''
    master.title("Combo Finder")
    self.vcmd = (self.master.register(self.validate_number),'%P')
    self.gui_interface(self.master)
    #Registers the validation function and creates a validation command. %P passes the new value of the entry widget to the validation function.


  def gui_interface(self,master):
    tk.Label(master, text="File Name").grid(row=0,column=0,padx=20,pady=10)
    self.browse_entry = tk.Entry(master,width=40)
    self.browse_entry.grid(row=0,column=1,padx=20,pady=10)

    self.browse_button = tk.Button(master, text="Browse File...", command=self.browse_file, width=15,height=5, bg='lightblue',fg='black')
    self.browse_button.grid(row=0,column=2,padx=20,pady=10)
    self.browse_entry = tk.Entry(master,width=40)
    self.browse_entry.grid(row=0,column=3)
    #We use either pack or grid
    tk.Label(master, text="Lower Limit").grid(row=1,column=0,padx=20,pady=35)
    self.lower_limit_entry = tk.Entry(master, width=10, validate="key", validatecommand=self.vcmd)
    self.lower_limit_entry.grid(row=1,column=1,padx=20,pady=35)

    tk.Label(master, text="Upper Limit").grid(row=1,column=2,padx=20,pady=35)
    self.upper_limit_entry = tk.Entry(master,width=10,validate="key",validatecommand=self.vcmd)
    self.upper_limit_entry.grid(row=1,column=3,padx=20,pady=35)

    tk.Label(master, text="Email Id").grid(row=2,column=0,padx=20,pady=35)
    self.email_entry = tk.Entry(master,width=40)
    self.email_entry.grid(row=2,column=1,padx=20,pady=35)

    self.submit_button = tk.Button(master, text="Submit", command=self.submit, bg='red', fg='white', width=15,height=2)
    self.submit_button.grid(row=3,column=2,pady=30)
    #Text widget to display the text
    self.result_text = tk.Text(master, height=10, width=85)
    self.result_text.grid(row=4, column=1, columnspan=8, padx=20, pady=20)



  def browse_file(self):
    file_path = filedialog.askopenfilename(initialdir="files", title="Browse File", filetypes=(("Text files", "*.txt; *.csv"),("all files", "*.*")))
    if file_path:
      self.file_path = file_path #instance variable(they are associated with class)
      read_file(self.file_path)
      self.browse_entry.delete(0, tk.END)
      self.browse_entry.insert(0, self.file_path) # To insert the file path in the entry
  
  def validate_number(self, input_value): #allows only digits to be entered 
    if input_value.isdigit() or input_value == "":
      return True
    else:
      return False
  
  def submit(self):
    self.file_name = self.browse_entry.get()
    self.lower_limit = int(self.lower_limit_entry.get())
    self.upper_limit = int(self.upper_limit_entry.get())
    self.email_id = self.email_entry.get()
    # Here you can add the code to handle the form submission
    self.combos, self.size = result(self.file_path, self.upper_limit, self.lower_limit)
    self.result_text.delete(1.0, tk.END) #1 means first line and 0 means 1st character in that line
    self.result_text.insert(tk.END, "Output:\n\n") #inserts string

    for combo in self.combos:
      self.result_text.insert(tk.END, str(combo) + "\n")
    self.result_text.insert(tk.END, "Total sets: " + str(self.size)+"\n")
