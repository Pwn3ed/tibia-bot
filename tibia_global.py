import pyautogui as auto
import threading
import time
import constants

targeting = False


def find_and_click_around(img, x, y):
    cords = auto.locateCenterOnScreen('./assets/' + img, grayscale=False, confidence=0.95)
    if cords:
        auto.click(cords.x + x, cords.y + y)


def anti_logout():
    while True:
        print('Executing anti_logout')
        # auto.keyDown('ctrl');
        # key('d')
        # key('a')
        # key('w')
        # key('s')
        # auto.keyUp('ctrl')
        mouse(930, 500)
        mouse(780, 500)
        time.sleep(120)


def mouse(x, y):
    auto.moveTo(x, y)
    auto.mouseDown()
    auto.mouseUp()


def find(img):
    cords = auto.locateOnScreen('./assets/' + img, grayscale=False, confidence=0.95)
    if cords:
        return True


def find_loot(img):
    cords = auto.locateOnScreen('./assets/' + img, grayscale=False, confidence=constants.LOOT_CONFIDENCE)
    if cords:
        return True


def find_and_click(img):
    cords = auto.locateCenterOnScreen('./assets/' + img, grayscale=False, confidence=0.95)
    if cords:
        mouse(cords.x, cords.y)


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
    while True:
        if not auto.pixelMatchesColor(constants.LIFE90_X, constants.LIFE_Y, constants.LIFE_RGB_GREEN, tolerance=10):
            auto.press('1')
            time.sleep(1)


def mana():
    while True:
        mana_full = auto.pixelMatchesColor(constants.MANA99_X, constants.MANA_Y, constants.MANA_RGB_BLUE, tolerance=1)
        if mana_full:
            auto.press('1')
            time.sleep(1)


def monster():
    if auto.pixelMatchesColor(constants.MONSTER_BATTLELIST_FIRST_X, constants.MONSTER_BATTLELIST_FIRST_Y, constants.MONSTER_PIXEL_RGB, tolerance=10):
        return True


def attack():
    while True:
        if monster():
            auto.press('space')
            time.sleep(0.9)


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


def loot():
    while True:
        if not monster():
            dropped = auto.locateOnScreen('./assets/loot_dropped.png', confidence=0.9, region=constants.REGION_CHAT)
            if dropped:
                print('dropped')
                loot = auto.locateAllOnScreen('./assets/wasp/loot.png', confidence=constants.LOOT_CONFIDENCE)
                if loot:
                    for box in loot:
                        x, y = auto.center(box)
                        auto.rightClick(x, y)
                        time.sleep(3)

                        item1 = auto.locateOnScreen('./assets/wasp/loot_honeycomb.png', confidence=0.9, region=constants.REGION_LOOT)
                        if item1:
                            x, y = auto.center(item1)
                            auto.moveTo(x, y)
                            time.sleep(0.2)
                            auto.dragTo(constants.LOOT_BP1_XY, button='left')
            time.sleep(2)


def loot_afk():
    while True:
        auto.keyDown('shift')
        auto.rightClick(858, 418)
        auto.rightClick(928, 422)
        auto.rightClick(935, 489)
        auto.rightClick(928, 567)
        auto.rightClick(860, 569)
        auto.rightClick(780, 569)
        auto.rightClick(783, 497)
        auto.rightClick(780, 441)
        auto.keyUp('shift')
        time.sleep(30)


def food():
    while True:
        if auto.locateOnScreen('./assets/food.png', confidence=0.9, region=constants.REGION_EFFECTS_TOP):
            auto.press('p')
            time.sleep(1)


def poison():
    while True:
        if auto.locateOnScreen('./assets/poison.png', confidence=0.9, region=constants.REGION_EFFECTS_TOP):
            auto.press('f3')
            time.sleep(1)


def ringPush():
    auto.hotkey(*constants.RING_STEALTH)


def ring():
    while True:
        ring_none = auto.locateOnScreen('./assets/ring_none.png', confidence=0.9, region=constants.REGION_RING)
        if ring_none:
            ringPush()
            time.sleep(1)


def cavebot():
    waypoint = 0
    while True:
        flags = auto.locateAllOnScreen('./assets/flag.png', confidence=0.9, region=constants.REGION_MAP)
        for flag in flags:
            print(flag)
            x, y = auto.center(flag)
            auto.click(x, y)
            waypoint += 1
            time.sleep(1)
        waypoint = 0


def anti_escape():
    while True:
        surface = auto.locateOnScreen('./assets/wasp/map_surface.png', confidence=0.8, region=constants.REGION_MAP)
        if (surface):
            # exit game
            auto.click(1895, 12)
            time.sleep(0.2)
            auto.click(1108, 573)
        time.sleep(5)

def main():
    print('... starting ...')
    click_tibia()

    # job_thread1 = threading.Thread(target=heal, name='heal')
    # job_thread1.start()

    job_thread2 = threading.Thread(target=attack, name='attack')
    job_thread2.start()

    # job_thread3 = threading.Thread(target=loot, name='loot')
    # job_thread3.start()

    # job_thread4 = threading.Thread(target=food, name='food')
    # job_thread4.start()

    # job_thread5 = threading.Thread(target=poison, name='poison')
    # job_thread5.start()

    # job_thread6 = threading.Thread(target=ring, name='ring')
    # job_thread6.start()

    # job_thread7 = threading.Thread(target=mana, name='mana')
    # job_thread7.start()

    # job_thread8 = threading.Thread(target=cavebot, name='cavebot')
    # job_thread8.start()

    job_thread9 = threading.Thread(target=anti_logout, name='anti_logout')
    job_thread9.start()

    job_thread10 = threading.Thread(target=loot_afk, name='loot_afk')
    job_thread10.start()

    job_thread11 = threading.Thread(target=anti_escape, name='anti_escape')
    job_thread11.start()


main()
time.sleep(1)
print('... ending ...')
