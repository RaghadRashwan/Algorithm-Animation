"""
Created on Wed Apr  6 07:33:56 2022

@author: areejalsini
"""

#Ref: https://pythonguides.com/python-tkinter-animation/

import tkinter
import time
 

Window_Width=500

Window_Height=400

min_movement = 5

Refresh_Sec = 0.01
 



def create_animation_window():
  Window = tkinter.Tk()
  Window.title("Algorithm result")
  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window
 

def create_animation_canvas(Window):
  canvas = tkinter.Canvas(Window)
  canvas.configure(bg="antiquewhite1")
  canvas.pack(fill="both", expand=True)
  return canvas
 

def animate(Window, canvas,xinc,yinc,textini):
  texty = canvas.create_text(20,20,fill="darkblue",font="Times 20 italic bold",
                        text=textini)
  while True:
    canvas.move(texty,xinc,yinc)
    Window.update()
    time.sleep(Refresh_Sec)
    texty_pos = canvas.coords(texty)
    # unpack array to variables
    al,bl = texty_pos
    if al >=500 or al<=0 :
      xinc = -xinc
    if bl >=400 or bl<=0 :
      yinc = -yinc




