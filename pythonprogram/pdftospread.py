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
    subjects = {}

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
                        "StudentName": student_name,
                        **subjects
                    })
                register_number, student_name = match_register.groups()
                subjects = {}  # Reset subjects for the new student
                continue  # Skip processing the rest of the line if it contains the register number

            # Check if there are at least 5 elements in the subject_details list
            subject_details = line.split()
            if len(subject_details) >= 5:
                subject_code = subject_details[0]
                internal_mark = subject_details[1]
                external_mark = subject_details[2]
                total_mark = subject_details[3]
                status = subject_details[4]

                # Replace "---" with "NA" in internal and external marks
                if internal_mark == "---":
                    internal_mark = "NA"
                if external_mark == "---":
                    external_mark = "NA"

                # Append the subject data to the subjects dictionary
                subjects[f"{subject_code}"] = {
                    "IN": internal_mark,
                    "EX": external_mark,
                    "TOTAL": total_mark,
                    "Status": status
                }

    # Add the last student's data to the list
    if register_number and student_name:
        student_data_list.append({
            "Register Number": register_number,
            "StudentName": student_name,
            **subjects
        })

# Create a Pandas DataFrame
df = pd.DataFrame(student_data_list)

# Reorder columns to match the desired order
column_order = ["Register Number", "StudentName"]
subject_codes = sorted({k for data in student_data_list for k in data.keys()} - {"Register Number", "StudentName"})
print(subject_codes)
column_order.extend(subject_codes)
df = df[column_order]

# Create a MultiIndex for the DataFrame
df.columns = pd.MultiIndex.from_tuples([(c.split('_')[0], c.split('_')[1]) for c in df.columns])

# Save the DataFrame to an Excel file
df.to_excel("student_data.xlsx", index=False, merge_cells=False)

print("Data has been exported to student_data.xlsx")
