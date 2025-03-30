import pandas as pd

class DataAgent:
    def __init__(self, filename="question_bank.csv"):
        self.filename = filename
        self.cleaned_filename = "cleaned_questions.csv"

    def load_and_clean_data(self):
        print("📂 載入試題...")
        try:
            df = pd.read_csv(self.filename, encoding="utf-8", on_bad_lines="skip")  # 跳過格式錯誤的行
            df.dropna(inplace=True)  # 移除空白行
            df.to_csv(self.cleaned_filename, index=False)  # 存回清理後的 CSV
            print(f"✅ 試題清理完成，存至 `{self.cleaned_filename}`")
            return df
        except FileNotFoundError:
            print("❌ 錯誤：找不到 `question_bank.csv`，請確認檔案是否存在。")
            return None
