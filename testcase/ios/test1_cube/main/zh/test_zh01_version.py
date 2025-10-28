# import allure
# import pytest
#
# from framework import common
# from framework.allure_mark import Feature, Story
# from module.mobile.cube_util import CubeUtil
# from module.mobile.custom_decorator import user_id
# from module.mobile.navigator import Navigator
# from module.mobile.tag import ZHID
# from module.pre_condition.pre_condition_ios_zh import PreConditionIosZh
#
# TS = 1
# A = lambda : ZHID(TS, 1)
#
# @pytest.mark.cube
# @pytest.mark.main
# @pytest.mark.zh
# @pytest.mark.ios
# @pytest.mark.reg
# class TestVersion(PreConditionIosZh):
#     case_map = {
#         'test_version_info_apin': 'apin_xm34624817',
#         'test_version_info_cpin': 'cpin_qw21521653'
#     }
#
#     def setup_method(self, method):
#         self.navigator = Navigator().ios.zh
#         self.navigator.cube.prelogin_process()
#         test_name = method.__name__
#         self.user = CubeUtil.ios_json_cube_user(self.case_map.get(test_name))
#         self.version = CubeUtil.get_env()['version']
#
#     @allure.feature(Feature.CUBE_IOS_MAIN)
#     @allure.story(Story.P1)
#     @user_id(case_map)
#     @pytest.mark.P1
#     @pytest.mark.aws
#     @pytest.mark.tqa
#     @pytest.mark.screenshot
#     @pytest.mark.skip_pre_login
#     @pytest.mark.xdist_group('iphone1')
#     def test_version_info_apin(self):
#         """
#         確認版本版號正確_apin
#         """
#         self.navigator.pre_login_page.login_button.assert_visible()
#         self.navigator.login_page.userid_input.send_keys(self.user['id'])
#         self.navigator.login_page.username_input.send_keys(common.generate_username())
#         self.navigator.login_page.userpsw_input.send_keys(self.user["psw"])
#         self.navigator.keyboard.done.click()
#         self.navigator.login_page.login_button.click()
#         # self.navigator.cube.skip_login_to_home_popups()
#         self.navigator.bottom.invest.click()
#         self.navigator.invest_main_page.ready(3,3).save_screenshot()
#         self.navigator.bottom.loan.click()
#         self.navigator.bottom.insurance.click()
#         self.navigator.insurance_main_page.save_screenshot("保險總覽頁")
#         self.navigator.bottom.more.click()
#
