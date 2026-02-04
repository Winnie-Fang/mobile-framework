from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.device_manager import DeviceManager


class TestElementsPage(BaseObject):
    def __init__(self, role=None):
        super().__init__()
        self.set_remark("測試元素頁")
        self.role = role
        self.driver = DeviceManager.get_driver(role=self.role)

    def enable_otp_btn(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/btn'))),
            remark=f"{self.remark()} > 啟用企業行動密碼按鈕"
        )

    def locale_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/localeTextView'),
            remark=f"{self.remark()} > 繁中"
        )

    def slogan_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/sloganTextView'),
            remark=f"{self.remark()} > Global MyB2B"
        )

    def gmb_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/gmbTextView'),
            remark=f"{self.remark()} > 企業網路銀行"
        )

    def not_enabled_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/imageView'),
            remark=f"{self.remark()} > 尚未啟用"
        )

    def login_gmb_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '登入企網銀'),
            remark=f"{self.remark()} > 登入企網銀"
        )

    def verify_trade_btn(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, '驗證網銀交易'))),
            remark=f"{self.remark()} > 驗證網銀交易"
        )

    def scroll_down_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/scrollDownAnim'),
            remark=f"{self.remark()} > 向下的按鈕"
        )

    def agree_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/rightButton'),
            remark=f"{self.remark()} > 已閱讀並同意"
        )

    def company_id_field(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="企業戶 ID / 統編"]/following-sibling::android.widget.EditText[1]'),
            remark=f"{self.remark()} > 企業戶id /統編"
        )

    def phone_number_field(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="手機號碼"]/following-sibling::android.widget.EditText[1]'),
            remark=f"{self.remark()} > 手機號碼"
        )

    def company_alias_field(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="公司別名"]/following-sibling::android.widget.EditText[1]'),
            remark=f"{self.remark()} > 公司別名"
        )

    def next_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button'),
            remark=f"{self.remark()} > 下一步"
        )
