from utils_category import open_product_v1_cat_asuspromaxm1, driver, close_dialog, up_button_asuspromaxm1, \
     SCROLL_REFRESH_CAT_PAGE
import time

# Setup Connection and product
SESSION = 30
SCROLL_LOOP = 6
CATEGORY = "Office"
CONNECTION = "192.168.0.100:5555"
SERVER_APPIUM_PORT = "4723"
SERVER_APPIUM_IP = "127.0.0.1"

DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
}

SC_1 = SCROLL_REFRESH_CAT_PAGE
driver = driver(SERVER_APPIUM_IP=SERVER_APPIUM_IP, SERVER_APPIUM_PORT=SERVER_APPIUM_PORT, desired_caps=DESIRED_CAPS)

### Scroll
startx = driver.get_window_size()['width']*1/4; endx = driver.get_window_size()['width']*1/4
starty = driver.get_window_size()['height']*8/11; endy = driver.get_window_size()['height']/8

A = 0
while A <= SESSION:
    k = 0
    while k <= SCROLL_LOOP:
        print (f"Scrape the loop at {k}")
        open_product_v1_cat_asuspromaxm1(CATEGORY=CATEGORY)
        driver.swipe(startx, 1855, endx, 445, 400) # Adjust with your device
        k = k + 1
    try: time.sleep(2); up_button_asuspromaxm1()
    except: pass
    time.sleep(2); driver.swipe(SC_1[0], SC_1[1], SC_1[2], SC_1[3], SC_1[4]) # Adjust with your device
    time.sleep(4); driver.swipe(startx, 1855, endx, 445, 400) # Adjust with your device
    try: time.sleep(1); close_dialog()
    except: pass
    A = A + 1