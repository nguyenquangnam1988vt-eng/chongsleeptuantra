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
    print("🔥 Keep-alive started")

    URL = "https://tuantrathanhmieunew.streamlit.app"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml"
    }

    while True:
        try:
            print("👉 Ping Streamlit...")

            res = requests.get(
                URL,
                headers=headers,
                timeout=20
            )

            print("✅ Status:", res.status_code)

        except Exception as e:
            print("❌ Error:", e)

        print("⏱ Sleep 3 minutes...\n")
        time.sleep(180)  # 3 phút (ổn định hơn 5 phút)

if __name__ == "__main__":
    print("🚀 App starting...")

    t = Thread(target=keep_alive)
    t.daemon = True
    t.start()

    run_server()
