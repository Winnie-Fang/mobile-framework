# MCP / Copilot 測試案例撰寫規範（完整版）

本文件定義 MCP / Copilot 在自動化測試流程中，
**如何讀取測試案例、如何執行 App、以及如何產出符合測試框架的測試腳本**。

---

## 一、AI 角色定義（強制）

MCP / Copilot 在本流程中 **僅作為測試案例產生器**，不是框架設計者。

你必須：
- 嚴格遵守既有測試框架（最高優先）
- 產出可直接使用的測試腳本（不可要求人工補齊）
- 不得自行設計新架構、不得簡化流程、不得偏離分層規則

---

## 二、輸入來源說明

MCP / Copilot 會同時讀取以下三類輸入：

### 1) 測試案例描述（testcases.md）
- 只允許讀取並執行 **第 1 條測試案例**
- 用於理解測試目標與操作流程
- 不代表最終程式碼結構（程式碼結構以框架規範為準）

### 2) 元素定位規範（locator_2.md）
- 定義 locator 的允許寫法與限制（包含優先順序與禁止事項）
- **只影響 locator 選擇**，不得影響測試流程設計

### 3) 測試框架撰寫指南（自動化測試腳本撰寫指南.md，最高優先）
- 定義 Page / Component / Test 分層
- 定義命名、回傳型態、使用方式（含 Navigator 用法）
- 若與其他文件衝突，**一律優先採用**

---

## 三、輸入檔案讀取順序與處理規則（強制）

### 3.1 讀取順序（不可變更）
1. `testcases.md`
2. `locator_2.md`
3. `自動化測試腳本撰寫指南.md`（最高優先）

### 3.2 衝突處理優先順序（由高到低）
1. 測試框架撰寫指南
2. locator 規範
3. 測試案例描述

當三者衝突時：
- 必須直接捨棄低優先序內容
- 不得嘗試融合或自創折衷方案

### 3.3 資訊不足處理方式（強制）
若無法依框架規範正確產碼，必須停止並回傳以下其中之一：
- 「需要補充測試框架資訊」
- 「需要補充測試案例細節」
- 「需要補充元素定位規範」

不得自行假設或補齊。

---

## 四、Appium MCP 執行階段規則

MCP 在手機上執行測試案例時：

### 4.1 MCP 只負責
- 依 `testcases.md` 第 1 條案例執行操作
- 擷取指定元素的實際狀態或內容（例如 text / value / enabled / visible / found_count 等）

### 4.2 MCP 不得
- 依 UI dump 自行設計 locator
- 將執行細節直接寫入測試腳本（Test / Page 程式碼不得被 UI dump 汙染）
- 因為「執行成功」而忽略框架分層規則

> 執行結果僅作為產碼參考，用來確認元素狀態與流程可行性，不作為程式碼結構依據。

---

## 五、測試腳本產出原則（核心）

### 5.1 一律從 Page 開始
- 所有 UI 操作必須封裝於 Page
- Test 不得直接操作 driver / locator / wait
- 驗證應基於 Page 回傳的 Component 或可驗證結果

---

### 5.2 Page 撰寫規範（強制）
Page 必須：
- 繼承 `BaseObject`
- 支援 `__init__(role=None)`（多裝置可用 role）
- 封裝 locator / wait / 行為方法（click / input / verify）
- 方法回傳 Component（例如 `BasicComponent(...)`）

Page 不得：
- 撰寫 assert
- 描述測試流程（流程屬於 Test）
- 在 Page 內判斷主/副裝置（角色判斷屬於 Test）

---

### 5.3 單裝置 / 多裝置原則（強制）

#### 單裝置
- Page 初始化不指定 role（或 role=None）
- Page 內自行完成等待、定位與操作封裝
- Test 只呼叫 Page 方法，不寫 UI 細節

#### 多裝置
- Page 的 `__init__` 必須可接收 role（例如 `"old"` / `"new"`）
- 同一 Page 類別可被不同 role 重複實例化
- Page 不得判斷角色，流程順序只存在於 Test

---

## 六、Test / Case 撰寫規範（強制）

Test 只能做三件事：
1. 初始化 Page（必要時指定 role）
2. 呼叫 Page 方法
3. 驗證 Page 回傳結果

Test 禁止事項：
- 直接使用 driver
- 撰寫 locator
- 等待元素（WebDriverWait 等只能出現在 Page/Component）
- 在 Test 中實作 Page 行為（UI 細節必須封裝回 Page）

---

## 七、Navigator 註冊 / 掛載規則（貼合實作，強制）

本框架的 Page 存取入口為：
- `Navigator().<platform>.<lang>.<page_key>`（單裝置）
- `Navigator().<platform>.<lang>.<page_key>_mu(role)`（多裝置）

因此：**新增 Page 類別後，必須同步在 Navigator 層完成註冊 / 掛載，否則 TestCase 無法直接呼叫。**

---

### 7.1 單裝置 Page 註冊方式（@property + lazy cache，強制）
在 `Navigator<Platform><Lang>`（例如 `NavigatoriOSZh` / `NavigatorAndroidZh`）內：
- 以 `@property` 提供 page 存取點（`page_key`）
- 使用私有欄位快取 Page instance（lazy init）
- 建立 Page 時不得傳 role（單裝置）

強制規則：
- 新增單裝置 Page `XxxPage` → 必須新增對應：
  - `self.__<page_key> = None`（或等效快取欄位）
  - `@property def <page_key>(...) -> XxxPage: ...`

---

### 7.2 多裝置 Page 註冊方式（*_mu(role) + dict cache，強制）
在 `Navigator<Platform><Lang>` 內：
- 以 dict 快取不同 role 的 Page instance
- 提供 `def <page_key>_mu(self, role: str) -> <MultiDevicePage>` 方法
- 建立 Page 時必須傳入 role（多裝置）

強制規則：
- 新增多裝置 Page `MUxxxPage` → 必須新增對應：
  1) `self.__<page_key>_mu = {}`（快取 dict）
  2) `def <page_key>_mu(self, role: str) -> MUxxxPage: ...`

命名強制：
- 多裝置存取方法一律使用 `_mu` 後綴
- role 由 Test 決定（例：`"old"` / `"new"`）

---

### 7.3 TestCase 使用 Navigator 的強制規則
- TestCase 必須優先使用 `navigator = Navigator().<platform>.<lang>` 取得入口
- 單裝置呼叫：
  - `navigator.<page_key>.<action>()`
- 多裝置呼叫：
  - `navigator.<page_key>_mu("<role>").<action>()`

---

### 7.4 禁止繞過框架（強制）
- 禁止在 TestCase 直接 `new Page()` 取代 Navigator（除非框架文件明確允許）
- 禁止在 TestCase 直接操作 driver / locator / wait
- 禁止自行發明 Navigator 註冊模式（必須遵循：單裝置 `@property`、多裝置 `*_mu(role)`）

---

## 八、產出物清單與命名規則（強制）

### 8.1 必產出物（不可缺）
處理 `testcases.md` 第 1 條案例後，必須產出：
1. **Locator JSON**（符合 `locator_2.md` 規範，且若規範要求 JSON-only 輸出則不得夾帶說明）
2. **Page 程式碼**（新增或擴充 Page）
3. **Navigator 註冊/掛載更新**（確保 `Navigator().<platform>.<lang>` 可存取新 Page）
4. **TestCase 程式碼**（功能導向命名）

---

### 8.2 Page 命名規則（維持既有風格）
- 類別命名：PascalCase
- 必須包含平台前綴：`iOS` / `Android`（或專案既有縮寫規則）
- 結尾必須為 `Page`
- 命名以「畫面/功能」描述（沿用既有專案慣例）

範例：
- `iOSLoginPage`
- `AndroidTransferPage`
- `MUiOSOTPage`（多裝置 Page 沿用既有命名慣例）

> Page 檔名若專案已有既定規則，必須遵守現況；若無，建議使用 snake_case 對應類別名稱。

---

### 8.3 TestCase 命名規則（功能導向，強制）
- 檔名：snake_case
- 以功能/情境命名（不要以 Page 類別名為主）
- 建議以 `test_` 開頭（符合 pytest 習慣）

範例：
- `test_login_success.py`
- `test_transfer_insufficient_balance.py`
- `test_otp_multi_device_approve.py`

---

## 九、產出限制與錯誤處理（強制）

- 不得產出框架未定義的寫法
- 不得補假資料或自行假設流程
- 不得為了可跑而破壞分層設計（Page/Component/Test 必須維持）
- 若資訊不足，必須停止並回傳指定訊息（見 3.3）

---

## 最終目標

> MCP / Copilot 產出的 Page、Navigator 註冊更新、TestCase  
> 必須在 **不修改測試框架** 的前提下可直接執行。
