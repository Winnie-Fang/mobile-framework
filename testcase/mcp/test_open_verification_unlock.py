from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

# Desired capabilities for Android
options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'Android Device'
options.app_package = 'com.cathaybk.geb.cubuat'
# options.app_activity = 'com.cathaybk.geb.cubuat.MainActivity'  # Assuming main activity
options.automation_name = 'UiAutomator2'
options.no_reset = True

# Initialize the driver
driver = webdriver.Remote('http://localhost:4723', options=options)

try:
    # Wait for app to load
    time.sleep(5)

    # Step 1: Click on "驗證網銀交易"
    element1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '驗證網銀交易')
    element1.click()
    time.sleep(2)

    # Step 2: Click on "解鎖"
    element2 = driver.find_element(AppiumBy.XPATH, "//*[@text='解鎖']")
    element2.click()
    time.sleep(2)

    print("Test steps completed successfully.")

finally:
    # Close the driver
    driver.quit()
