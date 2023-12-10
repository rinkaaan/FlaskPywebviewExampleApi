from threading import Thread, Event

import webview

from api.app import app
from api.utils import get_free_port

stop_event = Event()
app_title = "Flask Pywebview Example"
host = "http://127.0.0.1"
port = get_free_port()


def run_api():
    while not stop_event.is_set():
        app.run(port=port, use_reloader=False)


if __name__ == '__main__':
    t = Thread(target=run_api)
    t.daemon = True
    t.start()

    webview.create_window(
        app_title,
        f"{host}:{port}",
        width=500,
        height=800,
        min_size=(500, 800),
    )

    webview.start()

stop_event.set()
