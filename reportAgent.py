import pandas as pd

class ReportAgent:
    def __init__(self, result_file="test_results.csv"):
        self.result_file = result_file

    def generate_report(self):
        print("📊 產生學習報告...")
        df = pd.read_csv(self.result_file)

        total_questions = len(df)
        correct_count = sum(df["Your Answer"].str.lower() == df["Correct Answer"].str.lower())

        accuracy = round((correct_count / total_questions) * 100, 2)
        print(f"📈 你的答對率: {accuracy}%")

        # 找出錯誤的題目
        wrong_answers = df[df["Your Answer"].str.lower() != df["Correct Answer"].str.lower()]
        if not wrong_answers.empty:
            print("\n❌ 你答錯的題目：")
            print(wrong_answers[["Question", "Your Answer", "Correct Answer"]])

        print("\n✅ 學習報告已生成！")
