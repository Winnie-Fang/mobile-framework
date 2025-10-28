from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.sliding_object import SlidingObject


class IOSPersonalPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("個人頁")
        self.driver = DeviceManager.get_driver()

    def prerequisites(self) -> None:
        self.personal_title().assert_visible()

    def personal_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "設定"`]'),
            remark=f"{self.remark()} > 頁面標題"
        )

    def setting(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "nav gearshape fill"),
            remark=f"{self.remark()} > 設定"
        )

    def general_setting(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "一般設定"),
            remark=f"{self.remark()} > 一般設定"
        )

    def image_box(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mugshot"),
            remark=f"{self.remark()} > 圖像框"
        )

    def take_photo(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "拍攝照片"),
            remark=f"{self.remark()} > 拍攝照片"
        )

    def select_photo(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "選擇照片"),
            remark=f"{self.remark()} > 選擇照片"
        )

    def reset_photo(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "還原預設圖片"),
            remark=f"{self.remark()} > 還原預設圖片"
        )

    def take_photo_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Photograph"),
            remark=f"{self.remark()} > 拍攝照片"
        )

    def select_photo_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Choose a Photo"),
            remark=f"{self.remark()} > 選擇照片"
        )

    def reset_photo_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Reset Photo"),
            remark=f"{self.remark()} > 還原預設圖片"
        )

    def company_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "國泰世華銀行"),
            remark=f"{self.remark()} > 公司別內容"
        )

    def division_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "人力資源部"),
            remark=f"{self.remark()} > 部門內容"
        )

    def department_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "策略諮詢顧問科"),
            remark=f"{self.remark()} > 科別內容"
        )

    def job_title_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "中級專員"),
            remark=f"{self.remark()} > 職稱內容"
        )

    def number_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "00589112"),
            remark=f"{self.remark()} > 集團員編內容"
        )

    def logout_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "登出"`]'),
            remark=f"{self.remark()} > 登出"
        )

    def logout_msg(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeAlert[`name == "確認登出應用程式？"`]'),
            remark=f"{self.remark()} > 登出訊息"
        )

    def logout_confirm(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "確認"),
            remark=f"{self.remark()} > 確認登出"
        )

    def logout_cancel(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "取消"),
            remark=f"{self.remark()} > 取消登出"
        )

    def language(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "語言"))),
            remark=f"{self.remark()} > 語言"
        )

    def screenshot_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "截圖錄影"))),
            remark=f"{self.remark()} > 截圖錄影"
        )

    def screenshot_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value]'),
            remark=f"{self.remark()} > 截圖錄影按鈕"
        )

    def traditional_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Traditional Chinese'),
            remark=f"{self.remark()} > 中文切換(英)"
        )

    def traditional_zh(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '繁體中文'))),
            remark=f"{self.remark()} > 中文切換"
        )

    def english(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'English'),
            remark=f"{self.remark()} > 英文切換"
        )
