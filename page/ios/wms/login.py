# from huskypo import By,Element
from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.basic_select import BasicWebSelect
from module.mobile.component.sliding_object import SlidingObject
from module.mobile.device_manager import DeviceManager
#
# Appium_TextField_ClassName = "XCUIElementTypeTextField"
# Appium_Label_ClassName = "XCUIElementTypeStaticText"
# Appium_Button_ClassName = "XCUIElementTypeButton"


class WMSLoginPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("智能財富顧問登入頁")
        self.driver = DeviceManager.get_driver()

    # 先決條件,可自定義頁面準備內容
    # def prerequisites(self) -> None:
    #     self.login_btn.assert_visible()
    #     self.account_filed.assert_visible()
    #     self.password_filed.assert_visible()

    @property
    def initial_txt(self):
        # SlidingObject.scroll_up()
        # self.scroll_to_bottom()
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "開始使用您的智能財富顧問"),
            f"{self.remark()} > 歡迎字樣",
        )

    @property
    def account_filed(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="帳號"]'),
            f"{self.remark()}輸入帳號"
        )


    @property
    def password_filed(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@value="密碼"]'),
            f"輸入密碼"
        )

    @property
    def login_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "登入"), f"登入按鈕"
        )

    @property
    def acc_warning(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="此為必填欄位"])[1]'),
            f"帳號必填提示"
        )

    @property
    def pwd_warning(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="此為必填欄位"])[2]'),
            f"密碼必填提示"
        )
    def  input_number(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,"請輸入五碼行編"),f'請輸入五碼行編'
        )


