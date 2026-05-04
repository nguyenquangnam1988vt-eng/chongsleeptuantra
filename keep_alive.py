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
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    print("🔥 Keep-alive started")

    URL = "https://tuantrathanhmieunew.streamlit.app"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html"
    }

    while True:
        try:
            print("👉 Giả lập người dùng truy cập...")

            # 1. Load trang chính
            res = requests.get(URL, headers=headers, timeout=20)
            print("✅ Main:", res.status_code)

            time.sleep(random.uniform(2, 5))

            # 2. Gọi health check (Streamlit nội bộ)
            res2 = requests.get(URL + "/_stcore/health", timeout=10)
            print("✅ Health:", res2.status_code)

            time.sleep(random.uniform(2, 5))

            # 3. Gọi thêm 1 lần nữa (giống user reload nhẹ)
            res3 = requests.get(URL, headers=headers, timeout=20)
            print("✅ Reload:", res3.status_code)

        except Exception as e:
            print("❌ Error:", e)

        # nghỉ 3–4 phút
        sleep_time = random.randint(180, 240)
        print(f"⏱ Sleep {sleep_time}s...\n")
        time.sleep(sleep_time)

if __name__ == "__main__":
    print("🚀 App starting...")

    t = Thread(target=keep_alive)
    t.daemon = True
    t.start()

    run_server()
