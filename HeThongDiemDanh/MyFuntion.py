from tkinter import Tk


def CenterWindowToDisplay(Screen: Tk, width: int, height: int):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    return f"{width}x{height}+{x}+{y}"