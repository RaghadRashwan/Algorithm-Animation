import time
import tkinter as tk
import tkinter.simpledialog
import tkinter.dialog
from randomMedian import *
from MedianSelect import *
from tkinter import messagebox
from animation import *



def but1Action():
    size = int(tkinter.simpledialog.askstring(title="Input Size"
    ,prompt="Enter input size"))
    arr=generateRandomArray(size)
    k=int(tkinter.simpledialog.askstring(title="rank",prompt="Enter input rank"))
    sTime=time.time()*10000000
    rank=Select(arr,0,size-1,k)
    eTime=(time.time()*10000000)-sTime
    messagebox.showinfo("Result",str(rank)+" Time of excution: "+str(eTime))
    Animation_Window = create_animation_window()
    Animation_canvas = create_animation_canvas(Animation_Window)
    animate(Animation_Window,Animation_canvas, 5, 5," Time of excution:\n"+str(eTime))

def but2Action():
    size =int( tkinter.simpledialog.askstring(title="Input Size",prompt="Enter input size"))
    arr=generateRandomArray(size)
    sTime=time.time()*10000000
    quickSelect(arr,0,size-1)
    eTime=(time.time()*10000000)-sTime
    saveArray("medianQS.txt",arr)
    messagebox.showinfo("Result","Array Sorted and saved in txt file Time of excution: "+str(eTime))
    Animation_Window = create_animation_window()
    Animation_canvas = create_animation_canvas(Animation_Window)
    animate(Animation_Window,Animation_canvas, 5, 5," Time of excution:\n"+str(eTime))

def but3Action():
    size = int(tkinter.simpledialog.askstring(title="Input Size",prompt="Enter input size"))
    arr=generateRandomArray(size)
    k=int(tkinter.simpledialog.askstring(title="rank",prompt="Enter input rank"))
    sTime=time.time()*10000000
    rank=findKthLargest(arr,k,0,size-1)
    eTime=(time.time()*10000000)-sTime
    messagebox.showinfo("Result",str(rank)+" Time of excution: "+str(eTime))
    Animation_Window = create_animation_window()
    Animation_canvas = create_animation_canvas(Animation_Window)
    animate(Animation_Window,Animation_canvas, 5, 5," Time of excution:\n"+str(eTime))

def but4Action():
    size = int(tkinter.simpledialog.askstring(title="Input Size",prompt="Enter input size"))
    arr=generateRandomArray(size)
    sTime=time.time()*10000000
    quickRandomSelect(arr,0,size-1)
    eTime=(time.time()*10000000)-sTime
    saveArray("medianRandomQS.txt",arr)
    messagebox.showinfo("Result","Array Sorted and saved in txt file Time of excution: "+str(eTime))
    Animation_Window = create_animation_window()
    Animation_canvas = create_animation_canvas(Animation_Window)
    animate(Animation_Window,Animation_canvas, 5, 5," Time of excution:\n"+str(eTime))


 
window = tk.Tk()
window.geometry('300x400')

window.rowconfigure([0,1,2,3], minsize=50)
window.columnconfigure(0, minsize=270)

label1 = tk.Label(text="Median Selection", bg="aquamarine4", fg="white")
label2 = tk.Label(text="Quick Sort ", bg="aquamarine4", fg="white")
label3 = tk.Label(text="Randomized Median Selection ", bg="aquamarine4", fg="white")
label4 = tk.Label(text="Quick Sort ", bg="aquamarine4", fg="white")

label1.grid(row=0, column=0, sticky="w", padx=10, pady=10)
label2.grid(row=1, column=0, sticky="w", padx=10, pady=10)
label3.grid(row=2, column=0, sticky="w", padx=10, pady=10)
label4.grid(row=3, column=0, sticky="w", padx=10, pady=10)

button1=tk.Button(text='Run',command = but1Action)
button2=tk.Button(text='Run',command = but2Action)
button3=tk.Button(text='Run',command = but3Action)
button4=tk.Button(text='Run',command = but4Action)
button1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
button2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
button3.grid(row=2, column=0, sticky="e", padx=10, pady=10)
button4.grid(row=3, column=0, sticky="e", padx=10, pady=10)

window.mainloop()

