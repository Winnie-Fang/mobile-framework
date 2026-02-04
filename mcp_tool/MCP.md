# Appium 元素定位規範（MCP / Copilot 強制）

## 1. 定位優先順序

### iOS

1. accessibility id
2. iOS Class Chain
3. iOS Predicate
4. name / id（非顯示文字）
5. XPath（最後手段）

### Android

1. accessibility id
2. resource-id（By.ID）
3. Android UIAutomator
4. XPath（最後手段）

---

## 2. XPath 強制規範（違反即錯）

- 嚴禁使用純 index：
    - ❌ `EditText[1]`
    - ❌ `TextField[2]`

- XPath **必須使用 Anchor + 相對定位**
- Anchor 必須為標題 / label / 描述文字
- 必須限制搜尋範圍（同容器優先）
- 能用 accessibility id / resource-id 時不得使用 XPath

---

## 標準 XPath 範例（必須遵循）

### Android

```xpath
//*[contains(@text,"使用者密碼")]
  /parent::*
  //android.widget.EditText
```

## 任務輸出規格（必須）

- 獲取測試執行的元素（每個元素包含：名稱/畫面描述/可能的錨點文字）
- 你必須為每個元素產出對應的 **locator**
- 每個 locator 必須包含：
    - platform：Android / iOS
    - strategy：AppiumBy.XXX
    - selector：對應字串

## name 命名規範（用途型，必須遵守）

- `name` 必須為「用途型中文」：`<動作/用途><元件類型>`
    - 範例：`登入按鈕`、`密碼輸入框`、`使用者名稱輸入框`、`錯誤提示文字`、`返回按鈕`
- `name` 禁止使用程式命名（如 `userNameTextView`）或英文

###  輸出格式（擇一，預設用 JSON）

```json
[
  {
    "name": "登入按鈕",
    "platform": "Android",
    "strategy": "AppiumBy.ID",
    "selector": "com.cathaybk.geb.cubuat:id/sloganTextView"
  }
]
```

##輸出檔案
- 請將輸出結果存為 `locator_output.json` ，路徑為：/mobile-framework/mcp_tool/locator附加於任務回覆中