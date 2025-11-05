import pytest
from module.mobile.navigator import Navigator
import time
import allure


@pytest.mark.ios_login
@allure.title('iOS 登入測試')
def test_ios_login():
    navigator = Navigator().ios.zh
    navigator.ios_login_page.login_slogan().assert_visible()
    navigator.ios_login_page.id_input().is_visible()
    navigator.ios_login_page.id_input().click()
    time.sleep(1)
    navigator.ios_login_page.id_input().send_keys("65141474")
    navigator.ios_login_page.user_name().send_keys("admin01")
    navigator.ios_login_page.user_pwd().send_keys("Ab123456")
    navigator.ios_overview_page.save_screenshot(case='photo', name='輸入使用者資訊', attach_jpg=True, remove=True)
    navigator.ios_login_page.login_btn().click()
    time.sleep(3)
    if navigator.ios_login_page.dialog_common_message().is_visible() is True:
        navigator.ios_overview_page.save_screenshot(case='photo', name='未正常登入', attach_jpg=True, remove=True)
        dialog_common_message_text = navigator.ios_login_page.dialog_common_message().text
        assert dialog_common_message_text == '您上次沒有正常登出，或是已在其他裝置登入，要改為登入目前的裝置嗎？(錯誤代碼：AP07)'
        navigator.ios_login_page.dialog_login_btn().click()
    # 信任裝置談窗
    if navigator.ios_login_page.truest_device_dialog().is_visible() is True:
        navigator.ios_overview_page.save_screenshot(case='photo', name=' 信任裝置', attach_jpg=True, remove=True)
        navigator.ios_login_page.next_time_btn().click()
        navigator.ios_login_page.remind_title().assert_visible()
        dialog_text = navigator.ios_login_page.remind_content().text
        assert dialog_text == '此裝置尚未加入您的信任清單，可能導致部分功能無法使用。'
        navigator.ios_login_page.check_btn().click()

    # 總覽頁面
    navigator.ios_overview_page.to_do_list().is_visible()
    navigator.ios_overview_page.account_overview().is_visible()
    navigator.ios_overview_page.overview().is_visible()
    navigator.ios_overview_page.detail().is_visible()
    navigator.ios_overview_page.payment().is_visible()
    navigator.ios_overview_page.more().is_visible()
    navigator.ios_overview_page.save_screenshot(case='photo', name='總覽頁面', attach_jpg=True, remove=True)
