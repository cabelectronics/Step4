import webview
import time


def reload(window):
    while True:
        time.sleep(3)
        window.load_url('index.html')

if __name__ == '__main__':
    window = webview.create_window('hello', 'index.html')

    webview.start(reload, window, http_server=True)

