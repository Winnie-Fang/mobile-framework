# from huskypo import By,Element
from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.sliding_object import SlidingObject
from module.mobile.device_manager import DeviceManager
#
# Appium_TextField_ClassName = "XCUIElementTypeTextField"
# Appium_Label_ClassName = "XCUIElementTypeStaticText"
# Appium_Button_ClassName = "XCUIElementTypeButton"


class WMSHomePage(SlidingObject):
    def __init__(self):
        super().__init__()
        self.set_remark("智能財富顧問首頁")
        self.driver = DeviceManager.get_driver()

    # 先決條件,可自定義頁面準備內容
    def prerequisites(self) -> None:
        self.logout_btn.assert_visible()
        self.initial_logo.assert_visible()

    @property
    def initial_logo(self):
        self.scroll_to_bottom()
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.NAME, "tabViewLogo"),
            f"{self.remark()} > 智能財富顧問Logo"
        )

    @property
    def logout_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, '登出'),
            f"{self.remark()} > 登出"
        )


    @property
    def logout_check_window(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="登出確認"])[2]'),
            f"{self.remark()} > 登出確認"
        )

    @property
    def window_let_me_think(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="我再想想"])[2]'),
            f"{self.remark()} > 我再想想"
        )

    @property
    def window_logout(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="登出"])[3]'),
            f"{self.remark()} > 登出"
        )

    @property
    def favorite_web_label(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="常用網站"]'),
            f"{self.remark()} > 常用網站"
        )

    @property
    def  add_web_btn(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="新增網站"]'),
            f"{self.remark()} > 新增網站"
        )

    @property
    def web_name_filed(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeTextField[@value="網站名稱*"]'),
            f"{self.remark()} > 網站名稱"
        )

    @property
    def web_link_filed(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeTextField[@value="網址*"]'),
            f"{self.remark()} > 網址"
        )

