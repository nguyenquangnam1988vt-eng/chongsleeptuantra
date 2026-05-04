from flask import Flask
from threading import Thread
from playwright.sync_api import sync_playwright
import time
import os
import traceback

os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

def run_server():
    print("🌐 Flask server starting...")
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    print("🔥 Thread keep_alive đã chạy")

    URL = "https://tuantrathanhmieunew.streamlit.app/?ping=1"

    while True:
        try:
            print("👉 Bắt đầu vòng lặp mới")

            print("👉 Khởi động Playwright")
            p = sync_playwright().start()

            print("👉 Mở browser")
            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-gpu",
                    "--no-zygote",
                    "--single-process"
                ]
            )

            print("👉 Tạo page")
            page = browser.new_page()

            print("👉 Đang vào web...")
            page.goto(URL, timeout=60000)

            print("👉 Giữ 20s")
            time.sleep(20)

            browser.close()
            p.stop()

            print("✅ Ping OK")

        except Exception as e:
            print("❌ Lỗi:", e)

        time.sleep(300)

if __name__ == "__main__":
    print("🚀 App start")

    t = Thread(target=keep_alive)
    t.daemon = True   # 🔥 QUAN TRỌNG
    t.start()

    print("✅ Thread đã start")

    run_server()
