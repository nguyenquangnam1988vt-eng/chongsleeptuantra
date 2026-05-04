from flask import Flask
from threading import Thread
from playwright.sync_api import sync_playwright
import time
import os
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

def run_server():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    URL = "https://tuantrathanhmieunew.streamlit.app/?ping=1"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )

        while True:
            try:
                page = browser.new_page()

                print("Đang vào web...")

                page.goto(
                    URL,
                    timeout=60000,
                    wait_until="networkidle"   # 🔥 đợi load thật sự
                )

                # 🔥 giả lập user thật
                page.mouse.move(100, 200)
                page.mouse.wheel(0, 500)

                # 🔥 giữ lâu hơn
                time.sleep(20)

                page.close()
                print("Ping OK")

            except Exception as e:
                print("Error:", e)

            time.sleep(300)  # 5 phút

if __name__ == "__main__":
    Thread(target=keep_alive).start()
    run_server()
