from flask import Flask
from threading import Thread
from playwright.sync_api import sync_playwright
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

def run_server():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    URL = "https://tuantrathanhmieunew.streamlit.app"

    while True:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(
                    headless=True,
                    args=["--no-sandbox", "--disable-dev-shm-usage"]
                )
                page = browser.new_page()

                page.goto(URL, timeout=60000)
                time.sleep(10)

                browser.close()
                print("Ping OK")

        except Exception as e:
            print("Error:", e)

        time.sleep(300)

if __name__ == "__main__":
    Thread(target=keep_alive).start()
    run_server()
