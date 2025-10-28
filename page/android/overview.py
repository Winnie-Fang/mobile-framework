from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.sliding_object import SlidingObject


class OverviewPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("總覽頁")
        self.driver = DeviceManager.get_driver()
    #
    # def prerequisites(self) -> None:
    #     self.overview_title().assert_visible()

    def overview_title(self):
        return BasicComponent(
            lambda : WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((AppiumBy.ID,"com.cathaybk.ihave.uat:id/toolbar_title"))
            ),
            remark=f"{self.remark()} > 總覽頁標題"
        )

    def menu(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,"com.cathaybk.ihave.uat:id/title"),
            remark= f"{self.remark()} > 菜單標題"
        )

    def overview_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/navigation_overview"),
            remark=f"{self.remark()} > 總覽頁面"
        )

    def person_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/navigation_settings"),
            remark=f"{self.remark()} > 個人頁面"
        )
    def question_btn(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ID,"com.cathaybk.ihave.uat:id/card_image"),
            remark= f"{self.remark()} > Questions"
        )