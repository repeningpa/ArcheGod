import threading
import flet as ft
import win32api, win32gui, win32con
from time import sleep
from fish import mainSearch
from keyboardClick import buffsOnHorse, qfClick, keyboardClick, testEventKeyUp, testEventKeyDown
import keyboard as kb
from keyEvent import keyEvent

keyPageUpBool = False
keyPageDownBool = False
keyHomeBool = False

windowKey = False

x1 = 275
x2 = 1180
y = 100
w = 140
h = 50

def main(page: ft.Page):
    page.title = "ArcheGod"
    page.window_width = 375 # Задаем ширину окна
    page.window_height = 350 # Задаем высоту окна
    page.window_resizable = False # Запрещаем изменять размеры окна
    page.update()
    
    def get_window_at_mouse_pos_win():
        x, y = win32api.GetCursorPos()
        window_id = win32gui.WindowFromPoint((x, y))
        headerText.value = window_id
        return window_id
    
    def changeEvent(e):
        if testCb.value == True:
            headerContainer.bgcolor = ft.colors.RED
        else:
            headerContainer.bgcolor = ft.colors.SURFACE_VARIANT
        page.update()

    def changeSecondWindow(e):
        global windowKey
        windowKey = secondWindow.value
        
    keyPageUpText = ft.Text(value = 'Page Up', size = 15, color = ft.colors.GREY)
    keyPageDownText = ft.Text(value = 'Page Down', size = 15, color = ft.colors.GREY)
    keyHomeText = ft.Text(value = 'Home', size = 15, color = ft.colors.GREY)
    
    labelPageUpText = ft.Text(value = 'Бард', size = 15, color = ft.colors.GREY, text_align = ft.TextAlign.CENTER, width = 85)
    labelPageDownText = ft.Text(value = 'ДД', size = 15, color = ft.colors.GREY, text_align = ft.TextAlign.CENTER, width = 85)
    labelHomeText = ft.Text(value = 'Рыбалка', size = 15, color = ft.colors.GREY, text_align = ft.TextAlign.CENTER, width = 85)

    secondWindow = ft.Checkbox(label = 'Второе окно', on_change = changeSecondWindow)
        
    def PageUpTest(e):
        global keyPageUpBool
        keyPageUpBool = not keyPageUpBool
        if keyPageUpBool == True:
            keyPageUp.border = ft.border.all(3, ft.colors.YELLOW)
            keyPageUp.content = ft.Text(value = 'Page Up', size = 15, color = ft.colors.YELLOW)
            labelPageUpText.color = ft.colors.YELLOW
        else:
            keyPageUp.border = ft.border.all(3, ft.colors.GREY)
            keyPageUp.content = ft.Text(value = 'Page Up', size = 15, color = ft.colors.GREY)
            labelPageUpText.color = ft.colors.GREY
        page.update()
        
    def PageDownTest(e):
        global keyPageDownBool
        keyPageDownBool = not keyPageDownBool
        if keyPageDownBool == True:
            keyPageDown.border = ft.border.all(3, ft.colors.RED)
            keyPageDown.content = ft.Text(value = 'Page Down', size = 15, color = ft.colors.RED)
            labelPageDownText.color = ft.colors.RED
        else:
            keyPageDown.border = ft.border.all(3, ft.colors.GREY)
            keyPageDown.content = ft.Text(value = 'Page Down', size = 15, color = ft.colors.GREY)
            labelPageDownText.color = ft.colors.GREY
        page.update()
        
    def HomeTest(e):
        global keyHomeBool
        keyHomeBool = not keyHomeBool
        if keyHomeBool == True:
            keyHome.border = ft.border.all(3, ft.colors.BLUE)
            keyHome.content = ft.Text(value = 'Home', size = 15, color = ft.colors.BLUE)
            labelHomeText.color = ft.colors.BLUE
        else:
            keyHome.border = ft.border.all(3, ft.colors.GREY)
            keyHome.content = ft.Text(value = 'Home', size = 15, color = ft.colors.GREY)
            labelHomeText.color = ft.colors.GREY
        page.update()

    testCb = ft.Checkbox(label = "Тест", on_change = changeEvent)
    headerText = ft.Text(size = 40, text_align = ft.TextAlign.CENTER)
    
    headerContainer = ft.Container(
        content = headerText,
        bgcolor = ft.colors.SURFACE_VARIANT,
        width = 500,
    )

    keyPageUp = ft.Container(
        content = keyPageUpText,
        alignment = ft.alignment.center,
        width = 70,
        height = 70,
        padding = 10,
        border_radius = 10,
        border = ft.border.all(3, ft.colors.GREY),
        on_click = PageUpTest,
    )
    
    keyPageDown = ft.Container(
        content = keyPageDownText,
        alignment = ft.alignment.center,
        width = 70,
        height = 70,
        padding = 10,
        border_radius = 10,
        border = ft.border.all(3, ft.colors.GREY),
        on_click = PageDownTest,
    )
    
    keyHome = ft.Container(
        content = keyHomeText,
        alignment = ft.alignment.center,
        width = 70,
        height = 70,
        padding = 10,
        border_radius = 10,
        border = ft.border.all(3, ft.colors.GREY),
        on_click = HomeTest,
    )

    def route_change(e):
        page.views.clear()        
        page.views.append(
            ft.View(
                "/",
                [
                    headerContainer,
                    ft.Container(
                        padding = 20,
                        content = ft.Row(
                            spacing = 30,
                            controls = [
                                ft.Column(
                                    [
                                        ft.Container(
                                            content = keyPageUp,
                                            alignment = ft.alignment.center,
                                            width = 85
                                        ),
                                        labelPageUpText,
                                    ]
                                ),
                                ft.Column(
                                    [
                                        ft.Container(
                                            content = keyPageDown,
                                            alignment = ft.alignment.center,
                                            width = 85
                                        ),
                                        labelPageDownText,
                                    ]
                                ),
                                ft.Column(
                                    [
                                        ft.Container(
                                            content = keyHome,
                                            alignment = ft.alignment.center,
                                            width = 85
                                        ),
                                        labelHomeText,
                                    ]
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        content = secondWindow,
                        padding = 25,
                    ),
                ],
                padding = 0,
                scroll = ft.ScrollMode.ADAPTIVE
            )
        )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    def miningWin1():
        while True:
            sleep(0.1)
            while keyPageUpBool == True:
                buffsOnHorse(window_handle1)
            while keyPageDownBool == True:
                qfClick(window_handle1)    
            while keyHomeBool == True:
                mainSearch(window_handle1, x1 if windowKey == False else x2, y, w, h)

    win32gui.MessageBox(None, '1', '', 0)
    window_handle1 = get_window_at_mouse_pos_win()
    win32gui.SetForegroundWindow(window_handle1) # hwnd

    kb.on_press_key('Page_Up', PageUpTest)
    kb.on_press_key('Page_Down', PageDownTest)
    kb.on_press_key('Home', HomeTest)
    
    threading.Thread(target = miningWin1, daemon = True).start() # поток с событиями
    
    page.on_route_change = route_change(page)
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)