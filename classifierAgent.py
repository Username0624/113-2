import pandas as pd

class ClassifierAgent:
    def __init__(self, data):
        """初始化分類器，接收清理後的試題 DataFrame"""
        self.data = data

    def classify_questions(self):
        """根據題目內容分類，新增 'category' 欄位"""
        if self.data is None or self.data.empty:
            print("❌ 無法分類：試題資料為空")
            return None

        # 簡單分類邏輯（根據題目類型）
        def categorize(row):
            if "Vocabulary" in row['Category']:
                return "Vocabulary"
            elif "Grammar" in row['Category']:
                return "Grammar"
            elif "General Knowledge" in row['Category']:
                return "General Knowledge"
            elif "Reading" in row['Category']:
                return "Reading"
            elif "Idioms" in row['Category']:
                return "Idioms"
            else:
                return "其他"

        self.data['category'] = self.data.apply(categorize, axis=1)
        print("✅ 試題分類完成！")
        return self.data
