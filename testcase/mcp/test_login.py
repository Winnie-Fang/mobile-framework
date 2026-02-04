import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class TestLogin:
    def setup_method(self):
        caps = {
            'platformName': 'Android',
            'deviceName': 'Android Device',
            'automationName': 'UiAutomator2',
            'appPackage': 'com.cathaybk.geb.cubuat',
            'appActivity': 'com.cathaybk.geb.cubuat.MainActivity',
            'appWaitActivity': 'com.cathaybk.geb.cubuat.MainActivity',
            'noReset': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        # 輸入企業戶ID
        company_id = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/companyIdEditText')
        company_id.send_keys('65141474')

        # 輸入使用者代號
        user_name = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/userNameEditText')
        user_name.send_keys('admin01')

        # 輸入使用者密碼
        password = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/pdEditText')
        password.send_keys('Ab123456')

        # 點擊登入
        login_btn = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/loginButton')
        login_btn.click()

        # 斷言：等待登入成功後的元素，例如主頁面元素
        # self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/main_page_element')
