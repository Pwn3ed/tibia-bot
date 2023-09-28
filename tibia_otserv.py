# from PIL import Image
# from PIL import ImageGrab
# from PIL import ImageChops
# import pytesseract as ocr
import numpy as np
# import cv2
import pyautogui as auto
import threading
import multiprocessing as mp
import schedule
import time
import constants

targeting = False


def find_and_click_around(img, x, y):
   cords = auto.locateCenterOnScreen('./assets/' + img, grayscale=False, confidence=0.95)
   if cords:
      auto.click(cords.x + (x), cords.y + (y))


def anti_logout():
    while True:
        print('Executing anti_logout')
        # auto.keyDown('ctrl');
        # key('d')
        # key('a')
        # key('w')
        # key('s')
        # auto.keyUp('ctrl')
        mouse(1000, 530)
        mouse(850, 530)
        time.sleep(120)


def mouse(x, y):
    auto.moveTo(x, y)
    auto.mouseDown()
    auto.mouseUp()


def find(img):
    cords = auto.locateOnScreen('./assets/' + img, grayscale=False, confidence=0.95)
    if cords:
        return True


def find_and_click(img):
    cords = auto.locateCenterOnScreen('./assets/' + img, grayscale=False, confidence=0.95)
    if cords:
        mouse(cords.x, cords.y)


def test1():
    print('test1 starts')
    while True:
        time.sleep(5)
        print('test1 ends')
        return


def test2():
    for thread in threading.enumerate():
        if thread.name == 'test1':
            print('test1 already running')
        else:
            print('trying to run test1')
    #print('2')
    time.sleep(1)


def run_threaded(func, args=None, name=None):
    job_thread = threading.Thread(target=func, args=(args,), name=name)
    job_thread.start()


def click_tibia():
   with auto.hold('alt'):
      auto.keyDown('tab')
      auto.keyUp('tab')
      find_and_click_around('obs.png', 0, +50)
   with auto.hold('alt'):
      auto.keyDown('tab')
      auto.keyUp('tab')
      find_and_click_around('tibia.png', 0, +50)


def heal():
    print('HEAL: ON')
    y = 38
    life0 = 189
    life30 = 260
    life50 = 434
    life70 = 607
    life90 = 781
    life100 = 868
    life_rgb = (0, 175, 0)
    life_none_rgb = (49, 49, 49)

    while True:
        # check if needs to heal and heal
        # print(auto.pixel(life90, y))
        if auto.pixelMatchesColor(life90, y, life_none_rgb, tolerance=10):
            auto.press('1')
            time.sleep(1)

        # print('HEAL: OFF')
        # return


def monster():
    x, y = 1594, 55
    pixel_rgb = (0, 0, 0)

    while True:
        if auto.pixelMatchesColor(x, y, pixel_rgb, tolerance=10) == True:
            auto.press('space')
            time.sleep(0.9)
            # if (find('targeting.png') or find('targeting2.png')):
            #     return True
            # else:
            #     auto.press('space')


def multipleTarget():
    while True:
        if monster():
            auto.press('r')
            time.sleep(2)
            auto.press('f')


def skillsr():
    while True:
        auto.hotkey('shift', 'r')
        time.sleep(8)


def skillr():
    while True:
        auto.press('r')
        time.sleep(2)


def singleTarget():
    while True:
#        if (monster()):
        auto.press('tab')
        auto.press('space')
        time.sleep(1.6)

def utito():
    battle_with_monster_rgb = (192, 192, 192)
    while True:
        if auto.pixelMatchesColor(1596, 46, battle_with_monster_rgb, tolerance=10) == True:
            auto.press('v')
            time.sleep(1)


def loot():
    confidenceLoot = 0.6
    while True:
        box = auto.locateAllOnScreen('./assets/loot5.png', confidence=confidenceLoot)
        for item in box:
            pass
            # print(item)
            # auto.click()


def food():
    while True:
        if (auto.locateOnScreen('./assets/food.png', confidence=0.9, region=config.REGION_FOOD)):
            auto.press('p')
            time.sleep(1)


def main():
    print('starting ...')
    click_tibia()
    # print(auto.pixel(1596, 46))

    job_thread1 = threading.Thread(target=heal, name='heal')
    job_thread1.start()

    job_thread2 = threading.Thread(target=monster, name='monster')
    job_thread2.start()

    job_thread3 = threading.Thread(target=loot, name='loot')
    job_thread3.start()

    job_thread4 = threading.Thread(target=food, name='food')
    job_thread4.start()


main()
time.sleep(1)
print('ending ...')
