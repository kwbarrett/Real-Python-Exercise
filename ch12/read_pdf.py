from PyPDF2 import PdfFileReader


file_path = "C:/Users/kenneth.barrett/Downloads/1342-pdf.pdf"
input_pdf = PdfFileReader(file_path)

print(input_pdf.getNumPages())
document_info = input_pdf.getDocumentInfo()
print(document_info)

print(type(document_info))

print(document_info.title)
print(document_info.author)

page0 = input_pdf.getPage(0)

print(page0.extractText())
for page in input_pdf.pages:
    print(page.extractText())