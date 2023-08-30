import pyautogui
import time


screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

coors = pyautogui.locateOnScreen('chrome2.png', grayscale= True, confidence =0.9)
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x),(coors_center.y))

time.sleep(5)
coors = pyautogui.locateOnScreen('tim1.png', grayscale= True, confidence =0.9)
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x)+70,(coors_center.y))
pyautogui.typewrite('facebook.com')
pyautogui.press('enter')

time.sleep(10)
coors = pyautogui.locateOnScreen('ava.png', grayscale= True, confidence =0.9)
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x)+50,(coors_center.y))
time.sleep(5)
pyautogui.typewrite('thu nghiem tuong tac may tinh')
time.sleep(5)
coors = pyautogui.locateOnScreen('dang.png', grayscale= True, confidence =0.9)
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x)+50,(coors_center.y))
pyautogui.press('enter')
