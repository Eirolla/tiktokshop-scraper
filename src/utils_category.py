from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup connection
ASUSPROMAXM1 = "192.168.0.106:5555"

# Setup Component for Asus Pro Max M1
SHARE_BUTTON = "com.ss.android.ugc.trill:id/i3u"
COPY_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView"
CLOSE_DIALOG = "com.ss.android.ugc.trill:id/iaz"
UP_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/X.UGo/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.view.UIView[18]"
BACK_BUTTON = "com.ss.android.ugc.trill:id/a43"

# Setup coordinat
"""
Setup Coordinat for Asus Pro Max M1
Structure (start_x, start_y, end_x, end_y, speed)
"""
SCROLL_REFRESH_CAT_PAGE = [500, 465, 500, 948, 400]
SELECT_PRODUCT = {210 : 443, 788 : 437, 211 : 1621, 791 : 1622}
SCROLL_DOWN = [555, 1828, 555, 551, 400]

# Setup the Appium driver
def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

# coordinat of up button # Adjust with your device
def up_button_asuspromaxm1(): 
    TouchAction(driver).tap(None, 962, 1762).perform()

# close unnecesary dialogbox
def close_dialog(): 
    return driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_DIALOG}").click() 

# Click share link and copy
def get_link_cat_asuspromaxm1():
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

# Open Product by Coordinat

def open_product_v1_cat_asuspromaxm1(CATEGORY):
    actions = TouchAction(driver)
    df = [] 
    # Click coordinat
    for i, j in SELECT_PRODUCT.items():
        try: time.sleep(2); actions.tap(None,i,j).perform()
        except: continue
        # try: close_dialog()
        # except: pass
        try:
            link = get_link_cat_asuspromaxm1()
            print("found link : ", link)
            df.append(link)
            driver.back(); continue
        except: pass
        try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click(); print("back, wrong click!")
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'./url/{CATEGORY}.csv', mode='a', index=False, header=False)