from flask import Flask
from threading import Thread
import time
import requests

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
            print("👉 Đang ping Streamlit...")
            res = requests.get(URL, timeout=30)

            print("✅ Status:", res.status_code)

        except Exception as e:
            print("❌ Lỗi:", e)

        print("⏱ Ngủ 5 phút...\n")
        time.sleep(300)

if __name__ == "__main__":
    print("🚀 App start")

    t = Thread(target=keep_alive)
    t.daemon = True
    t.start()

    print("✅ Thread đã start")

    run_server()
