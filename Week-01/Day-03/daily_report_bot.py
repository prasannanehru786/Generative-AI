import pyautogui
import time
from datetime import datetime

# ----------------------------------
# CONFIGURATION
# ----------------------------------
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

FIFA_TEAMS = (
    "Argentina, Brazil, France, England, Spain, Germany, "
    "Portugal, Netherlands, Belgium, Uruguay, Colombia, Morocco, Japan"
)

COMMENT = "FIFA 2026 World Cup Report Generated Automatically"

# ----------------------------------
# FUNCTIONS
# ----------------------------------

def open_chrome():
    print("Opening Chrome...")

    pyautogui.press("win")
    time.sleep(1)

    pyautogui.write("chrome", interval=0.05)
    pyautogui.press("enter")

    time.sleep(5)


def open_google_sheets():
    print("Opening Google Sheets...")

    pyautogui.hotkey("ctrl", "l")

    pyautogui.write(
        "https://docs.google.com/spreadsheets/create",
        interval=0.02
    )

    pyautogui.press("enter")

    time.sleep(10)


def create_headers():
    print("Creating headers...")

    headers = ["Timestamp", "FIFA 2026 Teams", "Comment"]

    for header in headers:
        pyautogui.write(header, interval=0.02)
        pyautogui.press("tab")

    # Go to next row
    pyautogui.press("enter")

    # Return to A2
    pyautogui.hotkey("shift", "tab")
    pyautogui.hotkey("shift", "tab")
    pyautogui.hotkey("shift", "tab")


def insert_report_data():
    print("Inserting report data...")

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    pyautogui.write(timestamp, interval=0.02)
    pyautogui.press("tab")

    pyautogui.write(FIFA_TEAMS, interval=0.01)
    pyautogui.press("tab")

    pyautogui.write(COMMENT, interval=0.02)

    print("Data inserted.")


def format_header_row():
    """
    Select first row and make it bold.
    Works in Google Sheets.
    """

    print("Formatting header row...")

    # Go to A1
    pyautogui.hotkey("ctrl", "home")
    time.sleep(1)

    # Select row 1
    pyautogui.hotkey("shift", "space")
    time.sleep(1)

    # Bold
    pyautogui.hotkey("ctrl", "b")
    time.sleep(1)

    # Return to A2
    pyautogui.press("down")
    pyautogui.press("down")


def rename_sheet():
    print("Renaming spreadsheet...")

    report_name = (
        "daily_report_" +
        datetime.now().strftime("%Y-%m-%d")
    )

    # Shortcut to rename document
    pyautogui.hotkey("alt", "shift", "f")
    time.sleep(2)

    pyautogui.write(report_name, interval=0.03)

    pyautogui.press("enter")

    print("Report Name:", report_name)


def save_screenshot():
    print("Capturing screenshot...")

    today = datetime.now().strftime("%Y-%m-%d")

    screenshot_name = (
        f"daily_report_{today}.png"
    )

    time.sleep(2)

    pyautogui.screenshot(screenshot_name)

    print("Saved:", screenshot_name)


# ----------------------------------
# MAIN
# ----------------------------------

def main():

    try:

        open_chrome()

        open_google_sheets()

        create_headers()

        insert_report_data()

        format_header_row()

        save_screenshot()

        print("\n======================")
        print("REPORT GENERATED")
        print("======================")

    except Exception as error:

        print("Error:", error)


if __name__ == "__main__":
    main()