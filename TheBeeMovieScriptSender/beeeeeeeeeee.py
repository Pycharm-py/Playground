from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
text = open("bee.txt", "r")
wut = text.read().split(" ")
time.sleep(1)
for i in wut:
    time.sleep(0.2)
    keyboard.type(i)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    if i == 'that..':
        break
