import pandas as pd
from fpdf import FPDF 



class PDF(FPDF):
    def header(self):
        """設定 PDF 標題"""
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Test Results Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        """設定頁尾"""
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf(csv_file="test_results.csv", pdf_file="test_results.pdf"):
    try:
        # 讀取 CSV
        df = pd.read_csv(csv_file)

        # 確保 CSV 內含必要欄位
        required_columns = {"Question", "Your Answer", "Correct Answer", "Category"}
        if not required_columns.issubset(df.columns):
            print("❌ CSV 檔缺少必要欄位！請檢查資料格式。")
            return

        # 創建 PDF 物件
        pdf = PDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "", 12)

        # 表格標題
        pdf.set_fill_color(200, 220, 255)  # 淺藍背景
        pdf.cell(50, 10, "Question", border=1, fill=True)
        pdf.cell(50, 10, "Your Answer", border=1, fill=True)
        pdf.cell(50, 10, "Correct Answer", border=1, fill=True)
        pdf.cell(40, 10, "Category", border=1, fill=True)
        pdf.ln()

        # 輸出測驗結果
        for _, row in df.iterrows():
            pdf.cell(50, 10, str(row["Question"]), border=1)
            pdf.cell(50, 10, str(row["Your Answer"]), border=1)
            pdf.cell(50, 10, str(row["Correct Answer"]), border=1)
            pdf.cell(40, 10, str(row["Category"]), border=1)
            pdf.ln()

        # 儲存 PDF
        pdf.output(pdf_file)
        print(f"✅ PDF 生成成功：{pdf_file}")

    except FileNotFoundError:
        print("❌ 找不到 test_results.csv，請先確保檔案存在！")
    except Exception as e:
        print(f"❌ 發生錯誤：{e}")

if __name__ == "__main__":
    generate_pdf()
