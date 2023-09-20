import re
import pdfplumber

def should_skip_line(line):
    skip_prefixes = [
        "Result Gally Sheet",
        "College :",
        "College:",
        "Course",
        "No of Papers",
        "No.of Papers",  # Added a comma to separate this item
        "SubCode",
        "Int",
        "NOTE",
        "UNIVERSITY",
        "*",
    ]
    return any(line.startswith(prefix) for prefix in skip_prefixes) or "No. of Papers" in line

# Create an empty list to store student data
student_data_list = []

# Initialize variables for register number and student name
register_number = ""
student_name = ""

# Open the PDF file using pdfplumber
pdf_path = r"C:\pythonprogram\results.pdf"
pdf = pdfplumber.open(pdf_path)

# Iterate through pages
for page in pdf.pages:
    page_text = page.extract_text()
    lines = page_text.splitlines()
    
    for line in lines:
        
        # Skip lines that should be removed
        if should_skip_line(line):
            continue
        
        # Split the line into subjects and their details
        subject_details = line.split()

        # Extract and format the register number and student name
        match_register = re.search(r'(\d{5}[A-Z]\d{5})\s+(.+)', line)
        if match_register:
            register_number, student_name = match_register.groups()
            continue

        # Ensure that there are at least 5 elements in the subject_details list
        if len(subject_details) >= 5:
            subjects = []
            for i in range(0, len(subject_details), 5):
                subject_code = subject_details[i]
                internal_mark = subject_details[i + 1]
                external_mark = subject_details[i + 2]
                total_mark = subject_details[i + 3]
                status = subject_details[i + 4]

                # Remove leading '0' from the first digit of marks if it is '0'
                internal_mark = internal_mark[1:] if internal_mark.startswith('0') else internal_mark
                external_mark = external_mark[1:] if external_mark.startswith('0') else external_mark
                total_mark = total_mark[1:] if total_mark.startswith('0') else total_mark

                # Replace "---" with "NA" in internal and external marks
                if internal_mark == "---":
                    internal_mark = "NA"
                if external_mark == "---":
                    external_mark = "NA"

                # Create a dictionary for the current subject
                subject_data = {
                    "Subject Code": subject_code,
                    "Internal Mark": internal_mark,
                    "External Mark": external_mark,
                    "Total Mark": total_mark,
                    "Status": status
                }

                # Append the subject data to the list of subjects for the current student
                subjects.append(subject_data)

            # Check if there are subjects for the current student
            if subjects:
                # Create a dictionary for the current student
                student_data = {
                    "Register Number": register_number,
                    "Student Name": student_name,
                    "Subjects": subjects
                }

                # Append the student data to the list of student data
                student_data_list.append(student_data)

# Print the extracted student data
for student_data in student_data_list:
    print(f"Register Number: {student_data['Register Number']}")
    print(f"Student Name: {student_data['Student Name']}")
    for subject_data in student_data['Subjects']:
        print(f"Subject Code: {subject_data['Subject Code']}")
        print(f"Internal Mark: {subject_data['Internal Mark']}")
        print(f"External Mark: {subject_data['External Mark']}")
        print(f"Total Mark: {subject_data['Total Mark']}")
        print(f"Status: {subject_data['Status']}")
