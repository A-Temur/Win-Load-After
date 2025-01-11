import win32gui


def is_window_focused(window_title):
    # Get the handle of the window with the specified title
    def enum_window_callback(hwnd, data):
        titles = data
        if win32gui.IsWindowVisible(hwnd) and window_title in win32gui.GetWindowText(hwnd):
            titles.append(hwnd)

    titles = []
    win32gui.EnumWindows(enum_window_callback, titles)

    # Check if the top window is the target window
    if titles:
        return win32gui.GetForegroundWindow() == titles[0]
    return False
