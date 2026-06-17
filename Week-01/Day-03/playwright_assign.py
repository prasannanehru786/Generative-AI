import os
import json
import random
import time
from datetime import datetime

import pandas as pd
from playwright.sync_api import sync_playwright

CONTACT_FILE = "contacts.csv"
SCREENSHOT_DIR = "screenshots"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def delay():
    time.sleep(random.uniform(2, 5))


def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        print(f"{CONTACT_FILE} not found!")
        return []

    return pd.read_csv(CONTACT_FILE).fillna("").to_dict("records")


def save_reports(results):

    today = datetime.now().strftime("%Y-%m-%d")

    json_file = f"whatsapp_report_{today}.json"
    excel_file = f"whatsapp_report_{today}.xlsx"

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    pd.DataFrame(results).to_excel(
        excel_file,
        index=False
    )

    print("\nReports Generated")
    print(json_file)
    print(excel_file)


def send_whatsapp_message(page, phone, message):

    url = (
        f"https://web.whatsapp.com/send"
        f"?phone={phone}"
        f"&text={message}"
    )

    page.goto(url)

    delay()

    page.wait_for_timeout(8000)

    page.keyboard.press("Enter")

    delay()


def main():

    contacts = load_contacts()

    if not contacts:
        return

    results = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        print("Opening WhatsApp Web...")
        page.goto("https://web.whatsapp.com")

        input(
            "\nScan QR Code and "
            "press ENTER when WhatsApp loads..."
        )

        for contact in contacts:

            name = str(contact["Name"])
            phone = str(contact["Phone"])
            message = str(contact["Message"])

            message = message.replace(
                "{name}",
                name
            )

            row = {
                "Name": name,
                "Phone": phone,
                "Status": "FAILED",
                "Screenshot": "",
                "LastMessages": []
            }

            try:

                print(f"\nSending to {name}")

                send_whatsapp_message(
                    page,
                    phone,
                    message
                )

                screenshot_file = os.path.join(
                    SCREENSHOT_DIR,
                    f"{name}.png"
                )

                page.screenshot(
                    path=screenshot_file
                )

                row["Screenshot"] = screenshot_file
                row["Status"] = "SENT"

                print("Success")

            except Exception as e:

                row["Status"] = str(e)

                print("Failed:", e)

            results.append(row)

            delay()

        save_reports(results)

        browser.close()

    print("\nCompleted Successfully")


if __name__ == "__main__":
    main()