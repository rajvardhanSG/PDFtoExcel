# PDF to Excel Converter

## Explanation

### Approach
This is my first time manipulating PDF files using Python. Although I have experience writing Python code for data analysis and machine learning tasks, I explored online resources for guidance. I discovered `pdftables_api`, `tabula`, and `pdfplumber`, which are used for extracting data from PDF files.

- I found that `pdfplumber` is the most efficient library for extracting tables from PDF files. The program enumerates pages and extracts tables from each page:

  ```python
  pdf = pdfplumber.open(pdf_path)
  for page_no, page in enumerate(pdf.pages, start=1):
      tables = page.extract_tables()
  ```

- The extracted tables are then processed using a `for` loop:
  - Each table is converted to a Pandas DataFrame:
    ```python
    df = pd.DataFrame(table)
    ```
  - A unique Excel file name is generated for each table:
    ```python
    file_path = os.path.join(output_folder, f"table_{table_count}.xlsx")
    ```
  - The DataFrame is saved as an Excel file:
    ```python
    file_path = os.path.join(output_folder, f"table_{table_count}.xlsx")
    ```
- This process is repeated for each page in the PDF, converting each table into an Excel file.

---

## How to Execute

### Direct Execution
1. Download and save all files from the repository.
2. Open a terminal in the folder or navigate to the folder where the files are stored using `cd`.
3. Install `pdfplumber`:
   ```sh
   pip install pdfplumber
   ```
4. Execute the script:
   ```sh
   python PDFtoExcel.py
   ```
5. If you encounter a `FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'output_tables_folder'`, delete the existing `output_tables_folder`.
6. Enter the PDF file path (e.g., `stock_market_dataset.pdf`).
7. Enter the folder path where you want to store the Excel files (e.g., `Provide_your_own_folder_path`).
![image](https://github.com/user-attachments/assets/4392ccaf-2168-410f-a53c-2d185aabb360)

### Using Jupyter Notebook
1. Download and save all files from the repository.
2. Open Jupyter Notebook and upload `PDFtoExcel.ipynb` and `stock_market_dataset.pdf`.
3. Install `pdfplumber` by running the following command in a notebook cell:
   ```sh
   !pip install pdfplumber
   ```
4. After successful installation, run the notebook cell by cell and provide the inputs as mentioned above.
![image](https://github.com/user-attachments/assets/04027f10-7327-434a-9c99-3ea242131636)


