from os import remove

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.device_manager import DeviceManager


class iOSLoginPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("GMB 登入頁")
        self.driver = DeviceManager.get_driver()

    # def ready(self):
    #     self.prerequisites()
    #     return self

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
            lambda: WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Global MyB2B"))),
            remark=f"{self.remark()} > 登入標語"
        )

    def id_input(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((AppiumBy.XPATH,
                                                        '//XCUIElementTypeStaticText[@name="企業戶 ID / 統編"]/../following-sibling::XCUIElementTypeOther'))),
            remark=f"{self.remark()} > 企業戶ID/統編"
        )

    # def id_input(self):
    #     return BasicComponent(
    #         lambda: WebDriverWait(self.driver,30).until(
    #             EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="企業戶 ID / 統編"]/../following-sibling::XCUIElementTypeOther'))),
    #         remark=f"{self.remark()} > 企業戶ID/統編"
    #     )

    def user_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[@name="使用者代號"]/../following-sibling::XCUIElementTypeOther'),
            remark=f"{self.remark()} > 使用者代號"
        )

    def user_pwd(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[@name="使用者密碼"]/../following-sibling::XCUIElementTypeOther'),
            remark=f"{self.remark()} > 使用者密碼"
        )

    def login_btn(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (AppiumBy.IOS_PREDICATE, 'name == "登入" AND label == "登入" AND type == "XCUIElementTypeButton"'))),
            remark=f"{self.remark()} > 登入按鈕"
        )

    def dialog_common_message(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
                                                  "您上次沒有正常登出，或是已在其他裝置登入，要改為登入目前的裝置嗎？(錯誤代碼：AP07)"))),
            remark=f"{self.remark()} > 未正常登出-彈跳視窗內容"
        )

    def dialog_login_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[@name="您上次沒有正常登出，或是已在其他裝置登入，要改為登入目前的裝置嗎？(錯誤代碼：AP07)"]/../following-sibling::XCUIElementTypeOther/XCUIElementTypeButton[2]'),
            remark=f"{self.remark()} > 未正常登出-彈跳視窗登入按鈕"
        )

    def dialog_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeNavigationBar[`name == "信任裝置"`]'),
            remark=f"{self.remark()} > 信任裝置標題"
        )

    def truest_device_dialog(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((AppiumBy.IOS_CLASS_CHAIN,
                                                                                           '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]'))),
            remark=f"{self.remark()} > 信任裝置彈跳視窗"
        )

    def truest_device_dialog2(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("信任裝置")'),
            remark=f"{self.remark()} > 信任裝置標題-彈跳視窗"
        )

    def next_time_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`name == "下次再說"`]'),
            remark=f"{self.remark()} > 下次再說按鈕"
        )

    def remind_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '提醒'))),
            remark=f"{self.remark()} > 提醒標題"
        )

    def remind_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '此裝置尚未加入您的信任清單，可能導致部分功能無法使用。'),
            remark=f"{self.remark()} > 提醒視窗內容"
        )

    def check_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`name == "我知道了"`]'),
            remark=f"{self.remark()} > 我知道了"
        )
