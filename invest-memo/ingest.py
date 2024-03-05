import PyPDF2

reader = PyPDF2.PdfReader('Hidden Level Market Study 8-31-23.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
test_string = reader.pages[2].extract_text()

print(type(test_string))
