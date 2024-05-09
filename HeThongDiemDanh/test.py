from tkinter import Tk
from MyFuntion import *

# Sử dụng hàm để đặt cửa sổ chính vào giữa màn hình
root = Tk()
root.geometry(CenterWindowToDisplay(root, 800, 500))
root.mainloop()