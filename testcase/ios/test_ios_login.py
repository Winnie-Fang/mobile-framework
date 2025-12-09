import pytest
from module.mobile.navigator import Navigator
import time
import allure
from page.ios.panel.keyboard import Keyboard


# @pytest.mark.ios_login
# @allure.epic("iOS")
# @allure.feature("登入")
# @allure.title("一般登入流程")
# def test_login_general():
#     navigator = Navigator().ios.zh
#     navigator.ios_login_page.login_slogan().assert_visible()
#     navigator.ios_login_page.id_input().is_visible()
#     navigator.ios_login_page.id_input().click()
#     time.sleep(1)
#     navigator.ios_login_page.id_input().send_keys("65141474")
#     navigator.ios_login_page.user_name().send_keys("admin01")
#     navigator.ios_login_page.user_pwd().send_keys("Ab123456")
#     time.sleep(0.5)
#     navigator.ios_login_page.login_btn().click()
#     navigator.ios_overview_page.save_screenshot(case='photo', name='輸入使用者資訊', attach_jpg=True, remove=True)
#
#     time.sleep(1)
#     if navigator.ios_login_page.dialog_common_message().is_visible() is True:
#         navigator.ios_overview_page.save_screenshot(case='photo', name='未正常登入', attach_jpg=True, remove=True)
#         dialog_common_message_text = navigator.ios_login_page.dialog_common_message().text
#         assert dialog_common_message_text == '您上次沒有正常登出，或是已在其他裝置登入，要改為登入目前的裝置嗎？(錯誤代碼：AP07)'
#         navigator.ios_login_page.dialog_login_btn().click()
#
#     time.sleep(1.5)
#     # 信任裝置談窗
#     if navigator.ios_login_page.truest_device_dialog().is_visible() is True:
#         navigator.ios_overview_page.save_screenshot(case='photo', name=' 信任裝置', attach_jpg=True, remove=True)
#         navigator.ios_login_page.next_time_btn().click()
#         navigator.ios_login_page.remind_title().assert_visible()
#         dialog_text = navigator.ios_login_page.remind_content().text
#         assert dialog_text == '此裝置尚未加入您的信任清單，可能導致部分功能無法使用。'
#         navigator.ios_login_page.check_btn().click()
#
#     # 總覽頁面
#     navigator.ios_overview_page.to_do_list().is_visible()
#     navigator.ios_overview_page.account_overview().is_visible()
#     navigator.ios_overview_page.overview().is_visible()
#     navigator.ios_overview_page.detail().is_visible()
#     navigator.ios_overview_page.payment().is_visible()
#     navigator.ios_overview_page.more().is_visible()
#     navigator.ios_overview_page.save_screenshot(case='photo', name='總覽頁面', attach_jpg=True, remove=True)


data =  [("經辦", "65141474", "user001", "Ab123456"),("主管", "65141474", "user002", "Ab123456")]
ids = [f"case : {i}"for i in range(1,len(data)+1)]
@pytest.mark.overview
@allure.epic("iOS")
@allure.feature("總覽")
@allure.title('經辦登入流程')
@pytest.mark.parametrize("role,id_number,username,password",data,ids=ids)
def test_ios_login(role,id_number, username, password):
    # allure.dynamic.description(f"當前啟動前登入資訊：\n ID: {id_number}\n 使用者代號: {username}\n 使用者密碼: {password}")
    navigator = Navigator().ios.zh
    navigator.ios_login_page.login_slogan().assert_visible()
    assert navigator.ios_login_page.id_input().is_ready() is True
    time.sleep(1)
    navigator.ios_login_page.id_input().click()
    navigator.ios_login_page.id_input().clear()
    # 數字鍵盤輸入
    navigator.keyboard.number_btn.click()
    navigator.keyboard.six.click()
    navigator.keyboard.five.click()
    navigator.keyboard.one.click()
    navigator.keyboard.four.click()
    navigator.keyboard.one.click()
    navigator.keyboard.four.click()
    navigator.keyboard.seven.click()
    navigator.keyboard.four.click()
    time.sleep(0.5)
    navigator.ios_login_page.user_name().send_keys(username)
    navigator.ios_login_page.user_pwd().send_keys(password)
    navigator.keyboard.done.click()
    navigator.ios_overview_page.save_screenshot(case='photo', name='輸入使用者資訊', attach_jpg=True, remove=True)
    navigator.ios_login_page.login_btn().click()
    # 未正常登出彈窗
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
    navigator.ios_overview_page.save_screenshot(case='photo', name='總覽頁面', attach_jpg=True, remove=True)
    assert navigator.ios_overview_page.to_do_list().is_visible() is True, "處理清單未顯示"
    assert navigator.ios_overview_page.account_overview().is_visible() is True, "帳戶摘要未顯示"
    assert navigator.ios_overview_page.recent_reserve().is_visible() is True, "近一年預約未顯示,請確認使用者權限"
    assert navigator.ios_overview_page.under_review().is_visible() is True, "送審中交易未顯示,請確認使用者權限"
    # 下方功能列
    assert navigator.ios_overview_page.overview().is_visible() is True, "總覽功能未顯示"
    assert navigator.ios_overview_page.detail().is_visible() is True, "明細功能未顯示"
    assert navigator.ios_overview_page.payment().is_visible() is True, "交易功能未顯示"
    assert navigator.ios_overview_page.more().is_visible() is True, "更多功能未顯示"
