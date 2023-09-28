from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops
import pyautogui as auto
# import numpy as np
# import cv2
import time


def capture_screen(x1=0, y1=0, x2=1920, y2=1080):
    screen = ImageGrab.grab((x1, y1, x2, y2))
    return screen


def equals(img1, img2):
    diff = ImageChops.difference(img1, img2)
    if diff.getbbox():
        print('different')
        return False
    else:
        print('equals')
        return True


def eat_food():
    auto.press('p')
    auto.press('o')


def reconnect():
    img = Image.open('./assets/reconnect.png')
    if auto.locateOnScreen(img):
        auto.press('enter')
        time.sleep(10)
        auto.rightClick(935, 550)


def attack():
    img = Image.open('./assets/attacking.png')
    img_ = auto.locateOnScreen(img, grayscale=True, confidence=0.95)
    print(img_)
    if not auto.locateOnScreen(img, grayscale=True, confidence=0.94):
        auto.rightClick(885, 550)
        print('to na funçao')


def attack_pixel():
    img = ImageGrab.grab()
    pixel = img.getpixel((830, 590))
    if pixel != (255, 0, 0):
        auto.keyUp('space')


def anti_logout():
    auto.keyDown('ctrl')
    auto.keyDown('ctrl')
    auto.press('d')
    auto.press('a')
    auto.press('w')
    auto.press('s')
    auto.keyUp('ctrl')


def find_and_click_around(img, x, y):
   cords = auto.locateCenterOnScreen('./assets/' + img, grayscale=False, confidence=0.95)
   if cords:
      auto.click(cords.x + (x), cords.y + (y))


def click_tibia():
   with auto.hold('alt'):
      auto.keyDown('tab')
      auto.keyUp('tab')
      find_and_click_around('tibia.png', 0, +50)


def main():
    # reconnect()
    # attack_pixel()
    # anti_logout()
    eat_food()



click_tibia()
while True:
    time.sleep(4)
    main()
