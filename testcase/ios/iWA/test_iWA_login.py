import pytest
import allure
from module.mobile.navigator import Navigator
import time

@pytest.mark.iWA_login
@allure.epic("登入測試")
class TestLogin:
    @allure.title("登入")
    @pytest.mark.parametrize("i",range(2))
    def test_login_IWA001(self,i):
        navigator = Navigator().ios.zh
        # time.sleep(3)
        # assert  navigator.iwa_login_page.account_input.is_visible() == True
        navigator.iwa_login_page.account_input.send_keys("03077")
        navigator.iwa_login_page.password_input().send_keys("275314")
        navigator.iwa_login_page.login_btn().click()
        # privacy_popup_text = navigator.iwa_login_page.privacy_popup_text().text
        # assert privacy_popup_text == "隱私權責同意書"
        # navigator.iwa_login_page.privacy_agree_btn().click()

