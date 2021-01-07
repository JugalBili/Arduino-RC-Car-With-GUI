import serial # pip install pyserial
from tkinter import *
import time

#Initializes main Tkinter window
root = Tk()
root.geometry("600x350")

# initializes serial communication with COM3 
ser = serial.Serial("COM3", 9600)


# Function runs when keyboard input is recieved
def key_press(event):
    #Forward
    if event.char == "w":
        ser.write(b'w')   # send the byte string 'w'

    #Backwards
    elif event.char == "s":
        ser.write(b's')   # send the byte string 's'

    #Left
    elif event.char == "a":
        ser.write(b'a')   # send the byte string 'a'

    #Right
    elif event.char == "d":
        ser.write(b'd')   # send the byte string 'd'
    else:
        pass

    time.sleep(0.045) #sleeps for 45ms after each input


# function called when right GUI button is pressed
def goRight():
    ser.write(b'd')

# function called when left GUI button is pressed
def goLeft():
    ser.write(b'a') 

# function called when forward GUI button is pressed
def goForward():
    ser.write(b'w') 

# function called when back GUI button is pressed
def goBack():
    ser.write(b's') 

#Diplays the 2 frames atatched to the main window
frame2 = LabelFrame(root, padx = 75, pady = 100)
frame = LabelFrame(root, padx = 100, pady = 100)
frame.pack(side = LEFT)
frame2.pack(side = RIGHT)
frame.focus_set()

# Creates button instances
buttonR = Button(frame, text = "←", padx = 20, pady = 20, font = (None, 15, "bold"), repeatdelay = 100, repeatinterval = 45, command = goRight)
buttonL = Button(frame, text = "→", padx = 20, pady = 20, font = (None, 15, "bold"), repeatdelay = 100, repeatinterval = 45, command = goLeft)
buttonF = Button(frame2, text = "↑", padx = 20, pady = 20, font = (None, 15, "bold"), repeatdelay = 100, repeatinterval = 45, command = goForward)
buttonB = Button(frame2, text = "↓", padx = 20, pady = 20, font = (None, 15, "bold"), repeatdelay = 100, repeatinterval = 45, command = goBack)

# Adds the buttons to the frames
buttonR.pack(side = LEFT)
Label(frame, padx = 10).pack(side =LEFT)
buttonL.pack(side = LEFT)

buttonF.grid(row = 1, column = 0)
Label(frame2, pady = 5).grid(row = 2, column = 0)
buttonB.grid(row = 3, column = 0)

#Binds keypress events to the frame
frame.bind("<Key>", key_press)
frame2.bind("<Key>", key_press)

root.mainloop()