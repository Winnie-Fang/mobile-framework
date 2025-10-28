import time

import pytest
import allure
from module.mobile.navigator import Navigator
from utils import com_func
from module.pre_condition.pre_condition_ios_zh import PreConditionIosZh

@pytest.mark.personal
@allure.epic("個人頁面")
class TestPersonal(PreConditionIosZh):
    @allure.title("個人功能切換")
    def test_personal_HD001(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        # assert navigator.ios_personal_page.personal_title().text == "個人"

    @allure.title("圖像變換功能")
    def test_personal_HD001_2(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        navigator.ios_personal_page.personal_title().is_visible()
        navigator.ios_personal_page.image_box().click()
        assert navigator.ios_personal_page.take_photo().is_visible() is True
        assert navigator.ios_personal_page.select_photo().is_visible() is True
        assert navigator.ios_personal_page.reset_photo().is_visible() is True

    @allure.title("設定功能測試")
    def test_personal_HD002(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        navigator.ios_personal_page.personal_title().is_visible()
        navigator.ios_personal_page.setting().click()
        assert navigator.ios_personal_page.general_setting().text == "一般設定"

    @allure.title("資訊欄顯示驗證")
    def test_opersonal_HD003(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        navigator.ios_personal_page.personal_title().is_visible()
        assert navigator.ios_personal_page.company_content().text == '國泰世華銀行'
        assert navigator.ios_personal_page.division_content().text == '人力資源部'
        assert navigator.ios_personal_page.department_content().text == '策略諮詢顧問科'
        assert navigator.ios_personal_page.job_title_content().text == '中級專員'
        assert navigator.ios_personal_page.number_content().text == '00589112'

    @allure.title("登出測試")
    def test_personal_HD004(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        navigator.ios_personal_page.personal_title().is_visible()
        navigator.ios_personal_page.logout_btn().click()
        assert navigator.ios_personal_page.logout_msg().is_visible() is True
        # 取消登出
        navigator.ios_personal_page.logout_cancel().click()
        # 正常登出
        navigator.ios_personal_page.logout_btn().click()
        assert navigator.ios_personal_page.logout_msg().is_visible() is True
        navigator.ios_personal_page.logout_confirm().click()

    @allure.title("語言切換")
    def test_personal_HD005(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        navigator.ios_personal_page.general_setting().is_visible()
        navigator.ios_personal_page.setting().click()
        navigator.ios_personal_page.language().click()
        assert navigator.ios_personal_page.traditional_zh().text == "繁體中文"
        navigator.ios_personal_page.english().click()
        assert navigator.ios_personal_page.traditional_en().text == "Traditional Chinese"
        time.sleep(1)

    @allure.title("截圖錄影功能")
    def test_personal_HD006(self):
        navigator = Navigator().ios.zh
        com_func.login_process_ios()
        navigator.ios_overview_page.overview_title().is_visible()
        navigator.ios_overview_page.person_btn().click()
        navigator.ios_personal_page.personal_title().is_visible()
        navigator.ios_personal_page.setting().click()
        assert navigator.ios_personal_page.screenshot_title().text == "截圖錄影"
        assert navigator.ios_personal_page.screenshot_btn().value == "0"
        navigator.ios_personal_page.screenshot_btn().click()
        assert navigator.ios_personal_page.screenshot_btn().value == "1"
