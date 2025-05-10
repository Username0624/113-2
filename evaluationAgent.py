import pandas as pd

class EvaluationAgent:
    def __init__(self, categorized_data):
        """初始化評分代理人，接收已分類的試題 DataFrame"""
        self.data = categorized_data.reset_index(drop=True)  # 確保有連續 index
        self.results = []  # 存儲測試結果（使用者答題與對錯）
        self.current_index = 0  # 指示目前正在作答的題號

    def get_total_questions(self):
        return len(self.data)

    def get_question(self, index):
        """根據 index 取得某一題資料（題目與選項）"""
        if 0 <= index < len(self.data):
            row = self.data.iloc[index]
            return {
                'index': index,
                'question': row['Question'],
                'options': {
                    'A': row['OptionA'],
                    'B': row['OptionB'],
                    'C': row['OptionC'],
                    'D': row['OptionD']
                }
            }
        else:
            return None

    def record_answer(self, index, user_answer):
        """記錄某一題的使用者答案與正確與否"""
        if 0 <= index < len(self.data):
            row = self.data.iloc[index]
            correct = (user_answer == row['Answer'])

            self.results.append({
                'Question': row['Question'],
                'Your Answer': user_answer,
                'Correct Answer': row['Answer'],
                'Category': row['Category'],
                'is_correct': correct
            })
            return correct
        return False

    def evaluate(self):
        """整理答題結果與錯誤題目"""
        correct_count = sum(1 for r in self.results if r['is_correct'])
        total_count = len(self.results)
        errors = [r for r in self.results if not r['is_correct']]

        # 儲存結果至 CSV
        df = pd.DataFrame(self.results)
        df.to_csv("test_results.csv", index=False)

        return correct_count, total_count, errors
