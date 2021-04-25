# Anime Censor

![alt text](https://github.com/mh5001/Anime-Censor/blob/main/screenshots/record.gif?raw=true)

## Description

Screen is recorded and a cascade for Anime character was used to detect pictures on screen. `PySimpleGUI` is then used to draw a black box around the location of the image. However, after drawing the box, the detection will not work anymore, as the image is censored. Therefore, a `Timer` from `threading` was implemented to periodically update the screen.