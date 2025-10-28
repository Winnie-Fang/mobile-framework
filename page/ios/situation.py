from appium.webdriver.common.appiumby import AppiumBy

from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent


class IOSSituationPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("回覆狀況查詢")
        self.driver = DeviceManager.get_driver()

    def in_progressing(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '進行中'),
            remark=f"{self.remark()} > 進行中"
        )

    def finished(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '已完成'),
            remark=f"{self.remark()} > 已完成"
        )

    def progressing_list(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="新增問卷測試"])[1]'),
            remark=f"{self.remark()} > 進行中問卷"
        )

    def finished_list(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="新增問卷測試"])[1]'),
            remark=f"{self.remark()} > 已完成問卷"
        )

    def unit_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 單位內容"
        )

    def time_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 時間內容"
        )

    def contact_person(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '聯絡人'),
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

    def part_time_unit_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '兼任單位'),
            remark=f"{self.remark()} > 兼任單位"
        )

    def subordinate_units_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '轄下單位'),
            remark=f"{self.remark()} > 轄下單位"
        )

    # =================================================== 轄下單位總覽 ==================================================
    def subordinate_overview(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '轄下單位總覽'),
            remark=f"{self.remark()} > 轄下單位總覽"
        )

    def response_rate(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[6]/XCUIElementTypeStaticText[1]'),
            remark=f"{self.remark()} > 回覆率"
        )

    '(//XCUIElementTypeStaticText[@name="回覆率"])[1]'

    def should_reply(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '應回覆'),
            remark=f"{self.remark()} > 應回覆"
        )

    def replied(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '已回覆'),
            remark=f"{self.remark()} > 已回覆"
        )

    def no_reply(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '未回覆'),
            remark=f"{self.remark()} > 未回覆"
        )

    def response_rate_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[6]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 回覆率內容"
        )

    def should_reply_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[7]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 應回覆內容"
        )

    def replied_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[8]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 已回覆內容"
        )

    def no_reply_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[9]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 未回覆內容"
        )

    # ==================================================================================================================
    def department_keyword(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '請輸入部門關鍵字'),
            remark=f"{self.remark()} > 請輸入部門關鍵字"
        )

    def keyword_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeTextField[`value == "請輸入部門關鍵字"`]'),
            remark=f"{self.remark()} > 請輸入部門關鍵字"
        )

    def option_hr(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '人力資源部'),
            remark=f"{self.remark()} > 部門關鍵字查詢 > 人力資源部"
        )

    # =================================================== 兼任單位總覽 ==================================================
    def select_down(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.down'),
            remark=f"{self.remark()} > 科別下拉式選單"
        )

    def option_strategy(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '策略諮詢顧問科'),
            remark=f"{self.remark()} > 科別下拉式選單"
        )

    def response_rate_2(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[8]/XCUIElementTypeStaticText[1]'),
            remark=f"{self.remark()} > 回覆率"
        )

    def part_response_rate_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[8]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 回覆率"
        )

    def part_should_reply_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[9]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 應回覆內容"
        )

    def part_replied_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[10]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 已回覆內容"
        )

    def part_no_reply_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[11]/XCUIElementTypeStaticText[2]'),
            remark=f"{self.remark()} > 未回覆內容"
        )

    # =================================================== 進行中問卷資訊 ==================================================
    def progressing_reply_rate(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "回覆率"`][2]'),
            remark=f"{self.remark()} > 進行中問卷回覆率"
        )

    def depart_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "部門"`][1]'),
            remark=f"{self.remark()} > 部門名稱"
        )

    def manager_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "主管姓名"`][1]'),
            remark=f"{self.remark()} > 主管姓名"
        )

    def telephone_info(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "電話"`][1]'),
            remark=f"{self.remark()} > 電話"
        )

    # =================================================== 轄下單位總覽 ==================================================
    def team_reply_rate(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "回覆率"`][1]'),
            remark=f"{self.remark()} > 進行中問卷回覆率"
        )

    def team_depart_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '部門'),
            remark=f"{self.remark()} > 部門名稱"
        )

    def team_manager_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '主管姓名'),
            remark=f"{self.remark()} > 主管姓名"
        )

    def team_telephone_info(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '電話'),
            remark=f"{self.remark()} > 電話"
        )
