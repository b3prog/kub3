import psycopg2
import tkinter as tk
from tkinter import ttk, messagebox
from trainschedule import TrainScheduleApp
from auth import register, login
from docx import Document
from utils import center_window, RoundedButton

class AuthWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Аутентификация")
        center_window(self.root, 0.17, 0.11)

        style = ttk.Style()
        style.configure("TLabel", font=("bahnschrift semilight", 12))
        style.configure("TEntry", font=("bahnschrift semilight", 12))

        # Добавление элементов интерфейса
        username_label = ttk.Label(root, text="Имя пользователя:")
        username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = ttk.Entry(root, style="TEntry")
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = ttk.Label(root, text="Пароль:")
        password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = ttk.Entry(root, show='*', style="TEntry")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        RoundedButton(root, text="Войти", command=self.handle_login, width=130, height=32).grid(row=2, column=0,
                                                                                                padx=10, pady=10)
        RoundedButton(root, text="Регистрация", command=self.handle_register, width=130, height=32).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = login(username, password)
        if success:
            self.root.destroy()
            self.open_main_app()
        else:
            messagebox.showerror("Ошибка", message)

    def handle_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = register(username, password)
        if success:
            messagebox.showinfo("Регистрация прошла успешно!", message)
        else:
            messagebox.showerror("Ошибка", message)

    def open_main_app(self):
        root = tk.Tk()
        app = TrainScheduleApp(root)
        root.mainloop()

if __name__ == "__main__":
        root = tk.Tk()
        auth_window = AuthWindow(root)
        root.mainloop()