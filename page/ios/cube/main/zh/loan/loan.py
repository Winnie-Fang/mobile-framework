# from huskypo import Page, Element, Elements, By
# from huskypo_extension import Page
#
# from appium.webdriver.common.appiumby import AppiumBy
#
# from module.mobile.component.base_object import BaseObject
# from module.mobile.component.basic_component import BasicComponent
# from module.mobile.component.basic_components import BasicComponents
# from module.mobile.device_manager import DeviceManager
# from page.ios.cube.main.zh.common.loading_v2 import Loading
#
#
# class LoanMainPage(BaseObject):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("貸款頁")
#         self.driver = DeviceManager.get_driver()
#
#     def prerequisites(self) -> None:
#         self.home_tab.assert_visible()
#
#     @property
#     def title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "貸款"`]'
#             ),
#             remark=f'{self.remark()} > 標題'
#         )
#
#     @property
#     def wait_amounts(self):
#         return BasicComponents(
#             lambda: self.driver.find_elements(
#                 AppiumBy.IOS_PREDICATE,
#                 'name CONTAINS "$"'
#             ),
#             remark=f'{self.remark()} > 等待金額'
#         )
#
#     @property
#     def credit_tab(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '信用貸款'
#             ),
#             remark=f'{self.remark()} > 信用貸款分頁鈕'
#         )
#
#     @property
#     def home_tab(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '房屋貸款'
#             ),
#             remark=f'{self.remark()} > 房屋貸款分頁鈕'
#         )
#
#     @property
#     def insurance_tab(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '保單借款'
#             ),
#             remark=f'{self.remark()} > 保單借款分頁鈕'
#         )
#
#     @property
#     def unstable_warning_text(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'name CONTAINS "系統不穩定"'
#             ),
#             remark=f'{self.remark()} > 系統不穩定文本'
#         )
#
#     @property
#     def credit_individual_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`name == "專人信貸諮詢"`]'
#             ),
#             remark=f'{self.remark()} > 專人信貸諮詢按鈕'
#         )
#
#     @property
#     def credit_online_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "線上申貸"`]'
#             ),
#             remark=f'{self.remark()} > 線上申貸按鈕'
#         )
#
#     @property
#     def my_credit_individual_text(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '專人信貸諮詢'
#             ),
#             remark=f'{self.remark()} > 專人信貸諮詢文本'
#         )
#
#     @property
#     def my_credit_individual_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`name == "免費預約"`]'
#             ),
#             remark=f'{self.remark()} > 免費預約按鈕'
#         )
#
#     @property
#     def credit_more_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '更多精選方案'
#             ),
#             remark=f'{self.remark()} > 更多精選方案按鈕'
#         )
#
#     @property
#     def home_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '貸您幸福成家'
#             ),
#             remark=f'{self.remark()} > 房貸標題'
#         )
#
#     @property
#     def home_more_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '更多精選方案'
#             ),
#             remark=f'{self.remark()} > 更多精選方案按鈕'
#         )
#
#     @property
#     def home_online_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label CONTAINS "線上填表"`]'
#             ),
#             remark=f'{self.remark()} > 線上填表按鈕'
#         )
#
#     @property
#     def my_credit_loan(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label == "我的貸款"'
#             ),
#             remark=f'{self.remark()} > 我的貸款'
#         )
#
#     @property
#     def my_credit1_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "信用貸款"`][2]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_標題'
#         )
#
#     @property
#     def my_credit1_arrow_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "icArrowrightCubeBlue"`][1]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_右箭鈕'
#         )
#
#     @property
#     def my_credit1_due_col(self):
#         xpath_my_credit1_cell = '(//XCUIElementTypeStaticText[@name="信用貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_credit1_cell}/XCUIElementTypeStaticText[@name="本期還款金額"]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_本期還款金額欄位'
#         )
#
#     @property
#     def my_credit1_due_amt(self):
#         xpath_my_credit1_cell = '(//XCUIElementTypeStaticText[@name="信用貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_credit1_cell}/XCUIElementTypeStaticText[starts-with(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_本期還款金額值'
#         )
#
#     @property
#     def my_credit1_debit_date_col(self):
#         xpath_my_credit1_cell = '(//XCUIElementTypeStaticText[@name="信用貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_credit1_cell}/XCUIElementTypeStaticText[@name="扣款日"]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_扣款日欄位'
#         )
#
#     @property
#     def my_credit1_debit_date_com(self):
#         xpath_my_credit1_cell = '(//XCUIElementTypeStaticText[@name="信用貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_credit1_cell}/XCUIElementTypeStaticText[contains(@name, "/")]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_扣款日日期'
#         )
#
#     @property
#     def my_credit1_term_col(self):
#         xpath_my_credit1_cell = '(//XCUIElementTypeStaticText[@name="信用貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_credit1_cell}/XCUIElementTypeStaticText[@name="期數"]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_期數欄位'
#         )
#
#     @property
#     def my_credit1_term_info(self):
#         xpath_my_credit1_cell = '(//XCUIElementTypeStaticText[@name="信用貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_credit1_cell}/XCUIElementTypeStaticText[starts-with(@name, "已繳")]'
#             ),
#             remark=f'{self.remark()} > 信貸資訊1_期數資訊'
#         )
#
#     @property
#     def my_credit_last_cell(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeTable/XCUIElementTypeCell[-3]'
#             ),
#             remark=f'{self.remark()} > 最後一筆貸款cell'
#         )
#
#     # 房屋貸款
#     @property
#     def my_home_loan(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label == "我的貸款"'
#             ),
#             remark=f'{self.remark()} > 我的貸款'
#         )
#
#     @property
#     def my_home_learn_more_text(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label BEGINSWITH "想了解更多"'
#             ),
#             remark=f'{self.remark()} > 想了解更多文本'
#         )
#
#     @property
#     def my_home_learn_more_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '更多精選方案'
#             ),
#             remark=f'{self.remark()} > 想了解更多_更多精選方案按鈕'
#         )
#
#     @property
#     def my_home1_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "房屋貸款"`][2]'
#             ),
#             remark=f'{self.remark()} > 房貸1_標題'
#         )
#
#     @property
#     def my_home1_arrow_button(self):
#         xpath_my_home1_cell = '(//XCUIElementTypeStaticText[@name="房屋貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_home1_cell}/XCUIElementTypeButton[@name="icArrowrightCubeBlue"]'
#             ),
#             remark=f'{self.remark()} > 房貸1_右箭鈕'
#         )
#
#     @property
#     def my_home1_due_col(self):
#         xpath_my_home1_cell = '(//XCUIElementTypeStaticText[@name="房屋貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_home1_cell}/XCUIElementTypeStaticText[@name="本期還款金額"]'
#             ),
#             remark=f'{self.remark()} > 房貸1_本期還款金額欄位'
#         )
#
#     @property
#     def my_home1_due_amt(self):
#         xpath_my_home1_cell = '(//XCUIElementTypeStaticText[@name="房屋貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_home1_cell}/XCUIElementTypeStaticText[starts-with(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 房貸1_本期還款金額總額'
#         )
#
#     @property
#     def my_home1_debit_date_col(self):
#         xpath_my_home1_cell = '(//XCUIElementTypeStaticText[@name="房屋貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_home1_cell}/XCUIElementTypeStaticText[@name="扣款日"]'
#             ),
#             remark=f'{self.remark()} > 房貸1_扣款日欄位'
#         )
#
#     @property
#     def my_home1_debit_date_com(self):
#         xpath_my_home1_cell = '(//XCUIElementTypeStaticText[@name="房屋貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_home1_cell}/XCUIElementTypeStaticText[contains(@name, "/")]'
#             ),
#             remark=f'{self.remark()} > 房貸1_扣款日日期'
#         )
#
#     @property
#     def my_home1_term_col(self):
#         xpath_my_home1_cell = '(//XCUIElementTypeStaticText[@name="房屋貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_home1_cell}/XCUIElementTypeStaticText[@name="期數"]'
#             ),
#             remark=f'{self.remark()} > 房貸1_期數欄位'
#         )
#
#     @property
#     def my_home1_term_info(self):
#         xpath_my_home1_cell = '(//XCUIElementTypeStaticText[@name="房屋貸款"])[2]/..'
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 f'{xpath_my_home1_cell}/XCUIElementTypeStaticText[starts-with(@name, "已繳")]'
#             ),
#             remark=f'{self.remark()} > 房貸1_期數資訊'
#         )
#
#     @property
#     def elas_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label == "個人專屬方案"'
#             ),
#             remark=f'{self.remark()} > 彈力貸_個人專屬方案'
#         )
#
#     @property
#     def elas_type_backup(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '彈性備用'
#             ),
#             remark=f'{self.remark()} > 彈力貸_彈性備用'
#         )
#
#     @property
#     def elas_type_backup_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '彈力貸月繳息'
#             ),
#             remark=f'{self.remark()} > 彈力貸月繳息'
#         )
#
#     @property
#     def elas_type_backup_quota_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "初步推估額度"`][1]'
#             ),
#             remark=f'{self.remark()} > 初步推估額度'
#         )
#
#     @property
#     def elas_type_backup_quota_rmk(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '額度回彈'
#             ),
#             remark=f'{self.remark()} > 額度回彈'
#         )
#
#     @property
#     def elas_type_backup_quota_2m(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '$2,000,000'
#             ),
#             remark=f'{self.remark()} > 額度200萬'
#         )
#
#     @property
#     def elas_type_backup_ir_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "貸款利率"`][1]'
#             ),
#             remark=f'{self.remark()} > 貸款利率'
#         )
#
#     @property
#     def elas_type_backup_ir_rate(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label ENDSWITH "%"`][1]'
#             ),
#             remark=f'{self.remark()} > 貸款利率值'
#         )
#
#     @property
#     def elas_type_backup_term_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "貸款期數"`][1]'
#             ),
#             remark=f'{self.remark()} > 貸款期數'
#         )
#
#     @property
#     def elas_type_backup_term_12(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '12 期'
#             ),
#             remark=f'{self.remark()} > 12期'
#         )
#
#     @property
#     def elas_type_backup_term_free(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '(不綁約)'
#             ),
#             remark=f'{self.remark()} > (不綁約)'
#         )
#
#     @property
#     def elas_type_backup_mgmt_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "帳管費"`][1]'
#             ),
#             remark=f'{self.remark()} > 帳管費'
#         )
#
#     @property
#     def elas_type_backup_mgmt_free(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '$0'
#             ),
#             remark=f'{self.remark()} > 帳管費免費'
#         )
#
#     @property
#     def elas_type_backup_mgmt_offer(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '限期優惠'
#             ),
#             remark=f'{self.remark()} > 帳管費限期優惠'
#         )
#
#     @property
#     def elas_type_backup_apply_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "我要申請"`][2]'
#             ),
#             remark=f'{self.remark()} > 我要申請按鈕'
#         )
#
#     @property
#     def elas1_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "彈力貸"`][1]'
#             ),
#             remark=f'{self.remark()} > 彈力貸'
#         )
#
#     @property
#     def elas1_type(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "本息攤" OR label == "月繳息"`][1]'
#             ),
#             remark=f'{self.remark()} > 本息攤或月繳息'
#         )
#
#     @property
#     def elas1_due_amount(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '(//XCUIElementTypeStaticText[@name="彈力貸"])[1]/../XCUIElementTypeStaticText[starts-with(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 彈力貸_本期還款金額'
#         )
#
#     @property
#     def elas1_debit_date_com(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '(//XCUIElementTypeStaticText[@name="彈力貸"])[1]/../XCUIElementTypeStaticText[contains(@name, "/")]'
#             ),
#             remark=f'{self.remark()} > 彈力貸_扣款日'
#         )
#
#     @property
#     def elas1_terms_info(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label BEGINSWITH "已繳"`][1]'
#             ),
#             remark=f'{self.remark()} > 彈力貸_期數資訊'
#         )
#
#     @property
#     def elas1_avail_info(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label BEGINSWITH "可動用金額"`][1]'
#             ),
#             remark=f'{self.remark()} > 彈力貸_可動用金額'
#         )
#
#     @property
#     def elas1_quota_info(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label BEGINSWITH "貸款額度"`][1]'
#             ),
#             remark=f'{self.remark()} > 彈力貸_貸款額度'
#         )
#
#     @property
#     def elas1_act_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "我要動用"`][1]'
#             ),
#             remark=f'{self.remark()} > 彈力貸_我要動用按鈕'
#         )
#
#     @property
#     def dedicated_consultation_text(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "專人信貸諮詢"`]'
#             ),
#             remark=f'{self.remark()} > 專人信貸諮詢文字'
#         )
#
#     @property
#     def dedicated_consultation_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "免費預約"`]'
#             ),
#             remark=f'{self.remark()} > 專人信貸諮詢免費預約按鈕'
#         )
#
#     @property
#     def more_featured_plans_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "更多精選方案"`]'
#             ),
#             remark=f'{self.remark()} > 更多精選方案按鈕'
#         )
#
#
# class ExclusivePlanPage(Page):
#     title_ = Element(By.ACCESSIBILITY_ID, '個人專屬方案')
#     back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black')
#
#     title_infos = Elements(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView/XCUIElementTypeCell[1]/XCUIElementTypeStaticText',
#         remark='彈力貸所有標頭資訊')
#
#     all_infos = Elements(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView/**/XCUIElementTypeStaticText',
#         remark='所有資訊')
#
#
# class MyLoanInfoPage(BaseObject):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("貸款資訊頁面")
#         self.driver = DeviceManager.get_driver()
#
#     @property
#     def title_(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "貸款資訊"`]'
#             ),
#             remark=f'{self.remark()} > 標題'
#         )
#
#     @property
#     def back_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'icon arrow left black'
#             ),
#             remark=f'{self.remark()} > 回到上一頁按鈕'
#         )
#
#     @property
#     def details_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '繳款明細'
#             ),
#             remark=f'{self.remark()} > 繳款明細按鈕'
#         )
#
#     @property
#     def debit_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeOther/XCUIElementTypeStaticText[`label == "本期還款金額"`]'
#             ),
#             remark=f'{self.remark()} > 本期還款金額標題'
#         )
#
#     @property
#     def debit_amount(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label BEGINSWITH "$"`][1]'
#             ),
#             remark=f'{self.remark()} > 本期還款金額值'
#         )
#
#     @property
#     def rate_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '貸款利率'
#             ),
#             remark=f'{self.remark()} > 貸款利率'
#         )
#
#     @property
#     def rate_value(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label ENDSWITH "%"'
#             ),
#             remark=f'{self.remark()} > 貸款利率值'
#         )
#
#     @property
#     def debit_date_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '扣款日'
#             ),
#             remark=f'{self.remark()} > 扣款日'
#         )
#
#     @property
#     def debit_date_com(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label CONTAINS "/"`][1]'
#             ),
#             remark=f'{self.remark()} > 扣款日期'
#         )
#
#     @property
#     def debit_date_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'ic cube information'
#             ),
#             remark=f'{self.remark()} > 扣款日備註鈕'
#         )
#
#     @property
#     def debit_pp_content(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label BEGINSWITH "如扣款日遇假日"'
#             ),
#             remark=f'{self.remark()} > 扣款日遇假日彈窗_內文'
#         )
#
#     @property
#     def debit_pp_confirm(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "我知道了"`]'
#             ),
#             remark=f'{self.remark()} > 扣款日遇假日彈窗_我知道了按鈕'
#         )
#
#     @property
#     def terms_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '期數'
#             ),
#             remark=f'{self.remark()} > 期數'
#         )
#
#     @property
#     def terms_info(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label CONTAINS "共" AND label CONTAINS "期"'
#             ),
#             remark=f'{self.remark()} > 期數資訊'
#         )
#
#     @property
#     def total_amount_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '貸款金額'
#             ),
#             remark=f'{self.remark()} > 貸款金額欄位'
#         )
#
#     @property
#     def total_amount_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label BEGINSWITH "$"`][2]'
#             ),
#             remark=f'{self.remark()} > 貸款金額值'
#         )
#
#     @property
#     def total_remain_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '貸款餘額'
#             ),
#             remark=f'{self.remark()} > 貸款餘額欄位'
#         )
#
#     @property
#     def total_remain_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label BEGINSWITH "$"`][3]'
#             ),
#             remark=f'{self.remark()} > 貸款餘額值'
#         )
#
#     @property
#     def disburse_date_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '撥款日期'
#             ),
#             remark=f'{self.remark()} > 撥款日期欄位'
#         )
#
#     @property
#     def disburse_date_com(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label CONTAINS "/"`][2]'
#             ),
#             remark=f'{self.remark()} > 撥款日期值'
#         )
#
#     @property
#     def final_date_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '最後還款日期'
#             ),
#             remark=f'{self.remark()} > 最後還款日期欄位'
#         )
#
#     @property
#     def final_date_com(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label CONTAINS "/"`][3]'
#             ),
#             remark=f'{self.remark()} > 最後還款日期值'
#         )
#
#     @property
#     def debit_account_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '扣款帳號'
#             ),
#             remark=f'{self.remark()} > 扣款帳號'
#         )
#
#     def dynamic_debit_account_id(self, id16: str):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 f'{id16}',
#             ),
#             remark=f'{self.remark()} > 扣款帳號'
#         )
#
#
# class MyLoanDetailsPage(BaseObject):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("繳款明細頁")
#         self.driver = DeviceManager.get_driver()
#
#     @property
#     def title_(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label == "繳款明細"'
#             ),
#             remark=f'{self.remark()} > 標題'
#         )
#
#     @property
#     def back_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'icon arrow left black'
#             ),
#             remark=f'{self.remark()} > 回到上一頁按鈕'
#         )
#
#     @property
#     def year_details_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`name CONTAINS "年明細"`]'
#             ),
#             remark=f'{self.remark()} > yyyy年明細按鈕'
#         )
#
#     @property
#     def year_details_text(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`name CONTAINS "年明細"`]'
#             ),
#             remark=f'{self.remark()} > yyyy年明細按鈕文本'
#         )
#
#     def dynamic_date_slash(self, year: str):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 f'**/XCUIElementTypeStaticText[`label BEGINSWITH "{year}/"`][1]'
#             ),
#             remark=f'{self.remark()} > 明細日期'
#         )
#
#     @property
#     def principle_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "本金"`][1]'
#             ),
#             remark=f'{self.remark()} > 本金欄位'
#         )
#
#     @property
#     def principle_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '(//XCUIElementTypeStaticText[@name="本金"])[1]/../XCUIElementTypeStaticText[starts-with(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 本金金額'
#         )
#
#     @property
#     def interest_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "利息"`][1]'
#             ),
#             remark=f'{self.remark()} > 利息欄位'
#         )
#
#     @property
#     def interest_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '(//XCUIElementTypeStaticText[@name="利息"])[1]/../XCUIElementTypeStaticText[starts-with(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 利息金額'
#         )
#
#
# class LoanCreditIndividualPage(Loading):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("信用貸款預約諮詢頁面")
#         self.driver = DeviceManager.get_driver()
#
#     def prerequisites(self) -> None:
#         self.app_loading.assert_invisible(False)
#         self.webview_redirecting.assert_invisible(False)
#         self.webview_progressing.assert_visible(False)
#         self.webview_progressing.assert_width()
#         self.webview_loading.assert_invisible(False)
#
#     @property
#     def title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`name == "信用貸款預約諮詢"`]'
#             ),
#             remark=f"{self.remark()} > 標題"
#         )
#
#     @property
#     def close_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'webview close'
#             ),
#             remark=f"{self.remark()} > 關閉按鈕"
#         )
#
#
# class LoanCreditOnlinePage(Loading):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("線上申請信用貸款頁面")
#         self.driver = DeviceManager.get_driver()
#
#     def prerequisites(self) -> None:
#         self.app_loading.assert_invisible(False)
#         self.webview_redirecting.assert_invisible(False)
#         self.webview_progressing.assert_visible(False)
#         self.webview_progressing.assert_width()
#         self.webview_loading.assert_invisible(False)
#
#     @property
#     def title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "線上申請信用貸款"`][1]'
#             ),
#             remark=f"{self.remark()} > 標題"
#         )
#
#     @property
#     def close_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'webview close'
#             ),
#             remark=f"{self.remark()} > 關閉按鈕"
#         )
#
#
# class LoanCreditMorePage(Loading):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("泰幸福貸就補頁面")
#         self.driver = DeviceManager.get_driver()
#
#     def prerequisites(self) -> None:
#         self.app_loading.assert_invisible(False)
#         self.webview_redirecting.assert_invisible(False)
#         self.webview_progressing.assert_visible(False)
#         self.webview_progressing.assert_width()
#         self.webview_loading.assert_invisible(False)
#
#     @property
#     def title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "泰幸福 貸就補"`]'
#             ),
#             remark=f"{self.remark()} > 標題"
#         )
#
#     @property
#     def close_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'webview close'
#             ),
#             remark=f"{self.remark()} > 關閉按鈕"
#         )
#
#
# class HomeLoanMainPage(BaseObject):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("一般購屋貸款頁面")
#         self.driver = DeviceManager.get_driver()
#
#     @property
#     def title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "一般購屋貸款"`][2]'
#             ),
#             remark=f"{self.remark()} > 標題"
#         )
#
#     @property
#     def close_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'webview close'
#             ),
#             remark=f"{self.remark()} > 關閉按鈕"
#         )
#
#
# class HomeLoanOnlinePage(BaseObject):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("線上申請房屋貸款頁面")
#         self.driver = DeviceManager.get_driver()
#
#     @property
#     def title1(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "線上申請房屋貸款"`][1]'
#             ),
#             remark=f"{self.remark()} > 標題1"
#         )
#
#     @property
#     def title2(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeStaticText[`label == "線上申請房屋貸款"`][2]'
#             ),
#             remark=f"{self.remark()} > 標題2"
#         )
#
#     @property
#     def close_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'webview close'
#             ),
#             remark=f"{self.remark()} > 關閉按鈕"
#         )
#
# class ElasMainPage(BaseObject):
#
#     def __init__(self):
#         super().__init__()
#         self.set_remark("彈力貸詳細資訊頁")
#         self.driver = DeviceManager.get_driver()
#
#     @property
#     def service_rmk(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label BEGINSWITH "系統服務時間"'
#             ),
#             remark=f'{self.remark()} > 系統服務時間資訊'
#         )
#
#     @property
#     def title_(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label BEGINSWITH "彈力貸"'
#             ),
#             remark=f'{self.remark()} > 彈力貸標題'
#         )
#
#     @property
#     def back_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'icon arrow left black'
#             ),
#             remark=f'{self.remark()} > 返回按鈕'
#         )
#
#     @property
#     def icon(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'ic_elastic_loan_interest'
#             ),
#             remark=f'{self.remark()} > 彈力貸icon'
#         )
#
#     @property
#     def all_amounts(self):
#         return BasicComponents(
#             lambda: self.driver.find_elements(
#                 AppiumBy.IOS_PREDICATE,
#                 'name CONTAINS "$"'
#             ),
#             remark=f'{self.remark()} > 所有金額'
#         )
#
#     @property
#     def avail_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '可動用額度'
#             ),
#             remark=f'{self.remark()} > 可動用額度標題'
#         )
#
#     # '//XCUIElementTypeStaticText[@name="可動用額度"]/../XCUIElementTypeStaticText[contains(@name, "$"]'
#
#     @property
#     def avail_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="可動用額度"]/following-sibling::XCUIElementTypeStaticText[1]',
#             ),
#             remark=f'{self.remark()} > 可動用額度總額'
#         )
#
#     @property
#     def acted_quota_title(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '已動用額度'
#             ),
#             remark=f'{self.remark()} > 已動用額度標題'
#         )
#
#     @property
#     def acted_quota_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="已動用額度"]/../XCUIElementTypeStaticText[contains(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 已動用額度總額'
#         )
#
#     @property
#     def due_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '本期應繳金額'
#             ),
#             remark=f'{self.remark()} > 本期應繳金額欄位'
#         )
#
#     @property
#     def due_ibtn(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 'ic cube information'
#             ),
#             remark=f'{self.remark()} > 本期應繳金額備註鈕'
#         )
#
#     @property
#     def due_pp_content(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label BEGINSWITH "本期應繳金額 ="'
#             ),
#             remark=f'{self.remark()} > 本期應繳金額彈窗內容'
#         )
#
#     @property
#     def due_pp_confirm(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "我知道了"`]'
#             ),
#             remark=f'{self.remark()} > 本期應繳金額彈窗確認按鈕'
#         )
#
#     @property
#     def due_total_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="本期應繳金額"]/../XCUIElementTypeStaticText[contains(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 本期應繳金額總額'
#         )
#
#     @property
#     def due_pcp_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="本金"]/../XCUIElementTypeStaticText[contains(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 本金金額'
#         )
#
#     @property
#     def due_ir_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="利息"]/../XCUIElementTypeStaticText[contains(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 利息金額'
#         )
#
#     @property
#     def due_else_amt(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="其他"]/../XCUIElementTypeStaticText[contains(@name, "$")]'
#             ),
#             remark=f'{self.remark()} > 其他金額'
#         )
#
#     @property
#     def debit_date_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '下次扣款日'
#             ),
#             remark=f'{self.remark()} > 下次扣款日欄位'
#         )
#
#     @property
#     def debit_date_com(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="下次扣款日"]/../XCUIElementTypeStaticText[contains(@name, "/")]'
#             ),
#             remark=f'{self.remark()} > 下次扣款日日期'
#         )
#
#     @property
#     def debit_account_id(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.XPATH,
#                 '//XCUIElementTypeStaticText[@name="扣款帳戶"]/../XCUIElementTypeStaticText[2]'
#             ),
#             remark=f'{self.remark()} > 扣款帳戶'
#         )
#
#     @property
#     def term_col(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 '期數'
#             ),
#             remark=f'{self.remark()} > 期數欄位'
#         )
#
#     @property
#     def terms_info(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_PREDICATE,
#                 'label BEGINSWITH "已繳"'
#             ),
#             remark=f'{self.remark()} > 期數已繳資訊'
#         )
#
#     @property
#     def repay_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "我要還本"`]'
#             ),
#             remark=f'{self.remark()} > 我要還本按鈕'
#         )
#
#     @property
#     def act_button(self):
#         return BasicComponent(
#             lambda: self.driver.find_element(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeButton[`label == "我要動用"`]'
#             ),
#             remark=f'{self.remark()} > 我要動用按鈕'
#         )
#
#     @property
#     def scrollview_statictexts(self):
#         return BasicComponents(
#             lambda: self.driver.find_elements(
#                 AppiumBy.IOS_CLASS_CHAIN,
#                 '**/XCUIElementTypeScrollView/**/XCUIElementTypeStaticText'
#             ),
#             remark=f'{self.remark()} > 滾動視圖內的所有文本'
#         )
#
#
# class ElasActSetupPage(Page):
#     page = '我要動用_設定頁'
#
#     title_ = Element(By.IOS_PREDICATE, 'label == "我要動用"', remark=f'{page}_標題')
#     back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black', remark=f'{page}_回到上一頁')
#
#     act_title = Element(By.ACCESSIBILITY_ID, '本次動用金額', remark=f'{page}_本次動用金額')
#     act_input_fld = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[1]', remark=f'{page}_本次動用金額輸入框')
#     act_rmk = Element(By.IOS_PREDICATE, 'label BEGINSWITH "最低動用"', remark=f'{page}_最低動用_可動用額度')
#     dst_account_col = Element(By.ACCESSIBILITY_ID, '轉入帳號', remark=f'{page}_轉入帳號')
#     dst_account_fld = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[2]', remark=f'{page}_轉入帳號選擇框')
#     ir_col = Element(By.ACCESSIBILITY_ID, '貸款利率', remark=f'{page}_貸款利率欄位')
#     ir_pct = Element(By.IOS_PREDICATE, 'label ENDSWITH "%"', remark=f'{page}_貸款利率百分比')
#     next_step_button = Element(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label BEGINSWITH "下一步"`]',
#         remark=f'{page}_下一步按鈕')
#
#
# class ElasActConfirmPage(Page):
#     page = '我要動用_確認頁'
#
#     title_ = Element(By.IOS_PREDICATE, 'label == "我要動用"', remark=f'{page}_標題')
#     back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black', remark=f'{page}_回到上一頁')
#
#     act_title = Element(By.ACCESSIBILITY_ID, '本次動用金額', remark=f'{page}_本次動用金額標題')
#     act_amt = Element(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label BEGINSWITH "$"`][1]',
#         remark=f'{page}_本次動用金額總額')
#
#     acted_pcp_col = Element(By.ACCESSIBILITY_ID, '動用後本金總計', remark=f'{page}_動用後本金總計欄位')
#     acted_pcp_amt = Element(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label BEGINSWITH "$"`][2]',
#         remark=f'{page}_動用後本金總計金額')
#
#     cur_monthly_due_col = Element(By.ACCESSIBILITY_ID, '目前月付金', remark=f'{page}_目前月付金欄位')
#     cur_monthly_due_amt = Element(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label BEGINSWITH "$"`][3]',
#         remark=f'{page}_目前月付金金額')
#
#     acted_month_col = Element(By.ACCESSIBILITY_ID, '動用後月付金', remark=f'{page}_動用後月付金欄位')
#     acted_month_info = Element(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label BEGINSWITH "約 $"`]',
#         remark=f'{page}_動用後月付金金額')
#
#     icc_dst = '**/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeOther'
#     act_dst_account_col = Element(By.ACCESSIBILITY_ID, '轉入帳戶', remark=f'{page}_轉入帳戶欄位')
#     act_dst_account_info = Element(
#         By.IOS_CLASS_CHAIN, f'{icc_dst}/XCUIElementTypeStaticText[2]',
#         remark=f'{page}_轉入帳戶資訊')
#
#     act_ir_col = Element(By.ACCESSIBILITY_ID, '貸款利率', remark=f'{page}_貸款利率欄位')
#     act_ir_percent = Element(By.IOS_PREDICATE, 'label ENDSWITH "%"', remark=f'{page}_貸款利率百分比')
#
#     act_confirm_button = Element(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "確定動用"`]',
#         remark=f'{page}_確定動用按鈕')
#
#
# class ElasActResultPage(Page):
#     page = '我要動用_結果頁'
#
#     title_ = Element(By.IOS_PREDICATE, 'label == "我要動用"', remark=f'{page}_標題')
#     back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black', remark=f'{page}_回到上一頁')
#
#     successful = Element(By.ACCESSIBILITY_ID, '動用成功', remark=f'{page}_動用成功')
#     failed = Element(By.IOS_PREDICATE, 'label CONTAINS "失敗"', remark=f'{page}_任何失敗訊息')
#
#     execute_time = Element(By.IOS_PREDICATE, 'label CONTAINS "/" AND label CONTAINS ":"', remark=f'{page}_執行時間')
#
#     acted_title = Element(By.ACCESSIBILITY_ID, '本次動用金額', remark=f'{page}_本次動用金額標題')
#     acted_amt = Element(
#         By.XPATH,
#         '//XCUIElementTypeStaticText[@name="本次動用金額"]/../XCUIElementTypeStaticText[starts-with(@name, "$")]',
#         remark=f'{page}_本次動用金額總額')
#
#     acted_pcp_col = Element(By.ACCESSIBILITY_ID, '動用後本金總計', remark=f'{page}_動用後本金總計欄位')
#     acted_pcp_amt = Element(
#         By.XPATH,
#         '//XCUIElementTypeStaticText[@name="動用後本金總計"]/../XCUIElementTypeStaticText[starts-with(@name, "$")]',
#         remark=f'{page}_動用後本金總計金額')
#
#     cur_monthly_due_col = Element(By.ACCESSIBILITY_ID, '目前月付金', remark=f'{page}_目前月付金欄位')
#     cur_monthly_due_amt = Element(
#         By.XPATH,
#         '//XCUIElementTypeStaticText[@name="目前月付金"]/../XCUIElementTypeStaticText[starts-with(@name, "$")]',
#         remark=f'{page}_目前月付金金額')
#
#     acted_month_col = Element(By.ACCESSIBILITY_ID, '動用後月付金', remark=f'{page}_動用後月付金欄位')
#     acted_monthly_due_info = Element(
#         By.XPATH,
#         '//XCUIElementTypeStaticText[@name="動用後月付金"]/../XCUIElementTypeStaticText[starts-with(@name, "約 $")]',
#         remark=f'{page}_動用後月付金金額')
#
#     acted_dst_account_col = Element(By.ACCESSIBILITY_ID, '轉入帳戶', remark=f'{page}_轉入帳戶欄位')
#     acted_dst_account_info = Element(
#         By.XPATH, '//XCUIElementTypeStaticText[@name="轉入帳戶"]/../XCUIElementTypeStaticText[2]',
#         remark=f'{page}_轉入帳戶資訊')
#
#     acted_ir_col = Element(By.ACCESSIBILITY_ID, '貸款利率', remark=f'{page}_貸款利率欄位')
#     acted_ir_percent = Element(
#         By.XPATH, '//XCUIElementTypeStaticText[@name="貸款利率"]/../XCUIElementTypeStaticText[contains(@name, "%")]',
#         remark=f'{page}_貸款利率百分比')
#
#     back_to_elas_button = Element(
#         By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "回彈力貸本息攤"`]',
#         remark=f'{page}_回彈力貸本息攤按鈕')
#
#
# class ElasRepaySetupPage(Page):
#     title_ = Element(By.IOS_PREDICATE, 'label == "我要還本"')
#     back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black')
#
#     repay_input_fld = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[1]')
#     repay_rmk = Element(By.IOS_PREDICATE, 'label BEGINSWITH "最低還本"')
#     src_account_fld = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[2]')
#     src_account_avail_info = Element(By.IOS_PREDICATE, 'label BEGINSWITH "可用餘額"')
#
#     next_step_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label BEGINSWITH "下一步"`]')
#
#
# class ElasRepayConfirmPage(Page):
#     title_ = Element(By.IOS_PREDICATE, 'label == "我要還本"')
#     back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black')
#
#     amount = Element(By.IOS_PREDICATE, 'label BEGINSWITH "$"')
#
#     src_account_info = Element(
#         By.XPATH,
#         '//XCUIElementTypeStaticText[@name="轉出帳戶"]/following-sibling::XCUIElementTypeStaticText')
#
#     confirm_repay_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "確定還本"`]')
#
#
# class ElasRepayResultPage(Page):
#     title_ = Element(By.IOS_PREDICATE, 'label == "我要還本"')
#
#     success = Element(By.ACCESSIBILITY_ID, '還本成功')
#
#     amount = Element(By.IOS_PREDICATE, 'label BEGINSWITH "$"')
#
#     src_account_info = Element(
#         By.XPATH,
#         '//XCUIElementTypeStaticText[@name="轉出帳戶"]/following-sibling::XCUIElementTypeStaticText')
#
#     back_to_main_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label BEGINSWITH "回彈力貸"`]')
