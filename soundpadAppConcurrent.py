# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a sound board app. It supports 2 types of buttons:
    1. buttons that can be pressed multiple times
    2. buttons that, when ctrl-keyed, stop
In linux, the numpad are the keybinds.
Windows may have keybind issues. The file paths may also need to be different.

It is easy to get sound samples from http://bbcsfx.acropolis.org.uk/
(for personal use)
"""

#import libraries
import tkinter
from pygame import mixer
import os

#define playing/stopping a sound
#don't load sounds until the first time they're used
#once used, sounds remain ready to be played
#the stop sound probably doesnt need to be able to add files but better than an error
_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    new_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = mixer.Sound(new_path)
    _sound_library[path] = sound
  sound.play()
  
def stop_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    new_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = mixer.Sound(new_path)
    _sound_library[path] = sound
  sound.stop()
  
  

  
#start interacting with the OS's sound system
mixer.init()

#here is where you define the files to be played
def btnClick0():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07043052.wav')
def btnClick1():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07043302.wav')
def btnClick2():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07045226.wav')
def btnClick3():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07045249.wav')
def btnClick4():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07071032.wav')
def btnClick5():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07043163.wav')
def btnClick6():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07074120.wav')
def btnClick7():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07055186.wav')
def btnClick8():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07058170.wav')
def btnClick9():
    play_sound(r'/media/AltDrive/Music/Sound Effects/07018034.wav')
def btnClick9ctl():
    stop_sound(r'/media/AltDrive/Music/Sound Effects/07018034.wav')






#initialize and lay out the GUI
window = tkinter.Tk()
window.title('Experimental Soundboard')
window.geometry('800x500')
lbl = tkinter.Label(window, text="Click for some sounds, brother")    
lbl.grid(column=0, row=0)

#make the buttons and set the keybinds
btn0 = tkinter.Button(window, text="Laughter", command = btnClick0)
window.bind('<KP_0>', lambda x: btnClick0())
btn1 = tkinter.Button(window, text="Laser", command = btnClick1)
window.bind('<KP_1>', lambda x: btnClick1())
btn2 = tkinter.Button(window, text="Cat Yowl", command = btnClick2)
window.bind('<KP_2>', lambda x: btnClick2())
btn3 = tkinter.Button(window, text="Car Skid", command = btnClick3)
window.bind('<KP_3>', lambda x: btnClick3())
btn4 = tkinter.Button(window, text="Phewww-Bonk", command = btnClick4)
window.bind('<KP_4>', lambda x: btnClick4())
btn5 = tkinter.Button(window, text="Breaking Glass", command = btnClick5)
window.bind('<KP_5>', lambda x: btnClick5())
btn6 = tkinter.Button(window, text="Breaking Plates", command = btnClick6)
window.bind('<KP_6>', lambda x: btnClick6())
btn7 = tkinter.Button(window, text="Double Honk", command = btnClick7)
window.bind('<KP_7>', lambda x: btnClick7())
btn8 = tkinter.Button(window, text="Record Scratch", command = btnClick8)
window.bind('<KP_8>', lambda x: btnClick8())
btn9 = tkinter.Button(window, text="Booing, ctrl for stop", command = btnClick9)
window.bind('<KP_9>', lambda x: btnClick9())
window.bind('<Control-KP_9>', lambda x: btnClick9ctl())

#draw the buttons in their correct spots to match numpad
btn0.grid(column=1, row=3)
btn1.grid(column=1, row=2)
btn2.grid(column=2, row=2)
btn3.grid(column=3, row=2)
btn4.grid(column=1, row=1)
btn5.grid(column=2, row=1)
btn6.grid(column=3, row=1)
btn7.grid(column=1, row=0)
btn8.grid(column=2, row=0)
btn9.grid(column=3, row=0)

#display the gui
window.mainloop()


