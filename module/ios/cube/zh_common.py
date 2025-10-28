# import time
# import random
# import string
#
# from selenium.common.exceptions import TimeoutException
#
# from huskypo import logstack, Element, SA
# from huskypo_extension import Page
# from huskypo_extension import assertion
#
# from framework import common, path
# from module.mobile.common import MobileCommon
# from page.ios.cube.main.zh.login.login_popup import LoginPopup
# from page.ios.panel.keyboard import Keyboard
# from page.ios.alert.notification import CathayNotiAlert
# from page.ios.cube.main.zh.common.error import AppErrorPage, WebErrorPage
# from page.ios.cube.main.zh.common.activate import *
# from page.ios.cube.main.zh.common.border_object import BorderObject
# from page.ios.cube.main.zh.common.area import Area
# from page.ios.cube.main.zh.common.bottom import Bottom
# from page.ios.cube.main.zh.common.loading import Loading
# from page.ios.cube.main.zh.common.loading_v2 import Loading as Loading_v2
# from page.ios.cube.main.zh.common.two_factor_auth import *
# from page.ios.cube.main.zh.finance.deposit import TWDDepositPage
# from page.ios.cube.main.zh.home.home import HomePage
# from page.ios.cube.main.zh.home.home_popup import HomePopup
# from page.ios.cube.main.zh.login.login import LoginPage, PreLoginPage, GestureLoginPage
#
# from page.ios.cube.main.zh.more.more import MorePage
# from page.ios.cube.main.zh.twd.tx_txn import TWDTransferStartPage
# from page.ios.panel.keyboard import Keyboard
#
#
# class CubeCommon:
#     """
#     存放CUBE產品通用的功能
#     """
#
#     def __init__(self, iphone):
#         self.iphone = iphone
#         self.page = Page(iphone)
#         self.mobile = MobileCommon(iphone)
#         self.noti_alert = CathayNotiAlert(iphone)
#         self.border_object = BorderObject(iphone)
#         self.area = Area(iphone)
#         self.app_error = AppErrorPage(iphone)
#         self.web_error = WebErrorPage(iphone)
#         self.launch_page = LaunchPage()
#         self.queue_popup = QueuePopup()
#         self.queue_page = QueuePage()
#         self.inform_popup = InformPopup()
#         self.keyboard = Keyboard()
#         # self.loading = Loading(iphone)
#         self.loading_v2 = Loading_v2()
#         self.login_page = LoginPage()
#         self.gesture_login_page = GestureLoginPage()
#         self.pre_login_page = PreLoginPage()
#         self.login_popup = LoginPopup()
#         self.tfa_verify_popup = TFAActivatePopup()
#         self.tfa_verify_page = TFAActivatePage()
#         self.tfa_activate_page = TFAOTPVerifyPage()
#         self.home_page = HomePage()
#         self.home_popup = HomePopup()
#         self.bottom = Bottom()
#         self.more_page = MorePage()
#         self.twd_page = TWDDepositPage()
#         self.txn_page = TWDTransferStartPage()
#         self.system_alert = CathayNotiAlert(iphone)
#
#     def skip_aws_device_farm_ios_alert(self, timeout: int = 1):
#         """
#         執行 aws device farm 時，略過 ios 系統彈窗
#         """
#         logstack.info('✅ 執行 aws device farm 流程')
#         remark = self.system_alert.dismiss.remark
#         if self.system_alert.dismiss.is_present(timeout):
#             logstack.info(f'✅ 元素 {remark} 在 {timeout} 秒內存在')
#             self.system_alert.dismiss.click()
#             logstack.info(f'🟢 元素 {remark} click 成功，但不能確定是否生效，請確認後續流程')
#             return True
#         else:
#             logstack.warning(f'🟡 元素 {remark} 在 {timeout} 秒內不存在，請確認執行流程是否為aws')
#             return False
#
#     def switch_to_zh(self):
#         if self.pre_login_page.language.text == '語系選擇目前為英文':
#             logstack.info('🕹️ 目前是英文版，先切換成中文版')
#             self.pre_login_page.language.click()
#             self.pre_login_page.language_zh.click()
#             self.pre_login_page.language_save_button.click()
#
#         if not self.pre_login_page.language.text == '語系選擇目前為中文':
#             raise Exception('❌ 尚未切換成中文版，請確認是否有其他問題。')
#
#     def switch_to_en(self):
#         if self.pre_login_page.language.text == '語系選擇目前為中文':
#             logstack.info('🕹️ 目前是中文版，先切換成英文版')
#             self.pre_login_page.language.click()
#             self.pre_login_page.language_en.click()
#             self.pre_login_page.language_save_button.click()
#
#         if not self.pre_login_page.language.text == '語系選擇目前為英文':
#             raise Exception('❌ 尚未切換成英文版，請確認是否有其他問題。')
#
#     def prelogin_process(self):
#         """
#         1. 確認APP啟動Logo可見
#         2. 略過啟動彈窗
#         3. 以中文版登入
#         """
#         if not self.launch_page.logo.is_ready(0.1, 3):
#             logstack.info('❌ Launch logo may not present.')
#         self.launch_page.connect_logo.assume_invisible()
#         self.prelogin_gcp()
#         self.skip_inform_popups()
#         # self.pre_login_page.login_button.assert_visible()
#         self.switch_to_zh()
#
#     def prelogin_gcp(self):
#         """
#         處理排隊機制流程
#         """
#         if self.queue_page.common_text.is_ready(0.1, 3):
#             if '目前使用人數較多' in self.queue_page.common_text.text:
#                 logstack.warning(f'🟡 [彈窗] 出現排隊機制(GCP)')
#                 self.save_screenshot("GCP", "彈窗")
#             self.queue_popup.confirm.click() if self.queue_popup.confirm.is_ready() else None
#             logstack.warning(f'🟡 GCP: 出現頁面')
#             self.queue_page.update_time_text.is_visible()
#             self.save_screenshot("GCP", "頁面")
#             self.queue_page.skip_queue_button.tap()
#             logstack.info('🕹️ 點擊排隊圖像略過排隊')
#
#     def skip_inform_popups(self):
#         """
#         略過開啟CUBE APP後出現的彈窗
#         """
#         # for _ in range(2):
#         #     if self.inform_popup.system_upgrade_inform_popop.is_ready(
#         #             0.5, 1) or self.inform_popup.force_upgrade_inform_popop.is_ready(0.5, 1):
#         #         self.inform_popup.accept_button.click()
#         while any(popup.is_ready(0.5, 1) for popup in [
#             self.inform_popup.system_upgrade_inform_popop,
#             self.inform_popup.force_upgrade_inform_popop,
#             self.inform_popup.decline_test_popop
#         ]):
#             self.inform_popup.accept_button.click()
#
#
#     def swich_login_method_from_gesture(self):
#         """
#         當手勢登入出現時 切換為以帳號密碼登入
#         """
#         if self.gesture_login_page.account_login.is_ready(0.5, 1):
#             logstack.info('🟡 出現手勢登入')
#             self.gesture_login_page.account_login.click()
#
#     def login(
#             self,
#             user: dict,
#             select_remember: bool = True,
#             real_password: bool = False,
#             screenshot: bool = False,
#             tfa_workaround1: bool = False
#     ):
#         """
#         CUBE登入功能
#         """
#         logstack.info(f'🕹️ 開始登入流程  👤 使用者資訊: {user}')
#         self.swich_login_method_from_gesture()
#         self.__if_save_screenshot(screenshot, '個人化預登入頁面', '登入')
#         self.pre_login_page.login_button.click()
#         self.swich_login_method_from_gesture()
#         self.__if_save_screenshot(screenshot, '登入頁面', '登入')
#
#         self.confirm_remember_status(select_remember)
#         username = common.generate_username()
#         password = user['psw']
#         if real_password:
#             logstack.info('🕹️ 使用真實密碼 需檢查至登入兩步驟前為止\n')
#             username, password = user['username_real'], user['psw_real']
#         self.login_page.userid_input.send_keys(user['id'])
#         self.login_page.username_input.send_keys(username)
#         self.login_page.userpsw_input.send_keys(password)
#         self.keyboard.done.click()
#         self.__if_save_screenshot(screenshot, '登入頁面輸入帳密完畢', '登入')
#
#         self.login_page.login_button.click()
#         remember_popup = self.skip_login_to_home_popups(screenshot, tfa_workaround1)
#
#         logstack.info('🕹️ 結束登入流程\n')
#         return remember_popup
#
#     def logout(self, screenshot: bool = False):
#         """
#         CUBE登出功能(需在Bottom Bar存在時才可呼叫)
#         """
#         logstack.info('🕹️ 開始登出流程')
#         self.bottom.more.click()
#         self.__if_save_screenshot(screenshot, '到更多頁面準備登出', '登出')
#         self.more_page.logout_button.click()
#         self.__if_save_screenshot(screenshot, '登出彈窗', '登出')
#         self.more_page.logout_popup_logout_button.click()
#         self.__if_save_screenshot(screenshot, '回到登入頁', '登出')
#         self.pre_login_page.ready()
#         logstack.info('🕹️ 結束登出流程\n')
#
#     def wait_app_loading_icon(self):
#         """
#         等待app loading icon不存在
#         """
#         self.loading_v2.ready(0.5, 20)
#
#     def confirm_remember_status(self, select: bool | None = None):
#         """
#         變更記住我的勾選狀態
#         """
#         current_status = True if self.login_page.remember_radio.text == '記住我的身分證字號，已勾選' else False
#         current_status_text = '已勾選' if current_status else '未勾選'
#         logstack.info(f'🟢 目前記住我狀態為: {current_status_text}')
#
#         if select is None:
#             logstack.info('🕹️ 不執行任何動作')
#             return current_status
#
#         if select != current_status:
#             select_action = '勾選' if select else '取消勾選'
#             logstack.info(f'🕹️ 開始執行 {select_action}記住我')
#             self.login_page.remember_radio.click()
#             new_status = True if self.login_page.remember_radio.text == '記住我的身分證字號，已勾選' else False
#             assert select == new_status, f'❌ 未成功執行 {select_action}記住我'
#
#     def __check_home_page_status(self):
#         """
#         確認首頁是否完整載入
#         """
#         condition = (self.home_page.title_.is_visible() and self.home_page.cdc_title.is_visible()
#                      and self.home_page.fxr_currency_text.is_visible())
#         if not condition:
#             logstack.error('❌ 首頁可能顯示不完全')
#
#     def skip_login_to_home_popups(
#             self,
#             screenshot: bool = False,
#             tfa_workaround2: bool = False
#     ) -> bool:
#         """
#         略過從按下登入後到進入首頁(帳務總覽頁)會出現的所有彈窗
#         """
#         remember_popup = False
#         for _ in range(4):  # 最多5個彈窗
#             if self.login_popup.common_text.is_ready(0.5, 1):
#                 popup_text = self.login_popup.common_text.text
#                 self.__handle_abnormal_logout_popup(popup_text, screenshot)
#                 remember_popup = self.__handle_remember_device_popup(popup_text, screenshot)
#                 self.__handle_biometrics_popup(popup_text, screenshot)
#                 self.__handle_recommended_fido_dismiss(popup_text, screenshot)
#                 self.__handle_password_change_popup(popup_text, screenshot)
#                 if self.home_page.title_.is_visible():
#                     break
#         self.handle_two_factor_auth_popup(screenshot) if tfa_workaround2 is True else None
#         for _ in range(5):  # 最多6個彈窗
#             if self.login_popup.common_text.is_ready(0.5, 1):
#                 popup_text = self.login_popup.common_text.text
#                 self.__handle_abnormal_logout_popup(popup_text, screenshot)
#                 remember_popup = self.__handle_remember_device_popup(popup_text, screenshot)
#                 self.__handle_biometrics_popup(popup_text, screenshot)
#                 self.__handle_recommended_fido_dismiss(popup_text, screenshot)
#                 self.__handle_password_change_popup(popup_text, screenshot)
#                 if self.home_page.title_.is_visible():
#                     break
#         self.skip_home_popup(screenshot)
#         self.__check_home_page_status()
#         return remember_popup
#
#     def skip_home_popup(self, screenshot: bool = False):
#         """
#         略過進入首頁(帳務總覽頁)後出現的彈窗(此時首頁已顯示)
#         """
#         for _ in range(3):  # 最多3個彈窗
#             if self.home_popup.common_text.is_ready(0.5, 1):
#                 popup_text = self.home_popup.common_text.text
#                 self.__handle_trust_device_popup(popup_text, screenshot)
#                 self.__handle_security_upgrade_popup(popup_text, screenshot)
#                 self.__handle_password_upgrade_popup(popup_text, screenshot)
#
#     def __handle_abnormal_logout_popup(self, popup_text: str, screenshot: bool = False):
#         if '未正常登出' in popup_text:
#             logstack.warning('🟡 觸發 [彈窗] 未正常登出')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.login_popup.abnormal_accept.click()
#
#     def __handle_remember_device_popup(self, popup_text, screenshot: bool = False) -> bool:
#         if '裝置記住我' in popup_text:
#             logstack.warning('🟡 觸發 [彈窗] 裝置記住我')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.login_popup.remember_accept.click()
#             return True  # 此彈窗需被驗證是否出現
#         else:
#             return False
#
#     def __handle_biometrics_popup(self, popup_text, screenshot: bool = False):
#         if '生物辨識' in popup_text:
#             logstack.warning('🟡 觸發 [彈窗] 生物辨識')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.login_popup.fido_dismiss.click()
#
#     def __handle_password_change_popup(self, popup_text, screenshot: bool = False):
#         if '變更密碼' in popup_text:
#             logstack.warning('🟡 觸發 [彈窗] 變更密碼')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.login_popup.psw_dismiss.click()
#
#     def __handle_trust_device_popup(self, popup_text, screenshot: bool = False):
#         if '信任這台裝置？' in popup_text:
#             logstack.warning('🟡 觸發 [彈窗] 信任裝置')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.home_popup.trust_device_dismiss.click()
#
#     def __handle_security_upgrade_popup(self, popup_text, screenshot: bool = False):
#         if '登入安全再升級' in popup_text:
#             logstack.warning('🟡 觸發 [彈窗] 登入安全再升級')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.home_popup.login_security_dismiss.click()
#
#     def __handle_password_upgrade_popup(self, popup_text, screenshot: bool = False):
#         if '立即升級您的網銀密碼' in popup_text:
#             logstack.warning('🟡 觸發 [彈窗] 立即升級您的網銀密碼')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.home_popup.upgrade_psw_dismiss.click()
#
#     def __handle_recommended_fido_dismiss(self, popup_text, screenshot: bool = False):
#         if '推薦您使用 FIDO 快速登入' in popup_text:
#             logstack.info('🟡 觸發 [彈窗] 推薦使用FIDO 彈窗')
#             self.__if_save_screenshot(screenshot, popup_text)
#             self.login_popup.recommended_fido_dismiss.click()
#
#     # def handle_two_factor_auth_popup(self, screenshot: bool=False):
#     #     if (self.login_page.forget_psw.is_visible()
#     #         or self.pre_login_page.signup_button.is_visible()
#     #     ) and not self.home_page.title_.is_visible():
#     #         logstack.info('🟡 觸發 [彈窗] 可能出現兩步驟驗證')
#     #         self.__if_save_screenshot(screenshot, '可能出現兩步驟驗證')
#     #         time.sleep(1)
#     #         self.login_popup.two_factor_auth_button().tap()
#     #         time.sleep(2)
#     #         self.verify_otp('555666')
#     #         time.sleep(2)
#
#     def handle_two_factor_auth_popup(self, screenshot: bool = False):
#         time.sleep(3)  # 手動觸發 兩步驟驗證 等待3s確保穩定性
#         logstack.info('🟡 觸發 [彈窗] 兩步驟驗證')
#         self.__if_save_screenshot(screenshot, '兩步驟驗證_彈窗')
#         self.login_popup.two_factor_auth_button.tap()
#         self.wait_app_loading_icon()
#         self.verify_otp('555666')
#         self.wait_app_loading_icon()
#
#         # 啟用兩步驟驗證頁 設定裝置名稱
#         if self.tfa_activate_page.device_image.is_ready(0.5, 1):
#             self.__if_save_screenshot(screenshot, '設定裝置名稱')
#             self.tfa_activate_page.activate_confirm_button.click()
#             self.wait_app_loading_icon()
#
#         # 啟用兩步驟驗證頁 啟用成功
#         if self.tfa_activate_page.activate_success.is_ready(0.5, 1):
#             self.__if_save_screenshot(screenshot, '啟用結果')
#             self.tfa_activate_page.activate_done_button.click()
#             self.wait_app_loading_icon()
#
#     def __if_save_screenshot(self, screenshot: bool = False, screenshot_name: str = "", case_name: str = '略過登入彈窗'):
#         """
#         判斷是否需要截圖
#         """
#         if screenshot:
#             self.login_popup.save_screenshot(case_name, screenshot_name)
#
#     def test_skip_twd_demand_more_function_inform(self):
#         """
#         略過 臺幣活存 更多功能在這裡
#         # TODO 目前僅使用於zh00
#         """
#         self.home_page.deposit_twd_amount.click()
#         self.twd_page.demand_more_button.tap()
#         self.wait_app_loading()
#         self.twd_page.demand_more_close.click()
#         logstack.info('✅ 已先點擊 台幣分頁 活存更多按鈕 避免通知阻擋')
#
#     def verify_otp(self, otp: str = '555666', screenshot: bool = True):
#         """
#         共用輸入OTP流程
#         """
#         self.tfa_activate_page.otp_field.send_keys(otp)
#         self.keyboard.done.click()
#         self.__if_save_screenshot(screenshot, '輸入otp完成', '輸入otp')
#         self.tfa_activate_page.confirm_button.click()
#
#     def login_tfa_flow(self, otp: str = '555666'):
#         """
#         判斷是否有登入並啟用兩步驟驗證流程
#         # TODO 此流程待 登入兩步驟驗證彈窗 可被定位時才可使用
#         """
#         flow = '登入兩步驟驗證'
#
#         if self.tfa_verify_popup.title_.is_ready(0.5, 1):
#             # 登入兩步驟驗證彈窗
#             logstack.info('🟡 需要登入兩步驟驗證')
#             self.tfa_verify_popup.save_screenshot(flow, "登入兩步驟驗證彈窗")
#             self.tfa_verify_popup.confirm.click()
#             self.wait_app_loading_icon()
#
#             # 登入兩步驟驗證頁 立即啟用
#             if self.tfa_verify_page.image.is_ready(1, 4):
#                 self.tfa_verify_page.save_screenshot(flow, "登入兩步驟驗證頁")
#                 if self.tfa_verify_page.accept.is_visible():
#                     self.tfa_verify_page.accept.click()
#
#             self.wait_app_loading_icon()
#
#             # 啟用兩步驟驗證頁 輸入otp
#             self.verify_otp(otp)
#
#             self.wait_app_loading_icon()
#
#             # 啟用兩步驟驗證頁 設定裝置名稱
#             if self.tfa_activate_page.device_image.is_ready():
#                 self.tfa_activate_page.save_screenshot(flow, "設定裝置名稱")
#                 self.tfa_activate_page.activate_confirm_button.click()
#                 self.wait_app_loading_icon()
#
#             # 啟用兩步驟驗證頁 啟用成功
#             if self.tfa_activate_page.activate_success.is_ready():
#                 self.tfa_activate_page.save_screenshot(flow, "啟用結果")
#                 self.tfa_activate_page.activate_done_button.click()
#                 self.wait_app_loading_icon()
#
#         else:
#             logstack.info('✅ 無需登入兩步驟驗證')
#
#     def go_to_home_page(self, case: str, name: str = '登入到首頁', screenshot: bool = True):
#         """
#         此處將斷言首頁是否依條件顯示，並將此流程放到登入後的每個測案的第一步
#         """
#         self.home_page.ready()
#         logstack.info('🟢 首頁等待結束')
#         self.__if_save_screenshot(screenshot, name, case)
#
#     def save_screenshot(
#             self,
#             case: str = 'case',
#             name: str = 'name',
#             sleep: int = 0.5,
#             to_jpg: bool = True,
#             jpg_ratio: int = 50,
#             jpg_quality: int = 50,
#             attach: bool = True,
#             attach_jpg: bool = True,
#             remove: bool = True,
#             errors_timeout: int = 1,
#             skip_errors: bool = False,
#             is_web: bool = False
#     ):
#         """
#         save_screenshot 後斷言頁面是否有錯誤訊息
#         可先在前面斷言 assume.wait() 等待條件後再使用 save_screenshot
#         不需再用 wait_screenshot 放入 waits 的方式了
#         """
#         self.page.save_screenshot(
#             case,
#             name,
#             sleep,
#             to_jpg,
#             jpg_ratio,
#             jpg_quality,
#             attach,
#             attach_jpg,
#             remove)
#         self.assert_page_no_error_messages(name, errors_timeout, skip_errors, is_web)
#
#     def assert_page_no_error_messages(self, page: str, timeout: int = 3, skip: bool = False, is_web: bool = False):
#         """
#         斷言無任何錯誤訊息
#         """
#         elements = self.web_error.messages if is_web else self.app_error.messages
#         elements.timeout = timeout
#         try:
#             error_messages = elements.texts
#             if skip:
#                 logstack.warning(f'🟡 頁面 "{page}" 略過斷言錯誤訊息: {error_messages}')
#             elif '您的帳號已從其他地方登入，將自動登出網銀App' in error_messages:
#                 assert False, f'頁面 "{page}" 帳號已從其他地方登入'
#             else:
#                 assertion.condition(False, f'頁面 "{page}" 等待 {timeout} 秒內出現錯誤訊息: {error_messages}')
#         except TimeoutException:
#             logstack.info(f'頁面 "{page}" 等待 {timeout} 秒內 無任何錯誤訊息')
#
#     def tap_non_center_element(self, target: Element):
#         """
#         點擊不在中間的元素
#         """
#         x, y = target.location['x'], target.location['y']
#         w, h = target.size['width'], target.size['height']
#         right_top_corner = (x + 9 / 10 * w, y + 1 / 5 * h)
#         left_top_corner = (x + 1 / 10 * w, y + 1 / 5 * h)
#         left_bottom_corner = (x + 1 / 10 * w, y + 4 / 5 * h)
#         right_bottom_corner = (x + 9 / 10 * w, y + 4 / 5 * h)
#         center = (target.center['x'], target.center['y'])
#         taps = [center, right_top_corner, left_top_corner, left_bottom_corner, right_bottom_corner]
#         for tap in taps:
#             if target.is_visible():
#                 logstack.info(f'🕹️ 嘗試點擊第 {taps.index(tap) + 1} 次')
#                 self.page.tap([tap])
#                 time.sleep(0.2)
#         if target.is_visible():
#             logstack.error('❌ 無法點擊該元素')
#
#     def generate_random_string(self, length: int):
#         """
#         產生英數字組合的亂數
#         """
#         letters_and_digits = string.ascii_letters + string.digits
#         return ''.join(random.choice(letters_and_digits) for i in range(length))
#
#     def suspend_and_wakeup(self):
#         logstack.info('🕹️ 嘗試suspend then resume iphone')
#         self.iphone.lock()
#         time.sleep(3)
#         self.iphone.execute_script('mobile: pressButton', {'name': 'home'})
#         logstack.info(f"loc:{self.keyboard.slide_bar.location}")
#         self.keyboard.swipe_by(
#             (self.keyboard.slide_bar.location['x'],
#              self.keyboard.slide_bar.location['y'],
#              self.keyboard.slide_bar.location['x'],
#              100),
#             duration=1000)
#
#         self.keyboard.zero.wait_present(timeout=10)
#
#         self.keyboard.zero.click()
#         self.keyboard.zero.click()
#         self.keyboard.zero.click()
#         self.keyboard.zero.click()
#         self.keyboard.zero.click()
#         self.keyboard.zero.click()
#         logstack.info('Resume iphone successfully')
#
# # ----------------------------------------------------- Huskypo ----------
#
#     def skip_popup(
#             self,
#             reference_element: Element,
#             button_element: Element,
#             timeout: int = 3,
#             screenshot: bool = True):
#         """
#         略過特定彈窗
#         - reference_element: 欲等待的彈窗元素
#         - button_element: 欲執行的彈窗按鈕
#         """
#         reference_element_remark = reference_element.remark
#         button_element_remark = button_element.remark
#         result = False
#         logstack.info(f'reference element: {reference_element_remark}')
#         if reference_element.is_present(timeout):
#             logstack.info(f'button element: {button_element_remark}')
#             if screenshot:
#                 self.page.save_screenshot('不定彈窗', reference_element_remark)
#             button_element.click()
#             result = True
#         result_text = '✅ 有出現' if result else '❎ 未出現'
#         logstack.info(f'{result_text}彈窗\n')
#         return result
#
#     def get_border(self, others_timeout: int = 1):
#         """
#         注意：更多功能頁因為多了登出框，請用 get_table_border 就好，否則 table bottom 會是錯的。
#
#         判斷 Table 或 ScrollView 類別元素的邊界
#         先以 Table 為準，沒有時再用 ScrollView 判斷
#         """
#         try:
#             table_border = self.border_object.table.border
#             if self.border_object.tabbar.is_present(others_timeout):
#                 table_border['bottom'] = self.border_object.tabbar.border['top']
#             return table_border
#         except Exception:
#             return self.border_object.scrollview.border
#
#     def get_table_border(self, order: int = 1):
#         """
#         取得 XCUIElementTypeTable 類別元素的邊界，
#         order 即為索引值，利用 IOS_CLASS_CHAIN **/XCUIElementTypeTable[{order}] 定位
#         """
#         q_tables = self.border_object.tables.quantity
#         if q_tables == 0:
#             logstack.warning('🟡 無任何 Table，先以目前視窗為邊界。如不符合需求，請改用其他元素取得邊界')
#             border = self.page.get_window_border()
#         elif q_tables == 1:
#             logstack.info('✅ 只有一個 Table，取其作為邊界。')
#             border = self.border_object.table_order(1).border
#         else:
#             logstack.info(f'✅ 有多個 Table，指定第 {order} 個 Table 作為邊界。')
#             border = self.border_object.table_order(order).border
#         return border
#
#     def get_table_rect(self, order: int = 1):
#         """
#         取得 XCUIElementTypeTable 類別元素的 rect。
#         order 即為索引值，利用 (By.IOS_CLASS_CHAIN, "**/XCUIElementTypeTable[{order}]") 定位
#         """
#         q_tables = self.area.tables.quantity
#         if q_tables == 0:
#             logstack.warning('🟡 無任何 Table，先以目前視窗為邊界。如不符合需求，請改用其他元素取得邊界')
#             return self.page.get_window_rect()
#         elif q_tables == 1:
#             logstack.info('✅ 只有一個 Table，取其作為邊界。')
#             return self.border_object.table_order(1).rect
#         else:
#             logstack.info(f'✅ 有多個 Table，指定第 {order} 個 Table 作為邊界。')
#             return self.border_object.table_order(order).rect
#
#     def get_rect(self, tabbar_timeout: int = 1, hover_element: int | float = 0):
#         """
#         取得rect
#         - tabbar_timeout 等待下方狀態列的時間
#         - hover_element 如果底部有特定元素需避開(ex:轉帳懸浮按鈕) 可以將該元素y值輸入此處
#         """
#         try:
#             table_border = self.border_object.table.rect
#             if self.border_object.tabbar.is_present(tabbar_timeout) and hover_element == 0:
#                 table_border['height'] = table_border['height'] - self.border_object.tabbar.rect['height']
#             elif hover_element != 0:
#                 table_border['height'] = table_border['height'] - (table_border['height'] - hover_element)
#             return table_border
#         except Exception:
#             return self.border_object.scrollview.rect
#
#     def wait_loading_by(self, element: Element, etimeout: int = 1, netimeout: int = 30):
#         """
#         等待指定的 loading 元素消失
#         """
#         result = None
#         remark = element.remark
#         if element.is_present(etimeout):
#             logstack.info(f'🟢 {etimeout}秒內 出現 {remark}')
#             if element.wait_not_present(netimeout, False):
#                 logstack.info(f'✅ {netimeout}秒內 完成 {remark}\n')
#                 result = True
#             else:
#                 logstack.warning(f'🟡 {netimeout}秒內 未完成 {remark}\n')
#                 result = False
#         else:
#             logstack.info(f'✅ 無任何 {remark}\n')
#             result = True
#         return assertion.wait(result, remark)
#
#     def wait_launching(self, etimeout=1, netimeout=60):
#         """
#         等待 cube launching 頁面消失
#         """
#         return self.wait_loading_by(self.launch_page.logo, etimeout, netimeout)
#
#     def wait_app_loading(self, etimeout=1, netimeout=60):
#         """
#         等待 cube 原生的 loading icon 消失
#         ACCESSIBILITY_ID: 'SVProgressHUD'
#         """
#         return self.wait_loading_by(self.loading.app_loading, etimeout, netimeout)
#
#     def wait_app_progressing(self, etimeout=1, netimeout=60):
#         """
#         等待 accessibility id = "進行中" 的元素消失
#         ACCESSIBILITY_ID: '進行中'
#         """
#         return self.wait_loading_by(self.loading.app_progressing, etimeout, netimeout)
#
#     def wait_app_activity_indicator_loading(self, etimeout=1, netimeout=60):
#         """
#         等待 XCUIElementTypeActivityIndicator 類別的元素消失
#         IOS_CLASS_CHAIN: '**/XCUIElementTypeActivityIndicator[-1]'
#         """
#         return self.wait_loading_by(self.loading.app_activity_indicator, etimeout, netimeout)
#
#     def wait_app_progress_indicator_loading(self, etimeout=1, netimeout=60):
#         """
#         等待 XCUIElementTypeProgressIndicator 類別的元素消失
#         IOS_CLASS_CHAIN: '**/XCUIElementTypeProgressIndicator[-1]'
#         """
#         return self.wait_loading_by(self.loading.app_progress_indicator, etimeout, netimeout)
#
#     def wait_webview_redirecting(self, etimeout=3, netimeout=60):
#         """
#         等待 cube webview 內嵌頁面的 redirect 消失
#         ACCESSIBILITY_ID: 'SuperRedirect'
#         """
#         return self.wait_loading_by(self.loading.webview_redirecting, etimeout, netimeout)
#
#     def wait_webview_progressing(
#             self,
#             timeout: int = 60,
#             poll: int = 1,
#             tolerance: int = 99,
#     ):
#         """
#         確認webview進度條和當前視窗寬度一致
#         """
#         try:
#             # 設定等待與通過門檻
#             element = self.loading.webview_progressing
#             window_width = self.page.get_window_size()['width']
#             passing_width = int(window_width * tolerance / 100)
#
#             # 開始執行等待
#             end_time = time.monotonic() + timeout
#             while True:
#                 element_width = element.size['width']
#                 logstack.info(f'------------------------------------------------------------------')
#                 logstack.info(f'視窗狀態 寬度: {window_width}  通過閥値: {passing_width}  通過閥率: {tolerance}%')
#                 logstack.info(f'🕛 目前閥値: {element_width}  目前進度: {int(element_width / window_width * 100)}%')
#                 if element_width < passing_width:
#                     logstack.info(f'🟡 尚未完成 webview progressing，繼續等待。\n')
#                     time.sleep(poll)
#                     if time.monotonic() > end_time:
#                         error_message = f'❌ 已達 timeout {timeout} 秒，尚未完成 webview loading。\n'
#                         raise TimeoutException(error_message)
#                 else:
#                     logstack.info(f'✅ 已於 {timeout} 秒內完成 webview progressing。\n')
#                     return True
#         except TimeoutException or AttributeError:
#             logstack.warning('🟡 無法定位webview導覽列 需確認實際等待狀況')
#             return False
#
#     def wait_webview_loading(self, etimeout=3, netimeout=60):
#         """
#         等待 cube webview 內嵌頁面的 loading 消失
#         IOS_PREDICATE: 'name IN {"Loading", "LOADING"} OR name CONTAINS "讀取中"'
#         """
#         return self.wait_loading_by(self.loading.webview_loading, etimeout, netimeout)
#
#     def wait_webview_all_loading(self, start: int = 3, end: int = 60):
#         """
#         執行webview所有等待狀況
#         """
#         self.wait_app_loading(start, end)
#         self.wait_webview_progressing(end)
#         self.wait_webview_loading(start, end)
