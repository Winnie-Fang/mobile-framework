from appium.webdriver.common.appiumby import AppiumBy

from module.mobile.component.base_object import BaseObject
from module.mobile.component.basic_component import BasicComponent
from module.mobile.component.basic_components import BasicComponents
from module.mobile.device_manager import DeviceManager


class InsuranceMainPage(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("保險總覽頁")
        self.driver = DeviceManager.get_driver()

    def prerequisites(self) -> None:
        self.my_insurance.assert_visible()

    @property
    def ins_table(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                'XCUIElementTypeTable'
            ),
            remark=f'{self.remark()} > 可滾動視窗'
        )

    @property
    def title_(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeStaticText[`label == "保險"`]'
            ),
            remark=f'{self.remark()} > 保險'
        )

    @property
    def claim_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '保單理賠'
            ),
            remark=f'{self.remark()} > 保單理賠按鈕'
        )

    @property
    def claim_texts(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                'label == "保單理賠"'
            ),
            remark=f'{self.remark()} > 保單理賠文本'
        )

    @property
    def claim_title_in_menu(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'type == "XCUIElementTypeStaticText" AND name == "保單理賠"'
            ),
            remark=f'{self.remark()} > 保單理賠選單標題'
        )

    @property
    def claim_property(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '國泰產險'
            ),
            remark=f'{self.remark()} > 國泰產險'
        )

    @property
    def claim_life(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '國泰人壽'
            ),
            remark=f'{self.remark()} > 國泰人壽'
        )

    @property
    def my_insurance(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeStaticText[`name == "我的保障"`]'
            ),
            remark=f'{self.remark()} > 我的保障'
        )

    @property
    def my_debit(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '保單借款'
            ),
            remark=f'{self.remark()} > 保單借款'
        )

    @property
    def next_debit_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeOther[`name == "下次應繳保費"`]/XCUIElementTypeStaticText[`label == "下次應繳保費"`]'
            ),
            remark=f'{self.remark()} > 下次應繳保費'
        )

    @property
    def next_debit_twd_col(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '臺幣繳款總額'
            ),
            remark=f'{self.remark()} > 臺幣繳款總額'
        )

    @property
    def next_debit_twd_dlr(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                'TWD'
            ),
            remark=f'{self.remark()} > TWD'
        )

    @property
    def next_debit_twd_grp(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeStaticText[@name="TWD"]/following-sibling::XCUIElementTypeStaticText[1]'
            ),
            remark=f'{self.remark()} > TWD 繳款組合'
        )

    @property
    def next_debit_usd_col(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '美元繳款總額'
            ),
            remark=f'{self.remark()} > 美元繳款總額'
        )

    @property
    def next_debit_usd_dlr(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                'USD'
            ),
            remark=f'{self.remark()} > USD'
        )

    @property
    def next_debit_usd_grp(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeStaticText[@name="USD"]/following-sibling::XCUIElementTypeStaticText[1]'
            ),
            remark=f'{self.remark()} > USD 繳款組合'
        )

    @property
    def next_debit_date_info(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'label BEGINSWITH "繳款日"'
            ),
            remark=f'{self.remark()} > 繳款日資訊'
        )

    @property
    def rcmd_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeOther[`name == "專屬推薦"`]/XCUIElementTypeStaticText[`label == "專屬推薦"`]'
            ),
            remark=f'{self.remark()} > 專屬推薦標題'
        )

    @property
    def rcmd_image(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="專屬推薦"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeImage'
            ),
            remark=f'{self.remark()} > 專屬推薦圖'
        )

    @property
    def rcmd_login(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeStaticText[`label == "登入"`]'
            ),
            remark=f'{self.remark()} > 登入'
        )

    @property
    def rcmd_close(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                'webview close'
            ),
            remark=f'{self.remark()} > 關閉按鈕'
        )

    @property
    def cube_limited_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeOther[`name == "CUBE限定"`]/XCUIElementTypeStaticText[`label == "CUBE限定"`]'
            ),
            remark=f'{self.remark()} > CUBE限定標題'
        )

    @property
    def cube_limited_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="CUBE限定"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeButton[@name="Button"]'
            ),
            remark=f'{self.remark()} > CUBE限定_區塊內容'
        )

    @property
    def cube_limited_realtime(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '利即保'
            ),
            remark=f'{self.remark()} > 利即保'
        )

    @property
    def cube_limited_realtime_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "我要參加"`]'
            ),
            remark=f'{self.remark()} > 我要參加按鈕'
        )

    @property
    def ins_right_now_subtitle(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeStaticText[@name="利即保"]/following-sibling::XCUIElementTypeStaticText[1]'
            ),
            remark=f'{self.remark()} > CUBE限定_立即保副標題'
        )

    @property
    def ins_right_now_img(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                'insuranceBgImg'
            ),
            remark=f'{self.remark()} > CUBE限定_立即保圖片'
        )

    def cube_text(self, text: str) -> BasicComponent:
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                f'name == "{text}"'
            ),
            remark=f'{self.remark()} > CUBE限定_牌卡文字_{text}'
        )

    @property
    def cube_explore_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "開始探索"`]'
            ),
            remark=f'{self.remark()} > CUBE限定_開始探索按鈕'
        )

    @property
    def news_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeOther[`name == "保險新知"`]'
            ),
            remark=f'{self.remark()} > 保險新知標題'
        )

    @property
    def news_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="保險新知"]/following-sibling::XCUIElementTypeCell[1]'
            ),
            remark=f'{self.remark()} > 保險新知_區塊內容'
        )

    @property
    def news_content_2nd_news(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="保險新知"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeButton[2]'
            ),
            remark=f'{self.remark()} > 保險新知_第二條新聞'
        )

    @property
    def news_infos(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="保險新知"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeStaticText'
            ),
            remark=f'{self.remark()} > 保險新知_所有新聞資訊'
        )

    @property
    def news_info2(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="保險新知"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeStaticText[3]'
            ),
            remark=f'{self.remark()} > 保險新知_第二條新聞資訊'
        )

    @property
    def news_more_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '顯示更多'
            ),
            remark=f'{self.remark()} > 顯示更多按鈕'
        )

    @property
    def online_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'label == "線上投保"'
            ),
            remark=f'{self.remark()} > 線上投保標題'
        )

    @property
    def online_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="線上投保"]/following-sibling::XCUIElementTypeCell'
            ),
            remark=f'{self.remark()} > 線上投保_區塊內容'
        )

    @property
    def online_vehicle_tab(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '行車保障'
            ),
            remark=f'{self.remark()} > 行車保障標籤'
        )

    @property
    def online_travel_tab(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '旅遊保險'
            ),
            remark=f'{self.remark()} > 旅遊保險標籤'
        )

    @property
    def online_pet_tab(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '寵物住宅'
            ),
            remark=f'{self.remark()} > 寵物住宅標籤'
        )

    @property
    def cars_insurance(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '汽車險'
            ),
            remark=f'{self.remark()} > 汽車險'
        )

    @property
    def travel_insurance(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '旅遊保險'
            ),
            remark=f'{self.remark()} > 國內外旅遊險'
        )

    @property
    def home_insurance(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '寵物住宅'
            ),
            remark=f'{self.remark()} > 住宅險'
        )

    @property
    def online_goto_button1(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeStaticText[`label == "立即投保"`][1]'
            ),
            remark=f'{self.remark()} > 立即投保按鈕1'
        )

    @property
    def online_goto_buttons(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                'name == "立即投保"'
            ),
            remark=f'{self.remark()} > 所有立即投保按鈕'
        )

    @property
    def online_infos(self):
        return BasicComponents(
            self.driver.find_elements(
                AppiumBy.XPATH,
                '//XCUIElementTypeOther[@name="線上投保"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeStaticText'
            ),
            remark=f'{self.remark()} > 線上投保_所有資訊'
        )

    @property
    def bottom_remark(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'name CONTAINS "產險商品" AND name CONTAINS "國泰產險"'
            ),
            remark=f'{self.remark()} > 產險商品底部備註'
        )


class MyInsurancePage(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("我的保單頁面")
        self.driver = DeviceManager.get_driver()

    @property
    def title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE, 'label == "我的保單"'
            ),
            remark=f'{self.remark()} > 標題'
        )

    @property
    def back_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, 'icon arrow left black'
            ),
            remark=f'{self.remark()} > 返回按鈕'
        )

    @property
    def null_info(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE, 'name CONTAINS "無保單資訊"'
            ),
            remark=f'{self.remark()} > 無保單資訊提示'
        )

    @property
    def valid_date_of_all_ins(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                'type == "XCUIElementTypeStaticText" AND name == "保單生效日"'
            ),
            remark=f'{self.remark()} > 所有保單生效日文本'
        )

    @property
    def all_ins_num(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                'type == "XCUIElementTypeStaticText" AND name CONTAINS "#"'
            ),
            remark=f'{self.remark()} > 所有保單號碼'
        )

    @property
    def ins1_infos(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText'
            ),
            remark=f'{self.remark()} > 第一筆保單全部資訊'
        )

    @property
    def ins2_infos(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeStaticText'
            ),
            remark=f'{self.remark()} > 第二筆保單全部資訊'
        )


# TODO Ives 一些彈窗如果和接下來的頁面相關，可以寫在一起


class WebviewInsurancePropertyPage(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("國泰產險頁面")
        self.driver = DeviceManager.get_driver()

    @property
    def goto_popup_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'name CONTAINS "國泰產險" AND visible == true'
            ),
            remark=f'{self.remark()}_popup_content'
        )

    @property
    def goto_popup_dismiss(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`name == "取消"`]'
            ),
            remark=f'{self.remark()}_popup_dismiss'
        )

    @property
    def goto_popup_accept(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`name == "確認"`]'
            ),
            remark=f'{self.remark()}_popup_accept'
        )

    @property
    def property_texts(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                'name CONTAINS "國泰產險"'
            ),
            remark=f'{self.remark()}_property_texts'
        )

    @property
    def close_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                'webview close'
            ),
            remark=f'{self.remark()}_close_button'
        )

    @property
    def remind_popup_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'name == "提醒您"'
            ),
            remark=f'{self.remark()}_remind_popup_title'
        )

    @property
    def remind_popup_confirm(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '我知道了'
            ),
            remark=f'{self.remark()}_remind_popup_confirm'
        )

    @property
    def user_id(self, id_: str):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                f'value == "{id_}"'
            ),
            remark=f'{self.remark()}_user_id_{id_}'
        )


# TODO Ives 一些彈窗如果和接下來的頁面相關，可以寫在一起


class WebviewInsuranceLifePage(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("國泰人壽頁面")
        self.driver = DeviceManager.get_driver()

    @property
    def popup_content(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'name CONTAINS "國泰人壽" AND visible == true'
            ),
            remark=f'{self.remark()}_popup_content'
        )

    @property
    def popup_dismiss(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "取消"`]'
            ),
            remark=f'{self.remark()}_popup_dismiss'
        )

    @property
    def popup_accept(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeButton[`label == "確認"`]'
            ),
            remark=f'{self.remark()}_popup_accept'
        )

    @property
    def life_texts(self):
        return BasicComponents(
            lambda: self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                'name CONTAINS "國泰人壽"'
            ),
            remark=f'{self.remark()}_life_texts'
        )

    @property
    def close_button(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                'webview close'
            ),
            remark=f'{self.remark()}_close_button'
        )


class OpenWebviewRcmdPopup(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("專屬推薦彈出視窗")
        self.driver = DeviceManager.get_driver()

    @property
    def content(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '將開啟國泰人壽網站'
            ),
            remark=f'{self.remark()} > 專屬推薦_彈出視窗標題'
        )

    @property
    def accept(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'name == "確認" AND type == "XCUIElementTypeButton"'
            ),
            remark=f'{self.remark()} > 專屬推薦_彈出視窗_確認按鈕'
        )

    @property
    def webview_title(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '外幣匯率'
            ),
            remark=f'{self.remark()} > 專屬推薦_轉跳目標web標題_外幣匯率'
        )


class OpenWebviewNewsPopup(BaseObject):

    def __init__(self):
        super().__init__()
        self.set_remark("保險新知彈出視窗")
        self.driver = DeviceManager.get_driver()

    @property
    def content(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                '前往國泰人壽網站閱讀全文'
            ),
            remark=f'{self.remark()}_彈出視窗標題'
        )

    @property
    def accept(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.IOS_PREDICATE,
                'name == "確認" AND type == "XCUIElementTypeButton"'
            ),
            remark=f'{self.remark()}_彈出視窗_確認按鈕'
        )

    @property
    def webview_url(self):
        return BasicComponent(
            lambda: self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                'www.cathaybk.com.tw'
            ),
            remark=f'{self.remark()}_轉跳目標web_網址欄'
        )
