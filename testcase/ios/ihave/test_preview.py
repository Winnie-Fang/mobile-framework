import pytest
import allure
from module.mobile.navigator import Navigator
from utils import com_func
from module.pre_condition.pre_condition_ios_zh import PreConditionIosZh

@pytest.mark.stiuat
@allure.epic("問卷預覽")
class TestSituation(PreConditionIosZh):
    @allure.title("問卷預覽顯示")
    def test_JA001(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_preview().click()
        assert navigator.preview_page.preview_title().text == "問卷預覽"

    @allure.title("問卷預覽資訊顯示")
    def test_JA002(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_preview().click()
        assert navigator.preview_page.preview_title().text == "問卷預覽"
        assert "新增問卷測試" in navigator.preview_page.test_questions().text
        assert navigator.preview_page.preview_list_info().text != ""
        navigator.preview_page.test_questions().click()

    @allure.title("發佈資訊")
    def test_JA003(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_preview().click()
        assert navigator.preview_page.preview_title().text == "問卷預覽"
        navigator.preview_page.test_questions().click()
        # 問卷發佈資訊
        assert navigator.preview_page.unit_content().text != ""
        assert navigator.preview_page.time_content().text != ""
        # 聯絡人
        navigator.preview_page.contact_person().click()
        assert navigator.preview_page.contact_info().text != ""
        assert navigator.preview_page.contact_name().text != ""
        assert navigator.preview_page.contact_tele().text != ""

    @allure.title("題目選項＆備註")
    def test_JA004_JA005(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_preview().click()
        assert navigator.preview_page.preview_title().text == "問卷預覽"
        navigator.preview_page.test_questions().click()
        # 選項
        navigator.preview_page.option1().click()
        navigator.preview_page.option2().click()
        # 備註
        assert navigator.preview_page.question_remark().text == "新增問卷測試-備註"

    @allure.title("下方按鈕_經辦")
    def test_JA006(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_preview().click()
        assert navigator.preview_page.preview_title().text == "問卷預覽"
        navigator.preview_page.test_questions().click()
        # 選項
        navigator.preview_page.option1().click()
        navigator.preview_page.send_out().assert_not_clickable()

    @allure.title("下方按鈕_經辦主管")
    def test_JA006(self):
        navigator = Navigator().ios.zh
        navigator.ihave_login_page.driver.switch_to.alert.accept()
        navigator.ihave_login_page.account_input.send_keys("00519943")
        navigator.ihave_login_page.password_input().send_keys("00000000")
        navigator.ihave_login_page.login_btn().click()
        navigator.ios_overview_page.question_btn().click()
        navigator.question_page.question_preview().click()
        assert navigator.preview_page.preview_title().text == "問卷預覽"
        navigator.preview_page.test_questions().click()
        # 選項
        navigator.preview_page.option1().click()
        navigator.preview_page.review_btn().click()
        # RWD 頁面
        assert navigator.preview_page.review_title().text == "問卷審核"
