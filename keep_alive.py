from playwright.sync_api import sync_playwright
import time

URL = "https://tuantrathanhmieunew.streamlit.app"

while True:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(URL, timeout=60000)
            time.sleep(10)

            browser.close()
            print("Ping OK")

    except Exception as e:
        print("Error:", e)

    time.sleep(300)