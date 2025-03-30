import pandas as pd

class ClassifierAgent:
    def __init__(self, filename="cleaned_questions.csv"):
        self.filename = filename

    def classify_questions(self):
        print("📂 試題分類中...")
        df = pd.read_csv(self.filename)

        # 根據關鍵字分類
        df["Type"] = df["Question"].apply(self.get_question_type)

        # 儲存分類後的檔案
        df.to_csv("classified_questions.csv", index=False)
        print("✅ 試題分類完成，存至 `classified_questions.csv`")
        return df

    def get_question_type(self, question):
        if "Fill in the blank" in question:
            return "填空題"
        elif "synonym" in question or "meaning of" in question:
            return "單字詞彙"
        else:
            return "選擇題"
