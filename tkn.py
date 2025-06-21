# Install mysql-connector-python by running the command: pip install mysql-connector-python
# Install tkinter by running the command: pip install tk
# Install pyodbc by running the command: pip install pyodbc
# Be sure you have already installed mysql and microsft sql server in your computer...
# By : Saad Almalki


from tkinter import *
import mysql.connector
import pyodbc
import threading
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)




def show_mysqldatabases():
    def task():
        try:
            L.config(text="Loading...")  # Show loading message
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES")
            databases = "\n".join([db[0] for db in cursor.fetchall()])
            L.config(text=databases)
            conn.close()
        except Exception as e:
            L.config(text=f"Error: {e}")

    threading.Thread(target=task).start()

def showmssqldatabases():
    def task():
        try:
            L.config(text="Loading...")  # Show loading message
            conn_str = (
                "DRIVER={SQL Server};"
                "SERVER=localhost;"
                "Trusted_Connection=yes;"
            )
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM master.sys.databases")
            databases = "\n".join([row[0] for row in cursor.fetchall()])
            L.config(text=databases)
            conn.close()
        except Exception as e:
            L.config(text=f"MSSQL Error: {e}")

    threading.Thread(target=task).start()

def connect_to_database():
    db_name = En1.get()
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=db_name
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = "\n".join([tbl[0] for tbl in cursor.fetchall()])
        L.config(text=f"Connected to '{db_name}':\n\n{tables}")
        conn.close()
    except Exception as e:
        L.config(text=f"Connection Error: {e}")

root = Tk()
root.geometry(f"{1010*2}x{550*2}+200+40")
root.resizable(False, False)
root.configure(bg='white')
root.title("Database Connector")
root.iconbitmap('images/logodb.ico')

title1 = Label(root, text="Database Connector", font=("dubai", 20, "bold"), bg="white", fg="white")
title1.pack(side=TOP, fill=X)

F1 = Frame(root, bg="black", bd=5, relief=GROOVE)
F1.place(x=10, y=50, width=990*2, height=520*2)

L = Label(F1, text="Your Databases", font=("dubai", 15, "bold"), bg="black", fg="white", wraplength=1900, justify=LEFT)
L.pack(side=TOP, fill=X, padx=20, pady=10)

button1 = Button(F1, text="Show MySQL Databases", font=("dubai", 15, "bold"), bg="black", fg="white", command=show_mysqldatabases)
button1.pack(side=TOP, fill=X, padx=10, pady=10)

button2 = Button(F1, text="Show MSSQL Databases", font=("dubai", 15, "bold"), bg="black", fg="white", command=showmssqldatabases)
button2.pack(side=TOP, fill=X, padx=10, pady=10)

L1 = Label(F1, text="Database Name", font=("dubai", 15, "bold"), bg="black", fg="white")
L1.pack(side=LEFT, fill=X)

En1 = Entry(F1, font=("dubai", 15, "bold"), bg="black", fg="white")
En1.pack(side=LEFT, fill=X)

def on_enter(e):
    e.widget.config(bg="gray", fg="black")

def on_leave(e):
    e.widget.config(bg="black", fg="white")

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)

root.mainloop()
