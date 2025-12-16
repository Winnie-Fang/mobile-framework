import pytest
import allure
from module.mobile.navigator import Navigator

@pytest.mark.ios
@pytest.mark.gmb_unlock
def test_unlock_001():
    navigator = Navigator().ios.zh
    navigator.ios_otp_page.verify_trade().click()
    assert navigator.ios_otp_page.company_layout().is_visible() is True
    phone_num = navigator.ios_otp_page.verify_phone_num().text
    if '手機號碼：0986****89' in phone_num:
        navigator.ios_otp_page.unlock_btn().click()
    else:
        pytest.skip(f"手機號碼不符，無法進行OTP解鎖測試,當前手機號碼為: {phone_num}")
    # 輸入企業行動密碼
    navigator.ios_otp_page.otp_input_title().assert_visible()
    navigator.ios_otp_page.otp_pwd_input_box(1).send_keys("2")
    navigator.ios_otp_page.otp_pwd_input_box(2).send_keys("7")
    navigator.ios_otp_page.otp_pwd_input_box(3).send_keys("5")
    navigator.ios_otp_page.otp_pwd_input_box(4).send_keys("3")
    navigator.ios_otp_page.otp_pwd_input_box(5).send_keys("1")
    navigator.ios_otp_page.otp_pwd_input_box(6).send_keys("4")
    navigator.ios_otp_page.otp_input_check().click()
    # 待驗證清單頁面
    navigator.ios_otp_page.verify_list_title()
    assert navigator.ios_otp_page.verify_list_title().is_visible() is True
    assert navigator.ios_otp_page.verify_list_item().text == "沒有待驗證交易"
