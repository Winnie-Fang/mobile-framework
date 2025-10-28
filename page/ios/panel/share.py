from huskypo import By, Element, Elements
from huskypo_extension import Page


class Share(Page):

    panel = '分享面板'

    close_button = Element(By.ACCESSIBILITY_ID, '關閉')
    content_view = Element(By.ACCESSIBILITY_ID, 'UIActivityContentView')

    def waits(self):
        return [self.content_view.wait_present(), self.airdrop_text.wait_present()]

    insert_msg_texts = 'name BEGINSWITH "I have transferred " OR label BEGINSWITH "我已經從國泰世華銀行" OR label CONTAINS "Cathay United Bank Account"'
    insert_msg_tx_success = Element(By.IOS_PREDICATE, insert_msg_texts)
    get_withdrawal_password_messege = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeOther[`name CONTAINS "請跟我索取密碼"`][2]',
        remark='太好轉分享頁面文本')

    airdrop_cell = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[`label == "AirDrop"`]', remark='AirDrop區塊')
    airdrop_text = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "AirDrop"`]')
    message_cell = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[`label == "訊息"`]', remark='訊息區塊')
    message_text = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "訊息"`]')

    windows = Elements(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow')

    copy_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[`label == "拷貝"`]', remark='拷貝按鈕')

    app_message_name = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "訊息"`]', remark='訊息app')
    app_message_body = Element(By.ACCESSIBILITY_ID, 'messageBodyField', remark='訊息app輸入框')
    app_message_cancel = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "取消"`]', remark='訊息app取消鈕')
