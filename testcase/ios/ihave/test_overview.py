import pytest
import allure
from module.mobile.navigator import Navigator
from module.pre_condition.pre_condition_zh import PreConditionZh
from module.pre_condition.pre_condition_ios_zh import PreConditionIosZh

from utils import com_func


@allure.epic("總覽頁面")
class TestOverview(PreConditionZh):
    system = "android"
    @allure.title("總覽功能切換")
    def test_overview_HC001(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        navigator.ios_overview_page.overview_btn().click()

    @allure.title("應用選單功能")
    def test_overview_HC002(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_clickable()
        navigator.ios_overview_page.question_btn().click()
        assert navigator.question_page.reference().text == "參考資料"


