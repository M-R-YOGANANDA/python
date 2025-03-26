import PyPDF2

with open("Fire station.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    
with open("Fire_station.txt", "w", encoding="utf-8") as output:
    output.write(text)
