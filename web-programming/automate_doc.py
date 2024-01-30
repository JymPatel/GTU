import os
from weasyprint import HTML, CSS
import tempfile

assignment_dir = 'html'

html_files = [f for f in os.listdir(assignment_dir) if f.endswith('.html')]

for html_file in html_files:
    html_path = os.path.join(assignment_dir, html_file)
    title = os.path.splitext(html_file)[0]

    with open(html_path, 'r') as f:
        content = f.read()
        
    # Extract aim 
    aim = content.split('-->')[0].replace('<!--', '').strip()
    
    # Escape HTML tags in code
    code = content.replace('<', '&lt;').replace('>', '&gt;')

    pdf_path = os.path.join(assignment_dir, f'{title}.pdf')
    
    html = HTML(string=f'''
    <h1>{title}</h1>
    <p style="font-size: 18px;"><b>Aim:</b> {aim}</p>
    <div class="code">
      <pre style="font-family: monospace;">{code}</pre>
    </div>
    <div class="preview">
      {HTML(string=content).render()}
    </div>
    ''')

    css = CSS(string='''
        @page {{
            size: A4 landscape;
            margin: 2cm;
        }}
        .code {{
            background-color: #f5f5f5;
            padding: 10px;
        }}
    ''')

    with open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(html.write_pdf(stylesheets=[css]))

print('Assignment PDFs saved')