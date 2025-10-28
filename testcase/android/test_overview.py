import pytest
import allure
from module.mobile.navigator import Navigator
from utils import com_func

@pytest.mark.overview
@allure.epic("總覽頁面")
class TestOverview:
    # @pytest.mark.HC001
    @allure.title("HC001")
    def test_overview_HC001(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.overview_page.overview_btn().click()

    # @pytest.mark.HC002
    @allure.title("HC002")
    def test_overview_HC002(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_clickable()
        navigator.overview_page.question_btn().click()
        assert navigator.overview_page.overview_title().text == "Questions"



