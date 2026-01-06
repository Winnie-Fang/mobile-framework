import pytest
import allure
from module.mobile.navigator import Navigator


@pytest.mark.ios
@pytest.mark.gmb_unlock
@allure.title("OTP解鎖測試")
def test_unlock_001():
    navigator = Navigator().ios.zh
    old = navigator.ios_otp_page_mu('old')
    old.verify_trade().click()

    assert old.company_layout().is_visible() is True
    phone_num = old.verify_phone_num().text

    if '手機號碼：0986****89' in phone_num:
        old.unlock_btn().click()
    else:
        pytest.skip(f"手機號碼不符，無法進行OTP解鎖測試,當前手機號碼為: {phone_num}")
    # 輸入企業行動密碼
    old.otp_input_title().assert_visible()
    old.otp_pwd_input_box(1).send_keys("2")
    old.otp_pwd_input_box(2).send_keys("7")
    old.otp_pwd_input_box(3).send_keys("5")
    old.otp_pwd_input_box(4).send_keys("3")
    old.otp_pwd_input_box(5).send_keys("1")
    old.otp_pwd_input_box(6).send_keys("4")
    old.otp_check_btn().click()
    # 待驗證清單頁面
    old.verify_list_title()
    assert old.verify_list_title().is_visible() is True
    assert old.verify_list_item().text == "沒有待驗證交易"
    # ========================= 解鎖到此結束 ==========================
    # 更多設定-設定換機密碼
    old.more_setting_btn().click()
    old.change_phone_setting().click()
    old.create_activation_code().click()
    old.continue_btn().click()
    old.create_number_msg().assert_visible()
    assert old.create_number_msg().text == "您即將創建換機啟用碼"
    old.create_btn().click()
    # 輸入企業行動密碼
    assert old.create_remind_msg().text == '驗證成功後即可進行換機'
    old.create_opt_input().send_keys("275314")
    # 換機啟用碼顯示頁面
    assert old.enabler_code_msg().text == '換機啟用碼'
    otp_code = "".join(old.enabler_code_content(i).text.strip() for i in range(2, 8))

    # ================================ 換機流程(第二台裝置) ================================
    new = navigator.ios_otp_page_mu('new')

    new.verify_trade().click()
    new.start_OTP_btn().assert_visible()
    new.start_OTP_btn().click()
    # 企業行動密碼條款
    new.service_title().assert_visible()
    new.scroll_down_btn().click()
    new.agree_btn().click()
    # 啟用企業行動密碼輸入畫面
    if new.otp_title().is_visible() is True:
        assert new.otp_title().text == '啟用企業行動密碼'
        new.otp_ID().send_keys("65141474")
        new.otp_phone_number().send_keys("0986543789")
        new.otp_company_name().send_keys('QAtest')
        navigator.keyboard_mu('new').done.click()
        new.otp_next_btn().click()

    # 輸入啟用碼
    assert new.otp_title().text == '啟用企業行動密碼'
    new.start_otp_input().send_keys(otp_code)

    # 設定企業行動密碼
    assert new.set_otp().text == '設定企業行動密碼'
    new.set_otp_input(1).send_keys("2")
    new.set_otp_input(2).send_keys("7")
    new.set_otp_input(3).send_keys("5")
    new.set_otp_input(4).send_keys("3")
    new.set_otp_input(5).send_keys("1")
    new.set_otp_input(6).send_keys("4")
    # 再次輸入企業行動密碼
    new.set_otp_again_input(1).send_keys("2")
    new.set_otp_again_input(2).send_keys("7")
    new.set_otp_again_input(3).send_keys("5")
    new.set_otp_again_input(4).send_keys("3")
    new.set_otp_again_input(5).send_keys("1")
    new.set_otp_again_input(6).send_keys("4")

    assert new.set_success_msg().text == '啟用成功'

    new.otp_check_btn().click()
    # 啟用生物辨識
    new.bio_check_title().assert_visible()
    new.bio_no_enable_btn().click()
    # 回到驗證網銀交易頁面
    assert new.company_layout().is_visible() is True


def test_lock_process():
    navigator = Navigator().ios.zh
    # role_1 = 'old'
    old = navigator.ios_otp_page_mu('old')
    # old_keyboard = navigator.keyboard_mu('old')
    old.verify_trade().click()
    old.start_OTP_btn().assert_visible()
    old.start_OTP_btn().click()
    # 企業行動密碼條款
    old.service_title().assert_visible()
    old.scroll_down_btn().click()
    old.agree_btn().click()
    # 啟用企業行動密碼輸入畫面
    if old.otp_title().is_visible() is True:
        assert old.otp_title().text == '啟用企業行動密碼'
        old.otp_ID().send_keys("65141474")
        old.otp_phone_number().send_keys("0986543789")
        old.otp_company_name().send_keys('QAtest')
        navigator.keyboard_mu('old').done.click()
        # old.otp_next_btn().click()
        # 輸入企業行動密碼
        # old.reset_otp_title().assert_visible()
        # old.otp_pwd_input_box(1)
    new = navigator.ios_otp_page_mu('new')

    new.verify_trade().click()
    new.start_OTP_btn().assert_visible()
    new.start_OTP_btn().click()
    # 企業行動密碼條款
    new.service_title().assert_visible()
    new.scroll_down_btn().click()
    new.agree_btn().click()
    # 啟用企業行動密碼輸入畫面
    if new.otp_title().is_visible() is True:
        assert old.otp_title().text == '啟用企業行動密碼'
        new.otp_ID().send_keys("65141474")
        new.otp_phone_number().send_keys("0986543789")
        new.otp_company_name().send_keys('QAtest')
        navigator.keyboard_mu('new').done.click()
    # old.otp_phone_number().clear()
    old.otp_company_name().send_keys('QA')
    old.otp_next_btn().click()
    # 輸入啟用碼
    assert old.otp_title().text() == '啟用企業行動密碼'
    # 設定企業行動密碼
    assert old.set_otp().text() == '設定企業行動密碼'
    old.set_otp_input(1).send_keys("2")
    old.set_otp_input(2).send_keys("7")
    old.set_otp_input(3).send_keys("5")
    old.set_otp_input(4).send_keys("3")
    old.set_otp_input(5).send_keys("1")
    old.set_otp_input(6).send_keys("4")
    # 再次輸入企業行動密碼
    old.set_otp_again_input(1).send_keys("2")
    old.set_otp_again_input(2).send_keys("7")
    old.set_otp_again_input(3).send_keys("5")
    old.set_otp_again_input(4).send_keys("3")
    old.set_otp_again_input(5).send_keys("1")
    old.set_otp_again_input(6).send_keys("4")

    assert old.set_success_msg().text == '啟用成功'

    old.check_btn().click()
    # 啟用生物辨識
    old.bio_check_title().assert_visible()
    old.bio_no_enable_btn().click()
    # 回到驗證網銀交易頁面
    assert old.company_layout().is_visible() is True
