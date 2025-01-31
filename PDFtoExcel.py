import pandas as pd
import pdfplumber
import os

def tableExtractor(pdf_path, output_folder):
    if not os.path.exists(pdf_path):
            print(f"Error: File '{pdf_path}' not found.")
            return
        
    if not os.path.exists(output_folder):
            output_folder = "output_tables_folder"
            os.makedirs(output_folder)
            print(f"Warning: File '{output_folder}' not found, hence folder named: 'output_tables_folder' created")
            
    pdf = pdfplumber.open(pdf_path)
    
    if len(pdf.pages) == 0:
            print("Error: This PDF is empty.")
            return
    
    table_count = 0
    for page_no, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()
        
        if not tables:
            continue
            
        for table in tables:
            if table:
                table_count += 1
                df = pd.DataFrame(table)
                
                file_path = os.path.join(output_folder, f"table_{table_count}.xlsx")
                
                df.to_excel(file_path, index=False, header=False)
                print(f"Extracted Table {table_count} from Page {page_no} -> {file_path}")
                
    print(f"Extraction complete. {table_count} tables saved in '{output_folder}'.")

pdf_path = str(input("Enter the path of PDF file: "))
output_folder = str(input("Enter the folder path for excel files: "))
tableExtractor(pdf_path, output_folder)
