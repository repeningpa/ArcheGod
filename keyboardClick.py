import win32gui, win32con, win32api
from time import sleep

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
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x74, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x74, 0)
    sleep(3)
    # 2
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x32, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x32, 0)
    sleep(3)
    # F3
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x72, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x72, 0)
    sleep(3)
    
def qfClick(window_handle):
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x51, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x51, 0)
    sleep(0.1)
    win32gui.SendMessage(window_handle, win32con.WM_KEYDOWN, 0x46, 0)
    sleep(0.1)
    win32api.SendMessage(window_handle, win32con.WM_KEYUP, 0x46, 0)