import pandas as pd

class EvaluationAgent:
    def __init__(self, categorized_data):
        """初始化評分代理人，接收已分類的試題 DataFrame"""
        self.data = categorized_data
        self.results = []  # 存儲測試結果

    def start_test(self):
        correct_count = 0
        total_count = 0
        errors = []

        """執行測驗，讓使用者回答問題，並記錄答案是否正確"""
        if self.data is None or self.data.empty:
            print("❌ 無法開始測試：試題資料為空")
            return None

        print("📌 測試開始！請輸入你的答案：")
        for index, row in self.data.iterrows():
            print(f"\n題目 {index + 1}: {row['Question']}")
            print(f"A. {row['OptionA']}  B. {row['OptionB']}  C. {row['OptionC']}  D. {row['OptionD']}")

            # 輸入驗證，確保答案為 A, B, C, D
            while True:
                user_answer = input("你的答案 (A/B/C/D)：").strip().upper()
                if user_answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("❌ 無效的選項，請重新輸入 A、B、C 或 D")

            total_count += 1
            correct = (user_answer == row['Answer']) 
            if correct:
                correct_count += 1
            else:
                errors.append(row)

            self.results.append({
                'Question': row['Question'],
                'Your Answer': user_answer,
                'Correct Answer': row['Answer'],
                'Category': row['Category'],
                'is_correct': correct  # 加入 is_correct 欄位
            })

        # 儲存結果至 CSV
        df = pd.DataFrame(self.results)
        df.to_csv("test_results.csv", index=False)
        print("✅ 測驗結果已儲存到 test_results.csv")

        print("\n✅ 測試完成！")
        return correct_count, total_count, errors
