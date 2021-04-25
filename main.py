import cv2
import sys
import time
from threading import Timer
import numpy
from mss import mss
import os.path
import PySimpleGUI as sg

cascade = cv2.CascadeClassifier("./cascade.xml")
sct = mss()

isRunning = True

prevFaces = []
windows = []

def clearWindows():
    for window in windows:
        window.CloseNonBlocking()
    windows.clear()

def newWindow(x, y, w, h):
    window = sg.Window('', no_titlebar=True, keep_on_top=True, location=(x, y), size=(w, h))
    window.Layout([[]])
    window.BackgroundColor = "black"

    windows.append(window)

def isSame(arr1, arr2):
    if len(arr1) == len(arr2):
        length = len(arr1)
        for i in range(length):
            for j in range(4):
                if (abs(arr1[i][j] - arr2[i][j]) > 5): return False
    else:
        return False
    
    return True

i = 0
while isRunning:
    array = numpy.array(sct.grab({"top": 0, "left": 0, "width": 1920, "height": 1080}))
    gray = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    for window in windows: window._ReadNonBlocking()

    faces = cascade.detectMultiScale(gray)
    if len(faces) > 0:
        if len(prevFaces) > 0:
            if not isSame(faces, prevFaces):
                clearWindows()
                for face in faces: newWindow(face[0], face[1], face[2], face[3])
        else:
            for face in faces: newWindow(face[0], face[1], face[2], face[3])

    prevFaces = faces

    i += 1
    if i > 50:
        clearWindows()
        i = 0
