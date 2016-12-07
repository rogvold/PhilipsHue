#from tkinter import *

from phue import Bridge

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *


b = Bridge('192.168.0.100')
b.connect()

lights = b.lights


def switch_white(event):
    for l in lights:
        print("white")
        l.saturation = 77
        l.hue = 41435
        # 100 for white
        l.brightness = 100


def switch_red(event):
    for l in lights:
        print("red")
        # l.xy = converter.rgbToCIE1931(red=255, green=0, blue=0)
        l.saturation = 255
        l.hue = 65280
        # 191 for red
        # 100 for white
        l.brightness = 191


def switch_green(event):
    print("green")
    for l in lights:
        # l.xy = converter.rgbToCIE1931(red=0, green=255, blue=0)
        l.saturation = 255
        l.hue = 25500
        l.brightness = 255


def switch_blue(event):
    print("blue")
    for l in lights:
        # l.xy = converter.rgbToCIE1931(red=0, green=0, blue=255)
        l.hue = 46920
        l.saturation = 255
        # brightness 213
        l.brightness = 213

root = Tk()

btn_white = Button(root, text='White')
btn_red = Button(root, text='Red')
btn_green = Button(root, text='Green')
btn_blue = Button(root, text='Blue')

btn_white.pack(side='bottom')
btn_red.pack(side='left')
btn_green.pack(side='top')
btn_blue.pack(side='right')

btn_white.bind("<Button-1>", switch_white)
btn_red.bind("<Button-1>", switch_red)
btn_blue.bind("<Button-1>", switch_blue)
btn_green.bind("<Button-1>", switch_green)

root.mainloop()
