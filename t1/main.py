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

    print("\n🔹 Step 2: 試題分類")
    classifierAgent = ClassifierAgent()
    df_classified = classifierAgent.classify_questions()

    print("\n🔹 Step 3: 開始測驗")
    evaluationAgent = EvaluationAgent()
    evaluationAgent.start_test()

    print("\n🔹 Step 4: 產生學習報告")
    reportAgent = ReportAgent()
    reportAgent.generate_report()

if __name__ == "__main__":
    main()
