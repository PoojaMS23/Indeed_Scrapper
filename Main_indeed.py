import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
from tensorflow.python import keras
print(keras.__version__)
import tensorflow as tf
print(tf.keras.__version__)


import Crawler as CR
import pandas as pandas

bgcolor="#A9DAE1"
bgcolor1="#000000"
fgcolor="#83A9AF"
print(pandas.__version__)

window = tk.Tk()
window.title("Indeed Job Posts Scrapper")

 
window.geometry('720x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
	

message1 = tk.Label(window, text="Indeed Job Posts Scrapper" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 25, 'italic bold underline')) 
message1.place(x=9, y=9)


def clear():
	print("Clear1")
	txt.delete(0, 'end') 
	
def Craw():
	CR.process()	
	tm.showinfo("Input error", "Finished")	

proc3 = tk.Button(window, text="Crawler", command=Craw  ,fg=fgcolor  ,bg=bgcolor1  ,width=16  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
proc3.place(x=300, y=300)


quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=300, y=500)

window.mainloop()

