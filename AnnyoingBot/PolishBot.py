import pyautogui
import time
a = 0
while True:
    file = open("NUMBERS.txt", "w+")
    file.truncate(0)
    a += 1
    file.write(str(a))
    time.sleep(0.5)
    like = pyautogui.locateOnScreen("Likeicon.png", confidence=0.8)
    if like == None:
        pass
        pyautogui.click(x=1709, y=148)
    else:
        time.sleep(0.3)
        pyautogui.click(like)
        time.sleep(0.7)
        pyautogui.click(x=1709, y=148)
        IkonkaKoma = pyautogui.locateOnScreen("Ikonakoma.png", confidence=0.8)
        if IkonkaKoma == None:
            pass
            pyautogui.click(x=1709, y=148)
        else:
            time.sleep(0.4)
            pyautogui.click(IkonkaKoma)
            time.sleep(1)
            pyautogui.typewrite("I'm a bot, please add me to your friends I want to see how long will it take for facebook to take me down. " + str(a), interval=0.25)
            pyautogui.sleep(0.8)
            pyautogui.press('enter')
            time.sleep(0.9)
            pyautogui.click(x=1709, y=148)
            time.sleep(1)
            friend = pyautogui.locateOnScreen("FriendRequest.png", confidence=0.8)
            if friend == None:
                pass
                pyautogui.click(x=1709, y=148)
            else:
                pyautogui.click(friend)
                time.sleep(2)
                accept = pyautogui.locateOnScreen("accept.png", confidence=0.8)
                time.sleep(1)
                pyautogui.click(accept)
                time.sleep(0.5)
                pyautogui.click(x=1709, y=148)
    time.sleep(0.2)
    pyautogui.click(x=1709, y=148)
    time.sleep(0.3)
    pyautogui.press("pagedown")
    time.sleep(1)