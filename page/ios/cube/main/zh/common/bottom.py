from appium.webdriver.common.appiumby import AppiumBy

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.device_manager import DeviceManager


class Bottom(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("底部導航")
        self.driver = DeviceManager.get_driver()

    @property
    def finance(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "帳務總覽"`]'
            ),
            remark=f'{self.remark()} > 帳務總覽'
        )

    @property
    def invest(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "投資"`]'
            ),
            remark=f'{self.remark()} > 投資'
        )

    @property
    def loan(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "貸款"`]'
            ),
            remark=f'{self.remark()} > 貸款'
        )

    @property
    def insurance(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "保險"`]'
            ),
            remark=f'{self.remark()} > 保險'
        )

    @property
    def more(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "更多"`]'
            ),
            remark=f'{self.remark()} > 更多'
        )
