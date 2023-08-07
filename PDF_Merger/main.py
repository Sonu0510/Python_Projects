import PyPDF2

pdfiles = ["Diploma.pdf", "Advanced_diploma.pdf"]
merger = PyPDF2.PdfMerger()
for file in pdfiles:
    pdfFile = open(file, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("Advanced_diploma_And_diploma.pdf")