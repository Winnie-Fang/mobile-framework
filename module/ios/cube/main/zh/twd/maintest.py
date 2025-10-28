# import random
# import time
# from datetime import datetime, timedelta
#
# from appium.webdriver.webdriver import WebDriver
#
# from huskypo import logstack, SA, Offset
# from huskypo_extension import assertion
#
# from framework import common, datetime_utility as dt
#
# from module.mobile import finlogic, pattern, typecast
# from module.ios.cube.zh_common import CubeCommon
# from module.ios.cube.main.zh.twd.record import FROM, TO, TXN, K
# from module.ios.cube.main.zh.twd.subtest import SubtestTX
#
# from page.ios.panel.keyboard import Keyboard
# from page.ios.cube.main.zh.common.loading import Loading
# from page.ios.cube.main.zh.common.bottom import Bottom
# from page.ios.cube.main.zh.home.home import HomePage
# from page.ios.cube.main.zh.more.more import MorePage
# from page.ios.cube.main.zh.finance.deposit import TWDDepositPage, TWDDemandMainPage
# from page.ios.cube.main.zh.twd.tx_txn import TWDTransferStartPage, TWDTransferConfirmPage, TWDTransferResultPage
# from page.ios.cube.main.zh.twd.tx_popup import TXSamePopup, TXNotiPopup
# from page.ios.cube.main.zh.twd.tx_qry import TWDScheduledInquiryMainPage, TXSchedInquiryDetailsPage, TWDAPPTransferRecordPage
# from page.ios.cube.main.zh.common.rating import RatingPopup
#
# # TODO 注意未來可能變成長列表的都要加vscroll_until_visible確保選得到指定帳號
#
#
# class MaintestTX:
#
#     def __init__(self, iphone: WebDriver, case: str = 'TX'):
#         self.iphone = iphone
#         self.case = case
#         self.cube = CubeCommon(iphone)
#         self.subtest = SubtestTX(iphone)
#         self.keyboard = Keyboard()
#         self.loading = Loading(iphone)
#         self.bottom = Bottom()
#         self.home_page = HomePage()
#         self.more_page = MorePage()
#         self.deposit_page = TWDDepositPage()
#         self.demand_page = TWDDemandMainPage()
#         self.start_page = TWDTransferStartPage()
#         self.confirm_page = TWDTransferConfirmPage()
#         self.result_page = TWDTransferResultPage()
#         self.inquiry_main_page = TWDScheduledInquiryMainPage()
#         self.inquiry_details_page = TXSchedInquiryDetailsPage()
#         self.record_page = TWDAPPTransferRecordPage()
#         self.same_popup = TXSamePopup(iphone)
#         self.noti_popup = TXNotiPopup(iphone)
#         self.rating_popup = RatingPopup(iphone)
#
#     def test_data(
#             self,
#             user: dict,
#             transfer_type: str = 'self',
#             bank_type: str = 'intra',
#             from_index: int = 0,
#             to_index: int = 1):
#         """
#         - transfer_type
#           - "self", "frequently", "designated", "nondesignated"
#         - bank_type
#           - "intro", "inter"
#         """
#
#         # 記錄交易類型
#         TXN.TYPE = transfer_type
#         TXN.BANK_TYPE = bank_type
#         if TXN.TYPE == 'self':
#             TXN.BANK_TYPE = 'intra'
#         elif TXN.TYPE == 'nondesignated':
#             TXN.BANK_TYPE = 'inter'
#
#         logstack.info(f'''🟢 DATA: 開始匯入轉帳相關資料
#                       交易類型是 {TXN.TYPE},
#                       銀行類型是 {TXN.BANK_TYPE}''')
#
#         # 轉出帳號資訊
#         FROM.ID12 = user['depo']['twd']['dmd']['account'][from_index]['id']
#         FROM.ID16 = finlogic.account_id_12to16(FROM.ID12)
#         logstack.info(f'轉出帳號ID12: {FROM.ID12}')
#         logstack.info(f'轉出帳號ID16: {FROM.ID16}')
#
#         # 轉入帳號資訊
#         if TXN.TYPE == 'self':
#             TO.ID12 = user['depo']['twd']['dmd']['account'][to_index]['id']
#             TO.ID16 = finlogic.account_id_12to16(TO.ID12)
#             logstack.info(f'轉入帳號ID12: {TO.ID12}')
#             logstack.info(f'轉入帳號ID16: {TO.ID16}')
#
#         elif TXN.TYPE == 'designated':
#             TO.ID16 = user['dsig']['twd']['account'][to_index]['id']
#             TO.ID12 = finlogic.account_id_16to12(TO.ID16)
#
#         elif TXN.TYPE == 'nondesignated':
#             TO.ID12 = common.generate_account_id(12, 12)
#             TO.ID16 = finlogic.account_id_12to16(TO.ID12)
#             TO.BANK[K.RBZH] = '(444) 財金測試'
#             TXN.VERIFY_CODE = '555666'
#             logstack.info(f'轉入帳號ID12: {TO.ID12}')
#             logstack.info(f'轉入帳號ID16: {TO.ID16}')
#
#         elif TXN.TYPE == 'frequently':
#             TO.ID16 = user['pref']['twd']['account'][to_index]['id']
#
#         else:
#             raise ValueError(f'❌ 無效的交易類型: {TXN.TYPE}, 請輸入 "self", "frequently", "designated" 或 "nondesignated"')
#
#         logstack.info(f'''✅ DATA: 結束匯入轉帳相關資料
#                       交易類型是 {TXN.TYPE}
#                       銀行類型是 {TXN.BANK_TYPE} 。\n''')
#
#     def test_before(self, nextstep: bool = True, switch: bool = True):
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'''🟢 BEFORE: 開始記錄轉帳前相關資訊
#                       交易類型是 {TXN.TYPE}
#                       銀行類型是 {TXN.BANK_TYPE}''')
#
#         # 首頁 記錄當前臺幣總額
#         self.subtest.home_page_open_eye()
#         self.cube.go_to_home_page(self.case)
#         FROM.BEFORE_TOTAL_AMOUNT[K.AMT] = self.home_page.deposit_twd_amount.text
#         FROM.BEFORE_TOTAL_AMOUNT[K.INT] = typecast.amt_to_num(FROM.BEFORE_TOTAL_AMOUNT[K.AMT])
#         self.home_page.deposit_twd_amount.click()
#
#         # 臺幣分頁 驗證可用餘額 記錄帳戶餘額
#         self.deposit_page.ready().save_screenshot(self.case, "存款頁_臺幣分頁_記錄轉出轉入帳號資訊")
#         FROM.BEFORE_TOTAL_AVAILABLE_BALANCE[K.AMT] = self.deposit_page.total_available_balance_amount.text
#         FROM.BEFORE_TOTAL_AVAILABLE_BALANCE[K.INT] = typecast.amt_to_num(FROM.BEFORE_TOTAL_AVAILABLE_BALANCE[K.AMT])
#         FROM.BEFORE_TOTAL_ACCOUNT_BALANCE[K.AMT] = self.deposit_page.total_account_balance_amount.text
#         FROM.BEFORE_TOTAL_ACCOUNT_BALANCE[K.INT] = typecast.amt_to_num(FROM.BEFORE_TOTAL_ACCOUNT_BALANCE[K.AMT])
#         assertion.ae(FROM.BEFORE_TOTAL_AVAILABLE_BALANCE[K.AMT], '==', FROM.BEFORE_TOTAL_AMOUNT[K.AMT])
#
#         # 臺幣分頁 記錄轉出帳號資訊
#         FROM.NAME = self.deposit_page.demand_account_name(FROM.ID12).text
#         FROM.BEFORE_ACCOUNT_BALANCE[K.AMT] = self.deposit_page.demand_account_amount(FROM.ID12).text
#         FROM.BEFORE_ACCOUNT_BALANCE[K.AMS] = typecast.amt_to_ams(FROM.BEFORE_ACCOUNT_BALANCE[K.AMT])
#         FROM.BEFORE_ACCOUNT_BALANCE[K.GRP] = typecast.amt_to_grp(FROM.BEFORE_ACCOUNT_BALANCE[K.AMT])
#         FROM.BEFORE_ACCOUNT_BALANCE[K.INT] = typecast.amt_to_num(FROM.BEFORE_ACCOUNT_BALANCE[K.AMT])
#
#         if TXN.TYPE == 'self':
#             # 同ID記錄轉入帳號總額
#             TO.BEFORE_ACCOUNT_BALANCE[K.AMT] = self.deposit_page.demand_account_amount(TO.ID12).text
#             TO.BEFORE_ACCOUNT_BALANCE[K.AMS] = typecast.amt_to_ams(TO.BEFORE_ACCOUNT_BALANCE[K.AMT])
#             TO.BEFORE_ACCOUNT_BALANCE[K.GRP] = typecast.amt_to_grp(TO.BEFORE_ACCOUNT_BALANCE[K.AMT])
#             TO.BEFORE_ACCOUNT_BALANCE[K.INT] = typecast.amt_to_num(TO.BEFORE_ACCOUNT_BALANCE[K.AMT])
#
#         if nextstep:
#             logstack.info('🟢 執行下一步')
#             self.deposit_page.transfer_button.click()
#             logstack.info('✅ BEFORE -> START')
#         else:
#             logstack.info('⛔️ 不執行下一步')
#
#         logstack.info(f'''✅ BEFORE: 結束記錄轉帳前相關資訊
#                       交易類型是 {TXN.TYPE}
#                       銀行類型是 {TXN.BANK_TYPE}''')
#
#         assertion.SWITCH = True
#
#     def test_start_realtime(self, min: int = 500, max: int = 1500, nextstep: str = True, switch: bool = True):
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'''🟢 START_REALTIME: 開始執行即時轉帳交易
#                       交易類型是 {TXN.TYPE}
#                       銀行類型是 {TXN.BANK_TYPE}''')
#
#         # 臺幣轉帳頁
#         self.cube.wait_app_loading()
#         self.start_page.ready().save_screenshot(self.case, "臺幣轉帳頁")
#
#         # 臺幣轉帳頁 驗證轉出帳號
#         self.start_page.from_account_field.tap_center()
#
#         self.start_page.from_account_list_title.ready().save_screenshot(self.case, "臺幣轉帳頁_選擇轉出帳號")
#         self.start_page.select_from_account(FROM.ID12).click()
#         self.start_page.from_account_available_amount_info.ready().save_screenshot(self.case, "臺幣轉帳頁_轉出帳號選擇完畢")
#
#         FROM.INFO[K.NM12] = f'{FROM.NAME} {FROM.ID12}'
#         assertion.attribute('value', self.start_page.update_from_account_field(
#             FROM.ID12), '==', FROM.INFO[K.NM12])
#         gv_src_bf_acct_info = f'可用餘額 {FROM.BEFORE_ACCOUNT_BALANCE[K.AMS]}'
#         assertion.text(self.start_page.from_account_available_amount_info, '==', gv_src_bf_acct_info)
#
#         # 臺幣轉帳頁 驗證轉入帳號
#         # 先判斷是否出現非約定轉帳按鈕
#         if TXN.TYPE == 'nondesignated':
#             self.start_page.to_account_field1.click()
#             assertion.wait_present(self.start_page.to_account_update_bank_column(TO.BANK[K.RBZH]))
#             self.cube.save_screenshot(self.case, '銀行選單')
#             area = self.cube.get_rect()
#             self.start_page.to_account_update_bank_column(
#                 TO.BANK[K.RBZH]).swipe_by(Offset.UP, area, max_swipe=30).click()
#             self.cube.save_screenshot(self.case, f'選擇{TO.BANK[K.RBZH]}')
#
#             self.start_page.to_account_field2.send_keys(TO.ID16)
#             self.keyboard.done.click()
#             TO.BANK[K.RB] = finlogic.bank_split(TO.BANK[K.RBZH])['rb']
#             TO.BANK[K.ID] = TO.BANK[K.RB].replace('(', '').replace(')', '')
#             TO.BANK[K.ZH] = finlogic.bank_split(TO.BANK[K.RBZH])['zh']
#             TO.BANK[K.IDZH] = f'{TO.BANK[K.ID]} {TO.BANK[K.ZH]}'
#
#         elif self.start_page.to_account_non_designated_button.is_present(3):
#             assertion.text(self.start_page.to_account_column, '==', '轉入帳號')
#             self.start_page.to_account_field.click()
#
#             assertion.wait_present(self.start_page.to_account_list_title)
#             border = self.cube.get_table_border()
#             assertion.viewable(self.start_page.to_account_list_account_id(TO.ID16).swipe_into_view(SA.VA, border))
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_選擇轉入帳號_滑動到指定帳號")
#
#             TO.NAME = self.start_page.to_account_list_account_name(TO.ID16).text
#             TO.BANK[K.RBZH] = self.start_page.to_account_list_account_bank_rbzh(TO.ID16).text
#             TO.BANK[K.RB] = finlogic.bank_split(TO.BANK[K.RBZH])['rb']
#             TO.BANK[K.ID] = TO.BANK[K.RB].replace('(', '').replace(')', '')
#             TO.BANK[K.ZH] = finlogic.bank_split(TO.BANK[K.RBZH])['zh']
#             TO.BANK[K.IDZH] = f'{TO.BANK[K.ID]} {TO.BANK[K.ZH]}'
#             self.start_page.to_account_list_account_id(TO.ID16).click()
#
#             assertion.wait_present(self.start_page.to_account_column)
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_轉入帳號選擇完畢")
#             TO.INFO[K.NM16] = f'{TO.NAME} {TO.ID16}'
#             TO.INFO[K.NMBR16] = f'{TO.NAME} {TO.BANK[K.RB]} {TO.ID16}'
#             assertion.attribute('value', self.start_page.to_account_update_account_field(
#                 TO.ID16), '==', TO.INFO[K.NMBR16])
#
#         else:
#             # 臺幣轉帳頁 驗證轉入銀行代碼 轉入銀行帳號
#             assertion.text(self.start_page.dst_account_col1, '==', '轉入銀行代碼')
#             assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號')
#             self.start_page.to_account_select_button.click()
#
#             assertion.wait_present(self.start_page.to_account_list_title)
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_選擇轉入帳號列表")
#             if self.start_page.to_account_new_feature_content.is_present(3):
#                 logstack.warning('🟡 出現新功能通知，關閉通知')
#                 self.cube.save_screenshot(self.case, "臺幣轉帳頁_出現新功能通知")
#                 self.start_page.to_account_new_feature_close_button.click()
#                 logstack.info('✅ 成功關閉新功能通知')
#
#             if TXN.TYPE == 'self':
#                 self.start_page.to_account_self_tab.click()
#             elif TXN.TYPE == 'designated':
#                 self.start_page.to_account_designated_tab.click()
#
#             border = self.cube.get_border()
#             assertion.viewable(self.start_page.to_account_list_account_id(TO.ID16).swipe_into_view('v', border))
#             self.cube.save_screenshot(self.case, "點擊帳號後")
#             TO.NAME = self.start_page.to_account_list_account_name(TO.ID16).text
#             TO.BANK[K.RBZH] = self.start_page.to_account_list_account_bank_rbzh(TO.ID16).text
#             TO.BANK[K.RB] = finlogic.bank_split(TO.BANK[K.RBZH])['rb']
#             TO.BANK[K.ID] = TO.BANK[K.RB].replace('(', '').replace(')', '')
#             TO.BANK[K.ZH] = finlogic.bank_split(TO.BANK[K.RBZH])['zh']
#             logstack.info(f'bank_rb: {TO.BANK[K.RB]}; bank_id: {TO.BANK[K.ID]}')
#             self.start_page.to_account_list_account_id(TO.ID16).click()
#
#             # TODO 需確認欄位變更狀況
#             assertion.wait_present(self.start_page.dst_account_col1)
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_更新轉入帳號資訊")
#
#             if TXN.BANK_TYPE == 'intra':
#                 assertion.text(self.start_page.dst_account_col1, '==', f'轉入{TO.NAME}')
#                 assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號/手機號碼')
#             elif TXN.BANK_TYPE == 'inter':
#                 if TXN.TYPE == 'frequently':  # TODO 這邊要確認各家銀行簡稱
#                     assertion.text(self.start_page.dst_account_col1, 'c', '轉入')
#                 else:
#                     assertion.text(self.start_page.dst_account_col1, '==', '轉入銀行代碼')
#                 assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號')
#
#                 # 注意轉出帳號會多出跨行手續費資訊
#                 txn_fee_info = self.start_page.txn_fee_info.text
#                 pattern.AMS
#                 assertion.ae(txn_fee_info, 'c', '本通路剩餘跨行轉帳免手續費')
#                 assertion.ae(txn_fee_info, 'c', '次')
#
#             assertion.attribute('value', self.start_page.to_account_update_bank_field(
#                 TO.BANK[K.RBZH]), '==', TO.BANK[K.RBZH])
#             assertion.attribute(
#                 'value', self.start_page.to_account_update_account_field(
#                     TO.ID16), '==', TO.ID16)
#
#         # 驗證轉帳金額
#         assertion.text(self.start_page.xfer_amount_column, '==', '轉帳金額')
#
#         TXN.AMOUNT[K.INT] = random.randint(min, max)
#         TXN.AMOUNT[K.AMT] = typecast.num_to_amt(TXN.AMOUNT[K.INT])
#         TXN.AMOUNT[K.AMS] = typecast.amt_to_ams(TXN.AMOUNT[K.AMT])
#         TXN.AMOUNT[K.GRP] = typecast.amt_to_grp(TXN.AMOUNT[K.AMT])
#
#         self.start_page.xfer_amount_field.send_keys(TXN.AMOUNT[K.INT])
#         self.keyboard.done.click()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_轉入金額輸入完畢")
#         assertion.attribute('value', self.start_page.xfer_amount_field, '==', TXN.AMOUNT[K.GRP])
#
#         # 驗證轉帳時間
#         assertion.text(self.start_page.xfer_time_col, '==', '轉帳時間')
#         assertion.text(self.start_page.xfer_time_rt, '==', '即時')
#
#         # 滑動到最底部 驗證備註
#         self.start_page.swipe_ratio('v', 80, 20)
#         assertion.text(self.start_page.remark_column, '==', '備註')
#
#         TXN.REMARK[K.INPUT] = datetime.now().strftime(dt.DATETIME_RMK)
#         self.start_page.remark_field.send_keys(TXN.REMARK[K.INPUT])
#         time.sleep(3)
#         self.keyboard.done.click()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_驗證備註")
#         assertion.attribute('value', self.start_page.remark_field, '==', TXN.REMARK[K.INPUT])
#
#         # 驗證備註勾選框
#         assertion.present(self.start_page.remark_unselected)
#         assertion.not_present(self.start_page.remark_selected)
#         self.start_page.remark_unselected.click()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_驗證備註同時顯示勾選框")
#         assertion.present(self.start_page.remark_selected)
#         assertion.not_present(self.start_page.remark_unselected)
#
#         if nextstep:
#             try:
#                 self.start_page.confirm_button.click()
#                 self.cube.wait_app_loading()
#                 self.cube.skip_popup(self.same_popup.same_txn_pp_ttl, self.same_popup.same_txn_pp_acc)
#                 logstack.info('🟢 TXN -> CNF')
#             except BaseException:
#                 logstack.error('🔴 FAILED: TXN -> CNF')
#         else:
#             logstack.warning('🟡 STOPED: TXN')
#
#         logstack.info(f'⌛️ TXN_RT: 結束執行即時轉帳交易，交易類型是 {TXN.TYPE}，銀行類型是 {TXN.BANK_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def test_confirm_realtime(self, nextstep: bool = True, switch: bool = True):
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'⏳ CNF_RT: 開始執行即時轉帳確認，交易類型是 {TXN.TYPE}，銀行類型是 {TXN.BANK_TYPE} 。')
#
#         self.cube.wait_app_loading()
#         self.cube.save_screenshot(self.case, "臺幣轉帳資訊確認頁_轉帳資訊確認")
#
#         assertion.text(self.confirm_page.title_, '==', '轉帳資訊確認')
#         assertion.text(self.confirm_page.rt_xfer_col, '==', '轉帳金額')
#         assertion.text(self.confirm_page.rt_xfer_wamount, '==', TXN.AMOUNT[K.AMS], log='比對轉帳金額')
#
#         # 收款人
#         if TXN.TYPE == 'designated' and TXN.BANK_TYPE == 'intra':
#             assertion.text(self.confirm_page.dsig_payee_col, '==', '收款人')
#             assertion.text(self.confirm_page.dynamic_designated_payee_name(TO.NAME), '==', TO.NAME)
#
#         # 轉入帳號
#         assertion.text(self.confirm_page.dst_account_col, '==', '轉入帳號')
#         if TXN.TYPE == 'self':
#             TO.INFO[K.NM16] = f'{TO.NAME} {TO.ID16}'
#             assertion.text(self.confirm_page.dynamic_destination_account_info(TO.ID16), '==', TO.INFO[K.NM16])
#         elif TXN.TYPE == 'designated' and TXN.TYPE == 'nondesignated':
#             TO.INFO[K.BC16] = f'{TO.BANK[K.RBZH]} {TO.ID16}'
#             assertion.text(self.confirm_page.dynamic_destination_account_info(TO.ID16), '==', TO.INFO[K.BC16])
#
#         # 轉出帳號
#         assertion.text(self.confirm_page.src_account_col, '==', '轉出帳號')
#         FROM.INFO[K.NM16] = f'{FROM.NAME} {FROM.ID16}'
#         assertion.text(self.confirm_page.dynamic_source_account_info(FROM.ID16), '==', FROM.INFO[K.NM16])
#
#         # 跨行交易手續費
#         if TXN.TYPE == 'designated' and TXN.BANK_TYPE == 'inter':
#             assertion.text(self.confirm_page.txn_fee_remark, '==', '跨行交易手續費將以實際計收為準')
#
#         # 交易類型
#         assertion.text(self.confirm_page.txn_type_col, '==', '交易類型')
#         if TXN.TYPE == 'self':
#             assertion.text(self.confirm_page.txn_type_self, '==', '本人國泰世華帳戶互轉')
#             self.confirm_page.txn_type_self_ibtn.click()
#             self.confirm_page.txn_type_self_pp_title.wait_visible()
#             self.cube.save_screenshot(self.case, "關於本人國泰世華互轉彈窗")
#             assertion.present(self.confirm_page.txn_type_self_pp_content)
#             self.confirm_page.txn_type_self_pp_confirm.click()
#             self.confirm_page.title_.wait_visible()
#             self.cube.save_screenshot(self.case, "回到轉帳資訊確認")
#
#         elif TXN.TYPE == 'frequently':
#             pass
#         elif TXN.TYPE == 'designated':
#             assertion.text(self.confirm_page.txn_type_dsig, '==', '約定轉帳')
#             self.confirm_page.txn_type_dsig_ibtn.click()
#             self.confirm_page.txn_type_dsig_pp_title.wait_visible()
#             self.cube.save_screenshot(self.case, "關於約定轉帳彈窗")
#             assertion.present(self.confirm_page.txn_type_dsig_pp_content)
#             self.confirm_page.txn_type_dsig_pp_confirm.click()
#             self.confirm_page.title_.wait_visible()
#             self.cube.save_screenshot(self.case, "回到轉帳資訊確認")
#         elif TXN.TYPE == 'nondesignated':
#             assertion.visible(self.confirm_page.txn_type_nondsig)
#             self.confirm_page.txn_type_dsig_ibtn.click()
#             assertion.wait_present(self.confirm_page.txn_type_nondsig_PP_title)
#             self.cube.save_screenshot(self.case, '關於非約定轉帳小i彈窗')
#             self.confirm_page.txn_type_dsig_pp_confirm.click()
#             assertion.wait_not_present(self.confirm_page.txn_type_nondsig_PP_title)
#             self.cube.save_screenshot(self.case, '轉帳確認頁面')
#
#         # 備註
#         TXN.REMARK[K.INFO] = f'備註： {TXN.REMARK[K.INPUT]}'
#         assertion.text(self.confirm_page.txn_remark_info, '==', TXN.REMARK[K.INFO])
#
#         # 提防詐騙訊息
#         assertion.text(self.confirm_page.noti_avoid_scam, '==', '交易前請再次確認，避免詐騙犯罪產生。')
#
#         if nextstep and TXN.TYPE in ['self', 'designated']:
#             try:
#                 self.confirm_page.cnf_xfer_button.click()
#                 self.cube.wait_app_loading()
#
#                 # 轉帳資訊確認頁 確認轉帳彈窗
#                 self.cube.save_screenshot(self.case, "臺幣轉帳資訊確認頁_確認轉帳彈窗")
#                 if TXN.TYPE == 'self':
#                     cnfpg_rt_pp_cnt = f'即將轉出 {TXN.AMOUNT[K.AMS]} 給\n {TO.INFO[K.NM16]}'
#                 elif TXN.TYPE == 'designated' and TXN.BANK_TYPE == 'intra':
#                     TO.INFO[K.NMBR16] = TO.NAME + '\n ' + TO.BANK[K.RB] + ' ' + TO.ID16  # 注意空格和換行
#                     cnfpg_rt_pp_cnt = f'即將轉出 {TXN.AMOUNT[K.AMS]} 給\n {TO.INFO[K.NMBR16]}'
#                 elif TXN.TYPE == 'designated' and TXN.BANK_TYPE == 'inter':
#                     TO.INFO[K.BR16] = f'{TO.BANK[K.RB]} {TO.ID16}'
#                     cnfpg_rt_pp_cnt = f'即將轉出 {TXN.AMOUNT[K.AMS]} 給\n {TO.INFO[K.BR16]}'
#
#                 assertion.text(self.confirm_page.cnf_xfer_pp_cnt, '==', cnfpg_rt_pp_cnt)
#                 TXN.START_DATETIME = datetime.now().replace(microsecond=0)
#                 self.confirm_page.cnf_xfer_pp_acc.click()
#
#                 logstack.info('🟢 CNF -> RES')
#             except BaseException:
#                 logstack.error('🔴 FAILED: CNF -> RES')
#         elif nextstep and TXN.TYPE == 'nondesignated':
#             try:
#                 # 進入交易驗證碼頁
#                 self.confirm_page.cnf_verify_button.click()
#                 self.cube.wait_app_loading(3, 60)
#                 assertion.wait_present(self.confirm_page.txn_verify_code_text)
#                 self.cube.save_screenshot(self.case, '輸入交易驗證碼')
#                 self.confirm_page.txn_verify_code_input_box.send_keys(TXN.VERIFY_CODE)
#                 self.keyboard.done.click()
#                 self.confirm_page.txn_verify_code_confirm_button.click()
#                 TXN.START_DATETIME = datetime.now().replace(microsecond=0)
#                 logstack.info('🟢 CNF -> RES')
#             except BaseException:
#                 logstack.error('🔴 FAILED: CNF -> RES')
#         else:
#             logstack.warning('🟡 STOPED: CNF')
#
#         logstack.info(f'⌛️ CNF_RT: 結束執行即時轉帳確認，交易類型是 {TXN.TYPE}，銀行類型是 {TXN.BANK_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def test_result_realtime(self, nextstep: bool = True, switch: bool = True):
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'⏳ RES_RT: 開始執行即時轉帳結果，交易類型是 {TXN.TYPE}，銀行類型是 {TXN.BANK_TYPE} 。')
#
#         # loading
#         self.cube.wait_app_loading(3, 60)
#
#         if self.result_page.rt_failed.is_present(3):
#             self.cube.save_screenshot(self.case, "❌ 交易失敗")
#             assert False, '❌ 交易失敗'
#
#         # 轉帳結果頁
#         self.result_page.txn_datetime_com.wait_visible()
#         self.cube.save_screenshot(self.case, "臺幣轉帳轉帳結果頁_轉帳結果確認", 3)
#         res_exedt_com = self.result_page.txn_datetime_com.text
#         TXN.END_DATETIME = datetime.now().replace(microsecond=0) + timedelta(seconds=30)
#         TXN.EXECUTE_DATETIME[K.COM] = res_exedt_com
#         TXN.EXECUTE_DATETIME[K.ORI] = datetime.strptime(res_exedt_com, dt.DATETIME_COM)
#         TXN.EXECUTE_DATE[K.COM] = res_exedt_com.split()[0]
#
#         # self.check_if_realtime_result_is_failed()
#
#         assertion.text(self.result_page.title_, '==', '轉帳結果')
#         assertion.text(self.result_page.rt_passed, '==', '交易成功')
#         logstack.info(
#             f'{type(TXN.START_DATETIME)}:{TXN.START_DATETIME}     {type(TXN.EXECUTE_DATETIME[K.ORI])}:{TXN.EXECUTE_DATETIME[K.ORI]}     {type(TXN.END_DATETIME)}:{TXN.END_DATETIME}')
#         assertion.datetime_in_range(TXN.START_DATETIME, TXN.EXECUTE_DATETIME[K.ORI], TXN.END_DATETIME)
#
#         assertion.text(self.result_page.rt_xfer_col, '==', '轉帳金額')
#         assertion.text(self.result_page.xfer_wamount, '==', TXN.AMOUNT[K.AMS])
#
#         # 約轉收款人
#         if TXN.TYPE == 'designated' and TXN.BANK_TYPE == 'intra':
#             assertion.text(self.result_page.dsig_payee_col, '==', '收款人')
#             assertion.text(self.result_page.dynamic_designated_payee_name(TO.NAME), '==', TO.NAME)
#
#         # 轉入帳號判斷
#         assertion.text(self.result_page.dst_account_col, '==', '轉入帳號')
#         if TXN.TYPE == 'self':
#             TO.INFO[K.NM16] = f'{TO.NAME} {TO.ID16}'
#             assertion.text(self.result_page.dynamic_destination_account_info(TO.ID16), '==', TO.INFO[K.NM16])
#         elif TXN.TYPE == 'designated' or TXN.TYPE == 'nondesignated':
#             TO.INFO[K.BC16] = f'{TO.BANK[K.RBZH]} {TO.ID16}'
#             assertion.text(self.result_page.dynamic_destination_account_info(TO.ID16), '==', TO.INFO[K.BC16])
#
#         # 轉出帳號
#         assertion.text(self.result_page.src_account_col, '==', '轉出帳號')
#         assertion.text(self.result_page.dynamic_source_account_info(FROM.ID16), '==', FROM.INFO[K.NM16])
#
#         # 跨行手續費
#         if TXN.BANK_TYPE == 'inter':
#             assertion.text(self.result_page.txn_fee_col, '==', '手續費')
#             TXN.FEE[K.AMS] = self.result_page.txn_fee_amt.text
#             TXN.FEE[K.AMT] = TXN.FEE[K.AMS].replace(' ', '')
#             TXN.FEE[K.GRP] = typecast.amt_to_grp(TXN.FEE[K.AMS])
#             TXN.FEE[K.INT] = typecast.grp_to_num(TXN.FEE[K.GRP])
#             assertion.pattern(TXN.FEE[K.AMS], pattern.AMS.O_INT)
#         else:
#             TXN.FEE[K.INT] = 0
#             TXN.FEE[K.GRP] = '0'
#
#         # 可用餘額 注意此處開眼後金額DOM排序會變
#         assertion.text(self.result_page.src_avail_col, '==', '可用餘額')
#         assertion.attribute('value', self.result_page.src_avail_eye, '==', '1')
#         assertion.text(self.result_page.src_avail_amount_hide, '==', '********')
#         self.result_page.src_avail_eye.click()
#         self.result_page.src_avail_amount_ams.wait_visible()
#         self.cube.save_screenshot(self.case, "可用餘額顯示")
#         assertion.attribute('value', self.result_page.src_avail_eye, '==', None)
#         FROM.AFTER_ACCOUNT_BALANCE[K.INT] = FROM.BEFORE_ACCOUNT_BALANCE[K.INT] - TXN.AMOUNT[K.INT] - TXN.FEE[K.INT]
#         FROM.AFTER_ACCOUNT_BALANCE[K.AMT] = typecast.num_to_amt(FROM.AFTER_ACCOUNT_BALANCE[K.INT])
#         FROM.AFTER_ACCOUNT_BALANCE[K.AMS] = typecast.amt_to_ams(FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#         assertion.text(self.result_page.src_avail_amount_ams, '==', FROM.AFTER_ACCOUNT_BALANCE[K.AMS])
#
#         # 金資序號
#         if TXN.BANK_TYPE == 'inter':
#             assertion.text(self.result_page.stnno_col, '==', '金資序號')
#             TXN.STAN_NO = self.result_page.stnno_value.text
#             assertion.pattern(TXN.STAN_NO, pattern.TWD.CAP_NUM_7)
#
#         # 交易序號
#         assertion.text(self.result_page.txnno_col, '==', '交易序號')
#         TXN.TXN_NO = self.result_page.txnno_value.text
#         assertion.pattern(TXN.TXN_NO, pattern.TWD.CAP_NUM_7)
#
#         # 備註
#         assertion.text(self.result_page.txn_remark_info, '==', TXN.REMARK[K.INFO])
#
#         # 底部堆播
#         border = self.cube.get_table_border()
#         self.result_page.xfer_again_button.swipe_into_view(SA.VA, border)
#         self.cube.save_screenshot(self.case, "再轉一筆")
#         assertion.text(self.result_page.xfer_again_msg, '==', '還需要轉帳給對方？請點此')
#         assertion.text(self.result_page.xfer_again_button, '==', '再轉一筆')
#
#         if nextstep:
#             try:
#                 self.result_page.done_button.click()
#                 self.cube.wait_app_loading()
#                 self.skip_noti_and_rating_popups()
#                 logstack.info(f'🟢 RES -> HOME')
#             except BaseException:
#                 logstack.error(f'🔴 FAILED: RES -> HOME')
#         else:
#             logstack.warning(f'🟡 STOPED: RES')
#
#         logstack.info(f'⌛️ RES_RT: 結束執行即時轉帳結果，交易類型是 {TXN.TYPE}，銀行類型是 {TXN.BANK_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def test_after_realtime(self, switch: bool = True):
#         """
#         bf: home acnt src dst
#         """
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'⏳ AF_RT_HOME: 開始驗證轉帳後的金額變化，交易類型是 {TXN.TYPE}，銀行類型是 {TXN.BANK_TYPE} 。')
#
#         # loading
#         self.cube.wait_app_loading()
#
#         # 首頁與存款頁驗證
#         if TXN.TYPE == 'self':
#             # 回到首頁 檢查總額應不變
#             assertion.wait_visible(self.home_page.deposit_twd_amount)
#             self.home_page.save_screenshot(self.case, "回到首頁")
#             FROM.AFTER_TOTAL_AMOUNT[K.AMT] = self.home_page.deposit_twd_amount.text
#             assertion.ae(FROM.AFTER_TOTAL_AMOUNT[K.AMT], '==', FROM.BEFORE_TOTAL_AMOUNT[K.AMT])
#             self.home_page.deposit_twd_amount.click()
#
#             # 存款頁 確認 dpal, dpac, src, dst 帳戶金額變化
#             assertion.wait_all_present(self.deposit_page.all_amounts)
#             self.cube.save_screenshot(self.case, "存款頁確認金額變化")
#
#             assertion.text(self.deposit_page.total_available_balance_amount,
#                            '==', FROM.AFTER_TOTAL_AMOUNT[K.AMT])
#             assertion.text(self.deposit_page.total_account_balance_amount, '==',
#                            FROM.BEFORE_TOTAL_ACCOUNT_BALANCE[K.AMT])
#             border = self.cube.get_table_border()
#             self.deposit_page.demand_account_amount(FROM.ID12).swipe_into_view(SA.VA, border)
#             assertion.text(self.deposit_page.demand_account_amount(FROM.ID12),
#                            '==', FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#
#             self.deposit_page.demand_account_id(FROM.ID12).click()
#             self.cube.wait_app_loading()
#             self.cube.wait_app_activity_indicator_loading()
#             self.cube.save_screenshot(self.case, "帳戶明細頁")
#
#             FROM.AFTER_ACCOUNT_BALANCE[K.GRP] = typecast.amt_to_grp(FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#             self.demand_page.newest_txn_amount.click()
#             assertion.wait_visible(self.demand_page.newest_txn_expand_info)
#             self.cube.save_screenshot(self.case, "展開帳戶明細")
#             assertion.text(self.demand_page.twd_amount, '==', f'TWD {FROM.AFTER_ACCOUNT_BALANCE[K.GRP]}')
#             assertion.text(self.demand_page.newest_txn_amount, '==', f'-{TXN.AMOUNT[K.AMT]}')
#             assertion.text(self.demand_page.newest_txn_avail, '==', FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#             self.demand_page.back_button.click()
#             assertion.wait_all_present(self.deposit_page.all_amounts)
#             self.cube.save_screenshot(self.case, "回到存款頁")
#
#             TO.AFTER_ACCOUNT_BALANCE[K.INT] = TO.BEFORE_ACCOUNT_BALANCE[K.INT] + TXN.AMOUNT[K.INT]
#             TO.AFTER_ACCOUNT_BALANCE[K.AMT] = typecast.num_to_amt(TO.AFTER_ACCOUNT_BALANCE[K.INT])
#             TO.AFTER_ACCOUNT_BALANCE[K.GRP] = typecast.amt_to_grp(TO.AFTER_ACCOUNT_BALANCE[K.AMT])
#             self.deposit_page.demand_account_amount(TO.ID12).swipe_into_view(SA.VA, border)
#             assertion.text(self.deposit_page.demand_account_amount(TO.ID12),
#                            '==', TO.AFTER_ACCOUNT_BALANCE[K.AMT])
#
#             self.deposit_page.demand_account_id(TO.ID12).click()
#             self.cube.wait_app_activity_indicator_loading()
#             self.cube.save_screenshot(self.case, "帳戶明細頁")
#
#             self.demand_page.newest_txn_amount.click()
#             # self.demand_page.newest_txn_amount.click()
#             assertion.wait_visible(self.demand_page.newest_txn_expand_info)
#             self.cube.save_screenshot(self.case, "展開帳戶明細")
#
#             assertion.text(self.demand_page.twd_amount, '==', f'TWD {TO.AFTER_ACCOUNT_BALANCE[K.GRP]}')
#             assertion.text(self.demand_page.newest_txn_amount, '==', TXN.AMOUNT[K.AMT])
#             assertion.text(self.demand_page.newest_txn_avail, '==', TO.AFTER_ACCOUNT_BALANCE[K.AMT])
#             self.demand_page.back_button.click()
#             self.deposit_page.total_available_balance_column.wait_visible()
#             self.cube.save_screenshot(self.case, "回到存款頁")
#
#         elif TXN.TYPE == 'designated' or TXN.TYPE == 'nondesignated':
#             # 回到首頁 檢查總額變化
#             self.home_page.table.wait_present()
#             self.home_page.save_screenshot(self.case, "回到首頁")
#             FROM.AFTER_TOTAL_AMOUNT[K.AMT] = self.home_page.deposit_twd_amount.text
#             expected_afhome_int = FROM.BEFORE_TOTAL_AMOUNT[K.INT] - TXN.AMOUNT[K.INT] - TXN.FEE[K.INT]
#             expected_afhome_ori = typecast.num_to_amt(expected_afhome_int)
#             assertion.ae(FROM.AFTER_TOTAL_AMOUNT[K.AMT], '==', expected_afhome_ori)
#             self.home_page.deposit_twd_amount.click()
#
#             # 存款頁 確認 dpal, dpac, src 帳戶金額變化
#             self.deposit_page.all_amounts.wait_all_present()
#             self.cube.save_screenshot(self.case, "存款頁確認金額變化")
#
#             assertion.text(self.deposit_page.total_available_balance_amount,
#                            '==', FROM.AFTER_TOTAL_AMOUNT[K.AMT])
#
#             FROM.AFTER_TOTAL_ACCOUNT_BALANCE[K.AMT] = self.deposit_page.total_account_balance_amount.text
#             expected_afdpac_int = FROM.BEFORE_TOTAL_ACCOUNT_BALANCE[K.INT] - TXN.AMOUNT[K.INT] - TXN.FEE[K.INT]
#             expected_afdpac_ori = typecast.num_to_amt(expected_afdpac_int)
#             assertion.ae(FROM.AFTER_TOTAL_ACCOUNT_BALANCE[K.AMT], '==', expected_afdpac_ori)
#             border = self.cube.get_table_border(True)
#             self.deposit_page.demand_account_amount(FROM.ID12).swipe_into_view(SA.VA, border)
#             assertion.text(self.deposit_page.demand_account_amount(FROM.ID12),
#                            '==', FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#
#             self.deposit_page.demand_account_id(FROM.ID12).click()
#             self.cube.wait_app_loading()
#             self.cube.wait_app_activity_indicator_loading()
#             self.cube.save_screenshot(self.case, "帳戶明細頁")
#
#             # 1801 更新定位
#             newest_txn_amount = self.demand_page.newest_txn_amount.text
#             second_txn_amount = self.demand_page.second_txn_amount.text
#             self.demand_page.newest_txn_amount.click()
#             self.demand_page.second_txn_amount.click()
#             self.demand_page.swipe_ratio(SA.V, 60, 40)
#             assertion.wait_visible(self.demand_page.newest_txn_expand_info)
#             assertion.wait_visible(self.demand_page.second_txn_expand_info)
#             self.cube.save_screenshot(self.case, "展開帳戶明細")
#
#             FROM.AFTER_ACCOUNT_BALANCE[K.GRP] = typecast.amt_to_grp(FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#             FROM.AFTER_ACCOUNT_BALANCE[K.INT] = typecast.amt_to_num(FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#             assertion.text(self.demand_page.twd_amount, '==', f'TWD {FROM.AFTER_ACCOUNT_BALANCE[K.GRP]}')
#             if TXN.BANK_TYPE == 'inter':
#                 assertion.ae(newest_txn_amount, '==', f'-{TXN.FEE[K.AMT]}')
#                 assertion.text(self.demand_page.newest_txn_avail, '==', FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#                 assertion.ae(second_txn_amount, '==', f'-{TXN.AMOUNT[K.AMT]}')
#                 expect_second_txn_avail_int = FROM.AFTER_ACCOUNT_BALANCE[K.INT] + TXN.FEE[K.INT]
#                 expect_second_txn_avail_amt = typecast.num_to_amt(expect_second_txn_avail_int)
#                 assertion.text(self.demand_page.second_txn_avail, '==', expect_second_txn_avail_amt)
#             else:
#                 assertion.ae(newest_txn_amount, '==', f'-{TXN.AMOUNT[K.AMT]}')
#                 assertion.text(self.demand_page.newest_txn_avail, '==', FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#             self.demand_page.back_button.click()
#             self.deposit_page.total_available_balance_column.wait_visible()
#             self.cube.save_screenshot(self.case, "回到存款頁")
#             assertion.wait_present(self.deposit_page.total_available_balance_column)
#
#         # APP轉帳紀錄頁驗證
#         self.bottom.more.click()
#         assertion.wait_visible(self.more_page.finance_twd)
#         border = self.cube.get_table_border()
#         self.more_page.finance_twd.click()
#         self.more_page.fin_twd_app_record.swipe_into_view(SA.VA, border)
#         self.cube.save_screenshot(self.case, '更多功能頁_展開台幣區塊')
#         self.more_page.fin_twd_app_record.click()
#
#         # APP轉帳紀錄頁
#         self.cube.wait_app_loading()
#         assertion.wait_present(self.record_page.title_)
#         self.cube.save_screenshot(self.case, '更多功能頁_APP轉帳紀錄頁')
#         # self.record_page.date(TXN.EXECUTE_DATE[K.COM]).swipe_into_view(SA.VA, border)
#         self.record_page.transfer_amount_by_id_and_account(
#             TO.ID16, TXN.EXECUTE_DATE[K.COM]).swipe_into_view(SA.VA, border)
#         self.cube.save_screenshot(self.case, 'APP轉帳紀錄頁_滑動到指定日期內最新紀錄')
#         self.record_page.transfer_amount_by_id_and_account(TO.ID16, TXN.EXECUTE_DATE[K.COM]).click()
#         if self.record_page.tx_result_popup_text.wait_present(3):
#             self.cube.save_screenshot(self.case, 'APP轉帳紀錄頁_如欲查詢交易結果彈窗')
#             self.record_page.tx_result_popup_confirm_button.click()
#         self.cube.save_screenshot(self.case, 'APP轉帳紀錄頁_展開記錄', 1)
#
#         if TXN.TYPE != 'self' and TXN.BANK_TYPE == 'intra':
#             dst_new_name = finlogic.name_replace(TO.NAME)
#             # 此處只能從轉帳起始頁取得名稱，中間字已被改成 ＊ 因此無法轉換回真實名稱
#             # 因此元素辨認邏輯修改為認第一與最後一個字
#             assertion.present(self.record_page.to_account_name(TXN.EXECUTE_DATE[K.COM], dst_new_name))
#         rcd_dst_biz16 = f'{TO.BANK[K.ID]} {TO.BANK[K.ZH]} {TO.ID16}'
#         self.record_page.to_account_bankid_bankzh_id16(
#             TXN.EXECUTE_DATE[K.COM], TO.ID16).swipe_into_view(SA.VA, border, 75, 25)
#         assertion.text(self.record_page.to_account_bankid_bankzh_id16(
#             TXN.EXECUTE_DATE[K.COM], TO.ID16), '==', rcd_dst_biz16)
#
#         # TODO Ives 太好轉特殊情境可以用條件判斷，否則其他case會不能執行
#         # if 太好轉 之類的再判斷這個
#         # 當轉帳紀錄同時存在太好轉與一般轉帳時 帶取款的太好轉會被置頂 不能單純判定日期下方第一個元素
#         # assertion.text(self.record_page.transfer_amount_by_id(TO.ID16), '==',
#         #                TXN.AMOUNT[K.AMT])
#
#         # 一般轉帳情境 勿mark 否則都會fail
#         # else
#         assertion.text(self.record_page.transfer_amount_by_id_and_account(
#             TO.ID16, TXN.EXECUTE_DATE[K.COM]), '==', TXN.AMOUNT[K.AMT])
#
#         assertion.text(self.record_page.src_account_col, '==', '轉出帳號')
#         assertion.text(self.record_page.from_account_name(FROM.NAME), '==', FROM.NAME)
#         assertion.text(self.record_page.from_account_id(FROM.ID12), '==', FROM.ID12)
#         assertion.text(self.record_page.txn_datetime_col, '==', '交易時間')
#         assertion.text(self.record_page.transfer_datetime(
#             TXN.EXECUTE_DATETIME[K.COM]), '==', TXN.EXECUTE_DATETIME[K.COM])
#         assertion.text(self.record_page.txn_type_col, '==', '轉帳型態')
#         assertion.text(self.record_page.txn_type_rt, '==', '即時')
#         assertion.text(self.record_page.txn_remark_col, '==', '備註')
#         assertion.text(self.record_page.transfer_remark_input(TXN.REMARK[K.INPUT]), '==', TXN.REMARK[K.INPUT])
#         assertion.text(self.record_page.txn_res_col, '==', '交易狀態')
#         assertion.text(self.record_page.txn_res_success, '==', '交易成功')
#         assertion.text(self.record_page.txn_fee_col, '==', '手續費')
#         assertion.text(self.record_page.transfer_fee_grouping(TXN.FEE[K.GRP]), '==', TXN.FEE[K.GRP])
#
#         self.record_page.tx_button.click()
#         self.cube.wait_app_loading()
#         assertion.wait_present(self.start_page.from_account_available_amount_info)
#         self.cube.save_screenshot(self.case, "導向到臺幣轉帳頁")
#
#         assertion.attribute('value', self.start_page.from_account_field, '==', FROM.INFO[K.NM12])
#         FROM.AFTER_ACCOUNT_BALANCE[K.AMS] = typecast.amt_to_ams(FROM.AFTER_ACCOUNT_BALANCE[K.AMT])
#         assertion.text(self.start_page.from_account_available_amount_info,
#                        '==', f'可用餘額 {FROM.AFTER_ACCOUNT_BALANCE[K.AMS]}')
#
#         if TXN.BANK_TYPE == 'intra':
#             # assertion.text(self.txnpg.dst_account_col1, '==', f'轉入{DST.NAME}')
#             assertion.text(self.start_page.dst_account_col1, '==', f'轉入銀行代碼')
#             assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號/手機號碼')
#         elif TXN.BANK_TYPE == 'inter':
#             if TXN.TYPE == 'frequently':  # TODO 這邊要確認各家銀行簡稱
#                 assertion.text(self.start_page.dst_account_col1, 'c', '轉入')
#             else:
#                 assertion.text(self.start_page.dst_account_col1, '==', '轉入銀行代碼')
#             assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號')
#
#             # 注意轉出帳號會多出跨行手續費資訊
#             txn_fee_info = self.start_page.txn_fee_info.text
#             assertion.ae(txn_fee_info, 'c', '本通路剩餘跨行轉帳免手續費')
#             assertion.ae(txn_fee_info, 'c', '次')
#         assertion.attribute('value', self.start_page.to_account_update_bank_field(
#             TO.BANK[K.RBZH]), '==', TO.BANK[K.RBZH])
#         assertion.attribute(
#             'value', self.start_page.to_account_update_account_field(
#                 TO.ID16), '==', TO.ID16)
#
#         assertion.attribute('value', self.start_page.xfer_amount_field, '==', TXN.AMOUNT[K.GRP])
#
#         assertion.attribute('value', self.start_page.remark_field, '==', TXN.REMARK[K.INPUT])
#
#         logstack.info(f'⌛️ AF_RT_HOME: 結束驗證轉帳後的金額變化，交易類型是 {TXN.TYPE}，銀行類型是 {TXN.BANK_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def test_start_scheduled(self, sdtype: str = 'single', weekday: int = 0,
#                              min: int = 500, max: int = 1500, nextstep: bool = True, switch: bool = True):
#
#         assertion.SWITCH = switch
#
#         # 記錄預約轉帳類型
#         TXN.SCHEDULED_TYPE = sdtype
#         logstack.info(f'⏳ TXN_SD: 開始執行預約轉帳交易，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。')
#
#         # 臺幣轉帳頁
#         self.cube.wait_app_loading()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁")
#
#         # 臺幣轉帳頁 驗證轉出帳號
#         assertion.text(self.start_page.from_account_column, '==', '轉出帳號')
#         self.start_page.from_account_field.tap()
#
#         self.start_page.from_account_list_title.wait_present()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_選擇轉出帳號")
#         border = self.cube.get_table_border()
#         self.start_page.select_from_account(FROM.ID12).swipe_into_view(SA.VA, border).click()
#
#         self.start_page.title_.wait_visible()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_轉出帳號選擇完畢")
#
#         FROM.INFO[K.NM12] = f'{FROM.NAME} {FROM.ID12}'
#         self.start_page.title_.wait_visible()
#         # assertion.attribute('value', self.txnpg.upd_src_account_fld(SRC.ID12), '==', SRC.INFO[K.NM12])
#         gv_src_bf_acct_info = f'可用餘額 {FROM.BEFORE_ACCOUNT_BALANCE[K.AMS]}'
#         assertion.text(self.start_page.from_account_available_amount_info, '==', gv_src_bf_acct_info)
#
#         # 臺幣轉帳頁 驗證轉入帳號
#         # 先判斷是否出現非約定轉帳按鈕
#         if self.start_page.to_account_non_designated_button.is_present(3):
#             assertion.text(self.start_page.to_account_column, '==', '轉入帳號')
#             self.start_page.to_account_field.click()
#
#             self.start_page.to_account_list_title.wait_present()
#             border = self.cube.get_table_border()
#             self.start_page.to_account_list_account_id(TO.ID16).swipe_into_view(SA.VA, border)
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_選擇轉入帳號_滑動到指定帳號")
#
#             TO.NAME = self.start_page.to_account_list_account_name(TO.ID16).text
#             TO.BANK[K.RBZH] = self.start_page.to_account_list_account_bank_rbzh(TO.ID16).text
#             TO.BANK[K.RB] = finlogic.bank_split(TO.BANK[K.RBZH])['rb']
#             TO.BANK[K.ID] = TO.BANK[K.RB].replace('(', '').replace(')', '')
#             TO.BANK[K.ZH] = finlogic.bank_split(TO.BANK[K.RBZH])['zh']
#             TO.BANK[K.IDZH] = f'{TO.BANK[K.ID]} {TO.BANK[K.ZH]}'
#             self.start_page.to_account_list_account_id(TO.ID16).click()
#
#             # TODO 需確認各種狀況
#             self.start_page.to_account_column.wait_present()
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_轉入帳號選擇完畢")
#             TO.INFO[K.NM16] = f'{TO.NAME} {TO.ID16}'
#             TO.INFO[K.NMBR16] = f'{TO.NAME} {TO.BANK[K.RB]} {TO.ID16}'
#             assertion.attribute('value', self.start_page.to_account_update_account_field(
#                 TO.ID16), '==', TO.INFO[K.NMBR16])
#
#         else:
#             # 臺幣轉帳頁 驗證轉入銀行代碼 轉入銀行帳號
#             assertion.text(self.start_page.dst_account_col1, '==', '轉入銀行代碼')
#             assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號')
#             self.start_page.to_account_select_button.click()
#
#             self.start_page.to_account_list_title.wait_present()
#             if self.start_page.to_account_new_feature_content.is_present(3):
#                 logstack.warning('🟡 出現新功能通知，關閉通知')
#                 self.cube.save_screenshot(self.case, "臺幣轉帳頁_出現新功能通知")
#                 self.start_page.to_account_new_feature_close_button.click()
#                 logstack.info('✅ 成功關閉新功能通知')
#
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_選擇轉入帳號列表")
#             border = self.cube.get_table_border()
#             self.start_page.to_account_list_account_id(TO.ID16).swipe_into_view(SA.VA, border)
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_滑動到指定約定帳號出現並選擇")
#             TO.NAME = self.start_page.to_account_list_account_name(TO.ID16).text
#             TO.BANK[K.RBZH] = self.start_page.to_account_list_account_bank_rbzh(TO.ID16).text
#             TO.BANK[K.RB] = finlogic.bank_split(TO.BANK[K.RBZH])['rb']
#             TO.BANK[K.ID] = TO.BANK[K.RB].replace('(', '').replace(')', '')
#             TO.BANK[K.ZH] = finlogic.bank_split(TO.BANK[K.RBZH])['zh']
#             logstack.info(f'bank_rb: {TO.BANK[K.RB]}; bank_id: {TO.BANK[K.ID]}')
#             self.start_page.to_account_list_account_id(TO.ID16).click()
#
#             # TODO 需確認欄位變更狀況
#             self.start_page.dst_account_col1.wait_present()
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_更新轉入帳號資訊")
#
#             if TXN.BANK_TYPE == 'intra':
#                 assertion.text(self.start_page.dst_account_col1, '==', f'轉入{TO.NAME}')
#                 assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號/手機號碼')
#             elif TXN.BANK_TYPE == 'inter':
#                 if TXN.TYPE == 'frequently':  # TODO 這邊要確認各家銀行簡稱
#                     assertion.text(self.start_page.dst_account_col1, 'c', '轉入')
#                 else:
#                     assertion.text(self.start_page.dst_account_col1, '==', '轉入銀行代碼')
#                 assertion.text(self.start_page.dst_account_col2, '==', '轉入銀行帳號')
#
#                 # 注意轉出帳號會多出跨行手續費資訊
#                 txn_fee_info = self.start_page.txn_fee_info.text
#                 assertion.ae(txn_fee_info, 'c', '本通路剩餘跨行轉帳免手續費')
#                 assertion.ae(txn_fee_info, 'c', '次')
#
#             assertion.attribute('value', self.start_page.to_account_update_bank_field(
#                 TO.BANK[K.RBZH]), '==', TO.BANK[K.RBZH])
#             assertion.attribute(
#                 'value', self.start_page.to_account_update_account_field(
#                     TO.ID16), '==', TO.ID16)
#
#         # 驗證轉帳金額
#         assertion.text(self.start_page.xfer_amount_column, '==', '轉帳金額')
#
#         TXN.AMOUNT[K.INT] = random.randint(min, max)
#         TXN.AMOUNT[K.AMT] = typecast.num_to_amt(TXN.AMOUNT[K.INT])
#         TXN.AMOUNT[K.AMS] = typecast.amt_to_ams(TXN.AMOUNT[K.AMT])
#         TXN.AMOUNT[K.GRP] = typecast.amt_to_grp(TXN.AMOUNT[K.AMT])
#
#         self.start_page.xfer_amount_field.send_keys(TXN.AMOUNT[K.INT])
#         self.keyboard.done.click()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_轉入金額輸入完畢")
#         assertion.attribute('value', self.start_page.xfer_amount_field, '==', TXN.AMOUNT[K.GRP])
#
#         # 驗證轉帳時間
#         assertion.text(self.start_page.xfer_time_col, '==', '轉帳時間')
#         self.start_page.xfer_time_sched.click()
#         assertion.text(self.start_page.xfer_time_sched, '==', '預約')
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_選擇預約")
#
#         # 轉帳頻率類別
#         if sdtype == 'single':
#             assertion.text(self.start_page.sd_freq_col, '==', '轉帳頻率')
#             assertion.attribute('value', self.start_page.sd_freq_fld, '==', '單次')
#
#             # 選取預約轉帳 驗證轉帳執行日
#             assertion.text(self.start_page.sd_date_col, '==', '轉帳執行日')
#
#             self.start_page.sd_date_fld.click()
#             self.start_page.date_picker.wait_present()
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_日期選擇器")
#             txn_date_now = datetime.now().date()
#             txn_sddate_ori = txn_date_now + timedelta(days=1)
#
#             TXN.SCHEDULED_DATE[K.ORI] = txn_sddate_ori
#             TXN.SCHEDULED_DATE[K.COM] = txn_sddate_ori.strftime(dt.DATE_COM)
#             TXN.SCHEDULED_DATE[K.YMZH] = txn_sddate_ori.strftime(dt.DATE_YMZH)
#             TXN.SCHEDULED_DATE[K.YYYY] = str(txn_sddate_ori.year)
#             TXN.SCHEDULED_DATE[K.M] = str(txn_sddate_ori.month)
#             TXN.SCHEDULED_DATE[K.MM] = TXN.SCHEDULED_DATE[K.M].zfill(2)
#             TXN.SCHEDULED_DATE[K.D] = str(txn_sddate_ori.day)
#             TXN.SCHEDULED_DATE[K.DD] = TXN.SCHEDULED_DATE[K.D].zfill(2)
#
#             self.start_page.select_datetime_done.click()
#
#             self.start_page.date_picker.wait_not_present()
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_日期選擇完畢")
#             assertion.attribute('value', self.start_page.sd_date_fld, '==', TXN.SCHEDULED_DATE[K.COM])
#             assertion.text(self.start_page.sd_date_remark, '==', '可預約次日起兩年內的轉帳交易。了解更多')
#
#         elif sdtype == 'weekly':
#             assertion.text(self.start_page.sd_freq_col, '==', '轉帳頻率')
#             self.start_page.sd_freq_fld.click()
#             self.cube.save_screenshot(self.case, "轉帳頻率彈窗")
#             self.start_page.sd_freq_weekly.click()
#             assertion.attribute('value', self.start_page.sd_freq_fld, '==', '每週')
#             self.cube.save_screenshot(self.case, "轉帳頻率每週")
#
#             # 驗證轉帳日
#             self.start_page.swipe_ratio('v', 90, 10)
#             assertion.text(self.start_page.sd_weekday_col, '==', '轉帳日(可複選)')
#             TXN.SCHEDULED_WEEKDAY[K.INDEX] = weekday
#             element_sd_weekday = self.start_page.sd_weekdays.find(weekday)
#             TXN.SCHEDULED_WEEKDAY[K.ZHCOM] = element_sd_weekday.text
#             element_sd_weekday.click()
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_隨機選擇轉帳日")
#
#             # 選取預約轉帳 驗證轉帳執行日 先限定到下個月28號
#             assertion.text(self.start_page.sd_date_col, '==', '轉帳執行日')
#             # self.txnpg.sd_date_fld.tap()
#             # if self.txnpg.date_picker.is_present(3):
#             #     logstack.info('此處已可用tap')
#             # 需特殊處理點擊位置
#             self.subtest.tap_tx_sd_weekly_date_field(self.start_page.sd_date_fld, self.start_page.date_picker)
#
#             self.start_page.date_picker.wait_present()
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_日期選擇器")
#
#             txn_date_now = datetime.now().date()
#             txn_sd_start_date_ori = txn_date_now + timedelta(days=1)
#             TXN.SCHEDULED_START_DATE[K.ORI] = txn_sd_start_date_ori
#             TXN.SCHEDULED_START_DATE[K.COM] = txn_sd_start_date_ori.strftime(dt.DATE_COM)
#             TXN.SCHEDULED_START_DATE[K.YMZH] = txn_sd_start_date_ori.strftime(dt.DATE_YMZH)
#             TXN.SCHEDULED_START_DATE[K.YYYY] = str(txn_sd_start_date_ori.year)
#             TXN.SCHEDULED_START_DATE[K.M] = str(txn_sd_start_date_ori.month)
#             TXN.SCHEDULED_START_DATE[K.MM] = TXN.SCHEDULED_START_DATE[K.M].zfill(2)
#             TXN.SCHEDULED_START_DATE[K.D] = str(txn_sd_start_date_ori.day)
#             TXN.SCHEDULED_START_DATE[K.DD] = TXN.SCHEDULED_START_DATE[K.D].zfill(2)
#
#             self.start_page.sd_picker_next_step_button.click()
#             self.start_page.sd_picker_next_month_button.click()  # TODO 這邊之後可以寫for來指定要幾個月後
#             self.start_page.scheduled_select_day('28').tap()  # simulator visible=False
#             # self.txnpg.sd_picker_select_day('28').click()
#
#             TXN.SCHEDULED_END_DATE[K.COM] = self.start_page.sd_picker_end_date.text
#             txn_sd_end_date_ori = datetime.strptime(TXN.SCHEDULED_END_DATE[K.COM], dt.DATE_COM)
#             TXN.SCHEDULED_END_DATE[K.ORI] = txn_sd_end_date_ori
#             TXN.SCHEDULED_END_DATE[K.YMZH] = txn_sd_end_date_ori.strftime(dt.DATE_YMZH)
#             TXN.SCHEDULED_END_DATE[K.YYYY] = str(txn_sd_end_date_ori.year)
#             TXN.SCHEDULED_END_DATE[K.M] = str(txn_sd_end_date_ori.month)
#             TXN.SCHEDULED_END_DATE[K.MM] = TXN.SCHEDULED_START_DATE[K.M].zfill(2)
#             TXN.SCHEDULED_END_DATE[K.D] = str(txn_sd_end_date_ori.day)
#             TXN.SCHEDULED_END_DATE[K.DD] = TXN.SCHEDULED_START_DATE[K.D].zfill(2)
#
#             self.start_page.sd_picker_done_button.click()
#
#             self.start_page.date_picker.wait_not_present()
#             self.cube.save_screenshot(self.case, "臺幣轉帳頁_日期選擇完畢")
#             TXN.SCHEDULED_PERIOD = f'{TXN.SCHEDULED_START_DATE[K.COM]} ~ {TXN.SCHEDULED_END_DATE[K.COM]}'
#             assertion.attribute('value', self.start_page.sd_date_fld, '==', TXN.SCHEDULED_PERIOD)
#             assertion.text(self.start_page.sd_date_remark, '==', '可預約次日起兩年內的轉帳交易。了解更多')
#
#         # 驗證備註
#         self.start_page.swipe_ratio('v', 90, 10)  # 滑動到最底部驗證備註
#         assertion.text(self.start_page.remark_column, '==', '備註')
#
#         TXN.REMARK[K.INPUT] = datetime.now().strftime(dt.DATETIME_RMK)
#
#         self.start_page.remark_field.send_keys(TXN.REMARK[K.INPUT])
#         time.sleep(3)
#         self.keyboard.done.click()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_驗證備註")
#         assertion.attribute('value', self.start_page.remark_field, '==', TXN.REMARK[K.INPUT])
#
#         # 驗證備註勾選框
#         assertion.present(self.start_page.remark_unselected)
#         assertion.not_present(self.start_page.remark_selected)
#         self.start_page.remark_unselected.click()
#         self.cube.save_screenshot(self.case, "臺幣轉帳頁_驗證備註同時顯示勾選框")
#         assertion.present(self.start_page.remark_selected)
#         assertion.not_present(self.start_page.remark_unselected)
#
#         if nextstep:
#             try:
#                 self.start_page.confirm_button.click()
#                 self.cube.wait_app_loading()
#                 self.cube.skip_popup(self.same_popup.same_txn_pp_ttl, self.same_popup.same_txn_pp_acc)
#                 logstack.info('🟢 TXN -> CNF')
#             except BaseException:
#                 logstack.error(f'🔴 FAILED: TXN -> CNF')
#         else:
#             logstack.info('🟡 STOPED: TXN')
#
#         logstack.info(f'⌛️ TXN_SD: 結束執行預約轉帳交易，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def test_confirm_scheduled(self, nextstep: bool = True, switch: bool = True):
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'⏳ CNF_SD: 開始執行預約轉帳確認，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。')
#
#         self.cube.wait_app_loading()
#         self.cube.save_screenshot(self.case, "臺幣轉帳資訊確認頁_轉帳資訊確認")
#
#         assertion.text(self.confirm_page.title_, '==', '轉帳資訊確認')
#         assertion.text(self.confirm_page.sd_xfer_col, '==', '預約轉帳金額')
#         assertion.text(self.confirm_page.sd_xfer_wamount, '==', TXN.AMOUNT[K.AMS])
#
#         assertion.text(self.confirm_page.dst_account_col, '==', '轉入帳號')
#         TO.INFO[K.NM16] = f'{TO.NAME} {TO.ID16}'
#         assertion.text(self.confirm_page.dynamic_destination_account_info(TO.ID16), '==', TO.INFO[K.NM16])
#
#         assertion.text(self.confirm_page.src_account_col, '==', '轉出帳號')
#         FROM.INFO[K.NM16] = f'{FROM.NAME} {FROM.ID16}'
#         assertion.text(self.confirm_page.dynamic_source_account_info(FROM.ID16), '==', FROM.INFO[K.NM16])
#
#         assertion.text(self.confirm_page.txn_type_col, '==', '交易類型')
#         assertion.text(self.confirm_page.txn_type_sd, '==', '預約轉帳')
#
#         if TXN.SCHEDULED_TYPE == 'single':
#             assertion.text(self.confirm_page.sd_period_col, '==', '生效期間')
#             assertion.text(self.confirm_page.dynamic_scheduled_period_date(
#                 TXN.SCHEDULED_DATE[K.COM]), '==', TXN.SCHEDULED_DATE[K.COM])
#
#         elif TXN.SCHEDULED_TYPE == 'weekly':
#             assertion.text(self.confirm_page.sd_period_col, '==', '生效期間')
#             assertion.text(self.confirm_page.dynamic_scheduled_period_interval(
#                 TXN.SCHEDULED_PERIOD), '==', TXN.SCHEDULED_PERIOD)
#
#             assertion.text(self.confirm_page.sd_weekday_col, '==', '轉帳週期')
#             TXN.SCHEDULED_WEEKDAY[K.ZHPER] = f'每{TXN.SCHEDULED_WEEKDAY[K.ZHCOM]}'
#             assertion.text(self.confirm_page.dynamic_scheduled_weekday(
#                 TXN.SCHEDULED_WEEKDAY[K.ZHPER]), '==', TXN.SCHEDULED_WEEKDAY[K.ZHPER])
#
#         TXN.REMARK[K.INFO] = f'備註： {TXN.REMARK[K.INPUT]}'
#         assertion.text(self.confirm_page.txn_remark_info, '==', TXN.REMARK[K.INFO])
#
#         assertion.text(self.confirm_page.noti_avoid_scam, '==', '交易前請再次確認，避免詐騙犯罪產生。')
#
#         if nextstep:
#             try:
#                 self.confirm_page.cnf_sd_button.click()
#                 self.cube.wait_app_loading()
#                 logstack.info('🟢 CNF -> RES')
#
#                 # 轉帳資訊確認頁 確認轉帳彈窗
#                 self.confirm_page.pp_scrollview.wait_present()
#                 self.cube.save_screenshot(self.case, "臺幣轉帳資訊確認頁_確認轉帳彈窗")
#                 if TXN.SCHEDULED_TYPE == 'single':
#                     cnfpg_cnf_sd_pp_cnt = f'預約在 {TXN.SCHEDULED_DATE[K.COM]} 轉出 {TXN.AMOUNT[K.AMS]} 給\n {TO.INFO[K.NM16]}'
#                 elif TXN.SCHEDULED_TYPE == 'weekly':
#                     cnfpg_cnf_sd_pp_cnt = f'預約在{TXN.SCHEDULED_WEEKDAY[K.ZHPER]}轉出 {TXN.AMOUNT[K.AMS]} 給\n {TO.INFO[K.NM16]}\n從 {TXN.SCHEDULED_PERIOD}'
#                 assertion.text(self.confirm_page.cnf_sd_pp_cnt, '==', cnfpg_cnf_sd_pp_cnt)
#                 TXN.START_DATETIME = datetime.now().replace(microsecond=0)
#
#                 self.confirm_page.cnf_sd_pp_acc.click()
#             except BaseException:
#                 logstack.error('🔴 FAILED: CNF -> RES')
#         else:
#             logstack.warning('🟡 STOPED: CNF')
#
#         logstack.info(f'⌛️ CNF_SD: 結束執行預約轉帳確認，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def test_result_scheduled(self, nextstep: str = 'done', switch: bool = True):
#         """
#         :param nextstep: (done: 完成); (inqury: 查看預約交易); (stop: 不進行下一步)
#         """
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'⏳ RES_SD: 開始執行預約轉帳結果，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。')
#
#         # 轉帳結果頁
#         self.cube.wait_app_loading()
#         if self.result_page.rt_failed.is_present(3):
#             self.cube.save_screenshot(self.case, "❌ 交易失敗")
#             # assertion.condition(False, '❌ 交易失敗')
#             assert False, '❌ 交易失敗'
#         TXN.EXECUTE_DATETIME[K.COM] = self.result_page.txn_datetime_com.text
#         TXN.END_DATETIME = datetime.now().replace(microsecond=0) + timedelta(seconds=30)
#         TXN.EXECUTE_DATETIME[K.ORI] = dt.str_to_datetime(TXN.EXECUTE_DATETIME[K.COM])
#         self.cube.save_screenshot(self.case, "臺幣轉帳轉帳結果頁_轉帳結果確認", 3)
#         # self.check_if_scheduled_result_is_failed()
#
#         assertion.text(self.result_page.title_, '==', '轉帳結果')
#         assertion.text(self.result_page.sd_successful, '==', '預約成功')
#         assertion.datetime_in_range(TXN.START_DATETIME, TXN.EXECUTE_DATETIME[K.ORI], TXN.END_DATETIME)
#
#         assertion.text(self.result_page.sd_xfer_col, '==', '預約轉帳金額')
#         assertion.text(self.result_page.sd_xfer_wamount, '==', TXN.AMOUNT[K.AMS])
#
#         assertion.text(self.result_page.dst_account_col, '==', '轉入帳號')
#         assertion.text(self.result_page.dynamic_destination_account_info(TO.ID16), '==', TO.INFO[K.NM16])
#
#         assertion.text(self.result_page.src_account_col, '==', '轉出帳號')
#         assertion.text(self.result_page.dynamic_source_account_info(FROM.ID16), '==', FROM.INFO[K.NM16])
#
#         if TXN.SCHEDULED_TYPE == 'single':
#             assertion.text(self.result_page.sd_period_col, '==', '生效期間')
#             assertion.text(self.result_page.dynamic_scheduled_period_date(
#                 TXN.SCHEDULED_DATE[K.COM]), '==', TXN.SCHEDULED_DATE[K.COM])
#         elif TXN.SCHEDULED_TYPE == 'weekly':
#             assertion.text(self.result_page.sd_period_col, '==', '生效期間')
#             assertion.text(self.result_page.dynamic_scheduled_period_interval(
#                 TXN.SCHEDULED_PERIOD), '==', TXN.SCHEDULED_PERIOD)
#
#             assertion.text(self.confirm_page.sd_weekday_col, '==', '轉帳週期')
#             assertion.text(self.confirm_page.dynamic_scheduled_weekday(
#                 TXN.SCHEDULED_WEEKDAY[K.ZHPER]), '==', TXN.SCHEDULED_WEEKDAY[K.ZHPER])
#
#         assertion.text(self.result_page.txn_remark_info, '==', TXN.REMARK[K.INFO])
#
#         if nextstep == 'done':
#             try:
#                 self.result_page.done_button.click()
#                 self.cube.wait_app_loading()
#                 logstack.info(f'🟢 RES -> HOME')
#                 self.skip_noti_and_rating_popups()
#             except BaseException:
#                 logstack.error(f'🔴 FAILED: RES -> HOME')
#         elif nextstep == 'inqury':
#             try:
#                 self.result_page.sd_inqury_button.click()
#                 self.cube.wait_app_loading()
#                 logstack.info(f'🟢 RES -> INQURY')
#                 self.skip_noti_and_rating_popups()
#             except BaseException:
#                 logstack.error(f'🔴 FAILED: RES -> INQURY')
#         else:
#             logstack.warning('🟡 STOPED: RES')
#
#         logstack.info(f'⌛️ RES_SD: 結束執行預約轉帳結果，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def test_after_scheduled(self, target: str = 'done', switch: bool = True):
#         """
#         bf: home acnt src dst
#         """
#
#         assertion.SWITCH = switch
#
#         logstack.info(f'⏳ AF_SD: 開始驗證預約轉帳後資訊，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。')
#
#         if target == 'done':
#             # 回到首頁 檢查總額應不變
#             self.cube.wait_app_loading()
#             self.home_page.deposit_twd_amount.wait_visible()
#             self.home_page.save_screenshot(self.case, '回到首頁')
#             FROM.AFTER_TOTAL_AMOUNT[K.AMT] = self.home_page.deposit_twd_amount.text
#             assertion.ae(FROM.AFTER_TOTAL_AMOUNT[K.AMT], '==', FROM.BEFORE_TOTAL_AMOUNT[K.AMT])
#             self.home_page.deposit_twd_amount.click()
#
#             # 存款頁 檢查相關金額皆無變動
#             self.deposit_page.all_amounts.wait_all_present()
#             self.cube.save_screenshot(self.case, '確認臺幣分頁金額皆無變動')
#             assertion.text(self.deposit_page.total_available_balance_amount,
#                            '==', FROM.AFTER_TOTAL_AMOUNT[K.AMT])
#             assertion.text(self.deposit_page.total_account_balance_amount, '==',
#                            FROM.BEFORE_TOTAL_ACCOUNT_BALANCE[K.AMT])
#             border = self.cube.get_table_border(True)
#             self.deposit_page.demand_account_amount(FROM.ID12).swipe_into_view(SA.VA, border)
#             assertion.text(self.deposit_page.demand_account_amount(FROM.ID12),
#                            '==', FROM.BEFORE_ACCOUNT_BALANCE[K.AMT])
#             self.deposit_page.demand_account_amount(TO.ID12).swipe_into_view(SA.VA, border)
#             assertion.text(self.deposit_page.demand_account_amount(TO.ID12),
#                            '==', TO.BEFORE_ACCOUNT_BALANCE[K.AMT])
#             self.bottom.more.click()
#
#             # 更多功能頁
#             self.more_page.finance.wait_visible()
#             self.more_page.save_screenshot(self.case, "完成預約轉帳_更多功能頁面")
#             self.more_page.finance_twd.click()
#             self.more_page.fin_twd_sd_qry.wait_present()
#             self.more_page.save_screenshot(self.case, "完成預約轉帳_臺外幣子列表")
#             self.more_page.fin_twd_sd_qry.click()
#
#         if TXN.SCHEDULED_TYPE == 'single':
#             # 預約轉帳查詢頁面
#             self.cube.wait_app_loading()
#             self.inquiry_main_page.title_.wait_present()
#             assertion.text(self.inquiry_main_page.title_, '==', '預約轉帳查詢')
#             assertion.attribute('value', self.inquiry_main_page.progressing_tab, '==', '1')
#             # self.operation.vscroll_to_element(self.sdqrypg.date(TXN.SDDATE[K.YMZH]))
#             # assertion.text(self.sdqrypg.date(TXN.SDDATE[K.YMZH]), '==', TXN.SDDATE[K.YMZH])
#
#             # 預約轉帳查詢頁面 識別時間備註
#             remark_fw = common.half_to_full(TXN.REMARK[K.INPUT])
#             logstack.info(f'藉由全形remark開始尋找: {remark_fw}')
#             border = self.cube.get_table_border()
#             self.inquiry_main_page.remark(remark_fw).swipe_into_view(SA.VA, border)
#             self.inquiry_main_page.save_screenshot(self.case, '滑動到指定預轉資訊')
#
#             remark = self.inquiry_main_page.remark(remark_fw).text
#             amount = self.inquiry_main_page.amount(remark_fw).text
#             payee_name = self.inquiry_main_page.payee_name(remark_fw, TO.NAME).text
#             freq_single = self.inquiry_main_page.frequency_single(remark_fw).text
#             nextdate_com = self.inquiry_main_page.next_date_slash(remark_fw, TXN.SCHEDULED_DATE[K.COM]).text
#
#             assertion.ae(remark, '==', remark_fw)
#             assertion.ae(amount, '==', TXN.AMOUNT[K.AMT])
#             # assertion.text(self.sdqrypg.payee_col(remark_fw), '==', '收款人')
#             assertion.ae(payee_name, '==', TO.NAME)
#             # assertion.text(self.sdqrypg.freq_col(remark_fw), '==', '轉帳頻率/剩餘次數')
#             assertion.ae(freq_single, '==', '單次/1 次')
#             # assertion.text(self.sdqrypg.nextdate_col(remark_fw), '==', '下次轉帳日')
#             assertion.ae(nextdate_com, '==', TXN.SCHEDULED_DATE[K.COM])
#
#             # TODO 詳細明細 和 取消預約
#             # 進入到詳細頁面
#             self.inquiry_main_page.remark(remark_fw).click()
#             self.inquiry_details_page.title_.wait_visible()
#             self.inquiry_details_page.save_screenshot(self.case, "預約轉帳明細")
#
#             expect_src_account_info = f'{FROM.NAME} {FROM.BANK[K.RB]} {FROM.ID16}'
#             expect_dst_account_info = f'{TO.NAME} {TO.BANK[K.RBZH]} {TO.ID16}'
#
#             assertion.text(self.inquiry_details_page.remark(remark_fw), '==', remark_fw)
#             assertion.text(self.inquiry_details_page.amount(amount), '==', amount)
#             assertion.text(self.inquiry_details_page.progressiing, '==', '進行中')
#             assertion.text(self.inquiry_details_page.source_account_info(FROM.ID16), '==', expect_src_account_info)
#             assertion.text(self.inquiry_details_page.destination_account_info(TO.ID16), '==', expect_dst_account_info)
#             assertion.text(self.inquiry_details_page.freq_single, '==', '單次')
#             assertion.text(self.inquiry_details_page.remain_times, '==', '1 次/共 1 次')
#             assertion.text(self.inquiry_details_page.next_date(nextdate_com), '==', nextdate_com)
#
#         elif TXN.SCHEDULED_TYPE == 'weekly':
#             # 預約轉帳查詢頁面
#             self.cube.wait_app_loading()
#             self.inquiry_main_page.title_.wait_present()
#             assertion.text(self.inquiry_main_page.title_, '==', '預約轉帳查詢')
#             assertion.attribute('value', self.inquiry_main_page.progressing_tab, '==', '1')
#             # self.operation.vscroll_to_element(self.sdqrypg.date(TXN.SDSTRDATE[K.YMZH]))
#             # assertion.text(self.sdqrypg.date(TXN.SDSTRDATE[K.YMZH]), '==', TXN.SDSTRDATE[K.YMZH])
#
#             # 預約轉帳查詢頁面 識別時間備註
#             remark_fw = common.half_to_full(TXN.REMARK[K.INPUT])
#             border = self.cube.get_table_border()
#             self.inquiry_main_page.remark(remark_fw).swipe_into_view(SA.VA, border)
#             self.inquiry_main_page.save_screenshot(self.case, '滑動到指定預轉資訊')
#
#             # 計算剩餘次數
#             TXN.SCHEDULED_WEEKDAY[K.ZHSPC] = TXN.SCHEDULED_WEEKDAY[K.ZHPER][:2] + \
#                 ' ' + TXN.SCHEDULED_WEEKDAY[K.ZHPER][2:]
#             start_date = datetime.strptime(TXN.SCHEDULED_START_DATE[K.COM], dt.DATE_COM).date()
#             end_date = datetime.strptime(TXN.SCHEDULED_END_DATE[K.COM], dt.DATE_COM).date()
#             qry_freq_times = dt.count_of_weekdays(TXN.SCHEDULED_WEEKDAY[K.INDEX], start_date, end_date)
#             qry_freq_info = f'{TXN.SCHEDULED_WEEKDAY[K.ZHSPC]}/{qry_freq_times} 次'
#
#             # 計算下次轉帳日
#             nextdate_ori = dt.next_weekday_date(start_date, TXN.SCHEDULED_WEEKDAY[K.INDEX])
#             expect_nextdate_com = nextdate_ori.strftime(dt.DATE_COM)
#             expect_date_ymzh = nextdate_ori.strftime(dt.DATE_YMZH)
#
#             remark = self.inquiry_main_page.remark(remark_fw).text
#             amount = self.inquiry_main_page.amount(remark_fw).text
#             payee_name = self.inquiry_main_page.payee_name(remark_fw, TO.NAME).text
#             freq_weekly = self.inquiry_main_page.frequency_weekly(remark_fw).text
#             actual_nextdate_com = self.inquiry_main_page.next_date_slash(remark_fw, expect_nextdate_com).text
#
#             assertion.text(self.inquiry_main_page.date(expect_date_ymzh), '==', expect_date_ymzh)
#
#             assertion.ae(remark, '==', remark_fw)
#             assertion.ae(amount, '==', TXN.AMOUNT[K.AMT])
#             # assertion.text(self.sdqrypg.payee_col(remark_fw), '==', '收款人')
#             assertion.ae(payee_name, '==', TO.NAME)
#             # assertion.text(self.sdqrypg.freq_col(remark_fw), '==', '轉帳頻率/剩餘次數')
#             assertion.ae(freq_weekly, '==', qry_freq_info)
#             # assertion.text(self.sdqrypg.nextdate_col(remark_fw), '==', '下次轉帳日')
#             assertion.ae(actual_nextdate_com, '==', expect_nextdate_com)
#
#             # 進入到詳細頁面
#             self.inquiry_main_page.remark(remark_fw).click()
#             self.inquiry_details_page.title_.wait_visible()
#             self.inquiry_details_page.save_screenshot(self.case, "預約轉帳明細")
#
#             expect_src_account_info = f'{FROM.NAME} {FROM.BANK[K.RB]} {FROM.ID16}'
#             expect_dst_account_info = f'{TO.NAME} {TO.BANK[K.RBZH]} {TO.ID16}'
#             expect_remain_times_info = f'{qry_freq_times} 次/共 {qry_freq_times} 次'
#
#             assertion.text(self.inquiry_details_page.remark(remark_fw), '==', remark_fw)
#             assertion.text(self.inquiry_details_page.amount(amount), '==', amount)
#             assertion.text(self.inquiry_details_page.progressiing, '==', '進行中')
#             assertion.text(self.inquiry_details_page.source_account_info(FROM.ID16), '==', expect_src_account_info)
#             assertion.text(self.inquiry_details_page.destination_account_info(TO.ID16), '==', expect_dst_account_info)
#             assertion.text(self.inquiry_details_page.period(TXN.SCHEDULED_PERIOD), '==', TXN.SCHEDULED_PERIOD)
#             assertion.text(self.inquiry_details_page.freq_weekly, '==', TXN.SCHEDULED_WEEKDAY[K.ZHSPC])
#             assertion.text(self.inquiry_details_page.remain_times, '==', expect_remain_times_info)
#             assertion.text(self.inquiry_details_page.next_date(actual_nextdate_com), '==', actual_nextdate_com)
#
#         self.inquiry_details_page.cancel_button.click()
#         self.inquiry_details_page.cancel_popup_title.wait_visible()
#         self.inquiry_details_page.save_screenshot(self.case, "取消本筆預約轉帳彈窗")
#         self.inquiry_details_page.cancel_popup_confirm.click()
#         self.cube.wait_app_loading()
#         self.inquiry_details_page.save_screenshot(self.case, "取消後資訊")
#         assertion.present(self.inquiry_details_page.canceled)
#
#         logstack.info(f'⌛️ AF_SD: 結束驗證預約轉帳後資訊，交易類型是 {TXN.TYPE} ，預約轉帳類型是 {TXN.SCHEDULED_TYPE} 。\n')
#
#         assertion.SWITCH = True
#
#     def skip_noti_and_rating_popups(self, timeout=1):
#         """
#         略過結果頁面後的推播通知與評分彈窗
#         """
#         while self.noti_popup.common_text.is_present(timeout):
#             common_text = self.noti_popup.common_text.text
#             if '推播通知' in common_text:
#                 logstack.info('🟢 出現 推播通知 彈窗')
#                 self.noti_popup.dismiss.click()
#             elif '喜歡這次的服務嗎' in common_text:
#                 logstack.info('🟢 出現 喜歡這次的服務嗎 彈窗')
#                 self.rating_popup.dismiss.click()
#             else:
#                 logstack.error('❌ 無對應文本，請再次確認')
#             self.cube.wait_app_loading()
