import time

import pytest
import allure
from PIL.ImageChops import screen

from module.mobile.navigator import Navigator
from utils import com_func

@pytest.mark.personal
@allure.epic("個人頁面")
class TestPersonal:
    # @pytest.mark.HD001
    @allure.title("HD001")
    def test_personal_HD001(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        assert navigator.personal_page.personal_title().text == "Personal"

    # @pytest.mark.HD001_2
    @allure.title("HD001_2")
    def test_personal_HD001_2(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.personal_title().is_visible()
        navigator.personal_page.image_box().click()
        navigator.personal_page.dialog().is_visible()
        assert navigator.personal_page.take_photo_en().is_visible() is True
        assert navigator.personal_page.select_photo_en().is_visible() is True
        assert navigator.personal_page.reset_photo_en().is_visible() is True

    # @pytest.mark.HD002
    @allure.title("HD002")
    def test_personal_HD002(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.personal_title().is_visible()
        navigator.personal_page.setting().click()
        assert navigator.personal_page.personal_title().text == "Setting"

    # @pytest.mark.HD003
    @allure.title("HD003")
    def test_opersonal_HD003(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.personal_title().is_visible()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        navigator.personal_page.traditional_en().click()
        for _ in range(2):
            navigator.personal_page.back().click()

        company_content = navigator.personal_page.company_content().text
        assert company_content == '國泰世華銀行'
        division_content = navigator.personal_page.division_content().text
        assert division_content == '人力資源部'
        department_content = navigator.personal_page.department_content().text
        assert department_content == '勞資關係科'
        job_title_content = navigator.personal_page.job_title_content().text
        assert job_title_content == '資深副理'
        number_content = navigator.personal_page.number_content().text
        assert number_content == '00584360'

    # @pytest.mark.HD004
    @allure.title("HD004")
    def test_personal_HD004(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.personal_title().is_visible()
        navigator.personal_page.logout_btn().click()
        assert navigator.personal_page.logout_msg().is_visible() is True
        # 取消登出
        navigator.personal_page.logout_cancel().click()
        # 正常登出
        navigator.personal_page.logout_btn().click()
        assert navigator.personal_page.logout_msg().is_visible() is True
        navigator.personal_page.logout_confirm().click()

    # @pytest.mark.HD005
    @allure.title("HD005")
    def test_personal_HD005(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.personal_title().is_visible()
        navigator.personal_page.setting().click()
        navigator.personal_page.language().click()
        assert navigator.personal_page.traditional_en().text == "Traditional Chinese"
        navigator.personal_page.traditional_en().click()
        time.sleep(1)
        assert navigator.personal_page.traditional_zh().text == "繁體中文"

    # @pytest.mark.HD006
    @allure.title("HD006")
    def test_personal_HD006(self):
        navigator = Navigator().android.zh
        com_func.login_process_android('00584360')
        navigator.overview_page.overview_title().is_visible()
        navigator.overview_page.person_btn().click()
        navigator.personal_page.setting().click()
        navigator.personal_page.screenshot_title().is_visible()
        # screenshot_btn()關閉時,'checked'attribute之value為false
        get_screenshot_btn_checked = navigator.personal_page.screenshot_btn().attribute('checked')
        assert get_screenshot_btn_checked == 'false'

        # screenshot_btn()開啟時,'checked'attribute之value為true
        navigator.personal_page.screenshot_btn().click()
        get_screenshot_btn_checked = navigator.personal_page.screenshot_btn().attribute('checked')
        assert get_screenshot_btn_checked == 'true'

