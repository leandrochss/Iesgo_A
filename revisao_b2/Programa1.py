import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Create a SQLite database and a users table
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()

class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Gestão de Usuários")

        self.tree = ttk.Treeview(root, columns=('ID', 'Username', 'Email'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Username', text='Usuário')
        self.tree.heading('Email', text='E-mail')
        self.tree.pack(padx=30, pady=10)

        self.load_data()

        add_button = tk.Button(root, text='Adicionar', command=self.show_add_user_window)
        add_button.pack(pady=10)

        delete_button = tk.Button(root, text='Remover', command=self.delete_user)
        delete_button.pack(pady=10)

    def load_data(self):
        # Fetch data from the database and populate the treeview
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def show_add_user_window(self):
        add_user_window = tk.Toplevel(self.root)
        add_user_window.title('Add User')

        username_label = tk.Label(add_user_window, text='Username:')
        username_label.grid(row=0, column=0, padx=10, pady=10)
        username
