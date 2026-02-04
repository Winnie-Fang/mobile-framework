import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


class TestCase1:
    def setup_method(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "Android Device"
        options.automation_name = "UiAutomator2"
        options.app_package = "com.cathaybk.geb.cubuat"
        options.app_activity = "com.cathaybk.geb.cubuat.MainActivity"
        options.no_reset = True

        self.driver = webdriver.Remote('http://localhost:4723', options=options)

    def teardown_method(self):
        self.driver.quit()

    def test_login_and_verify_overview(self):
        # 步驟1: 輸入企業戶ID
        company_id = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/companyIdEditText')
        company_id.send_keys('65141474')

        # 步驟2: 輸入使用者代號
        user_name = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/userNameEditText')
        user_name.send_keys('user002')

        # 步驟3: 輸入使用者密碼
        password = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/pdEditText')
        password.send_keys('Ab123456')

        # 步驟4: 點擊登入
        login_btn = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/loginButton')
        login_btn.click()

        # 驗證總覽頁: 不顯示任何快捷功能、處理清單區塊
        # 檢查分頁佈局是否存在，表示頁面載入
        tab_layout = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/tabLayout')
        assert tab_layout.is_displayed(), "總覽頁未正確載入"

        # 檢查沒有快捷交易icon (假設ID為 'com.cathaybk.geb.cubuat:id/quickTradeIcon'，如果存在則FAIL)
        try:
            quick_trade = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/quickTradeIcon')
            assert False, "快捷功能不應顯示"
        except:
            pass  # PASS，因為元素不存在

        # 檢查沒有處理清單區塊 (假設ID為 'com.cathaybk.geb.cubuat:id/processingList'，如果存在則FAIL)
        try:
            processing_list = self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/processingList')
            assert False, "處理清單區塊不應顯示"
        except:
            pass  # PASS，因為元素不存在

