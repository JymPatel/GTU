import os
import sys

FORCED = False
if "--force" in sys.argv:
    print("Forcing conversion...")
    FORCED = True


# Function to convert .ipynb to PDF
def convert_ipynb_to_pdf(input_file):
    os.system(f"jupyter nbconvert --to pdf {input_file} --template=hide_header")


# Get a list of all .ipynb files in the current directory
notebooks = [file for file in os.listdir() if file.endswith('.ipynb')]
pdfs = [file for file in os.listdir() if file.endswith('.pdf')]

# Loop through the list and convert each notebook to PDF
for notebook in notebooks:
    pdf_filename = os.path.splitext(notebook)[0] + '.pdf'
    if pdf_filename in pdfs and not FORCED:
        continue
    convert_ipynb_to_pdf(notebook)
    print(f'Converted {notebook} to {pdf_filename}')
