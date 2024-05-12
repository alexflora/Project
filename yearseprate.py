import re
import pdfplumber
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def should_skip_line(line):
    skip_prefixes = [
        "Result Gally Sheet",
        "College :",
        "College:",
        "College",
        "Course",
        "No of Papers",
        "No. of Papers",
        "Total Paper(s) :",
        "THIRUVALLUVAR",
        "SubCode",
        "UG",
        "Sub Code ",
        "Int",
        "NOTE",
        "UNIVERSITY",
        "ELIGIBLE",
        "NR",
        "*",
    ]
    return any(line.startswith(prefix) for prefix in skip_prefixes)

def normalize_mark(mark):
    if mark in ('---', '-'):
        return 'NA'
    elif mark in ('WHI', 'WHE'):
        return mark
    else:
        # Ensure marks are three digits
        return str(mark).zfill(3)

def extract_student_data(lines):
    student_data_list = []
    register_number = ""
    student_name = ""
    subjects = {}

    for line in lines:
        # Skip lines that should be removed
        if should_skip_line(line):
            continue

        subject_matches = re.findall(r'(\d*[A-Z]+\s?\d+\s?[A-Z]*\s?\d*)\s+(-{1,3}|\d+|A{3}|WHE|WHI)\s+(-{1,3}|\d+|A{3}|WHE|WHI)\s+(-{1,3}|\d+|A{3}|WHE|WHI)\s+(PASS|RA|(?:A{3}|WHE|WHI))', line)
        if subject_matches:
            for match in subject_matches:
                subject_code = match[0].replace(" ", "")
                internal_mark = normalize_mark(match[1])
                external_mark = normalize_mark(match[2])
                total_mark = normalize_mark(match[3])
                status = match[4] if match[4] != '---' else 'NA'

                # Create a dictionary for the current subject
                subjects[subject_code] = total_mark

        # Extract and format the register number and student name
        match_register = re.search(r'(\d{3}\d{2}[A-Z]\d{5})\s+(.+)', line)
        if match_register:
            if student_name:  # If there is student data, save it
                student_data = {
                    "Register Number": register_number,
                    "Student Name": student_name,
                    **subjects,  # Flatten subject data
                }
                student_data_list.append(student_data)
                subjects = {}  # Reset subjects
            register_number, student_name = match_register.groups()

    if student_name:  # If there is student data, save it
        student_data = {
            "Register Number": register_number,
            "Student Name": student_name,
            **subjects,  # Flatten subject data
        }
        student_data_list.append(student_data)

    return student_data_list

# Open the PDF file
pdf_path = r"C:\pythonprogram\PDFCONVERT\BBA.pdf"
with pdfplumber.open(pdf_path) as pdf:
    all_student_data = {}
    lines_buffer = []
    year = None

    for page in pdf.pages:
        page_text = page.extract_text()
        lines = page_text.splitlines()

        for line in lines:
            match_register = re.search(r'(\d{3}\d{2}[A-Z]\d{5})\s+(.+)', line)
            if match_register:
                if lines_buffer:
                    student_data = extract_student_data(lines_buffer)
                    if year not in all_student_data:
                        all_student_data[year] = []
                    all_student_data[year].extend(student_data)
                    lines_buffer = []
                
                register_number, student_name = match_register.groups()
                year = register_number[3:5]

                # Filter and store only the register numbers that match the pattern "U09"
                if "U09" or "U18" or "P15" or "P02"in register_number:
                    lines_buffer.append(line)
            elif lines_buffer:
                lines_buffer.append(line)

    # Process the last student's data
    if lines_buffer:
        student_data = extract_student_data(lines_buffer)
        if year not in all_student_data:
            all_student_data[year] = []
        all_student_data[year].extend(student_data)

# Create an Excel writer object
excel_file_name = "BBA.xlsx"
with pd.ExcelWriter(excel_file_name, engine="openpyxl") as writer:
    if "Sheet" in writer.book.sheetnames:
        writer.book.remove(writer.book["Sheet"])

    for year, student_data in all_student_data.items():
        df_year = pd.DataFrame(student_data)
        sheet = year

        data = []
        data.append(df_year.columns.tolist())
        for row in dataframe_to_rows(df_year, index=False, header=False):
            data.append(row)

        writer.book.create_sheet(title=sheet)
        sheet = writer.book[sheet]
        for row_data in data:
            sheet.append(row_data)

print("Success")
