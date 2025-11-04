from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent


class GMBOverviewPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("總覽頁")
        self.driver = DeviceManager.get_driver()

    def overview_title(self):
        return BasicComponent(
            lambda : WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("總覽").instance(0)'))
            ),
            remark=f"{self.remark()} > 總覽頁標題"
        )

    def to_do_list(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ID,'com.cathaybk.geb.cubuat:id/toDoListTextView'),
            remark=f"{self.remark()} > 處理清單"
        )

    def to_do_trade(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("待覆核交易")'),
            remark=f"{self.remark()} > 待覆核交易"
        )
    def recent_reserve(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("近 1 年預約")'),
            remark=f"{self.remark()} > 近一年預約"
        )
    def under_review(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("送審中交易")'),
            remark=f"{self.remark()} > 送審中交易"
        )
    def account_overview(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ID,'com.cathaybk.geb.cubuat:id/accountOverviewTextView'),
            remark=f"{self.remark()} > 帳戶摘要"
        )
    # ================================================= 總覽下方功能列 =================================================
    def menu_bar(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ID,'com.cathaybk.geb.cubuat:id/bottom_nav'),
            remark=f"{self.remark()} > 總覽下方功能列"
        )
    def overview(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'總覽'),
            remark=f"{self.remark()} > 總覽功能"
        )
    def detail(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'明細'),
            remark=f"{self.remark()} > 明細功能"
        )

    def payment(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'交易'),
            remark=f"{self.remark()} > 交易功能"
        )
    def more(self):
        return BasicComponent(
            lambda : self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'更多'),
            remark=f"{self.remark()} > 更多功能"
        )


