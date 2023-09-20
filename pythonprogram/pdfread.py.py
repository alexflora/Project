import re
import pdfplumber
import pandas as pd

def should_skip_line(line):
    skip_prefixes = [
        "Result Gally Sheet",
        "College :",
        "Course",
        "No of Papers",
        "SubCode",
        "Int",
        "NOTE",
        "UNIVERSITY",
        "*",
    ]
    return any(line.startswith(prefix) for prefix in skip_prefixes)

# Create an empty list to store student data
student_data_list = []

# Open the PDF file
with pdfplumber.open("C:\\pythonprogram\\CsResult.pdf") as pdf:
    register_number = ""
    student_name = ""
    subjects = []

    for pages in pdf.pages:
        for line in pages.extract_text().splitlines():
            # Skip lines that should be removed
            if should_skip_line(line):
                continue

            # Extract and format the register number and student name
            match_register = re.search(r'(\d{5}[A-Z]\d{5})\s+(.+)', line)
            if match_register:
                # If we are processing a new student, add the previous student's data to the list
                if register_number and student_name:
                    student_data_list.append({
                        "Register Number": register_number,
                        "Student Name": student_name,
                        "Subjects": subjects
                    })
                register_number, student_name = match_register.groups()
                subjects = []  # Reset subjects for the new student
                continue  # Skip processing the rest of the line if it contains the register number

            # Check if there are at least 5 elements in the subject_details list
            subject_details = line.split()
            if len(subject_details) >= 5:
                # Iterate over subject details in groups of 5
                for i in range(0, len(subject_details), 5):
                    subject_code = subject_details[i]
                    internal_mark = subject_details[i + 1]
                    external_mark = subject_details[i + 2]
                    total_mark = subject_details[i + 3]
                    status = subject_details[i + 4]

                    # Replace "---" with "NA" in internal and external marks
                    if internal_mark == "---":
                        internal_mark = "NA"
                    if external_mark == "---":
                        external_mark = "NA"

                    # Create a dictionary for the current subject
                    subject_data = {
                        "Subject Code": subject_code,
                        "Internal": internal_mark,
                        "External": external_mark,
                        "Total": total_mark,
                        "Status": status
                    }

                    # Append the subject data to the list of subjects for the current student
                    subjects.append(subject_data)

    # Add the last student's data to the list
    if register_number and student_name:
        student_data_list.append({
            "Register Number": register_number,
            "Student Name": student_name,
            "Subjects": subjects
        })

# Create a DataFrame from the student data
df_list = []
for student_data in student_data_list:
    register_number = student_data['Register Number']
    student_name = student_data['Student Name']
    for subject_data in student_data['Subjects']:
        subject_code = subject_data['Subject Code']
        internal_mark = subject_data['Internal']
        external_mark = subject_data['External']
        total_mark = subject_data['Total']
        status = subject_data['Status']
        df_list.append([register_number, student_name, subject_code, internal_mark, external_mark, total_mark, status])

# Create a DataFrame with appropriate column names
df = pd.DataFrame(df_list, columns=["Register Number", "Student Name", "Subject Code", "Internal", "External", "Total", "Status"])

# Save the DataFrame to an Excel file
df.to_excel("student_data.xlsx", index=False)
