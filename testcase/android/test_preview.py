import pytest
import allure
# from selenium.webdriver.common.devtools.v133.page import navigate_to_history_entry

from module.mobile.navigator import Navigator
from utils import com_func
from datetime import datetime

# @pytest.mark.preview
@allure.epic("問卷預覽頁面")
class TestQuestion:
    # @pytest.mark.JA001
    @allure.title("JA001")
    def test_question_JA001(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00583904')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.preview_survey().click()
        preview_title = navigator.question_page.preview_title().text
        assert preview_title == '問卷預覽'

        navigator.question_page.preview_reviewlist().is_visible()

    # @pytest.mark.JA002
    @allure.title("JA002")
    def test_question_JA002(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00583904')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.preview_survey().click()
        preview_title = navigator.question_page.preview_title().text
        assert preview_title == '問卷預覽'

        unverify_content = navigator.question_page.unverify_content().text
        # 將”人力資源部 2025/04/29 14:35:48“分割一次為“人力資源部”和“2025/04/29 14:35:48”
        department, date_str = unverify_content.split(' ', 1)
        assert department == "人力資源部"
        assert datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")
        navigator.question_page.preview_list1().click()

    # @pytest.mark.JA003
    @allure.title("JA003")
    def test_question_JA003(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00583904')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.preview_survey().click()
        preview_title = navigator.question_page.preview_title().text
        assert preview_title == '問卷預覽'

        navigator.question_page.preview_list1().click()
        preview_unit = navigator.question_page.preview_unit().text
        assert preview_unit == '人力資源部'
        preview_date = navigator.question_page.preview_date().text
        assert datetime.strptime(preview_date, "%Y/%m/%d %H:%M:%S")
        navigator.question_page.preview_contact_title().click()

        preview_contact_name = navigator.question_page.preview_contact_name().text
        assert preview_contact_name == '林○鴻'
        navigator.question_page.preview_contact_phone().click()

    # @pytest.mark.JA004
    @allure.title("JA004")
    def test_question_JA004(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00583904')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.preview_survey().click()
        preview_title = navigator.question_page.preview_title().text
        assert preview_title == '問卷預覽'

        navigator.question_page.preview_list1().click()
        navigator.question_page.preview_answer_layout().is_visible()

    # @pytest.mark.JA005
    @allure.title("JA005")
    def test_question_JA005(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00583904')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.preview_survey().click()
        preview_title = navigator.question_page.preview_title().text
        assert preview_title == '問卷預覽'

        navigator.question_page.preview_list1().click()
        preview_remind = navigator.question_page.preview_remind().text
        assert preview_remind == '新增問卷測試-備註'

    # @pytest.mark.JA006
    @allure.title("JA006")
    def test_question_JA006(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00583904')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.preview_survey().click()
        preview_title = navigator.question_page.preview_title().text
        assert preview_title == '問卷預覽'

        navigator.question_page.preview_list1().click()
        navigator.question_page.preview_verify_btn().click()
        preview_verify_rwd = navigator.question_page.preview_verify_rwd().text
        assert preview_verify_rwd == '審核'
