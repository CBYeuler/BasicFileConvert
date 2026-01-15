from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def convert(txt_path, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    y = height - 40

    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            c.drawString(40, y, line.strip())
            y -= 15
            if y < 40:
                c.showPage()
                y = height - 40

    c.save()
