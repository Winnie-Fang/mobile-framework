from os import remove

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.device_manager import DeviceManager


class GMBLoginPage(BaseObject):
    def __init__(self, role=None):
        super().__init__()
        self.set_remark("GMB 登入頁多裝置測試")
        self.driver = DeviceManager.get_driver(role)

    def prerequisites(self) -> None:
        self.pre_login().assert_visible()
        self.pre_login().assert_invisible()

    def pre_login(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().className("android.view.View").instance(1)'),
            remark=f"{self.remark()} > 登入前導頁"
        )

    def login_slogan(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/sloganTextView"),
            remark=f"{self.remark()} > 登入標語"
        )

    def id_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/companyIdEditText"),
            remark=f"{self.remark()} > 企業戶ID/統編"
        )

    def user_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/userNameEditText"),
            remark=f"{self.remark()} > 使用者代號"
        )

    def user_pwd(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/pdEditText"),
            remark=f"{self.remark()} > 使用者密碼"
        )

    def login_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/loginButton"),
            remark=f"{self.remark()} > 登入按鈕"
        )

    def dialog_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/dialog_common_message"),
            remark=f"{self.remark()} > 彈跳視窗內容"
        )

    def dialog_login_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/dialog_common_message"),
            remark=f"{self.remark()} > 彈跳視窗登入按鈕"
        )

    def dialog_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("信任裝置")'),
            remark=f"{self.remark()} > 信任裝置標題"
        )

    def truest_device_dialog(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().className("android.view.View").instance(5)'),
            remark=f"{self.remark()} > 信任裝置彈跳視窗"
        )

    def truest_device_dialog2(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("信任裝置")'),
            remark=f"{self.remark()} > 信任裝置標題-彈跳視窗"
        )

    def next_time_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("下次再說")'),
            remark=f"{self.remark()} > 下次再說按鈕"
        )

    def remind_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("提醒")'),
            remark=f"{self.remark()} > 提醒標題"
        )

    def remind_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("此裝置尚未加入您的信任清單，可能導致部分功能無法使用。")'),
            remark=f"{self.remark()} > 提醒視窗內容"
        )

    def check_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().className("android.widget.Button")'),
            remark=f"{self.remark()} > 我知道了"
        )

    def dialog_common_message(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/dialog_common_message'),
            remark=f"{self.remark()} > 未正常登出，已在其他裝置登入[彈跳視窗內容]"
        )

    def dialog_common_right_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/dialog_common_right_btn'),
            remark=f"{self.remark()} > 未正常登出，已在其他裝置登入[登入]"
        )

    # =================================================== 企業行動密碼 ===================================================
    def verify_trade(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, '驗證網銀交易'))),
            remark=f"{self.remark()} > 驗證網銀交易選項"
        )

    def start_OTP_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/btn'),
            remark=f"{self.remark()} > 啟用企業行動密碼按鈕"
        )

    def scroll_down_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/scrollDownAnim'),
            remark=f"{self.remark()} > 向下滑動按鈕"
        )

    def service_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/title_textView'),
            remark=f"{self.remark()} > 服務條款標題"
        )

    # 共用元素(同意/確認)
    def agree_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/rightButton'),
            remark=f"{self.remark()} > 已閱讀並同意服務條款/確認按鈕"
        )

    def otp_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/title_textView'),
            remark=f"{self.remark()} > 啟用企業行動密碼"
        )

    def otp_ID(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().className("android.widget.EditText").instance(0)'),
            remark=f"{self.remark()} > OTP_輸入企業戶ID/統編"
        )

    def otp_phone_number(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().className("android.widget.EditText").instance(1)'),
            remark=f"{self.remark()} > OTP_手機號碼"
        )

    def otp_company_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().className("android.widget.EditText").instance(1)'),
            remark=f"{self.remark()} > OTP_公司別名"
        )

    def otp_next_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().className("android.widget.Button")'),
            remark=f"{self.remark()} > OTP_下一步按鈕"
        )

    def otp_recovered(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/recoveredTextView'),
            remark=f"{self.remark()} > OTP_已申請過企業行動密碼"
        )

    def otp_success_msg(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/messageTextView'),
            remark=f"{self.remark()} > OTP_啟用成功訊息"
        )

    def bio_check_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/dialog_common_title'),
            remark=f"{self.remark()} > 生物辨識標題"
        )

    def bio_check_msg(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/dialog_common_message'),
            remark=f"{self.remark()} > 生物辨識內容"
        )

    def bio_no_enable_(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/dialog_common_message'),
            remark=f"{self.remark()} > 生物辨識_不啟用"
        )

    def unlock_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/verifyReviewedButton'),
            remark=f"{self.remark()} > 解鎖按鈕"
        )

    def otp_input_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/titleTextView'))),
            remark=f"{self.remark()} > 輸入OTP標題"
        )

    def otp_pwd_input_box(self, num):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, f'com.cathaybk.geb.cubuat:id/codeInput{num}'),
            remark=f"{self.remark()} > 第{num}密碼輸入框"
        )

    def otp_input_check(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/transactionRightButton'),
            remark=f"{self.remark()} > 確認按鈕"
        )

    def display_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/transactionDisplayPinCheckBox'),
            remark=f"{self.remark()} > 顯示隱碼按鈕"
        )

    def verify_list_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("待驗證清單")'))),
            remark=f"{self.remark()} > 待驗證清單標題"
        )

    def verify_list_item(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("沒有待驗證交易")'),
            remark=f"{self.remark()} > 沒有待驗證交易"
        )

    def verify_phone_num(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.TextView[@resource-id="com.cathaybk.geb.cubuat:id/phoneNumberTextView"and contains(@text, "手機號碼")]'))),
            remark=f"{self.remark()} > 驗證網銀交易-手機號碼"
        )

    def verify_phone_num2(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                                                         '//android.view.ViewGroup[@resource-id="com.cathaybk.geb.cubuat:id/companyConstraintLayout"]/android.widget.TextView[3]'))),
            remark=f"{self.remark()} > 驗證網銀交易-手機號碼"
        )

    def company_layout(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((AppiumBy.ID,
                                                                                           'com.cathaybk.geb.cubuat:id/companyConstraintLayout'))),
            remark=f"{self.remark()} > 公司別名區塊"
        )
