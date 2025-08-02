from datetime import datetime
import database
import home
import tkinter as tk

def initialize_app():
    database.create_table()
    root = tk.Tk()
    app = home.App(root)
    root.mainloop()

if __name__ == "__main__":
    initialize_app()