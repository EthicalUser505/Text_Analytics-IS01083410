import PyPDF2

# Read the PDF file
with open('Business_Proposal.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Extract text from page 2 (index 1)
    page_2_text = reader.pages[1].extract_text()

# Print the extracted text
print("Extracted Page 2 Text:\n", page_2_text)

# Save the extracted text to a file
with open('business_proposal_page_2.txt', 'w', encoding='utf-8') as output:
    output.write(page_2_text)
