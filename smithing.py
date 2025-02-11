import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")

def ironChest():

    # click on anvil
    points = [1334,504]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)

    # click on iron plate
    points = [782,563]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(15)

    # click bank booth
    points = [495,630]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)   

    # click on iron plate in inventory
    points = [1761,871]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    # click on iron bar in bank
    points = [759,692]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    # repeat
    ironChest()

def smeltCannonBalls():
    # click on furnance
    points = [1367,410]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(6)
    # click on cannonball in menu
    points = [262,1080]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(75)
    # click on bank booth
    points = [454,815]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(6)
    # click on steel bar
    points = [1006,275]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # time.sleep(1)
    # repeat
    smeltCannonBalls()



def close():
   root.destroy()
#    root.quit()

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startIronChestButton = Button(root, text="Start iron chest", command=ironChest)
startIronChestButton.pack()

startSmeltCannonBallsButton = Button(root, text="Start cannonballs", command=smeltCannonBalls)
startSmeltCannonBallsButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()