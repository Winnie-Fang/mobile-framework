from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.sliding_object import SlidingObject


class PersonalPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("個人頁")
        self.driver = DeviceManager.get_driver()

    def prerequisites(self) -> None:
        self.personal_title().assert_visible()

    def personal_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/toolbar_title"),
            remark=f"{self.remark()} > 頁面標題"
        )

    def setting(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/setting"),
            remark=f"{self.remark()} > 設定"
        )

    def image_box(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/person_setting_img"),
            remark=f"{self.remark()} > 圖像框"
        )

    def dialog(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "com.cathaybk.ihave.uat:id/select_dialog_listview")),
            ),
            remark=f"{self.remark()} > 圖像選擇對話框"
        )

    def take_photo(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="android:id/text1" and @text="拍攝照片"]'),
            remark=f"{self.remark()} > 拍攝照片"
        )

    def select_photo(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="android:id/text1" and @text="選擇照片"]'),
            remark=f"{self.remark()} > 選擇照片"
        )

    def reset_photo(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="android:id/text1" and @text="還原預設圖片"]'),
            remark=f"{self.remark()} > 還原預設圖片"
        )

    def take_photo_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="android:id/text1" and @text="Photograph"]'),
            remark=f"{self.remark()} > 拍攝照片"
        )

    def select_photo_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="android:id/text1" and @text="Choose a Photo"]'),
            remark=f"{self.remark()} > 選擇照片"
        )

    def reset_photo_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="android:id/text1" and @text="Reset Photo"]'),
            remark=f"{self.remark()} > 還原預設圖片"
        )

    def company_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/company_content"),
            remark=f"{self.remark()} > 公司別"
        )

    def division_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/division_content"),
            remark=f"{self.remark()} > 部門"
        )

    def department_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/department_content"),
            remark=f"{self.remark()} > 科別"
        )

    def job_title_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/job_title_content"),
            remark=f"{self.remark()} > 職稱"
        )

    def number_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/number_content"),
            remark=f"{self.remark()} > 集團員編"
        )

    def logout_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/btn_logout"),
            remark=f"{self.remark()} > 登出"
        )

    def logout_msg(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "android:id/message"),
            remark=f"{self.remark()} > 登出訊息"
        )

    def logout_confirm(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "android:id/button1"),
            remark=f"{self.remark()} > 確認登出"
        )

    def logout_cancel(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "android:id/button2"),
            remark=f"{self.remark()} > 取消登出"
        )

    def language(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.ID, "com.cathaybk.ihave.uat:id/language_title"))),
            remark=f"{self.remark()} > 語言"
        )

    def screenshot_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/screen_title"),
            remark=f"{self.remark()} > 截圖錄影"
        )

    def screenshot_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, "com.cathaybk.ihave.uat:id/screen_content"),
            remark=f"{self.remark()} > 截圖錄影按鈕"
        )

    def traditional_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.RadioButton[@resource-id="com.cathaybk.ihave.uat:id/radio" and @text="Traditional Chinese"]'),
            remark=f"{self.remark()} > 中文切換(英)"
        )
    def traditional_zh(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.RadioButton[@resource-id="com.cathaybk.ihave.uat:id/radio" and @text="繁體中文"]'))),
            remark=f"{self.remark()} > 中文切換"
        )

    def english_zh(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.RadioButton[@resource-id="com.cathaybk.ihave.uat:id/radio" and @text="英文"]'),
            remark=f"{self.remark()} > 英文切換"
        )

    def back(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID,"com.cathaybk.ihave.uat:id/img_back"),
            remark=f"{self.remark()} > 回上一頁btn"
        )