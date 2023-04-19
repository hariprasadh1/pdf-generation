from fpdf import FPDF
import pandas

df = pandas.read_csv("topics.csv", sep=",")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    if row["Pages"] >= 1:
        pdf.add_page()
        pdf.set_font(family="Times", style="I", size=24)
        pdf.set_text_color(236, 130, 49)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1, border=0)
        pdf.line(10, 21, 200, 21)
        while row["Pages"] - 1 > 0:
            pdf.add_page()
            row["Pages"] -= 1


pdf.output("output.pdf")

