import pyautogui as pag
from keyboardClick import keyboardClick
from time import sleep

down = './img/fish/down.png'
end = './img/fish/end.png'
left = './img/fish/left.png'
right = './img/fish/right.png'
up = './img/fish/up.png'

def mainSearch(window_handle):
    # sleep(0.5)
    # print(window_handle)
    try:
        downImg = pag.locateOnScreen(down, region = (775, 60, 140, 40), confidence = 0.7)
        # print('downImg', downImg)
        # pag.screenshot('downImg.png', region = (775, 60, 140, 40))
        # keyboardClick(window_handle, ord('s'))
        keyboardClick(window_handle, 0x28)
    except pag.ImageNotFoundException:
        try:
            endImg = pag.locateOnScreen(end, region = (775, 60, 140, 40), confidence = 0.7)
            # pag.screenshot('endImg.png', region = (775, 60, 140, 40))
            # print('endImg', endImg)
            # keyboardClick(window_handle, ord('p'))
            keyboardClick(window_handle, 0x50)
        except pag.ImageNotFoundException:
            try:
                leftImg = pag.locateOnScreen(left, region = (775, 60, 140, 40), confidence = 0.7)
                # pag.screenshot('leftImg.png', region = (775, 60, 140, 40))
                # print('leftImg', leftImg)
                # keyboardClick(window_handle, ord('a'))
                keyboardClick(window_handle, 0x25)
            except pag.ImageNotFoundException:
                try:
                    rightImg = pag.locateOnScreen(right, region = (775, 60, 140, 40), confidence = 0.7)
                    # pag.screenshot('rightImg.png', region = (775, 60, 140, 40))
                    # print('rightImg', rightImg)
                    # keyboardClick(window_handle, ord('d'))
                    keyboardClick(window_handle, 0x27)
                except pag.ImageNotFoundException:
                    try:
                        upImg = pag.locateOnScreen(up, region = (775, 60, 140, 40), confidence = 0.7)
                        # pag.screenshot('upImg.png', region = (775, 60, 140, 40))
                        # print('upImg', upImg)
                        # keyboardClick(window_handle, ord('w'))
                        keyboardClick(window_handle, 0x26)
                    except pag.ImageNotFoundException:
                        sleep(0.5)
