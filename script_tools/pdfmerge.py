from pypdf import PdfWriter


merger = PdfWriter()

for pdf in ["intenso_ssd.pdf", "lufter.pdf"]:
    merger.append(pdf)

merger.write("bestellung.pdf")
merger.close()
