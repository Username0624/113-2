import pandas as pd

class DataAgent:
    def __init__(self, file_path="question_bank.csv"):
        self.file_path = file_path

    def load_and_clean_data(self):
        """載入並清理試題"""
        print("🔹 Step 1: 載入與清理試題")
        try:
            df = pd.read_csv(self.file_path)  # 讀取 CSV
            df.dropna(inplace=True)  # 移除空值
            df.reset_index(drop=True, inplace=True)
            print("✅ 試題載入完成，共 {} 題".format(len(df)))
            return df
        except Exception as e:
            print(f"❌ 錯誤：{e}")
            return None
