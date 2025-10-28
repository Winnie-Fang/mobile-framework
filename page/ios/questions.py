from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent


class IOSQuestionsPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("Questions")
        self.driver = DeviceManager.get_driver()

    def notification(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "推播管理"),
            remark=f"{self.remark()} > 推播管理"
        )

    def question_manage(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "問卷管理"),
            remark=f"{self.remark()} > 問卷管理"
        )

    def question_preview(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "問卷預覽"),
            remark=f"{self.remark()} > 問卷預覽"
        )

    def question_reply(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, '問卷回覆'))),
            remark=f"{self.remark()} > 問卷回覆"
        )

    def reply_status_inquiry(self):
        return BasicComponent(

            lambda: WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,"回覆狀況查詢"))),
            remark=f"{self.remark()} > 回覆狀況查詢"
        )

    def reference(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "參考資料"),
            remark=f"{self.remark()} > 參考資料"
        )

    def replied(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "已回覆"),
            remark=f"{self.remark()} > 已回覆"
        )

    def no_reply(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "未回覆"),
            remark=f"{self.remark()} > 未回覆"
        )

    def no_reply_list(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="新增問卷測試"])[1]'),
            remark=f"{self.remark()} > 未回覆清單"
        )

    def list_info(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[contains(@name, "人力資源部")]'),
            remark=f"{self.remark()} > 問卷資訊"
        )

    def reply_list(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[12]'),
            remark=f"{self.remark()} > 已回覆清單"
        )

    def department_unit(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '單位'),
            remark=f"{self.remark()} > ˇ單位"
        )

    def time(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '時間'),
            remark=f"{self.remark()} > 時間"
        )

    def contact_person(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "聯絡人"`]'),
            remark=f"{self.remark()} > 聯絡人"
        )

    def telephone(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '電話'),
            remark=f"{self.remark()} > 電話"
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

    def send_confirm(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '確認'),
            remark=f'{self.remark()} > 送出確認'
        )

    def send_fail(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "送出失敗"`]'),
            remark=f"{self.remark()} > 送出失敗"
        )

    def send_out(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "送出"`]'),
            remark=f"{self.remark()} > 送出"
        )

    def send_succeed(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`name == "送出成功"`]'),
            remark=f"{self.remark()} > 送出成功"
        )
