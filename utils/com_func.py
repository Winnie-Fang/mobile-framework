from module.mobile.navigator import Navigator
import logging

def login_process_android(empid):
    navigator = Navigator().android.zh
    navigator.ihave_login_page.account_input.send_keys(empid)
    navigator.ihave_login_page.password_input().send_keys("00000000")
    navigator.ihave_login_page.login_btn().click()
    logging.info("✅ 成功登入iHave")

def login_process_ios():
    navigator = Navigator().ios.zh
    navigator.ihave_login_page.driver.switch_to.alert.accept()
    navigator.ihave_login_page.account_input.send_keys("00589112")
    navigator.ihave_login_page.password_input().send_keys("00000000")
    navigator.ihave_login_page.login_btn().click()
    logging.info("✅ 成功登入iHave")