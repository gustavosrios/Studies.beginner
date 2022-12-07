import PyPDF2
f = open('Working_Business_Proposal.pdf','rb')
all_pages = open('PDF_all_pages.pdf','wb')
pdf_writer = PyPDF2.PdfFileWriter()
pdf_reader = PyPDF2.PdfFileReader(f)
#page = pdf_reader.getPage(0)
#page_text = page.extractText()
i=0
while True:
    page = pdf_reader.getPage(i)
    page_text = page.extractText()
    if page_text != '':
        pdf_writer.addPage(page)
        pdf_writer.write(all_pages) 
        i+=1
        continue
    else:
        break   
f.close()
all_pages.close()


import PyPDF2
f = open('Working_Business_Proposal.pdf','rb')
all_pages = open('PDF_all_pages02.pdf','wb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_text = []
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_writer.addPage(page)
    pdf_writer.write(all_pages)
    pdf_text.append(page.extractText())
for text in pdf_text:
    print(text)
f.close()
all_pages.close()


import re 
import PyPDF2
pattern = r'\d{3}.\d{3}.\d{4}' #r'(\d{3})(\d{3})(\d{4})'
all_text = ''
f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
for i in range(pdf_reader.numPages):
    page = pdf_reader.getPage(i)
    page_text = page.extractText()
    all_text = all_text+' '+page_text
    for match_obj in re.finditer(pattern,all_text):
        print(match_obj.group())
f.close()
