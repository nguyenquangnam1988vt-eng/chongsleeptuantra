from flask import Flask
from threading import Thread
import time
import requests
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

def run_server():
    print("🌐 Flask server starting...")
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    print("🔥 Keep-alive started")

    URL = "https://tuantrathanhmieunew.streamlit.app"

    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        ]),
        "Accept": "text/html,application/xhtml+xml"
    }

    while True:
        try:
            print("👉 Ping Streamlit...")

            res = requests.get(URL, headers=headers, timeout=60)

            print("✅ Status:", res.status_code)

            # giả lập người dùng "ở lại trang"
            time.sleep(random.randint(10, 20))

        except Exception as e:
            print("❌ Error:", e)

        print("⏱ Sleep ~4 phút...\n")
        time.sleep(random.randint(200, 260))

if __name__ == "__main__":
    print("🚀 App starting...")

    t = Thread(target=keep_alive)
    t.daemon = True
    t.start()

    run_server()
