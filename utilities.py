import tkinter as tk


# Window center.
def window_center(root):
    root.update_idletasks()

    width = 1024  # root.winfo_width()
    height = 768  # root.winfo_height()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y - 50}")


def new_window_center(root):
    root.update_idletasks()

    width = 768  # root.winfo_width()
    height = 500  # root.winfo_height()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y - 50}")


# Error loader draw.
def xml_load_error(root):
    tk.Label(
        root,
        text="File not found or invalid XML file.",
        background="#ff6666",
        font=("Helvetica", 8, "bold"),
    ).pack()


def xml_save_error(root):
    tk.Label(
        root,
        text="Saving error.",
        background="#ff6666",
        font=("Helvetica", 8, "bold"),
    ).pack()
