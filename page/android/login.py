from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.basic_select import BasicWebSelect
from module.mobile.component.sliding_object import SlidingObject
from module.mobile.device_manager import DeviceManager


class IhaveLoginPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("國泰員工服務登入頁")
        self.driver = DeviceManager.get_driver()

    # 先決條件
    # def ready(self):
    #     self.prerequisites()
    #     return self

    def prerequisites(self) -> None:
        self.login_logo().assert_visible()
        self.account_input.assert_visible()
        self.password_input().assert_visible()

    # @property
    def login_logo(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/login_logo"),
            remark=f"{self.remark()} > 登入logo"
        )

    # def login_logo(self):
    #     return BasicComponent(
    #         lambda: WebDriverWait(self.driver,20).until(EC._element_if_visible()),
    #         remark=f"{self.remark()} > 登入logo"
    #     )
    @property
    def account_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/login_id_input"),
            remark=f"{self.remark()} > 輸入帳號"
        )

    def password_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/login_pw_input"),
            remark=f"{self.remark()} > 輸入密碼"
        )

    def password_toggle(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/login_pw_toggle"),
            remark=f"{self.remark()} > 密碼遮蔽鈕"
        )

    def login_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/btn_login"),
            remark=f"{self.remark()} > 登入"
        )

    def login_alert(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))
            ),
            remark=f"{self.remark()} > 登入失敗彈窗"
        )

    def alert_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/alertTitle"),
            remark=f"{self.remark()} > 登入失敗標題"
        )
    # def close_alert(self):
    #     return BasicComponent(
    #         lambda: self.driver.find_element(AppiumBy.ID, "android:id/button1"),
    #         remark=f"{self.remark()} > 關閉彈窗"
    #     )

    def close_alert(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))
            ),
            remark=f"{self.remark()} > 關閉登入失敗彈窗"
        )

    def login_instruction(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/about_login"),
            remark=f"{self.remark()} > 登入說明"
        )

    def login_instruction_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/about_login_title"),
            remark=f"{self.remark()} > 登入說明標題"
        )

    def login_instruction_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/about_login_acc_pw"),
            remark=f"{self.remark()} > 登入說明內容"
        )

    def close_instruction(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "android:id/button2"),
            remark=f"{self.remark()} > 關閉登入說明"
        )


    def logout(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/btn_logout"),
            remark=f"{self.remark()} > 登出"
        )
