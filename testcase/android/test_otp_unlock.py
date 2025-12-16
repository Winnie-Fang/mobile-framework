import pytest
import allure
from module.mobile.navigator import Navigator


# @pytest.mark.gmb_unlock
def test_unlock_001():
    navigator = Navigator().android.zh
    navigator.gmb_login_page.pre_login().assert_visible()
    navigator.gmb_login_page.login_slogan().assert_visible()
    navigator.gmb_login_page.id_input().is_visible()
    navigator.gmb_login_page.verify_trade().click()
    assert navigator.gmb_login_page.company_layout().is_visible() is True
    phone_num = navigator.gmb_login_page.verify_phone_num2().text
    if phone_num  == '手機號碼：0986****89':
        navigator.gmb_login_page.unlock_btn().click()
    else:
        pytest.skip(f"手機號碼不符，無法進行OTP解鎖測試,當前手機號碼為: {phone_num}")
    # 輸入企業行動密碼
    navigator.gmb_login_page.otp_input_title().assert_visible()
    navigator.gmb_login_page.otp_pwd_input_box(1).send_keys("2")
    navigator.gmb_login_page.otp_pwd_input_box(2).send_keys("7")
    navigator.gmb_login_page.otp_pwd_input_box(3).send_keys("5")
    navigator.gmb_login_page.otp_pwd_input_box(4).send_keys("3")
    navigator.gmb_login_page.otp_pwd_input_box(5).send_keys("1")
    navigator.gmb_login_page.otp_pwd_input_box(6).send_keys("4")
    navigator.gmb_login_page.otp_input_check().click()
    # 待驗證清單頁面
    navigator.gmb_login_page.verify_list_title()
    assert navigator.gmb_login_page.verify_list_title().is_visible() is True
    assert navigator.gmb_login_page.verify_list_item().text == "沒有待驗證交易"




