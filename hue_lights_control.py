try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
   # for Python3
    from tkinter import *

from phue import Bridge

# To find the bridge if please visit https://www.meethue.com/api/nupnp
BRIDGE_IP = '192.168.0.101'

WHITE_SATURATION = 77
WHITE_HUE = 41435
WHITE_BRIGHTNESS = 100

RED_SATURATION = 255
RED_HUE = 65280
RED_BRIGHTNESS = 191

GREEN_SATURATION = 255
GREEN_HUE = 25500
GREEN_BRIGHTNESS = 255

BLUE_SATURATION = 255
BLUE_HUE = 46920
BLUE_BRIGHTNESS = 213


b = Bridge(BRIDGE_IP)
b.connect()

lights = b.lights


def switch_white(event):
    print("white")
    for l in lights:
        l.on = True
        l.saturation = WHITE_SATURATION
        l.hue = WHITE_HUE
        l.brightness = WHITE_BRIGHTNESS


def switch_red(event):
    print("red")
    for l in lights:
        l.on = True
        l.saturation = RED_SATURATION
        l.hue = RED_HUE
        l.brightness = RED_BRIGHTNESS


def switch_green(event):
    print("green")
    for l in lights:
        l.on = True
        l.saturation = GREEN_SATURATION
        l.hue = GREEN_HUE
        l.brightness = GREEN_BRIGHTNESS


def switch_blue(event):
    print("blue")
    for l in lights:
        l.on = True
        l.saturation = BLUE_SATURATION
        l.hue = BLUE_HUE
        l.brightness = BLUE_BRIGHTNESS


def switch_off(event):
    print("off")
    for l in lights:
        l.on = False


root = Tk()

btn_height = 5
btn_width = 10

btn_white = Button(root, text='White', height=btn_height, width=btn_width)
btn_red = Button(root, text='Red', height=btn_height, width=btn_width)
btn_green = Button(root, text='Green', height=btn_height, width=btn_width)
btn_blue = Button(root, text='Blue', height=btn_height, width=btn_width)
btn_off = Button(root, text='Off', height=btn_height, width=btn_width)

btn_white.pack(side='bottom')
btn_red.pack(side='left')
btn_green.pack(side='top')
btn_blue.pack(side='right')
btn_off.pack(side='bottom')

btn_white.grid(row=1)
btn_red.grid(row=2)
btn_green.grid(row=3)
btn_blue.grid(row=4)
btn_off.grid(row=5)

btn_white.bind("<Button-1>", switch_white)
btn_red.bind("<Button-1>", switch_red)
btn_blue.bind("<Button-1>", switch_blue)
btn_green.bind("<Button-1>", switch_green)
btn_off.bind("<Button-1>", switch_off)

root.mainloop()
