import pytest
import allure
from module.mobile.navigator import Navigator

import time

@pytest.mark.gmb_login
def test_login_gmb_001():
    navigator = Navigator().android.zh
    navigator.gmb_login_page.pre_login().assert_visible()
    navigator.gmb_login_page.login_slogan().assert_visible()
    navigator.gmb_login_page.id_input().is_visible()
    navigator.gmb_login_page.id_input().send_keys("65141474")
    navigator.gmb_login_page.user_name().send_keys("admin01")
    navigator.gmb_login_page.user_pwd().send_keys("Ab123456")
    navigator.gmb_login_page.login_btn().click()
    time.sleep(3)
    if navigator.gmb_login_page.dialog_common_message().is_visible() is True:
        dialog_common_message_text=navigator.gmb_login_page.dialog_common_message().text
        assert dialog_common_message_text == '您上次沒有正常登出，或是已在其他裝置登入，要改為登入目前的裝置嗎？'
        navigator.gmb_login_page.dialog_common_right_btn().click()
    time.sleep(3)
    # 信任裝置談窗
    if navigator.gmb_login_page.truest_device_dialog2().is_visible() is True:
        navigator.gmb_login_page.next_time_btn().click()
        navigator.gmb_login_page.remind_title().assert_visible()
        dialog_text = navigator.gmb_login_page.remind_content().text
        assert dialog_text == '此裝置尚未加入您的信任清單，可能導致部分功能無法使用。'
        navigator.gmb_login_page.check_btn().click()

    # 總覽頁面
    navigator.gmb_overview_page.to_do_list().is_visible()
    navigator.gmb_overview_page.account_overview().is_visible()
    navigator.gmb_overview_page.overview().is_visible()
    navigator.gmb_overview_page.detail().is_visible()
    navigator.gmb_overview_page.payment().is_visible()
    navigator.gmb_overview_page.more().is_visible()
    navigator.gmb_overview_page.save_screenshot(case='photo',name= '總覽頁面',attach_jpg=True,remove=True)
