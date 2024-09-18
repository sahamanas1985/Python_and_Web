import fitz
 
# Open the PDF file
pdf_path = "TR.pdf"
pdf_document = fitz.open(pdf_path)

target_page_number = 2
target_page = pdf_document[target_page_number]

rect_coordinate = (30, 730, 300, 800)
target_page.draw_rect(rect_coordinate, color=(0,1,0), width=2, fill=(0,1,0), overlay = True)

 
# Save the changes to a new PDF file
output_pdf_path = "rectangulos_modificados.pdf"
pdf_document.save(output_pdf_path)

print("Done!")