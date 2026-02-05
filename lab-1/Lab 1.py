import PyPDF2

# Read the PDF file
with open('lab-1/Business_Proposal.pdf', 'rb') as file:
 reader = PyPDF2.PdfReader(file)
 text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

# Print the extracted text
print("Extracted PDF Text:\n", text)

# Store the extracted text in a file
with open('business_proposal_all.txt', 'w', encoding='utf-8') as output:
 output.write(text)
