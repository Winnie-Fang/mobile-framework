import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions


def is_element_present(driver, by, selector):
    try:
        driver.find_element(by, selector)
        return True
    except NoSuchElementException:
        return False

@pytest.fixture(scope="function")
def driver():
    # desired_caps = {
    #     "platformName": "Android",
    #     "udid": "58301FDCR0030G",
    #     "automationName": "UiAutomator2",
    #     "appPackage": "com.cathaybk.geb.cubuat",
    #     "appActivity": "com.cathaybk.geb.cubuat.MainActivity",
    #     "noReset": True
    # }
    option =AppiumOptions()
    option.set_capability("platformName", "Android")
    option.set_capability("udid", "58301FDCR0030G")
    option.set_capability("automationName", "UiAutomator2")
    option.set_capability("appPackage", "com.cathaybk.geb.cubuat")
    option.set_capability("appActivity", "com.cathaybk.geb.cubuat.MainActivity")
    option.set_capability("noReset", True)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=option)
    yield driver
    driver.quit()

def test_android_simple(driver):
    # Simple test: Login and reach overview page

    # Input login details
    company_id = driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/companyIdEditText')
    company_id.send_keys("65141474")
    user_name = driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/userNameEditText')
    user_name.send_keys("admin01")
    password = driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/pdEditText')
    password.send_keys("Ab123456")
    login_btn = driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/loginButton')
    login_btn.click()

    # Handle popups
    if is_element_present(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("下次再說")'):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("下次再說")').click()
    if is_element_present(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")'):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")').click()

    # Wait for overview page
    WebDriverWait(driver, 30).until(lambda d: is_element_present(d, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("總覽").instance(0)'))

    # Simple assertion: Overview title is displayed
    assert is_element_present(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("總覽").instance(0)'), "總覽頁標題 should be displayed"
