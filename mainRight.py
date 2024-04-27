import threading
import flet as ft
import win32api, win32gui
from time import sleep
from fish import mainSearch
from keyboardClick import buffsOnHorse, qfClick, keyboardClick
import keyboard as kb

def main(page: ft.Page):
    page.title = "ArcheGod"
    page.window_width = 350 # Задаем ширину окна
    page.window_height = 500 # Задаем высоту окна
    page.window_resizable = False # Запрещаем изменять размеры окна
    page.update()
    
    def get_window_at_mouse_pos_win():
        x, y = win32api.GetCursorPos()
        window_id = win32gui.WindowFromPoint((x, y))
        headerText.value = window_id
        return window_id
    
    def changeEvent(e):
        if fishCb.value == True or bardCb.value == True or qfCb.value == True:
            headerContainer.bgcolor = ft.colors.RED
        else:
            headerContainer.bgcolor = ft.colors.SURFACE_VARIANT
        page.update()

    fishCb = ft.Checkbox(label = "Долбить рыбу", on_change = changeEvent)
    bardCb = ft.Checkbox(label = "Ебашить по флейте", on_change = changeEvent)
    qfCb = ft.Checkbox(label = "QF", on_change = changeEvent)
    headerText = ft.Text(size = 40, text_align = ft.TextAlign.CENTER)
    
    bardRow = ft.ExpansionTile(
        title = ft.Text("Бард"),
        subtitle = ft.Text("Макросы для хилочки..."),
        affinity = ft.TileAffinity.LEADING,
        collapsed_text_color = ft.colors.GREEN,
        text_color = ft.colors.GREEN,
        controls_padding = 25,
        controls=[
            bardCb,
        ],
    )
    
    ddRow = ft.ExpansionTile(
        title = ft.Text("ДД"),
        affinity = ft.TileAffinity.LEADING,
        collapsed_text_color = ft.colors.RED,
        text_color = ft.colors.RED,
        controls_padding = 25,
        controls=[
            qfCb,
        ],
    )
    
    headerContainer = ft.Container(
        content = headerText,
        bgcolor = ft.colors.SURFACE_VARIANT,
        width = 350,
    )
    
    # input_column = ft.Column([headerText])

    def route_change(e):
        page.views.clear()        
        page.views.append(
            ft.View(
                "/",
                [
                    # input_column,
                    headerContainer,
                    ft.ExpansionTile(
                        title = ft.Text("Рыбалка"),
                        subtitle = ft.Text("Общие..."),
                        affinity = ft.TileAffinity.LEADING,
                        collapsed_text_color = ft.colors.BLUE,
                        text_color = ft.colors.BLUE,
                        controls_padding = 25,
                        controls = [
                            fishCb,
                        ],
                    ),
                    bardRow,
                    ddRow
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
        
    def mining():
        while True:
            sleep(2)
            while bardCb.value == True:
                buffsOnHorse(window_handle)
            while fishCb.value == True:
                # sleep(0.1)
                # pag.screenshot('test1.png', region = (1180, 100, 140, 50))
                mainSearch(window_handle, 1180, 100, 140, 50)
                # mainSearch(window_handle, 275, 100, 140, 50)
            while qfCb.value == True:
                qfClick(window_handle)

    win32gui.MessageBox(None, '1', '', 0)
    window_handle = get_window_at_mouse_pos_win()
    print(window_handle)
    win32gui.SetForegroundWindow(window_handle) # hwnd
    
    threading.Thread(target = mining, daemon = True).start() # поток с событиями
    
    page.on_route_change = route_change(page)
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)