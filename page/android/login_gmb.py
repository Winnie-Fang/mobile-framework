from os import remove

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.device_manager import DeviceManager


class GMBLoginPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("GMB 登入頁")
        self.driver = DeviceManager.get_driver()



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
            lambda :self.driver.find_element(AppiumBy.ID,"com.cathaybk.geb.cubuat:id/dialog_common_message"),
            remark=f"{self.remark()} > 彈跳視窗內容"
        )

    def dialog_login_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.geb.cubuat:id/dialog_common_message"),
            remark=f"{self.remark()} > 彈跳視窗登入按鈕"
        )
    def dialog_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("信任裝置")'),
            remark=f"{self.remark()} > 信任裝置標題"
        )
    def truest_device_dialog(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(5)'),
            remark=f"{self.remark()} > 信任裝置彈跳視窗"
        )

    def truest_device_dialog2(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("信任裝置")'),
            remark=f"{self.remark()} > 信任裝置標題-彈跳視窗"
        )

    def next_time_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("下次再說")'),
            remark=f"{self.remark()} > 下次再說按鈕"
        )
    def remind_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提醒")'),
            remark=f"{self.remark()} > 提醒標題"
        )
    def remind_content(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("此裝置尚未加入您的信任清單，可能導致部分功能無法使用。")'),
            remark=f"{self.remark()} > 提醒視窗內容"
        )
    def check_btn(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Button")'),
            remark=f"{self.remark()} > 我知道了"
        )
    def dialog_common_message(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.geb.cubuat:id/dialog_common_message'),
            remark=f"{self.remark()} > 未正常登出，已在其他裝置登入[彈跳視窗內容]"
        )
    def dialog_common_right_btn(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.geb.cubuat:id/dialog_common_right_btn'),
            remark=f"{self.remark()} > 未正常登出，已在其他裝置登入[登入]"
        )
    # 'new UiSelector().text("我知道了"
