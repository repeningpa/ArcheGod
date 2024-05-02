import win32gui, win32con, win32api
from time import sleep
import keyboard as kb

def keyboardClick(window_handle, key):
    # win32api.SendMessage(window_handle, win32con.WM_CHAR, key, 0)
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, key, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, key, 0)

def buffsOnHorse(window_handle):
    # F1
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x70, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x70, 0)
    sleep(3)
    # F4
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x73, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x73, 0)
    sleep(3)
    # F5
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x74, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x74, 0)
    sleep(3)
    # F2
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x71, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x71, 0)
    sleep(3)
    # 2
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x32, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x32, 0)
    sleep(3)
    # F3
    # win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x72, 0)
    # sleep(0.1)
    # win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x72, 0)
    # sleep(3)
    
def qfClick(window_handle):
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x51, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x51, 0)
    sleep(0.1)
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x46, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x46, 0)
    
def testEventKeyUp(window_handle):
    print('up')
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('q'), 0)
    sleep(1)
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('w'), 0)
    sleep(1)
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('e'), 0)
    sleep(1)
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('r'), 0)
    
def testEventKeyDown(window_handle):
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('a'), 0)
    sleep(1)
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('s'), 0)
    sleep(1)
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('d'), 0)
    sleep(1)
    win32api.SendMessage(window_handle, win32con.WM_CHAR, ord('f'), 0)

def bigHeal(window_handle):
    # F3
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x72, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x72, 0)
    sleep(0.5)
    
    # 4
    for n in range(5):
        win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x34, 0)
        sleep(0.1)
        win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x34, 0)
        sleep(0.5)

    # F1
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x70, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x70, 0)
    sleep(1)

    # 5
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x35, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x35, 0)
    sleep(1.5)
    
    # 3
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x33, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x33, 0)
    sleep(0.5)

def farm(window_handle):
    # 2
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x72, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x72, 0)
    sleep(0.5)
    
    # 4
    for n in range(5):
        win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x34, 0)
        sleep(0.1)
        win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x34, 0)
        sleep(0.5)