import keyboard as kb

def keyEvent(testCb):
    def here(e):
        testCb.value = not testCb.value
        print('Page_Up')
    
    def here1(e):
        print('Page_Down')

    kb.on_press_key('Page_Up', here)
    kb.on_press_key('Page_Down', here1)