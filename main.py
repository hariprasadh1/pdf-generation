from fpdf import FPDF
import pandas

df = pandas.read_csv("topics.csv", sep=",")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    if row["Pages"] >= 1:
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(236, 130, 49)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1, border=0)

        for y in range(20, 280, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(255)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(120, 120, 120)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for i in range(row["Pages"] - 1):
            pdf.add_page()
            pdf.ln(265)

            pdf.set_font(family="Times", style="I", size=10)
            pdf.set_text_color(160, 160, 160)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

            for y in range(20, 280, 10):
                pdf.line(10, y, 200, y)

pdf.output("output.pdf")

