# from appium.webdriver.webdriver import WebDriver
#
# from huskypo import logstack, Element
# from huskypo_extension import assertion
#
# from module.mobile import pattern, typecast
# from module.mobile.cube_util import CubeUtil
# from module.mobile.component import basic_assertion
# from module.ios.cube.zh_common import CubeCommon
#
# from page.ios.panel.keyboard import Keyboard
# from page.ios.cube.main.zh.common.bottom import Bottom
# from page.ios.cube.main.zh.home.home import HomePage
# from page.ios.cube.main.zh.more.more import MorePage
# from page.ios.cube.main.zh.finance.deposit import TWDDepositPage
# from page.ios.cube.main.zh.twd.tx_txn import TWDTransferStartPage
#
#
# class SubtestTX:
#
#     def __init__(self, iphone: WebDriver, case: str = None):
#         self.iphone = iphone
#         self.case = case
#         self.cube = CubeCommon(iphone)
#         self.keyboard = Keyboard()
#         self.bottom = Bottom()
#         self.home_page = HomePage()
#         self.more_page = MorePage()
#         self.twd_deposit_page = TWDDepositPage()
#         self.twd_xfer_start_page = TWDTransferStartPage()
#
#     def home_page_open_eye(self):
#         """
#         確保帳戶金額出現用
#         """
#         eye_value = self.home_page.depo_eye.value
#         logstack.info(f'eye_value: {eye_value}')
#         if eye_value == '1':
#             self.home_page.depo_eye.click()
#             CubeUtil.reload_page()
#
#     def deposit_demand_account_overview(self):
#         """
#         斷言臺幣分頁帳戶總覽
#         """
#         total_dmd_number = self.twd_deposit_page.account_cells.quantity
#         if self.twd_deposit_page.fix_total_pv.is_visible():
#             total_dmd_number -= 1
#             logstack.info('有定存')
#         else:
#             logstack.info('無定存')
#         logstack.info(f'共有 {total_dmd_number} 個活存帳戶')
#
#         int_amounts = []
#         total_available_balance_amount = self.twd_deposit_page.total_available_balance_amount.text
#         total_available_balance_int = typecast.amt_to_num(total_available_balance_amount)
#         int_amounts.append(total_available_balance_int)
#         self.twd_deposit_page.ready().save_screenshot(self.case, "預設顯示帳戶")
#         for i in range(1, total_dmd_number + 1):
#             self.twd_deposit_page.demand_account_amount_by_order(i).ready().save_screenshot(self.case, f"第{i}筆帳戶")
#             name = self.twd_deposit_page.demand_account_name_by_order(i).text
#             id_ = self.twd_deposit_page.demand_account_id_by_order(i).text
#             amount = self.twd_deposit_page.demand_account_amount_by_order(i).text
#             int_amount = typecast.amt_to_num(amount)
#             int_amounts.append(int_amount)
#             basic_assertion.logic(int_amounts[i - 1], '>=', int_amounts[i])  # 前一筆 >= 下一筆
#             basic_assertion.pattern(id_, pattern.DEPO.ID12)
#             basic_assertion.pattern(amount, pattern.AMT.ON_INT)
#         logstack.info(f'活存餘額列表: {int_amounts}')
#         return int_amounts
#
#     def tap_tx_sd_weekly_date_field(
#             self, date_fld: Element, date_picker: Element, tap: bool = True, deduct: float = 0.05):
#         """
#         處理以下特殊點擊情境
#         臺幣 預約轉帳 每週 轉帳日期選擇框
#         """
#         logstack.info(f"element is: {date_fld.remark}")
#
#         elem_loc = date_fld.location_in_view
#         x = elem_loc['x']
#         y = elem_loc['y']
#         logstack.info(f"location: {elem_loc}")
#
#         elem_size = date_fld.size
#         width = elem_size['width']
#         height = elem_size['height']
#         logstack.info(f"size: {elem_size}")
#
#         if tap:
#             factor = 1
#             while not date_picker.is_present(3):
#                 factor -= deduct
#                 icon_x = int(x + width - height * (1 - factor))
#                 icon_y = int(y + height * factor)
#                 self.twd_xfer_start_page.tap([(icon_x, icon_y)])
#                 if factor == 0:
#                     logstack.warning(f'factor已減為0，點擊依舊無效')
#                     break
#             final = (icon_x, icon_y)
#             logstack.info(f'最終座標: {final}, factor: {factor}')
#             return final
#         else:
#             return {'loc': elem_loc, 'size': elem_size}
