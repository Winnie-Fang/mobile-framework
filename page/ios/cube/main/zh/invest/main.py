# from huskypo import By, Element, Elements, dynamic
# # from huskypo_extension import Page
#
# from appium.webdriver.common.appiumby import AppiumBy
#
# from module.mobile.component.base_object import BaseObject
# from module.mobile.component.basic_component import BasicComponent
# from module.mobile.component.basic_components import BasicComponents
# from module.mobile.device_manager import DeviceManager
#
#
# class InvestMainPage(BaseObject):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("投資總覽頁")
#         self.driver = DeviceManager.get_driver()
#
#     def prerequisites(self) -> None:
#         self.pv_column.assert_visible()
#
#     # def waitings(self, timeout: int = 60):
#     #     waits = []
#     #     waits.append(self.pv_total_amount.wait_present(timeout, False))
#     #     waits.append(self.fund_waiting.wait_present(timeout, False))
#     #     return waits
#
#     @property
#     def fund_waiting(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'name IN {"顯示我的專屬基金推薦", "參考現值(TWD)"}'
#             ),
#             remark=f'{self.remark()} > 基金等待元素'
#         )
#
#     @property
#     def title_(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label == "投資總覽"'
#             ),
#             remark=f'{self.remark()} > 標題'
#         )
#
#     @property
#     def pv_column(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '參考總現值(TWD)'
#             ),
#             remark=f'{self.remark()} > 參考總現值TWD欄位'
#         )
#
#     @property
#     def pv_expand_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'ic expand'
#             ),
#             remark=f'{self.remark()} > 參考總現值TWD展開鈕'
#         )
#
#     @property
#     def pv_compress_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'ic compress'
#             ),
#             remark=f'{self.remark()} > 參考總現值TWD收合鈕'
#         )
#
#     @property
#     def pv_total_amount(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'//XCUIElementTypeStaticText[@name="參考總現值(TWD)"]/../XCUIElementTypeStaticText[starts-with(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 參考總現值TWD金額'
#         )
#
#     @property
#     def pv_total_roi(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'//XCUIElementTypeStaticText[@name="參考總現值(TWD)"]/../XCUIElementTypeStaticText[contains(@name, "%")]'
#             ),
#             remark=f'{self.remark()} > 參考總現值TWD投資報酬率'
#         )
#
#     @property
#     def kyc_info_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label BEGINSWITH "風險屬性"'
#             ),
#             remark=f'{self.remark()} > 風險屬性資訊按鈕'
#         )
#
#     pv_type_list = ['基金', '智能投資', '證券', '國外ETF', '債券', '結構型商品']
#
#     @property
#     def pv_type_common(self, i: int = 1):
#         # ios_class_chain位置要平移3個
#         i += 3
#         predicate = 'label IN {"基金", "智能投資", "證券", "國外ETF", "債券", "結構型商品"}'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 f'**/XCUIElementTypeStaticText[`{predicate}`][{i}]'
#             ),
#             remark=f'{self.remark()} > 投資圓餅圖共用類別'
#         )
#
#     @property
#     def pv_ratio_common(self, pv_type: str):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'(//XCUIElementTypeStaticText[@name="{pv_type}"])[1]/following-sibling::XCUIElementTypeStaticText[contains(@name, "%")]'
#             ),
#             remark=f'{self.remark()} > {pv_type}百分比'
#         )
#
#     @property
#     def pv_pie_chart(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Pie Chart. 6 Elements'),
#             remark=f'{self.remark()} > 圓餅圖'
#         )
#
#     @property
#     def pv_pie_ratios(self):
#         return BasicComponents(
#             lambda: self.driver.find_elements(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeOther[@name="Pie Chart. 6 Elements"]/following-sibling::XCUIElementTypeOther'
#             ),
#             remark=f'{self.remark()} > 圓餅圖全比例資訊'
#         )
#
#     @property
#     def pv_total_principal_column(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '總本金(TWD)'),
#             remark=f'{self.remark()} > 總本金TWD欄位'
#         )
#
#     @property
#     def pv_total_principal_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "i"`][1]'
#             ),
#             remark=f'{self.remark()} > 總本金TWD備註按鈕'
#         )
#
#     @property
#     def pv_total_principal_amount(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label BEGINSWITH "$"`][2]'
#             ),
#             remark=f'{self.remark()} > 總本金TWD金額'
#         )
#
#     @property
#     def pv_total_reward_column(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '不含息參考報酬(TWD)'),
#             remark=f'{self.remark()} > 不含息參考報酬TWD欄位'
#         )
#
#     @property
#     def pv_total_reward_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "i"`][2]'
#             ),
#             remark=f'{self.remark()} > 不含息參考報酬TWD備註按鈕'
#         )
#
#     @property
#     def pv_total_reward_amount(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label CONTAINS "$"`][3]'
#             ),
#             remark=f'{self.remark()} > 不含息參考報酬TWD金額'
#         )
#
#     @property
#     def sign_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label ENDSWITH "立即簽署"'),
#             remark=f'{self.remark()} > 首次申購立即簽署訊息'
#         )
#
#     @property
#     def fund_tab_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "基金"`][1]'
#             ),
#             remark=f'{self.remark()} > 基金分頁鈕'
#         )
#
#     @property
#     def robo_tab_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "智能投資"`][1]'
#             ),
#             remark=f'{self.remark()} > 智能投資分頁鈕'
#         )
#
#     @property
#     def secs_tab_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "證券"`][1]'
#             ),
#             remark=f'{self.remark()} > 證券分頁鈕'
#         )
#
#     @property
#     def other_tab_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '其他商品'),
#             remark=f'{self.remark()} > 其他商品分頁鈕'
#         )
#
#     @property
#     def my_rcmd_fund_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
#                                              '**/XCUIElementTypeButton[`label == "我的推薦基金"`]'),
#             remark=f'{self.remark()} > 我的推薦基金按鈕'
#         )
#
#     @property
#     def tsec_account_tab(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '台股帳戶'),
#             remark=f'{self.remark()} > 台股帳戶'
#         )
#
#     @property
#     def asec_account_tab(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '複委託帳戶'),
#             remark=f'{self.remark()} > 複委託帳戶'
#         )
#
#
# class KYCInfoPage(Page):
#     page = '我的投資屬性頁'
#
#     title_ = Element(By.ACCESSIBILITY_ID, '我的投資屬性', remark=f'{page}_標題')
#     back_button = Element(By.ACCESSIBILITY_ID, 'btn arrowleft n', remark=f'{page}_上一頁按鈕')
#
#     risk_column = Element(By.ACCESSIBILITY_ID, '風險承受度', remark=f'{page}_風險承受度欄位')
#     risk_type = Element(By.XPATH,
#                         '//XCUIElementTypeStaticText[@name="風險承受度"]/../XCUIElementTypeStaticText[last()]')
#     due_info = Element(By.IOS_PREDICATE, 'label ENDSWITH "前有效"', remark=f'{page}_至YYYY/MM/DD前有效')
#     reanalyze_button = Element(
#         By.IOS_CLASS_CHAIN,
#         '**/XCUIElementTypeButton[`label == "重新分析"`]',
#         remark=f'{page}_重新分析按鈕')
#
#
# class KYCReanalyzeLimitErrorPage(Page):
#     # error_image = Element(By.ACCESSIBILITY_ID, 'img_cube_system_unexpectederror')
#     error_message = Element(By.IOS_PREDICATE,
#                             'name CONTAINS "投資屬性分析次數已達本日上限" AND name CONTAINS "IB-9999"')
#     back_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "返回"`]', remark='返回按鈕')
#
#
# class KYCAnalyzePage(Page):
#     page = '投資屬性分析頁'
#
#     next_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "下一步"`]')
#
#     title_ = Element(By.ACCESSIBILITY_ID, '投資屬性分析')
#     back_button = Element(By.ACCESSIBILITY_ID, 'btn arrowleft n', remark=f'{page}_上一頁按鈕')
#
#     step1_info = Element(By.ACCESSIBILITY_ID, '1 / 4')
#     step2_info = Element(By.ACCESSIBILITY_ID, '2 / 4')
#     step3_info = Element(By.ACCESSIBILITY_ID, '3 / 4')
#     step4_info = Element(By.ACCESSIBILITY_ID, '4 / 4')
#
#     reanalyze_factor = Element(By.IOS_PREDICATE, 'label BEGINSWITH "B.財務狀況異動"')
#
#     next_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "下一步"`]')
#
#     confirm_email_check = Element(
#         By.XPATH, '//XCUIElementTypeStaticText[@name="基本資料"]/following::XCUIElementTypeButton[1]')
#
#     edu_phd = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name == "E.博士"`]')
#
#     medical_none = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name == "B.否"`]')
#
#     finance_salary = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name == "A.薪資所得"`]')
#     finance_investment = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "C.投資所得"`]')
#     finance_else = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name == "H.其他"`]')
#
#     period_over_7_years = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.7年"`]')
#
#     funds_abundant = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.我還有"`]')
#
#     annual_over_110 = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.110"`]')
#
#     status_far_exceed = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.大幅超過"`]')
#
#     knowledge_extensive = Element(By.IOS_CLASS_CHAIN,
#                                   '**/XCUIElementTypeTextView[`name BEGINSWITH "E.對一般的金融商品"`]')
#
#     investment_extensive = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.我在金融商品"`]')
#
#     investment_purpose = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.以最高回報為主"`]')
#
#     risk_over_25_percent = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.上下幅度超過"`]')
#
#     loss_decision = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`name BEGINSWITH "E.把握獲利機會"`]')
#
#
# class KYCBeforeResultPage(Page):
#     title_ = Element(By.IOS_PREDICATE, 'name == "投資屬性分析"')
#     back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black')
#
#     a1_fld = Element(By.XPATH, '//XCUIElementTypeStaticText[starts-with(@name, "Q1")]/../XCUIElementTypeTextField')
#
#     a2_7 = Element(By.ACCESSIBILITY_ID, '7')
#     a2_5 = Element(By.ACCESSIBILITY_ID, '5')
#
#     a3_agree = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "同意"`][1]')
#     a3_disagree = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "不同意"`][1]')
#
#     a4_agree = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "同意"`][2]')
#     a4_disagree = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "不同意"`][2]')
#
#     a5_agree = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "同意"`][3]')
#     a5_disagree = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "不同意"`][3]')
#
#     send_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "送出"`]')
#
#
# class KYCAfterResultPage(Page):
#     title_ = Element(By.ACCESSIBILITY_ID, '我的投資屬性分析')
#
#     risk_type = Element(By.XPATH,
#                         '//XCUIElementTypeStaticText[@name="風險承受度"]/../XCUIElementTypeStaticText[last()]')
#
#     done_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "完成"`]')
