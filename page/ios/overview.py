from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.sliding_object import SlidingObject


class IOSOverviewPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("總覽頁")
        self.driver = DeviceManager.get_driver()

    # def prerequisites(self) -> None:
    #     self.overview_title().assert_visible()

    def overview_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "總覽"`]'))
            ),
            remark=f"{self.remark()} > 總覽頁標題"
        )

    def menu(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '應用選單'),
            remark=f"{self.remark()} > 應用選單標題"
        )

    def overview_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "tab_overview"),
            remark=f"{self.remark()} > 總覽頁面"
        )

    def person_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "tab_person"),
            remark=f"{self.remark()} > 個人頁面"
        )

    def question_btn(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"app_questions"))),
            remark=f"{self.remark()} > Questions"
        )

    def question_title(self):
        return BasicComponent(
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Questions"`]'))
            ),
            remark=f"{self.remark()} > Question 標題"
        )
