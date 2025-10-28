from appium.webdriver.common.appiumby import AppiumBy

from framework.cleaning import remove_logs
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.basic_components import BasicComponents


class PreviewPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("問卷預覽")
        self.driver = DeviceManager.get_driver()

    def preview_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "問卷預覽"`]'))),
            remark=f"{self.remark()} > 問卷預覽標題"
        )

    def preview_list(self):
        return BasicComponents(
            lambda: self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeCollectionView/XCUIElementTypeCell"),
            remark=f"{self.remark()} > 問卷預覽清單"
        )

    def preview_list_info(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             "//XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeStaticText[2]"),
            remark=f"{self.remark()} > 問卷清單發布資訊"
        )

    def test_questions(self):
        return BasicComponent(
                lambda: self.driver.find_element(AppiumBy.XPATH,
                                                 '(//XCUIElementTypeStaticText[@name="新增問卷測試"])[1]'),
            remark=f"{self.remark()} > 測試問卷"
        )

    def unit(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "單位"),
            remark=f"{self.remark()} > 單位"
        )

    def time(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "時間"),
            remark=f"{self.remark()} > 時間"
        )

    def unit_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             "//XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeStaticText[2]"),
            remark=f"{self.remark()} > 單位內容"
        )

    def time_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             "//XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[2]"),
            remark=f"{self.remark()} > 時間內容"
        )

    def contact_person(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "聯絡人"),
            remark=f"{self.remark()} > 聯絡人"
        )

    def contact_info(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeStaticText'),
            remark=f"{self.remark()} > 聯絡人 > 聯絡人科別"
        )

    def contact_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"○")]'),
            remark=f"{self.remark()} > 聯絡人 > 聯絡人姓名"
        )

    def contact_tele(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeButton'),
            remark=f"{self.remark()} > 聯絡人 > 聯絡人電話"
        )

    def option1(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             "//XCUIElementTypeCollectionView/XCUIElementTypeCell[7]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]"),
            remark=f"{self.remark()} > 安全選項"
        )

    def option2(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             "//XCUIElementTypeCollectionView/XCUIElementTypeCell[8]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]"),
            remark=f"{self.remark()} > 不安全選項"
        )

    def question_remark(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '新增問卷測試-備註'),
            remark=f"{self.remark()} > 問卷備註"
        )

    def send_out(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "送出"`]'),
            remark=f"{self.remark()} > 送出"
        )

    def review_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "審核"`]'),
            remark=f"{self.remark()} > 審核"
        )
    def review_title(self):
        return BasicComponent(
            lambda :WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeStaticText[`name == "問卷審核"`][2]'))),
            remark=f"{self.remark()} > 問卷審核"
        )

