import pyautogui as auto

def main():
    auto.locateOnScreen('./assets/tibia.png', grayscale=False, confidence=0.95)
    # cords = auto.locateCenterOnScreen('./assets/' + img, grayscale=False, confidence=0.95)