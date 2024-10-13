import tkinter as tk

def center_window(window, width_ratio, height_ratio):
    """Центрирует окно на экране."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = int(screen_width * width_ratio)
    height = int(screen_height * height_ratio)
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

class RoundedButton(tk.Canvas):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.text = text

        # Установите размеры и закругление
        self.width = kwargs.get('width', 150)
        self.height = kwargs.get('height', 50)
        self.corner_radius = 25  # Увеличьте радиус

        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

        self.draw_button()

    def draw_button(self):
        self.delete("all")
        self.create_rounded_rectangle(0, 0, self.width, self.height, self.corner_radius, fill="#767d89", outline="")
        self.create_text(self.width / 2, self.height / 2, text=self.text, fill="white", font=('bahnschrift bold', 10))

        self.config(width=self.width, height=self.height)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1, x2, y1 + radius,
            x2, y2 - radius, x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2, x1, y2 - radius,
            x1, y1 + radius, x1, y1
        ]
        self.create_polygon(points, **kwargs, smooth=True)

    def on_click(self, event):
        if self.command:
            self.command()

    def on_enter(self, event):
        self.create_rounded_rectangle(0, 0, self.width, self.height, self.corner_radius, fill="#e21a1a", outline="")
        self.create_text(self.width / 2, self.height / 2, text=self.text, fill="white", font=('bahnschrift bold', 10))

    def on_leave(self, event):
        self.draw_button()
