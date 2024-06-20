import os
import tkinter as tk
from gui import ComboFinder

if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("940x600+200+200")
  root.configure(bg='#f5f5f5')
  app = ComboFinder(root)
  root.mainloop()
