import pytest
import allure
from module.mobile.navigator import Navigator


@pytest.mark.gmb_unlock
@allure.title("OTP解鎖測試-iOS換機Android")
def test_ios_to_android():
    navigator_ios = Navigator().ios.zh
    navigator_and = Navigator().android.zh
    old = navigator_ios.ios_otp_page_mu('old')
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

    # ================================ 換機流程(第二台裝置-android) ================================
    new = navigator_and.otp_page('new')

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
        new.otp_next_btn().click()

    # 輸入啟用碼
    assert new.otp_common_title().text == '輸入 6 位數「啟用碼」'
    new.otp_pwd_input_box(1).send_keys(otp_code[0])
    new.otp_pwd_input_box(2).send_keys(otp_code[1])
    new.otp_pwd_input_box(3).send_keys(otp_code[2])
    new.otp_pwd_input_box(4).send_keys(otp_code[3])
    new.otp_pwd_input_box(5).send_keys(otp_code[4])
    new.otp_pwd_input_box(6).send_keys(otp_code[5])

    # 設定企業行動密碼
    assert new.set_otp_title().text == '設定企業行動密碼'
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

    assert new.otp_success_msg().text == '啟用成功'
    new.agree_btn().click()
    # 啟用生物辨識
    new.bio_check_title().assert_visible()
    new.bio_no_enable_btn().click()
    # 回到驗證網銀交易頁面
    assert new.company_layout().is_visible() is True


@pytest.mark.gmb_unlock
@allure.title("OTP解鎖測試-Android換機iOS")
def test_android_to_ios():
    navigator_ios = Navigator().ios.zh
    navigator_and = Navigator().android.zh
    old = navigator_and.otp_page('old')
    # 同意服務條款
    if old.service_title().is_visible() is True:
        old.scroll_down_btn().click()
        old.agree_btn().click()
    # 驗證網銀交易
    old.verify_trade().click()
    assert old.company_layout().is_visible() is True
    phone_num = old.verify_phone_num2().text
    if phone_num == '手機號碼：0986****89':
        old.unlock_btn().click()
    else:
        pytest.skip(f"手機號碼不符，無法進行OTP解鎖測試,當前手機號碼為: {phone_num}")
    # 輸入企業行動密碼
    old.otp_common_title().assert_visible()
    old.otp_pwd_input_box(1).send_keys("2")
    old.otp_pwd_input_box(2).send_keys("7")
    old.otp_pwd_input_box(3).send_keys("5")
    old.otp_pwd_input_box(4).send_keys("3")
    old.otp_pwd_input_box(5).send_keys("1")
    old.otp_pwd_input_box(6).send_keys("4")
    old.otp_input_check().click()
    # 待驗證清單頁面
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
    old.create_opt_input(1).send_keys("2")
    old.create_opt_input(2).send_keys("7")
    old.create_opt_input(3).send_keys("5")
    old.create_opt_input(4).send_keys("3")
    old.create_opt_input(5).send_keys("1")
    old.create_opt_input(6).send_keys("4")
    # 換機啟用碼顯示頁面
    # TODO 加入loading 等待
    assert old.enabler_code_msg().text == '換機啟用碼'
    otp_code = "".join(old.enabler_code_content(i).text.strip() for i in range(2, 8))
    # ================================ 換機流程(第二台裝置-iOS) ================================
    new = navigator_ios.ios_otp_page_mu('new')

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
        navigator_ios.keyboard_mu('new').done.click()
        new.otp_next_btn().click()

    # 輸入啟用碼
    assert new.otp_title().text == '啟用企業行動密碼'
    # new.start_otp_input().send_keys(otp_code)

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
