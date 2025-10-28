import pytest
import allure
from module.mobile.navigator import Navigator
from utils import com_func
from module.pre_condition.pre_condition_ios_zh import PreConditionIosZh



@allure.epic("回覆狀況查詢")
class TestSituation(PreConditionIosZh):
    @allure.title("進行中、已完成問卷顯示")
    def test_IB001_IB002(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.in_progressing().assert_visible()
        navigator.situation_page.finished().assert_visible()

    @allure.title("進行中＿問卷發佈")
    def test_IB003(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00547683")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.progressing_list().click()
        # 權限切換鈕
        navigator.situation_page.subordinate_units_btn().click()
        navigator.situation_page.part_time_unit_btn().click()
        # 問卷發佈資訊
        assert navigator.situation_page.unit_content().text != ""
        assert navigator.situation_page.time_content().text != ""
        # 聯絡人
        navigator.situation_page.contact_person().click()
        assert navigator.situation_page.contact_info().text != ""
        assert navigator.situation_page.contact_name().text != ""
        assert navigator.situation_page.contact_tele().text != ""

    @allure.title("進行中＿問卷發佈_科主管")
    def test_IB004(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00547683")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().assert_visible()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.progressing_list().click()
        # 切換權限(科主管)
        navigator.situation_page.part_time_unit_btn().click()
        # 問卷內容
        navigator.situation_page.response_rate_2().assert_visible()
        assert navigator.situation_page.response_rate_2().text == "回覆率"
        assert navigator.situation_page.should_reply().text == "應回覆"
        assert navigator.situation_page.replied().text == "已回覆"
        assert navigator.situation_page.no_reply().text == "未回覆"
        assert navigator.situation_page.part_response_rate_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_no_reply_content() != ""

    @allure.title("進行中＿問卷發佈_高階主管")
    def test_IB005(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00519943")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.progressing_list().click()
        # 問卷內容(轄下單位總覽)
        assert navigator.situation_page.response_rate().text == "回覆率"
        assert navigator.situation_page.should_reply().text == "應回覆"
        assert navigator.situation_page.replied().text == "已回覆"
        assert navigator.situation_page.no_reply().text == "未回覆"
        assert navigator.situation_page.response_rate_content().text != ""
        assert navigator.situation_page.should_reply_content().text != ""
        assert navigator.situation_page.replied_content().text != ""
        assert navigator.situation_page.no_reply_content().text != ""
        # 部門關鍵字
        assert navigator.situation_page.department_keyword().text == "請輸入部門關鍵字"
        # 進行中內容
        assert navigator.situation_page.progressing_reply_rate().text == "回覆率"
        assert navigator.situation_page.depart_name().text == "部門"
        assert navigator.situation_page.manager_name().text == "主管姓名"
        assert navigator.situation_page.telephone_info().text == "電話"

    @allure.title("進行中＿問卷發佈_雙權限")
    def test_IB006(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00547683")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.progressing_list().click()
        # 轄下單位
        # 部門關鍵字
        assert navigator.situation_page.department_keyword().text == "請輸入部門關鍵字"
        # 進行中內容
        assert navigator.situation_page.team_reply_rate().text == "回覆率"
        assert navigator.situation_page.team_depart_name().text == "部門"
        assert navigator.situation_page.team_manager_name().text == "主管姓名"
        assert navigator.situation_page.team_telephone_info().text == "電話"
        # 切換權限(兼任單位)
        navigator.situation_page.part_time_unit_btn().click()
        # 問卷內容
        navigator.situation_page.response_rate_2().assert_visible()
        assert navigator.situation_page.response_rate_2().text == "回覆率"
        assert navigator.situation_page.should_reply().text == "應回覆"
        assert navigator.situation_page.replied().text == "已回覆"
        assert navigator.situation_page.no_reply().text == "未回覆"
        assert navigator.situation_page.part_response_rate_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_no_reply_content() != ""

    @allure.title("已完成＿問卷發佈")
    def test_IB007(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00547683")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.finished_list().click()
        # 權限切換鈕
        navigator.situation_page.subordinate_units_btn().click()
        navigator.situation_page.part_time_unit_btn().click()
        # 問卷發佈資訊
        assert navigator.situation_page.unit_content().text != ""
        assert navigator.situation_page.time_content().text != ""
        # 聯絡人
        navigator.situation_page.contact_person().click()
        assert navigator.situation_page.contact_info().text != ""
        assert navigator.situation_page.contact_name().text != ""
        assert navigator.situation_page.contact_tele().text != ""

    @allure.title("已完成＿問卷發佈_科主管")
    def test_IB008(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00547683")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().assert_visible()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.finished_list().click()
        # 切換權限(科主管)
        navigator.situation_page.part_time_unit_btn().click()
        # 問卷內容
        navigator.situation_page.response_rate_2().assert_visible()
        assert navigator.situation_page.response_rate_2().text == "回覆率"
        assert navigator.situation_page.should_reply().text == "應回覆"
        assert navigator.situation_page.replied().text == "已回覆"
        assert navigator.situation_page.no_reply().text == "未回覆"
        assert navigator.situation_page.part_response_rate_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_no_reply_content() != ""

    @allure.title("已完成＿問卷發佈_高階主管")
    def test_IB009(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00519943")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.finished_list().click()
        # 問卷內容(轄下單位總覽)
        assert navigator.situation_page.response_rate().text == "回覆率"
        assert navigator.situation_page.should_reply().text == "應回覆"
        assert navigator.situation_page.replied().text == "已回覆"
        assert navigator.situation_page.no_reply().text == "未回覆"
        assert navigator.situation_page.response_rate_content().text != ""
        assert navigator.situation_page.should_reply_content().text != ""
        assert navigator.situation_page.replied_content().text != ""
        assert navigator.situation_page.no_reply_content().text != ""
        # 部門關鍵字
        assert navigator.situation_page.department_keyword().text == "請輸入部門關鍵字"
        # 進行中內容
        assert navigator.situation_page.progressing_reply_rate().text == "回覆率"
        assert navigator.situation_page.depart_name().text == "部門"
        assert navigator.situation_page.manager_name().text == "主管姓名"
        assert navigator.situation_page.telephone_info().text == "電話"

    @allure.title("已完成＿問卷發佈_雙權限")
    def test_IB010(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00547683")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.reply_status_inquiry().click()
        navigator.situation_page.finished_list().click()
        # 轄下單位
        # 部門關鍵字
        assert navigator.situation_page.department_keyword().text == "請輸入部門關鍵字"
        # 進行中內容
        assert navigator.situation_page.team_reply_rate().text == "回覆率"
        assert navigator.situation_page.team_depart_name().text == "部門"
        assert navigator.situation_page.team_manager_name().text == "主管姓名"
        assert navigator.situation_page.team_telephone_info().text == "電話"
        # 切換權限(兼任單位)
        navigator.situation_page.part_time_unit_btn().click()
        # 問卷內容
        navigator.situation_page.response_rate_2().assert_visible()
        assert navigator.situation_page.response_rate_2().text == "回覆率"
        assert navigator.situation_page.should_reply().text == "應回覆"
        assert navigator.situation_page.replied().text == "已回覆"
        assert navigator.situation_page.no_reply().text == "未回覆"
        assert navigator.situation_page.part_response_rate_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_replied_content() != ""
        assert navigator.situation_page.part_no_reply_content() != ""

