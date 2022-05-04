from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import io

def add_image():
    in_pdf_file = 'gene_chrom.pdf'
    out_pdf_file = 'gene_chrom_legends.pdf'
    img_file = 'legends_crop.png'

    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    # can.drawString(10, 100, "Hello world")
    x_start = 415
    y_start = 0
    can.drawImage(img_file, x_start, y_start, width=80, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.showPage()
    can.showPage()
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)

    new_pdf = PdfFileReader(packet)

    # read the existing PDF
    existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
    output = PdfFileWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(i))
        output.addPage(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()

add_image()