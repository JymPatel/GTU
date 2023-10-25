import PyPDF2
from PyPDF2.pdf import PageObject
from PyPDF2.pdf import writer
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def add_roll_number(input_pdf, output_pdf, roll_number):
    # Create a PDF canvas to generate a roll number page
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    width, height = letter
    c.drawString(width - 100, height - 30, f"Roll Number: {roll_number}")
    c.save()

    # Move the packet's cursor to the beginning
    packet.seek(0)
    new_pdf = PyPDF2.PdfFileReader(packet)

    # Open the input PDF and create the output PDF
    input_pdf_reader = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
    output_pdf_writer = writer.PdfFileWriter()

    # Iterate through each page and merge with the roll number
    for page_num in range(input_pdf_reader.getNumPages()):
        page = input_pdf_reader.getPage(page_num)
        page.mergePage(new_pdf.getPage(0))
        output_pdf_writer.addPage(page)

    # Save the final PDF with the roll number
    with open(output_pdf, 'wb') as output_file:
        output_pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf = "input.pdf"  # Replace with your input PDF file
    output_pdf = "output.pdf"  # Replace with the desired output file name
    roll_number = "123456"  # Replace with your roll number

    add_roll_number(input_pdf, output_pdf, roll_number)
