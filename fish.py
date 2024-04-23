import pyautogui as pag
from keyboardClick import keyboardClick
from time import sleep

down = './img/fish/200interface1024/down.png'
end = './img/fish/200interface1024/end.png'
left = './img/fish/200interface1024/left.png'
right = './img/fish/200interface1024/right.png'
up = './img/fish/200interface1024/up.png'

def mainSearch(window_handle, x, y, w, h):
    # pag.screenshot('test1.png', region = (x, y, w, h))
    sleep(0.5)
    try:
        downImg = pag.locateOnScreen(down, region = (x, y, w, h), confidence = 0.7)
        # print(f'downImg{window_handle}', downImg)
        # pag.screenshot('downImg.png', region = (x, y, w, h))
        # keyboardClick(window_handle, ord('s'))
        keyboardClick(window_handle, 0x28)
    except pag.ImageNotFoundException:
        try:
            endImg = pag.locateOnScreen(end, region = (x, y, w, h), confidence = 0.7)
            # pag.screenshot('endImg.png', region = (x, y, w, h))
            # print(f'endImg{window_handle}', endImg)
            # keyboardClick(window_handle, ord('p'))
            keyboardClick(window_handle, 0x50)
        except pag.ImageNotFoundException:
            try:
                leftImg = pag.locateOnScreen(left, region = (x, y, w, h), confidence = 0.7)
                # pag.screenshot('leftImg.png', region = (x, y, w, h))
                # print(f'leftImg{window_handle}', leftImg)
                # keyboardClick(window_handle, ord('a'))
                keyboardClick(window_handle, 0x25)
            except pag.ImageNotFoundException:
                try:
                    rightImg = pag.locateOnScreen(right, region = (x, y, w, h), confidence = 0.7)
                    # pag.screenshot('rightImg.png', region = (x, y, w, h))
                    # print(f'rightImg{window_handle}', rightImg)
                    # keyboardClick(window_handle, ord('d'))
                    keyboardClick(window_handle, 0x27)
                except pag.ImageNotFoundException:
                    try:
                        upImg = pag.locateOnScreen(up, region = (x, y, w, h), confidence = 0.7)
                        # pag.screenshot('upImg.png', region = (x, y, w, h))
                        # print(f'upImg{window_handle}', upImg)
                        # keyboardClick(window_handle, ord('w'))
                        keyboardClick(window_handle, 0x26)
                    except pag.ImageNotFoundException:
                        sleep(0.5)
