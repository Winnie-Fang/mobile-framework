import time

import pytest
import allure
from module.mobile.navigator import Navigator
# from module.pre_condition.pre_condition_ios_zh import PreConditionIosZh


@pytest.mark.login_ihave
@allure.epic("登入測試")
# class TestLogin(PreConditionIosZh):
class TestLogin:
    @allure.title("登入")
    def test_login_HA001(self):
        navigator = Navigator().ios.zh
        # with allure.step("正常輸入帳號密碼"):
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.login_logo().assert_visible()
        navigator.ihave_login_page.account_input.send_keys("00584360")
        navigator.ihave_login_page.password_input().send_keys("0000000")
        assert navigator.ihave_login_page.password_input().text == "•••••••"
        # # with allure.step("帳號不足8碼"):
        navigator.ihave_login_page.account_input.clear()
        navigator.ihave_login_page.account_input.send_keys("00584")
        navigator.ihave_login_page.login_btn().click()
        navigator.ihave_login_page.login_alert().is_visible()
        navigator.ihave_login_page.close_alert().is_clickable()
        navigator.ihave_login_page.close_alert().click()
        # # with allure.step("帳號超過8碼"):
        navigator.ihave_login_page.account_input.clear()
        navigator.ihave_login_page.account_input.send_keys("0058436079")
        assert navigator.ihave_login_page.account_input.text == "00584360"
        navigator.ihave_login_page.save_screenshot("登入")
        # with allure.step("帳號超過8碼"):

    @pytest.mark.password
    @allure.title("密碼遮罩測試")
    def test_login_HA002(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.login_logo().assert_visible()
        navigator.ihave_login_page.account_input.send_keys("00584360")
        navigator.ihave_login_page.password_input().send_keys("0000123")
        navigator.ihave_login_page.eyes_close().click()
        assert navigator.ihave_login_page.password_open_input().text == '0000123'
        navigator.ihave_login_page.save_screenshot("顯示密碼")
        navigator.ihave_login_page.eyes_open().click()
        assert navigator.ihave_login_page.password_input().text == '•••••••'
        navigator.ihave_login_page.save_screenshot("遮蓋密碼")

    @allure.title("登入說明測試")
    def test_login_HA003(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.login_logo().is_visible()
        navigator.ihave_login_page.login_instruction().click()
        navigator.ihave_login_page.login_instruction_title().assert_visible()
        assert navigator.ihave_login_page.login_instruction_text().text is not None
        navigator.ihave_login_page.save_screenshot("登入說明畫面")
        navigator.ihave_login_page.close_instruction().click()

    @allure.title("登入說明測試")
    def test_login_HA004(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.login_logo().is_visible()
        # 登入失敗
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00584360")
        navigator.ihave_login_page.password_input().send_keys("0000123")
        navigator.ihave_login_page.login_btn().click()
        assert navigator.ihave_login_page.alert_title().text == "登入失敗"
        navigator.ihave_login_page.driver.save_screenshot("登入失敗")
        navigator.ihave_login_page.login_alert().is_visible()
        navigator.ihave_login_page.close_alert().click()
        # 登入成功
        navigator.ihave_login_page.password_input().clear()
        navigator.ihave_login_page.password_input().send_keys("00001234")
        navigator.ihave_login_page.login_btn().click()
        assert navigator.ios_overview_page.overview_title().text == "總覽"
        navigator.ihave_login_page.driver.save_screenshot("登入成功")

