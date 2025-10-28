from appium.webdriver.common.appiumby import AppiumBy
from module.mobile.device_manager import DeviceManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.sliding_object import SlidingObject


class QuestionPageSliding(SlidingObject):
    def __init__(self):
        super().__init__()
        self.set_remark("問卷頁")
        self.driver = DeviceManager.get_driver()
    #
    # def prerequisites(self) -> None:
    #     self.overview_title().assert_visible()
    def survey_management(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title" and @text="問卷管理"]'),
            remark=f"{self.remark()} > 問卷管理"
        )
    def notification_management(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title" and @text="推播管理"]'),
            remark=f"{self.remark()} > 推播管理"
        )
    def preview_survey(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title" and @text="問卷預覽"]'),
            remark=f"{self.remark()} > 問卷預覽"
        )
    def survey_responses(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title" and @text="問卷回覆"]'),
            remark=f"{self.remark()} > 問卷回覆"
        )
    def search_response_results(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title" and @text="回覆狀況查詢"]'),
            remark=f"{self.remark()} > 回覆狀況查詢"
        )
    def reference(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title" and @text="參考資料"]'),
            remark=f"{self.remark()} > 參考資料"
        )

    def unresponded_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="未回覆"]'),
            remark=f"{self.remark()} > 未回覆"
        )

    def responded_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="已回覆"]'),
            remark=f"{self.remark()} > 已回覆"
        )

    def unresponded_list1(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cathaybk.ihave.uat:id/no_reply_list"]/android.view.ViewGroup[1]'),
            remark=f"{self.remark()} > 未回覆問卷_第一欄"
        )

    def unresponded_content(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cathaybk.ihave.uat:id/no_reply_list"]/android.view.ViewGroup[1]/android.view.ViewGroup[@resource-id="com.cathaybk.ihave.uat:id/info"]/android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/content"]'),
            remark=f"{self.remark()} > 未回覆問卷_部門發布日期"
        )

    def unresponded_name(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cathaybk.ihave.uat:id/no_reply_list"]/android.view.ViewGroup[1]/android.view.ViewGroup[@resource-id="com.cathaybk.ihave.uat:id/info"]/android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title"]'),
            remark=f"{self.remark()} > 未回覆問卷_名稱"
        )

    def unresponded_layout(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/noReplyLayout'),
            remark=f"{self.remark()} > 未回覆問卷區塊"
        )

    def responded_list1(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cathaybk.ihave.uat:id/reply_list"]/android.view.ViewGroup[1]'),
            remark=f"{self.remark()} > 未回覆問卷_第一欄"
        )

    def responded_content(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cathaybk.ihave.uat:id/reply_list"]/android.view.ViewGroup[1]/android.view.ViewGroup[@resource-id="com.cathaybk.ihave.uat:id/info"]/android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/content"]'),
            remark=f"{self.remark()} > 已回覆問卷_部門發布日期"
        )

    def responded_name(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cathaybk.ihave.uat:id/reply_list"]/android.view.ViewGroup[1]/android.view.ViewGroup[@resource-id="com.cathaybk.ihave.uat:id/info"]/android.widget.TextView[@resource-id="com.cathaybk.ihave.uat:id/title"]'),
            remark=f"{self.remark()} > 已回覆問卷_名稱"
        )

    def responded_layout(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'com.cathaybk.ihave.uat:id/replyLayout'),
            remark=f"{self.remark()} > 已回覆問卷區塊"
        )

    def answer_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/toolbar_title'),
            remark=f"{self.remark()} > 回覆_標題"
        )

    def answer_contact(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/contact_title'),
            remark=f"{self.remark()} > 回覆_標題"
        )

    def answer_radio_btn1(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="com.cathaybk.ihave.uat:id/radio"])[1]'),
            remark=f"{self.remark()} > 回覆_radio_btn_1"
        )

    def answer_radio_btn2(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="com.cathaybk.ihave.uat:id/radio"])[2]'),
            remark=f"{self.remark()} > 回覆_radio_btn_2"
        )

    def answer_comment(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="com.cathaybk.ihave.uat:id/radio"])[2]'),
            remark=f"{self.remark()} > 回覆_備註"
        )

    def answer_remind(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.ihave.uat:id/remind'),
            remark=f"{self.remark()} > 回覆_備註"
        )

    def answer_submit(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.ihave.uat:id/btn_submit'),
            remark=f"{self.remark()} > 回覆_送出"
        )
    def confirm_window_confirm_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'android:id/button1'),
            remark=f"{self.remark()} > 確認視窗_確認btn"
        )
    def confirm_window_cancel_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'android:id/button2'),
            remark=f"{self.remark()} > 確認視窗_取消btn"
        )

    def confirm_window_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'android:id/message'),
            remark=f"{self.remark()} > 確認視窗_內容"
        )

    def fail_window_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.ihave.uat:id/title_template'),
            remark=f"{self.remark()} > 失敗視窗_標題"
        )

    def fail_window_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'android:id/message'),
            remark=f"{self.remark()} > 失敗視窗_內容"
        )

    def fail_window_close_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'android:id/button1'),
            remark=f"{self.remark()} > 失敗視窗_關閉btn"
        )

    def contact_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/toolbar_title'),
            remark=f"{self.remark()} > 聯絡人_標題"
        )
    def contact_name(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/name_content'),
            remark=f"{self.remark()} > 聯絡人_姓名"
        )
    def contact_phone(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/phone_content'),
            remark=f"{self.remark()} > 聯絡人_電話"
        )
    '''回覆狀況查詢頁_start'''
    def search_response_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/toolbar_title'),
            remark=f"{self.remark()} > 回覆狀況查詢_title"
        )
    def search_response_process_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="進行中"]'),
            remark=f"{self.remark()} > 回覆狀況查詢_進行中title"
        )
    def search_response_process_list(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/no_reply_list'),
            remark=f"{self.remark()} > 回覆狀況查詢_進行中list"
        )
    def search_response_finish_title(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="已完成"]'),
            remark=f"{self.remark()} > 回覆狀況查詢_已完成title"
        )
    def search_response_finish_list(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/reply_list'),
            remark=f"{self.remark()} > 回覆狀況查詢_已完成list"
        )

    def survey_information_subordinateunits(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.HorizontalScrollView[@resource-id="com.cathaybk.ihave.uat:id/tabLayout"]/android.widget.LinearLayout/android.widget.LinearLayout[1]'),
            remark=f"{self.remark()} > 回覆狀況查詢_轄下單位"
        )
    def survey_information_cosupervisedunits(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.XPATH,'//android.widget.HorizontalScrollView[@resource-id="com.cathaybk.ihave.uat:id/tabLayout"]/android.widget.LinearLayout/android.widget.LinearLayout[2]'),
            remark=f"{self.remark()} > 回覆狀況查詢_兼任單位"
        )
    def survey_information_unit(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/division'),
            remark=f"{self.remark()} > 回覆狀況查詢_部門"
        )
    def survey_information_date(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/date'),
            remark=f"{self.remark()} > 回覆狀況查詢_發布日期"
        )
    def survey_information_contact(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/contact_title'),
            remark=f"{self.remark()} > 回覆狀況查詢_聯絡人"
        )
    def cosupervisedunits_select_text(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/select_text'),
            remark=f"{self.remark()} > 兼任單位_選單文字"
        )
    def cosupervisedunits_info_unit(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/select_text'),
            remark=f"{self.remark()} > 兼任單位_單位文字"
        )
    def cosupervisedunits_info_response_rate(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/response_rate'),
            remark=f"{self.remark()} > 兼任單位_回覆率"
        )
    def cosupervisedunits_info_response_total(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/response_total'),
            remark=f"{self.remark()} > 兼任單位_應回覆"
        )
    def cosupervisedunits_info_received(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/received'),
            remark=f"{self.remark()} > 兼任單位_已回覆"
        )
    def cosupervisedunits_info_not_received(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/not_received'),
            remark=f"{self.remark()} > 兼任單位_未回覆"
        )
    def cosupervisedunits_info_phone(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/phone_content'),
            remark=f"{self.remark()} > 兼任單位_手機"
        )
    def cosupervisedunits_info_emergency_contact(self):
        return BasicComponent(
            lambda :self.driver.find_element(AppiumBy.ID,'com.cathaybk.ihave.uat:id/emergency_block'),
            remark=f"{self.remark()} > 兼任單位_緊急聯絡人"
        )
    '''回覆狀況查詢頁_end'''
    def back(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID,"com.cathaybk.ihave.uat:id/img_back"),
            remark=f"{self.remark()} > 回上一頁btn"
        )
