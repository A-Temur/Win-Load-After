# import win32gui
# import win32con
#
#
# def set_square_corners(hwnd, _):
#     # Remove WS_EX_WINDOWEDGE which might cause rounded corners
#     style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
#     style &= ~win32con.WS_EX_WINDOWEDGE
#     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style)

import webview
import threading
import helpers
import time
import keyboard
import datetime


default_width = 1937
default_height = 1071

# zoom level 0.6
# default_width = 1169
# default_height = 659


zoom_level = 0.6


class PywebAPI:

    def __init__(self):
        self._window = None
        self.last_modifier_key = ("", datetime.datetime)
        self.modifier_keys = ["Shift", "Control"]

    def set_window(self, window):
        self._window = window

    def destroy(self):
        print('Destroying window..')
        self._window.destroy()
        print('Destroyed!')

    def log_keypress(self, press):
        if press in self.modifier_keys:
            self.modifier_key_pressed(press, datetime.datetime.now())

    def modifier_key_pressed(self, key, timepressed):
        self.last_modifier_key = (key, timepressed)

    def check_modfier_keypress(self):
        now = datetime.datetime.now()
        pass


def set_zoom(window, zoom):
    # Set zoom level; 1.0 is 100%, 1.5 is 150%, etc.
    script = f'document.body.style.zoom = "{zoom}"'
    window.evaluate_js(script)


def custom_round(value):
    # Adding a tiny amount to the value to shift .5 to be rounded up
    return round(value + 0.0000001)


def check_key_press(keypress):
    if keypress.name == "esc":
        # webview.windows[0].destroy()
        # sys.exit()
        pass
    else:
        print(keypress.name)


def action_loop():
    while True:
        window_focused = helpers.is_window_focused('Program Master 2000')
        if window_focused:
            keyboard.on_press(callback=check_key_press)
        else:
            keyboard.unhook_all()
        time.sleep(0.5)


def run_webview():
    zoomed_width = custom_round(default_width * zoom_level) + 7
    zoomed_height = custom_round(default_height * zoom_level) + 16

    api = PywebAPI()

    # Use localhost URL where FastAPI is served
    window = webview.create_window('Program Master 2000',
                          'prod_maintab.html', js_api=api,
                          width=zoomed_width, height=zoomed_height, frameless=True)

    api.set_window(window)
    threading.Thread(target=action_loop, daemon=True).start()

    webview.start(func=lambda: set_zoom(window, zoom_level))


if __name__ == '__main__':
    # Run FastAPI on a separate thread
    #threading.Thread(target=run_api, daemon=True).start()

    # Run the PyWebview window
    run_webview()


