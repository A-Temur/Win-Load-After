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
import uvicorn
from app import app  # import the FastAPI app


default_width = 1937
default_height = 1071

# zoom level 0.6
# default_width = 1169
# default_height = 659


zoom_level = 0.6


def set_zoom(window, zoom):
    # Set zoom level; 1.0 is 100%, 1.5 is 150%, etc.
    script = f'document.body.style.zoom = "{zoom}"'
    window.evaluate_js(script)


def run_api():
    uvicorn.run(app, port=8000, host='127.0.0.1')


def custom_round(value):
    # Adding a tiny amount to the value to shift .5 to be rounded up
    return round(value + 0.0000001)


def run_webview():
    zoomed_width = custom_round(default_width * zoom_level) + 7
    zoomed_height = custom_round(default_height * zoom_level) + 16

    # Use localhost URL where FastAPI is served
    window = webview.create_window('My Application',
                          'http://localhost:63342/LoadOrder/next/prod_maintab.html?_ijt=rijkh7kjsf9s0t0o8h38p7q1vl&_ij_reload=RELOAD_ON_SAVE',
                          width=zoomed_width, height=zoomed_height, frameless=True)
    webview.start(func=lambda: set_zoom(window, zoom_level))


if __name__ == '__main__':
    # Run FastAPI on a separate thread
    threading.Thread(target=run_api, daemon=True).start()

    # Run the PyWebview window
    run_webview()
