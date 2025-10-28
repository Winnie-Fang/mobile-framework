from appium.webdriver.common.appiumby import AppiumBy

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.basic_components import BasicComponents
from module.mobile.device_manager import DeviceManager


class InsuranceDebitPage(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("貸款頁面")
        self.driver = DeviceManager.get_driver()

    @property
    def title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeStaticText[`label == "貸款"`]'
            ),
            remark=f'{self.remark()} > 標題'
        )

    @property
    def tab(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '保單借款'
            ),
            remark=f'{self.remark()} > 保單借款標籤'
        )

    @property
    def all_infos(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeScrollView/**/XCUIElementTypeStaticText'
            ),
            remark=f'{self.remark()} > 保單借款全部資訊'
        )

    @property
    def insurance_value_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'name == "查看保單價值" AND type == "XCUIElementTypeButton"'
            ),
            remark=f'{self.remark()} > 查看保單價值按鈕'
        )