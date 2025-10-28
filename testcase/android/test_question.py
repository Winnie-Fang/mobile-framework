import pytest
import allure
# from selenium.webdriver.common.devtools.page import navigate_to_history_entry

from module.mobile.navigator import Navigator
from utils import com_func
from datetime import datetime


# @pytest.mark.question
@allure.epic("問卷頁面")
class TestQuestion:
    # @pytest.mark.IA001
    @allure.title("IA001")
    def test_question_IA001(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00597756')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        question_reply = navigator.question_page.survey_responses().text
        reference = navigator.question_page.reference().text
        assert question_reply == '問卷回覆'
        assert reference == '參考資料'

    # @pytest.mark.IA002
    @allure.title("IA002")
    def test_question_IA002(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00504309')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        question_reply = navigator.question_page.survey_responses().text
        search_response_results = navigator.question_page.search_response_results().text
        reference = navigator.question_page.reference().text
        assert question_reply == '問卷回覆'
        assert search_response_results == '回覆狀況查詢'
        assert reference == '參考資料'

    # @pytest.mark.IA003
    @allure.title("IA003")
    def test_question_IA003(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        survey_management = navigator.question_page.survey_management().text
        notification_management = navigator.question_page.notification_management().text
        preview_survey = navigator.question_page.preview_survey().text
        question_reply = navigator.question_page.survey_responses().text
        search_response_results = navigator.question_page.search_response_results().text
        reference = navigator.question_page.reference().text
        assert survey_management == '問卷管理'
        assert notification_management == '推播管理'
        assert preview_survey == '問卷預覽'
        assert question_reply == '問卷回覆'
        assert search_response_results == '回覆狀況查詢'
        assert reference == '參考資料'

    # @pytest.mark.IA004
    @allure.title("IA004")
    def test_question_IA004(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00597756')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.survey_responses().click()

        navigator.question_page.unresponded_layout().is_visible()
        navigator.question_page.responded_layout().is_visible()
        unresponded_title = navigator.question_page.unresponded_title().text
        responded_title = navigator.question_page.responded_title().text

        assert unresponded_title == '未回覆'
        assert responded_title == '已回覆'

    # @pytest.mark.IA005
    @allure.title("IA005")
    def test_question_IA005(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00597756')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.survey_responses().click()

        unresponded_content = navigator.question_page.unresponded_content().text
        # 將”人力資源部 2025/04/29 14:35:48“分割一次為“人力資源部”和“2025/04/29 14:35:48”
        department, date_str = unresponded_content.split(' ', 1)
        assert department == "人力資源部"
        assert datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")

        unresponded_name = navigator.question_page.unresponded_name().text
        navigator.question_page.unresponded_list1().click()
        answer_title = navigator.question_page.answer_title().text
        assert unresponded_name == answer_title

    # @pytest.mark.IA006
    @allure.title("IA006")
    def test_question_IA006(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00597756')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.survey_responses().click()

        responded_content = navigator.question_page.responded_content().text
        # 將”人力資源部 2025/04/29 14:35:48“分割一次為“人力資源部”和“2025/04/29 14:35:48”
        department, date_str = responded_content.split(' ', 1)
        assert department == "人力資源部"
        assert datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")

        responded_name = navigator.question_page.responded_name().text
        navigator.question_page.responded_list1().click()
        answer_title = navigator.question_page.answer_title().text
        assert responded_name == answer_title

        navigator.question_page.back().click()
        responded_name = navigator.question_page.responded_name().text
        assert responded_name == answer_title

    # @pytest.mark.IA007
    @allure.title("IA007")
    def test_question_IA007(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00597756')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.survey_responses().click()
        navigator.question_page.unresponded_list1().click()

        answer_contact = navigator.question_page.answer_contact().text
        navigator.question_page.answer_contact().click()
        contact_title = navigator.question_page.contact_title().text
        assert answer_contact == contact_title

        navigator.question_page.contact_phone().is_clickable()
        navigator.question_page.contact_phone().click()

    # @pytest.mark.IA009
    @allure.title("IA009")
    def test_question_IA009(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00597756')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.survey_responses().click()
        navigator.question_page.unresponded_list1().click()

        answer_remind = navigator.question_page.answer_remind().text
        assert answer_remind == '新增問卷測試-備註'

    # @pytest.mark.IA008ANDIA010
    @allure.title("IA008ANDIA010")
    def test_question_IA008ANDIA010(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00597756')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.survey_responses().click()
        navigator.question_page.unresponded_list1().click()

        navigator.question_page.answer_submit().click()
        confirm_window_content = navigator.question_page.confirm_window_content().text
        assert confirm_window_content == '請確認問卷填寫的內容，點選確認後即送出問卷，將無法再進行修改。'
        navigator.question_page.confirm_window_confirm_btn().click()

        navigator.question_page.fail_window_title().is_visible()
        fail_window_content = navigator.question_page.fail_window_content().text
        assert fail_window_content == '您尚有題目未填答完成，請再次確認。'
        navigator.question_page.fail_window_close_btn().click()

        navigator.question_page.answer_radio_btn2()
        navigator.question_page.answer_radio_btn1()
        navigator.question_page.answer_submit().click()

    # @pytest.mark.IB001
    @allure.title("IB001")
    def test_question_IB001(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00595053')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()

        search_response_title = navigator.question_page.search_response_title().text
        assert search_response_title == '回覆狀況查詢'

        response_process_title = navigator.question_page.search_response_process_title().text
        assert response_process_title == '進行中'
        navigator.question_page.search_response_process_list().is_visible()

    # @pytest.mark.IB002
    @allure.title("IB002")
    def test_question_IB002(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00595053')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()

        search_response_title = navigator.question_page.search_response_title().text
        assert search_response_title == '回覆狀況查詢'

        response_process_title = navigator.question_page.search_response_finish_title().text
        assert response_process_title == '已完成'
        navigator.question_page.search_response_finish_list().is_visible()

    # @pytest.mark.IB003
    @allure.title("IB003")
    def test_question_IB003(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.unresponded_list1().click()

        navigator.question_page.survey_information_cosupervisedunits().click()
        navigator.question_page.survey_information_subordinateunits().click()
        survey_information_unit = navigator.question_page.survey_information_unit().text
        assert survey_information_unit == '人力資源部'
        survey_information_date = navigator.question_page.survey_information_date().text
        assert datetime.strptime(survey_information_date, "%Y/%m/%d %H:%M:%S")
        navigator.question_page.survey_information_contact().click()

    # @pytest.mark.IB004
    @allure.title("IB004")
    def test_question_IB004(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.unresponded_list1().click()

        navigator.question_page.survey_information_cosupervisedunits().click()

        cosupervisedunits_select_text = navigator.question_page.cosupervisedunits_select_text().text
        info_unit = navigator.question_page.info_unit().text
        assert info_unit == cosupervisedunits_select_text

        for _ in range(5):
            navigator.question_page_sliding.scroll_down()

        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""

        navigator.question_page.info_Name().is_visible()
        navigator.question_page.info_phone().is_visible()
        navigator.question_page.info_emergency_contact().is_visible()
        navigator.question_page.info_phone().click()

    # @pytest.mark.IB005
    @allure.title("IB005")
    def test_question_IB005(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.unresponded_list1().click()

        for _ in range(5):
            navigator.question_page_sliding.scroll_down()

        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""

        navigator.question_page.info_Name().is_visible()
        navigator.question_page.info_phone().is_visible()
        navigator.question_page.info_emergency_contact().is_visible()
        navigator.question_page.info_phone().click()

    # @pytest.mark.IB006
    @allure.title("IB006")
    def test_question_IB006(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.unresponded_list1().click()

        info_unit = navigator.question_page.overview_info_title().text
        assert info_unit == '轄下單位總覽'
        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""

        navigator.question_page.survey_information_cosupervisedunits().click()
        cosupervisedunits_select_text = navigator.question_page.cosupervisedunits_select_text().text
        info_unit = navigator.question_page.overview_info_title().text
        assert info_unit == cosupervisedunits_select_text
        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""

    # @pytest.mark.IB007
    @allure.title("IB007")
    def test_question_IB007(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.responded_list1().click()

        navigator.question_page.survey_information_cosupervisedunits().click()
        navigator.question_page.survey_information_subordinateunits().click()
        survey_information_unit = navigator.question_page.survey_information_unit().text
        assert survey_information_unit == '人力資源部'
        survey_information_date = navigator.question_page.survey_information_date().text
        assert datetime.strptime(survey_information_date, "%Y/%m/%d %H:%M:%S")
        navigator.question_page.survey_information_contact().click()

    # @pytest.mark.IB008
    @allure.title("IB008")
    def test_question_IB008(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.responded_list1().click()

        navigator.question_page.survey_information_cosupervisedunits().click()

        cosupervisedunits_select_text = navigator.question_page.cosupervisedunits_select_text().text
        info_unit = navigator.question_page.info_unit().text
        assert info_unit == cosupervisedunits_select_text

        for _ in range(5):
            navigator.question_page_sliding.scroll_down()

        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""

    # @pytest.mark.IB009
    @allure.title("IB009")
    def test_question_IB009(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.responded_list1().click()

        for _ in range(5):
            navigator.question_page_sliding.scroll_down()

        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""

        navigator.question_page.info_Name().is_visible()
        navigator.question_page.info_phone().is_visible()
        navigator.question_page.info_emergency_contact().is_visible()

    # @pytest.mark.IB0010
    @allure.title("IB0010")
    def test_question_IB010(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00547683')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        navigator.overview_page.overview_btn().click()
        navigator.overview_page.question_btn().click()
        navigator.question_page.search_response_results().click()
        navigator.question_page.responded_list1().click()

        info_unit = navigator.question_page.overview_info_title().text
        assert info_unit == '轄下單位總覽'
        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""

        navigator.question_page.survey_information_cosupervisedunits().click()
        cosupervisedunits_select_text = navigator.question_page.cosupervisedunits_select_text().text
        info_unit = navigator.question_page.overview_info_title().text
        assert info_unit == cosupervisedunits_select_text
        info_response_rate = navigator.question_page.info_response_rate().text
        assert info_response_rate != ""
        info_response_total = navigator.question_page.info_response_total().text
        assert info_response_total != ""
        info_received = navigator.question_page.info_received().text
        assert info_received != ""
        info_not_received = navigator.question_page.info_not_received().text
        assert info_not_received != ""
