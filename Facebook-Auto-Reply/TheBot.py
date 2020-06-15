import pyautogui
import datetime
import time
while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    start = '00:00:00'  # midnight
    end = '09:00:00'  # 9 A.M.
    x = pyautogui.locateOnScreen("Xbutton.png", confidence=0.8)
    message = pyautogui.locateOnScreen("TheMessagePoll.png", confidence=0.8)
    # If current time is between "start" and "end"
    if start < current_time < end:
        time.sleep(0.1)
        pyautogui.moveTo(x)
        pyautogui.click(x)
        time.sleep(0.2)
        pyautogui.click(x=1684, y=165)  # Change that for your resolution (It should click on any clear field like the end that blue bar on the top)
        time.sleep(0.2)
        pyautogui.moveTo(message)
        pyautogui.click(message)
        pyautogui.write("I'm sleeping... Text to me later", interval=0.2)  # the message
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.click(x=1684, y=165)  # Change that for your resolution (It should click on any clear field like the end that blue bar on the top)
    else:
        time.sleep(0.2)
        pyautogui.click(x=1684, y=165)  # Change that for your resolution (It should click on any clear field like the end that blue bar on the top)
        pyautogui.moveTo(x)
        time.sleep(0.1)
        pyautogui.click(x)
        time.sleep(0.2)
        pyautogui.moveTo(message)
        pyautogui.click(message)
        time.sleep(0.2)
        pyautogui.click(x=1684, y=165)  # Change that for your resolution (It should click on any clear field like the end that blue bar on the top)
