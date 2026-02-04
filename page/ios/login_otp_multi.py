from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.device_manager import DeviceManager


class MUiOSOTPage(BaseObject):
    def __init__(self, role=None):
        super().__init__()
        self.set_remark("驗證網銀交易-多裝置測試")
        # self.driver = DeviceManager.get_driver()
        self.role = role
        # 使用多裝置模式時，需將 role 傳入以取得對應 driver
        self.driver = DeviceManager.get_driver(role=self.role)

    def verify_trade(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, '驗證網銀交易'))),
            remark=f"{self.remark()} > 驗證網銀交易選項"
        )

    def start_OTP_btn(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "啟用企業行動密碼"`]'))),
            remark=f"{self.remark()} > 啟用企業行動密碼按鈕"
        )

    def scroll_down_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]'),
            remark=f"{self.remark()} > 向下滑動按鈕"
        )

    def service_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((AppiumBy.IOS_CLASS_CHAIN,
                                                                                           '**/XCUIElementTypeStaticText[`name == "服務條款"`]'))),
            remark=f"{self.remark()} > 服務條款"
        )

    # 共用元素(同意/確認)
    def agree_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`name == "已閱讀並同意"`]'),
            remark=f"{self.remark()} > 已閱讀並同意服務條款/確認按鈕"
        )

    def otp_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (AppiumBy.XPATH,
                 '//XCUIElementTypeButton[@name="ic g3 close gray 24"]/../XCUIElementTypeStaticText[@name="啟用企業行動密碼"]'))),
            remark=f"{self.remark()} > 啟用企業行動密碼"
        )

    def otp_ID(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[@name="企業戶 ID / 統編"]/../following-sibling::XCUIElementTypeOther'),
            remark=f"{self.remark()} > OTP_輸入企業戶ID/統編"
        )

    def otp_phone_number(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[@name="手機號碼"]/../following-sibling::XCUIElementTypeOther'),
            remark=f"{self.remark()} > OTP_手機號碼"
        )

    def otp_company_name(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[@name="公司別名"]/../following-sibling::XCUIElementTypeOther'),
            remark=f"{self.remark()} > OTP_公司別名"
        )

    def otp_next_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`name == "下一步"`]'),
            remark=f"{self.remark()} > OTP_下一步按鈕"
        )

    def otp_recovered(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/recoveredTextView'),
            remark=f"{self.remark()} > OTP_已申請過企業行動密碼"
        )

    def otp_success_msg(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ID, 'com.cathaybk.geb.cubuat:id/messageTextView'),
            remark=f"{self.remark()} > OTP_啟用成功訊息"
        )

    def bio_check_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '啟用生物辨識'))),
            remark=f"{self.remark()} > 生物辨識標題"
        )

    def bio_check_msg(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '啟用後可以使用 Face ID 快速登入。'),
            remark=f"{self.remark()} > 生物辨識內容"
        )

    def bio_no_enable_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "不啟用"`]'),
            remark=f"{self.remark()} > 生物辨識_不啟用"
        )

    def verify_phone_num(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN,
                                                                                         '**/XCUIElementTypeStaticText[`name CONTAINS " 企業戶 ID / 統編：6514***4 手機號碼：0986****89"`]'))),
            remark=f"{self.remark()} > 驗證網銀交易-手機號碼"
        )

    def company_layout(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name CONTAINS " 企業戶 ID / 統編"`]'))),
            remark=f"{self.remark()} > 公司別名區塊"
        )

    def unlock_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "解鎖"`]'),
            remark=f"{self.remark()} > 解鎖按鈕"
        )

    def otp_input_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '輸入企業行動密碼'))),
            remark=f"{self.remark()} > 輸入OTP標題"
        )

    def otp_pwd_input_box(self, num):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//XCUIElementTypeStaticText[@name="輸入企業行動密碼"]/../../following-sibling::XCUIElementTypeOther[1]//XCUIElementTypeStaticText[{num}]'),
            remark=f"{self.remark()} > 第{num}密碼輸入框"
        )

    def otp_pwd_input_box2(self, num):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//XCUIElementTypeStaticText[@name="輸入企業行動密碼"]/../../following-sibling::XCUIElementTypeOther[1]//XCUIElementTypeStaticText[{num}]'),
            remark=f"{self.remark()} > 第{num}密碼輸入框"
        )

    def otp_check_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "確認"`]'),
            remark=f"{self.remark()} > 確認按鈕"
        )

    def display_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'ic g3 eye close green 24'),
            remark=f"{self.remark()} > 顯示隱碼按鈕"
        )

    def verify_list_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "待驗證清單"`]'))),
            remark=f"{self.remark()} > 待驗證清單標題"
        )

    def verify_list_item(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '沒有待驗證交易'),
            remark=f"{self.remark()} > 沒有待驗證交易"
        )

    def more_setting_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`name == "更多設定"`]'),
            remark=f"{self.remark()} > 更多設定按鈕"
        )

    # ================================================= 更多設定頁面元素 =================================================
    def change_phone_setting(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '更換手機'))),
            remark=f"{self.remark()} > 更換手機"
        )

    def create_number_msg(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '您即將創建換機啟用碼'))),
            remark=f"{self.remark()} > 您即將創建換機啟用碼內容"
        )
    def create_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "創建"`]'),
            remark=f"{self.remark()} > 創建"
        )
    def create_remind_msg(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '驗證成功後即可進行換機'))),
            remark=f"{self.remark()} > 驗證成功後即可進行換機"
        )

    def create_opt_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//XCUIElementTypeStaticText[@name="輸入企業行動密碼"]/../../following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText/..'),
            remark=f"{self.remark()} > 創建-輸入企業行動密碼"
        )

    def enabler_code_msg(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '換機啟用碼'))),
            remark=f"{self.remark()} > 換機啟用碼標題"
        )

    def enabler_code_content(self, num):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//XCUIElementTypeStaticText[@name="換機啟用碼"]/following-sibling::XCUIElementTypeStaticText[{num}]'),
            remark=f"{self.remark()} > 換機啟用碼內容"
        )

    # ================================================= 更換手機頁面元素 =================================================
    def change_phone_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "更換手機"`]'))),
            remark=f"{self.remark()} > 更換手機標題"
        )
    def start_otp_input(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="輸入 6 位數「啟用碼」"]/../../following-sibling::XCUIElementTypeOther'))),
            remark=f"{self.remark()} > 輸入啟用碼輸入框"
        )
    def start_otp_input2(self,num):
        return BasicComponent(
            lambda: WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((AppiumBy.XPATH,f'//XCUIElementTypeStaticText[@name="輸入 6 位數「啟用碼」"]/../../following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText[{num}]'))),
            remark=f"{self.remark()} > 輸入啟用碼輸入框"
        )

    def change_phone_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '此組企業行動密碼已在其他裝置啟用，若要在此裝置啟用，請選擇換機方式並回原裝置操作。'),
            remark=f"{self.remark()} > 更換手機內容"
        )

    def create_activation_code(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '創建啟用碼'),
            remark=f"{self.remark()} > 創建啟用碼"
        )

    def continue_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '繼續'),
            remark=f"{self.remark()} > 繼續按鈕"
        )

    def change_msg(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '請於原裝置創建啟用碼'),
            remark=f"{self.remark()} > 請於原裝置創建啟用碼內容"
        )

    def start_change_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '開始換機'),
            remark=f"{self.remark()} > 開始換機按鈕"
        )

    def warning_dialog(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '換機失敗'))),
            remark=f"{self.remark()} > 換機失敗"
        )

    def check_btn(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`name == "我知道了"`]'),
            remark=f"{self.remark()} > 我知道了"
        )

    def set_otp(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '設定企業行動密碼'))),
            remark=f"{self.remark()} > 設定企業行動密碼"
        )

    def set_otp_input(self, num):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//XCUIElementTypeStaticText[@name="設定企業行動密碼"]/../../following-sibling::XCUIElementTypeOther[1]//XCUIElementTypeStaticText[{num}]'),
            remark=f"{self.remark()} > 設定企業行動密碼輸入框 > {num}"
        )

    def set_otp_again_input(self, num):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//XCUIElementTypeStaticText[@name="再次輸入企業行動密碼"]/../../following-sibling::XCUIElementTypeOther[1]//XCUIElementTypeStaticText[{num}]'),
            remark=f"{self.remark()} > 再次輸入企業行動密碼輸入框 > {num}"
        )

    def set_success_msg(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '啟用成功'))),
            remark=f"{self.remark()} > 啟用成功"
        )

    # ================================================= 更換手機頁面元素 =================================================

    def reset_otp_title(self):
        return BasicComponent(
            lambda: WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "復原企業行動密碼"`]'))),
            remark=f"{self.remark()} > 復原企業行動密碼"
        )


# **/XCUIElementTypeStaticText[`name == "密碼檢核中，請稍候(0:02)"`]