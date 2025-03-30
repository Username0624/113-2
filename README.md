# 113-2
# 41271223H 李宛諭
# 資料結構

## AI 英檢考試複習系統

### 1. 專案概述
本專案是一個基於 AI 代理人架構的英檢考試複習系統，能夠自動載入試題、分類題型、評分並產生學習報告，幫助使用者高效準備英語檢定考試。

### 2. 主要功能
- **試題載入與清理（dataAgent.py）**
  - 讀取 `question_bank.csv` 試題檔案
  - 清理無效數據，格式化內容
- **試題分類（classifierAgent.py）**
  - 根據題型（單字詞彙、文法、閱讀理解等）分類試題
- **考試評分（evaluationAgent.py）**
  - 自動評分使用者的作答紀錄
  - 記錄錯誤與正確答案
- **學習報告生成（reportAgent.py）**
  - 根據考試結果產生個人化學習報告
  
### 3. 系統架構
該系統採用 AI 多代理人架構，每個代理人負責不同的工作，協同完成英檢考試複習流程。

### 4. 環境與安裝
#### 4.1 環境需求
- Python 3.10 或更新版本
- `pip` 套件管理工具

#### 4.2 安裝步驟
1. **Clone 本專案**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **建立虛擬環境並安裝相依套件**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 用 `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. **設置 API Key**
   - 在專案根目錄建立 `.env` 檔案，內容如下：
     ```plaintext
     GEMINI_API_KEY=your_api_key_here
     ```
   - 可從 Google Gemini API 取得金鑰。

### 5. 使用方式
#### 5.1 啟動考試系統
```bash
python main.py
```

#### 5.2 執行流程
1. `dataAgent.py` 讀取並整理試題
2. `classifierAgent.py` 根據題型分類試題
3. `evaluationAgent.py` 負責評分與答題記錄
4. `reportAgent.py` 生成學習報告


