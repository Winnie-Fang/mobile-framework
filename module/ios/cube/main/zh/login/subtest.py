# from huskypo import logstack, SA
#
# from module.ios.cube.zh_common import CubeCommon
# from page.ios.cube.main.zh.common.two_factor_auth import *
# from page.ios.cube.main.zh.home.home import HomePage
# from page.ios.cube.main.zh.home.home_popup import HomePopup
# from page.ios.cube.main.zh.common.bottom import Bottom
# from page.ios.cube.main.zh.more.more import MorePage
# from page.ios.cube.main.zh.login.login_settings import LoginSettingsPage
# from page.ios.cube.main.zh.login.login import GestureLoginPage
# from page.ios.cube.main.zh.common.navi import NaviCommonPage
#
#
# class SubtestLogin:
#
#     def __init__(self, iphone, case: str = 'testcase'):
#         self.iphone = iphone
#         self.case = case
#         self.cube = CubeCommon(iphone)
#         self.navi = NaviCommonPage(iphone)
#         self.tfa_verify_popup = TFAActivatePopup()
#         self.tfa_verify_page = TFAActivatePage()
#         self.tfa_activate_page = TFAOTPVerifyPage()
#         self.home_page = HomePage()
#         self.home_popup = HomePopup()
#         self.bottom = Bottom(iphone)
#         self.more_page = MorePage()
#         self.geature_login_page = GestureLoginPage()
#         self.login_settings_page = LoginSettingsPage()
#
#     # def test_login_tfa_flow(self, otp: str = '555666'):
#     #     """
#     #     1701流程確認
#     #     """
#     #     flow = '登入兩步驟驗證'
#     #     if self.tfa_verify_popup.title_.is_present(3):
#     #         logstack.info('🟡 需要登入兩步驟驗證')
#     #         # 登入兩步驟驗證彈窗
#     #         waits = self.tfa_verify_popup.title_.wait_present()
#     #         self.cube.save_screenshot(flow, "登入兩步驟驗證彈窗")
#     #         self.tfa_verify_popup.confirm.click()
#     #         self.cube.wait_app_loading()
#     #         # 啟用兩步驟驗證頁 輸入otp
#     #         self.cube.verify_otp(otp)
#     #         self.cube.wait_app_loading()
#     #         self.cube.wait_launching()
#     #         # 進入首頁後會有信任此裝置
#     #         if self.home_popup.trust_device_title.is_present(1):
#     #             self.cube.save_screenshot(flow, "信任裝置彈窗")
#     #             self.home_popup.trust_device_accept.click()
#     #         # 啟用兩步驟驗證頁 設定裝置名稱
#     #         if self.tfa_activate_page.device_image.is_present(1):
#     #             self.cube.save_screenshot(flow, "設定裝置名稱")
#     #             self.tfa_activate_page.activate_confirm_button.click(1)
#     #         # 啟用兩步驟驗證頁 啟用成功
#     #         if self.tfa_activate_page.activate_success.is_visible():
#     #             self.cube.save_screenshot(flow, "啟用結果")
#     #             self.tfa_activate_page.activate_done_button.click()
#     #         # 確認首頁有顯示
#     #         self.home_page.wait_amounts.wait_any_visible()
#     #         self.cube.save_screenshot(flow, "回到首頁")
#     #     else:
#     #         logstack.info('✅ 無需登入兩步驟驗證')
#     #         self.cube.wait_launching()
#
#     def test_cancel_gesture(self):
#         """
#         取消手勢登入 避免影響下個testcase
#         """
#         # 進到首頁後點擊底部更多
#         self.bottom.more.click()
#         self.more_page.set_cell.ready()
#         self.more_page.set_gen.click()
#         self.more_page.set_gen_fast.click()
#         self.login_settings_page.delete_fast_login.click()
#         self.login_settings_page.save_screenshot(self.case, "取消手勢登入")
#         self.login_settings_page.delete_fast_popup_accept.click()
#         self.login_settings_page.is_ready()
#         self.login_settings_page.save_screenshot(self.case, "取消手勢登入後_確認圖像變回灰色")
#         self.navi.back_button.click()
#         logstack.info('✅ 確認已取消手勢登入')
