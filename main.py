from dataAgent import DataAgent
from classifierAgent import ClassifierAgent
from evaluationAgent import EvaluationAgent
from reportAgent import ReportAgent

def main():
  
    print("\n🔹 Step 1: 載入與清理試題")
    dataAgent = DataAgent()
    df_cleaned = dataAgent.load_and_clean_data()
    if df_cleaned is None:
        return

    print("🔹 Step 2: 試題分類")
    classifierAgent = ClassifierAgent(df_cleaned)  # 傳入試題數據
    categorized_data = classifierAgent.classify_questions()

    print("✅ 試題分類完成")

    # Step 3: 評分與答題記錄
    print("🔹 Step 3: 評分與答題記錄")
    evaluationAgent = EvaluationAgent(categorized_data)  # ✅ 正確：提供 categorized_data
    correct_count, total_count, errors = evaluationAgent.start_test()


    print("\n🔹 Step 4: 產生學習報告")
    reportAgent = ReportAgent()
    reportAgent.generate_report()


if __name__ == "__main__":
    main()
