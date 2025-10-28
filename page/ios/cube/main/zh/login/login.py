from appium.webdriver.common.appiumby import AppiumBy

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.sliding_object import SlidingObject
from module.mobile.device_manager import DeviceManager


class PreLoginPage(BaseObject):
    def __init__(self):
        super().__init__()
        self.set_remark("個人化預登入頁面")
        self.driver = DeviceManager.get_driver()

    def prerequisites(self) -> None:
        self.login_button.assert_visible(False)
        self.pre_login_image.assert_visible(False)

    @property
    def title_(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '國泰世華銀行 CUBE App，登入頁'),
            f"{self.remark()} > 標題"
        )

    @property
    def typetable(self, x=None):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTable"'),
            f"{self.remark()} > TypeTable"
        )

    @property
    def pre_login_image(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'img_gradientbg'),
            f"{self.remark()} > 預登入圖片"
        )

    @property
    def language(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE,
                                             'name IN {"語系選擇目前為中文", "語系選擇目前為英文"}'),
            f"{self.remark()} > 語言"
        )

    @property
    def exchange_rate_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "更多匯率"`]'
            ),
            f'{self.remark()} > 更多匯率按鈕'
        )

    @property
    def cube_plan_cell(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label BEGINSWITH "您目前CUBE方案為"`]'
            ),
            f'{self.remark()} > cube方案區塊'
        )

    @property
    def remind_text(self):
        SlidingObject().scroll_to_bottom()
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeStaticText[`name CONTAINS "本服務由國泰綜合"`]',
            ),
            f'{self.remark()} > 首頁下方提醒文字'
        )

    @property
    def remind_text_expend_button(self):
        SlidingObject().scroll_to_element(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "...顯示全部"`]')
        )
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "...顯示全部"`]'),
            f'{self.remark()} > 首頁下方提醒文字顯示全部按鈕')

    @property
    def bell_popup(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeImage[2]'
            ),
            f'{self.remark()} > 彈窗小鈴鐺'
        )

    @property
    def language_image(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'img_a11y_language'),
            f"{self.remark()} > 語言圖片"
        )

    @property
    def language_zh(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '中文'),
            f"{self.remark()} > 中文選項"
        )

    @property
    def language_en(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'English'),
            f"{self.remark()} > 英文選項"
        )

    @property
    def language_save_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`name IN {"儲存", "Save"}`]'),
            f"{self.remark()} > 儲存按鈕"
        )

    @property
    def login_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "登入"`]'),
            f"{self.remark()} > 登入按鈕"
        )

    @property
    def uat_version(self):
        SlidingObject().scroll_to_element(
            lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label BEGINSWITH "App版本UAT "')
        )
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label BEGINSWITH "App版本UAT "'),
            f"{self.remark()} > UAT版本資訊"
        )

    @property
    def stg_version(self):
        SlidingObject().scroll_to_element(
            lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label BEGINSWITH "App版本STG"')
        )
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label BEGINSWITH "App版本STG"'),
            f"{self.remark()} > STG版本資訊"
        )

    @property
    def signup_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '開戶、啟用App或開卡'),
            f"{self.remark()} > 註冊按鈕"
        )

    @property
    def bell_popup(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[2]'),
            f"{self.remark()} > 彈窗小鈴鐺"
        )

    @property
    def type_image(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_PREDICATE, 'type=="XCUIElementTypeImage"'),
            f"{self.remark()} > 類型圖片"
        )

    @property
    def menu(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label == "左側選單"`]'),
            f"{self.remark()} > 菜單按鈕"
        )

    @property
    def fin(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '金融商品'),
            f"{self.remark()} > 金融商品區塊"
        )

    @property
    def fin_exr(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '利匯率'),
            f"{self.remark()} > 利匯率選項"
        )

    @property
    def fin_exr_twd(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '臺幣存放款利率'),
            f"{self.remark()} > 臺幣存放款利率"
        )

    @property
    def fin_exr_frd(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '外幣存款利率'),
            f"{self.remark()} > 外幣存款利率"
        )

    @property
    def fin_exr_fxr(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '外幣匯率'),
            f"{self.remark()} > 外幣匯率"
        )

    @property
    def fin_exr_est(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '換匯試算'),
            f"{self.remark()} > 換匯試算"
        )

    @property
    def others(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '其他'),
            f"{self.remark()} > 其他"
        )

    @property
    def others_go_to_web_cube(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '前往網銀'),
            f"{self.remark()} > 前往網銀"
        )

    @property
    def single_api_path_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '單一 API Path'),
            f"{self.remark()} > 單一 API Path文字"
        )

    @property
    def mock_api_text_field(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField'),
            f"{self.remark()} > 單一api Text Field"
        )

    @property
    def error_mode_text(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Error Mode'),
            f"{self.remark()} > Error Mode文字"
        )

    @property
    def error_mode_field(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeStaticText[@name="Error Mode"]/following-sibling::*[@type="XCUIElementTypeStaticText"]'),
            f"{self.remark()} > 單一api Text Field")

    @property
    def error_mode_http_error(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'httperror'),
            f"{self.remark()} > httpError error mode"
        )

    @property
    def error_mode_timeout(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'timeout'),
            f"{self.remark()} > timeout error mode"
        )

    @property
    def error_mode_response_empty(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'responseempty'),
            f"{self.remark()} > responseEmpty error mode"
        )

    @property
    def error_mode_response_error(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'responseformaterror'),
            f"{self.remark()} > responseError error mode"
        )

    @property
    def error_mode_status_code_9999(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'status_code_9999'),
            f"{self.remark()} > status_code_9999 error mode"
        )

    @property
    def reset_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "重置"`]'),
            f"{self.remark()} > 重置按鈕"
        )

    @property
    def apply_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "套用"`]'),
            f"{self.remark()} > 套用按鈕"
        )

    @property
    def face_id_fail_pp(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`label == "無法辨識臉部"`]'),
            f"{self.remark()} > FaceID辨識失敗彈窗"
        )

    @property
    def cancel_face_id_pp(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "取消"`]'),
            f"{self.remark()} > 取消FaceID彈窗"
        )

    @property
    def login_with_face_id(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label == "Face ID登入"`]'),
            f"{self.remark()} > 透過FaceID登入按鈕"
        )

    @property
    def login_with_pw(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label == "改用代號密碼登入"`]'),
            f"{self.remark()} > 透過密碼登入按鈕"
        )

    @property
    def face_id_fail_attempts_too_many_pp_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`label CONTAINS "驗證錯誤次數過多"`]'),
            f"{self.remark()} > FaceID失敗次數過多彈窗_文本"
        )


class LoginPage(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("登入頁面")
        self.driver = DeviceManager.get_driver()

    def prerequisites(self) -> None:
        self.login_button.assert_visible()
        self.forget_psw.assert_visible()

    @property
    def remember_radio(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label BEGINSWITH "記住我的身分證字號，"`]'),
            f"{self.remark()} > 記住我單選框"
        )

    @property
    def userid_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeSecureTextField[`label BEGINSWITH "身分證字號"`]'),
            f"{self.remark()} > 身分證字號輸入框"
        )

    @property
    def username_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeSecureTextField[`label BEGINSWITH "用戶代號"`]'),
            f"{self.remark()} > 用戶代號輸入框"
        )

    @property
    def userpsw_input(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeSecureTextField[`label BEGINSWITH "網銀密碼"`]'),
            f"{self.remark()} > 網銀密碼輸入框"
        )

    @property
    def userid_input_eye(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label BEGINSWITH "身分證字號目前為"`]'),
            f"{self.remark()} > 身分證字號顯示按鈕"
        )

    @property
    def username_input_eye(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label BEGINSWITH "用戶代號目前為"`]'),
            f"{self.remark()} > 用戶代號顯示按鈕"
        )

    @property
    def userpsw_input_eye(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label BEGINSWITH "網銀密碼目前為"`]'),
            f"{self.remark()} > 網銀密碼顯示按鈕"
        )

    @property
    def login_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label == "登入"`]'),
            f"{self.remark()} > 登入按鈕"
        )

    @property
    def forget_psw(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label == "重設代號及密碼"`]'),
            f"{self.remark()} > 忘記代號密碼按鈕"
        )

    @property
    def gesture_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`name == "Login with pattern" OR name == "改用手勢登入"`]'),
            f"{self.remark()} > 手勢登入按鈕")


class GestureLoginPage(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("手勢登入頁面")
        self.driver = DeviceManager.get_driver()

    def prerequisites(self) -> None:
        self.account_login.assert_visible()
        self.content.assert_visible()

    @property
    def content(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeStaticText[`label CONTAINS "手勢登入9宮格矩陣，"`]'),
            f"{self.remark()} > 說明"
        )

    @property
    def account_login(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label == "改用代號密碼登入"`]'),
            f"{self.remark()} > 帳號密碼登入按鈕"
        )

    @property
    def dots(self):
        return BasicComponent(
            lambda: self.driver.find_elements(AppiumBy.IOS_CLASS_CHAIN,
                                              '**/XCUIElementTypeButton[`name CONTAINS "九宮格矩陣之"`]'),
            f"{self.remark()} > 九宮格矩陣"
        )

    def get_dots_location_then_draw_gesture(self, gesture: str):
        """
        獲取座標點並繪製手勢
        """
        dots = self.driver.find_elements(
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeButton[`name CONTAINS "九宮格矩陣之"`]')
        dots_dic = [
            {'x': int(rect['x'] + rect['width'] / 2), 'y': int(rect['y'] + rect['height'] / 2)}
            for element in dots if element.is_displayed()  # 檢查元素是否顯示
            for rect in [element.rect]
        ]
        SlidingObject().draw_gesture(dots_dic, gesture)

    @property
    def verify_popup_confirm(self):
        return BasicComponent(
            lambda: self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                             '**/XCUIElementTypeButton[`label == "立即驗證"`]'),
            f"{self.remark()} > 立即驗證按鈕"
        )
