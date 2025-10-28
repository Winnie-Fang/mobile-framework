from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.basic_select import BasicWebSelect
from module.mobile.component.sliding_object import SlidingObject
from module.mobile.device_manager import DeviceManager


class IWALoginPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("國泰智能財富顧問")
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
    @property
    def account_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@value='帳號']"),
            remark=f"{self.remark()} > 輸入帳號"
        )

    def password_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@value="密碼"]'),
            remark=f"{self.remark()} > 輸入密碼"
        )

    def password_open_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="0000123"]'),
            remark=f"{self.remark()} > 密碼內容(無隱碼）"
        )

    def eyes_close(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "eyeClose"),
            remark=f"{self.remark()} > 密碼遮蔽鈕(關閉)"
        )

    def eyes_open(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "eyeOpen"),
            remark=f"{self.remark()} > 密碼遮蔽鈕(開啟)"
        )

    def login_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='登入']"),
            remark=f"{self.remark()} > 登入"
        )
    def privacy_popup_text(self):
        return BasicComponent(
            self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='隱私權責同意書']"),
            remark=f"{self.remark()} > 隱私權責同意書_文字"
        )
    def privacy_other_btn(self):
        return BasicComponent(
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "使用其他服務方式"),
            remark=f"{self.remark()} > 使用其他服務方式_btn"
        )
    def privacy_agree_btn(self):
        return BasicComponent(
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "同意並承諾上開事項"),
            remark=f"{self.remark()} > 同意並承諾上開事項_btn"
        )
    def login_alert(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((AppiumBy.IOS_CLASS_CHAIN,
                                            '**/XCUIElementTypeAlert[`name == "登入失敗"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]'))
            ),
            remark=f"{self.remark()} > 登入失敗彈窗"
        )

    def alert_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "登入失敗"`]'),
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
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "關閉"))
            ),
            remark=f"{self.remark()} > 關閉登入失敗彈窗"
        )

    def login_instruction(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "登入說明"`]'),
            remark=f"{self.remark()} > 登入說明"
        )

    def login_instruction_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "登入說明"`][2]'),
            remark=f"{self.remark()} > 登入說明標題"
        )

    def login_instruction_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '帳號：國泰員工入口網帳號 \n密碼：國泰員工入口網密碼 \n\n若忘記密碼，請至 國泰員工入口網 \n點選忘記密碼，重新申請補發。'),
            remark=f"{self.remark()} > 登入說明內容"
        )

    def close_instruction(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "關閉"),
            remark=f"{self.remark()} > 關閉登入說明"
        )

    def logout(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/btn_logout"),
            remark=f"{self.remark()} > 登出"
        )
