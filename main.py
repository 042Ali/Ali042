import turtle
import keyboard

ninja = turtle.Turtle()

while True:
    if keyboard.is_pressed("w"):
        ninja.forward(10)
        
    if keyboard.is_pressed("d"):
        ninja.left(20)
        
    if keyboard.is_pressed("esc"):
        break    