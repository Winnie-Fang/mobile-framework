import pytest
import allure
from module.mobile.navigator import Navigator


@pytest.mark.android
# @pytest.mark.gmb_test
@allure.title("啟用企業行動密碼測試")
def test_enable_otp():
    navigator = Navigator().android.zh
    old = navigator.otp_page('old')
    # 步驟 1: 點擊驗證網銀交易
    old.verify_trade().click()
    # 步驟 2: 點擊啟用企業行動密碼
    old.start_OTP_btn().click()
    # 步驟 3: 點擊向下的按鈕並點擊已閱讀並同意
    old.scroll_down_btn().click()
    old.agree_btn().click()
    # 步驟 4: 在企業戶id /統編欄位輸入：65141474
    old.otp_ID().send_keys("65141474")
    # 步驟 5: 在手機號碼欄位輸入：0986543789
    old.otp_phone_number().send_keys("0986543789")
    # 步驟 6: 公司別名欄位輸入：QAtest
    old.otp_company_name().send_keys('QAtest')
    # 點選下一步
    old.otp_next_btn().click()
