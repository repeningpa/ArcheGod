import threading
import flet as ft
import win32api, win32gui
from time import sleep
from fish import mainSearch
from keyboardClick import buffsOnHorse, qfClick

def main(page: ft.Page):
    page.title = "ArcheGod"
    page.window_width = 350 # Задаем ширину окна
    page.window_height = 500 # Задаем высоту окна
    page.window_resizable = False # Запрещаем изменять размеры окна
    page.update()
    
    def get_window_at_mouse_pos():
        x, y = win32api.GetCursorPos()
        window_id = win32gui.WindowFromPoint((x, y))
        headerText.value = f'{win32gui.GetWindowText(window_id)} - {window_id}'
        return window_id
    
    def changeFishEvent(e):
        if fishCb.value == True:
            showBannerClick(e)
        else:
            closeBanner(e)
            
    def changeFarmEvent(e):
        if bardCb.value == True:
            showBannerClick(e)
        else:
            closeBanner(e)
            
    def changeQfEvent(e):
        if qfCb.value == True:
            showBannerClick(e)
        else:
            closeBanner(e)
            
    fishCb = ft.Checkbox(label = "Долбить рыбу", on_change = changeFishEvent)
    bardCb = ft.Checkbox(label = "Ебашить по флейте", on_change = changeFarmEvent)
    qfCb = ft.Checkbox(label = "QF", on_change = changeQfEvent)
    headerText = ft.Text()
    
    input_column = ft.Column([headerText])

    def route_change(e):
        page.views.clear()        
        page.views.append(
            ft.View(
                "/",
                [
                    input_column,
                    ft.ExpansionTile(
                        title=ft.Text("Общие"),
                        subtitle=ft.Text("Раблка и прочее..."),
                        affinity=ft.TileAffinity.LEADING,
                        collapsed_text_color=ft.colors.BLUE,
                        text_color=ft.colors.BLUE,
                        controls_padding = 25,
                        controls=[
                            fishCb,
                        ],
                    ),
                    ft.ExpansionTile(
                        title=ft.Text("Макросы для хилочки"),
                        subtitle=ft.Text("Спам на флейте..."),
                        affinity=ft.TileAffinity.LEADING,
                        collapsed_text_color=ft.colors.GREEN,
                        text_color=ft.colors.GREEN,
                        controls_padding = 25,
                        controls=[
                            bardCb,
                        ],
                    ),
                    ft.ExpansionTile(
                        title=ft.Text("ДД макросы"),
                        subtitle=ft.Text("Основа..."),
                        affinity=ft.TileAffinity.LEADING,
                        collapsed_text_color=ft.colors.RED,
                        text_color=ft.colors.RED,
                        controls_padding = 25,
                        controls=[
                            qfCb,
                        ],
                    ),
                ],
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
            while fishCb.value == True:
                sleep(0.5)
                mainSearch(window_handle) # fullHD MainScreen
            while bardCb.value == True:
                sleep(0.5)
                buffsOnHorse(window_handle)
            while qfCb.value == True:
                sleep(0.5)
                qfClick(window_handle)

    def closeBanner(e):
        page.banner.open = False
        page.update()
    
    def showBannerClick(e):
        page.banner.open = True
        page.update()
        
    page.banner = ft.Banner(
        bgcolor = ft.colors.RED,
        leading = ft.Icon(ft.icons.DOWNLOADING, color = ft.colors.WHITE, size=40),
        content = ft.Text("Вы запустили действие", color = ft.colors.WHITE),
        actions=[
            ft.TextButton("Закрыть", on_click = closeBanner),
        ],
    )

    win32gui.MessageBox(None, '', '', 0)
    window_handle = get_window_at_mouse_pos()
    print(window_handle)
    win32gui.SetForegroundWindow(window_handle) # hwnd
    threading.Thread(target = mining, daemon = True).start()
    
    page.on_route_change = route_change(page)
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)