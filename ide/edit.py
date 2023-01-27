"""
Based off of my Text editor: https://github.com/Electro-Corp/Python-Text-Editor/blob/main/main.py
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Frame, Menu
import tkinter.font as font
from tkinter import *
import os
import editor as t    
root = tk.Tk()
root.title("GOOFY AHH IDE")
root.geometry("350x300")
app = t.TextEditor(root)
tk.mainloop()