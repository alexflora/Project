# Import libraries
import requests
from bs4 import BeautifulSoup
import pdfplumber
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter

# URL from which pdfs to be downloaded
url = "https://www.tvu.edu.in/wp-content/uploads/2017/06/PG_apr-may17.pdf"
local_path = "C:\pythonprogram\sample.pdf"

headings = []
print(headings)
table_data = []
start_table = False

try:
    # Send an HTTP GET request to the PDF URL
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Open the local file for writing in binary mode
        with open(local_path, "wb") as file:
            # Write the content of the response (PDF content) to the local file
            file.write(response.content)
        print(f"PDF file downloaded and saved to {local_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

with pdfplumber.open(local_path) as pdf:
     #pdf = PdfReader(local_path)
     for page_number in range(len(pdf.pages)):
         
        # Select the current page
        page = pdf.pages[page_number]

        # Extract text content from the page
        text = page.extract_text()
        #table = page.extract_table()
        #images = page.images

        
        lines = text.split('\n')
        
        if lines:
                headings = lines[0].split('\t')
                

        for line in lines:
            # You need to define some criteria to detect the start and end of the table
            # For example, you might look for specific keywords or patterns.
            if "REG_NO" in line and "STUDENT_NAME" in line and "PAPER_CODE" in line and "TOTAL" in line and "RESULT" in line:
                start_table = True
                continue

            if start_table:
            # Split the line into columns using a delimiter (e.g., tab or comma)
                columns = line.split('\t')  # Adjust the delimiter as needed
                # Append the columns to the table_data list
                table_data.append(columns)
    

df = pd.DataFrame(table_data)
#print(pd.DataFrame(table[1:], columns=table[0]))
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df.fillna(0, inplace=True)
df.drop_duplicates(subset="STUDENT_NAME", keep="first")
df.drop("EXAM")

url_xl=r'C:\pythonprogram\Book1.xlsx'
df.to_excel(url_xl,index=False)
print("Successfully convert from PDF to spreed sheet")
