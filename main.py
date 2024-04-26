# main.py

from tkinter import Tk
from view import View

if __name__ == "__main__":
    root = Tk()
    root.title("Menu Driven Program")
    app = View(root)
    root.mainloop()

