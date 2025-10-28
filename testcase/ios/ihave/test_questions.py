from module.mobile.navigator import Navigator
from utils import com_func
import allure
from datetime import datetime
from module.pre_condition.pre_condition_ios_zh import PreConditionIosZh


@allure.epic("Questions 問卷回覆")
class TestQuestions(PreConditionIosZh):
    @allure.title("介面顯示測試＿員工")
    def test_IA001(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        assert navigator.question_page.question_reply().text == "問卷回覆"
        assert navigator.question_page.reference().text == "參考資料"

    @allure.title("介面顯示測試＿科主管")
    def test_IA002(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00561099")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        assert navigator.question_page.question_reply().text == "問卷回覆"
        assert navigator.question_page.reference().text == "參考資料"
        assert navigator.question_page.reply_status_inquiry().text == "回覆狀況查詢"

    @allure.title("介面顯示測試＿業管經辦/主管")
    def test_IA003(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        assert navigator.question_page.question_reply().text == "問卷回覆"
        assert navigator.question_page.reference().text == "參考資料"
        assert navigator.question_page.reply_status_inquiry().text == "回覆狀況查詢"
        assert navigator.question_page.question_manage().text == "問卷管理"
        assert navigator.question_page.notification().text == "推播管理"
        assert navigator.question_page.question_preview().text == "問卷預覽"

    @allure.title("問卷回覆清單")
    def test_IA004(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_reply().click()
        navigator.question_page.replied().assert_visible()
        assert navigator.question_page.replied().text == "已回覆"
        assert navigator.question_page.no_reply().text == "未回覆"

    @allure.title("問卷回覆清單_未回覆")
    def test_IA005(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_reply().click()
        navigator.question_page.replied().assert_visible()
        department = navigator.question_page.list_info().text.split()[0]
        date = navigator.question_page.list_info().text.split()[1]
        assert department == "人力資源部"
        assert "2025" in date
        navigator.question_page.no_reply_list().click()

    @allure.title("問卷回覆清單_已回覆")
    def test_IA006(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_reply().click()
        navigator.question_page.replied().assert_visible()
        navigator.question_page.reply_list().click()
        navigator.question_page.question_reply().click()

    @allure.title("未回覆問卷_發佈資訊")
    def test_IA007(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_reply().click()
        navigator.question_page.replied().assert_visible()
        navigator.question_page.no_reply_list().click()
        # 未回覆問卷
        navigator.question_page.department_unit().assert_visible()
        navigator.question_page.time().assert_visible()
        navigator.question_page.contact_person().click()
        navigator.question_page.telephone().assert_visible()

    @allure.title("未回覆問卷_內容驗證")
    def test_IA008_IA009(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_reply().click()
        navigator.question_page.replied().assert_visible()
        navigator.question_page.no_reply_list().click()
        # 未回覆問卷_選項
        navigator.question_page.option1().click()
        navigator.question_page.option2().click()
        # 未回覆問卷_備註
        assert navigator.question_page.question_remark().text == "新增問卷測試-備註"

    @allure.title("未回覆問卷_填寫送出")
    def test_IA0010(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_reply().click()
        navigator.question_page.replied().assert_visible()
        navigator.question_page.no_reply_list().click()
        # 未回覆問卷內容
        navigator.question_page.send_out().click()
        assert navigator.question_page.send_fail().text == "送出失敗"
        navigator.question_page.driver.switch_to.alert.accept()
        navigator.question_page.option1().click()
        navigator.question_page.send_out().click()
        navigator.question_page.driver.switch_to.alert.accept()
        assert navigator.question_page.send_succeed().text == "送出成功"
        navigator.question_page.driver.switch_to.alert.accept()
