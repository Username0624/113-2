import pandas as pd

class EvaluationAgent:
    def __init__(self, filename="classified_questions.csv"):
        self.filename = filename
        self.results = []

    def start_test(self):
        print("📝 開始測驗！")
        df = pd.read_csv(self.filename)

        score = 0
        total_questions = len(df)

        for index, row in df.iterrows():
            print(f"🔹 題目 {index + 1}: {row['Question']}")
            user_answer = input("✏ 你的答案: ")

            if user_answer.strip().lower() == str(row["Answer"]).strip().lower():
                print("✅ 正確！")
                score += 1
            else:
                print(f"❌ 錯誤，正確答案是: {row['Answer']}")

            self.results.append({"Question": row["Question"], "Your Answer": user_answer, "Correct Answer": row["Answer"]})

        print(f"\n🎯 測驗結束！你的分數: {score}/{total_questions}")

        # 存檔
        self.save_results(score, total_questions)

    def save_results(self, score, total):
        df_results = pd.DataFrame(self.results)
        df_results.to_csv("test_results.csv", index=False)
        print("✅ 測驗結果已存至 `test_results.csv`")
