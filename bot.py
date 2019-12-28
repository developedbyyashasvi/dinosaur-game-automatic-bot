from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn = (480,500)
    dinosaur = (187,510)

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.01)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Coordinates.dinosaur[0]+70, Coordinates.dinosaur[1], Coordinates.dinosaur[0]+100, Coordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

restartGame()

while True:
    if (imageGrab()!= 1146):
        pressSpace()
        time.sleep(0.1)

#def main():
    #restartGame()
    #while True:
        #if(imageGrab()==1146):
            #pressSpace()
            #time.sleep(0.1)