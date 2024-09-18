import os
import fitz
 
# Folder path containing PDF files
folder_path = "./"
 
# Iterate through all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(folder_path, f"PharmaSUG_{filename}")
 
        # Open the PDF file and create a handle
        file_handle = fitz.open(input_file)
 
        # Delete the last page (indexing starts from 0)
        last_page_index = file_handle.page_count - 1
        file_handle.delete_page(last_page_index)
 
        # Save the modified file
        file_handle.save(output_file)
        file_handle.close()
 
        print(f"Last page removed from {filename}. Modified file saved as {output_file}")
