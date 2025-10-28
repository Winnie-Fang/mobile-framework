import pytest
import allure
from module.mobile.navigator import Navigator
from utils import com_func,appium_manager
# from module.pre_condition.pre_condition_android_zh import PreConditionAndroidZh

@pytest.mark.android_login
@allure.epic("登入測試")
# class TestLogin(PreConditionAndroidZh):
class TestLogin:
    # @pytest.mark.HA001
    @allure.title("HA001")
    def test_login_HA001(self):
        # appium_manager.AppiumManager(4801).start()
        navigator = Navigator().android.zh
        # with allure.step("正常輸入帳號密碼"):
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
        # with allure.step("帳號超過8碼"):

    # @pytest.mark.HA002
    @allure.title("HA002")
    def test_login_HA002(self):
        navigator = Navigator().android.zh
        #navigator.ihave_login_page.login_logo().assert_visible()
        navigator.ihave_login_page.account_input.send_keys("00584360")
        navigator.ihave_login_page.password_input().send_keys("0000123")
        navigator.ihave_login_page.password_toggle().click()
        assert navigator.ihave_login_page.password_input().text == '0000123'
        navigator.ihave_login_page.save_screenshot("顯示密碼")
        navigator.ihave_login_page.password_toggle().click()
        assert navigator.ihave_login_page.password_input().text == '•••••••'
        navigator.ihave_login_page.save_screenshot("遮蓋密碼")

    # @pytest.mark.HA003
    @allure.title("HA003")
    def test_login_HA003(self):
        navigator = Navigator().android.zh
        #navigator.ihave_login_page.login_logo().is_visible()
        com_func.login_process_android('00583904')
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.screenshot_btn().click()
        navigator.personal_page.back().click()
        navigator.personal_page.logout_btn().click()
        navigator.personal_page.logout_confirm().click()
        navigator.ihave_login_page.login_instruction().click()
        navigator.ihave_login_page.login_instruction_title().assert_visible()
        assert navigator.ihave_login_page.login_instruction_text().text is not None
        #navigator.ihave_login_page.save_screenshot("登入說明畫面")
        navigator.ihave_login_page.close_instruction().click()

    # @pytest.mark.HA004
    @allure.title("HA004")
    def test_login_HA004(self):
        navigator = Navigator().android.zh
        navigator.ihave_login_page.login_logo().is_visible()
        # 登入失敗
        navigator.ihave_login_page.account_input.send_keys("00584360")
        navigator.ihave_login_page.password_input().send_keys("0000123")
        navigator.ihave_login_page.login_btn().click()
        assert navigator.ihave_login_page.alert_title().text == "Login Failed"
        navigator.ihave_login_page.driver.save_screenshot("登入失敗")
        navigator.ihave_login_page.login_alert().is_visible()
        navigator.ihave_login_page.close_alert().click()
        # 登入成功
        navigator.ihave_login_page.password_input().clear()
        navigator.ihave_login_page.password_input().send_keys("00001234")
        navigator.ihave_login_page.login_btn().click()
        assert navigator.overview_page.overview_title().text == "Overview"
        navigator.ihave_login_page.driver.save_screenshot("登入成功")
