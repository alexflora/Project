import re

data = """35821P15009 SHARMILA MARY F
DCS41 AAA AAA AAA AAA DCS42 AAA AAA AAA AAA DECS43B AAA AAA AAA AAA
DOTA44B AAA AAA AAA AAA DPCS45 --- 70 70 PASS DPCS46 --- 77 77 PASS
"""

# Split the data by newline characters to get individual lines
lines = data.split('\n')

# Initialize variables to store extracted information
register_number = ""
student_name = ""

# Iterate through each line of data
for line in lines:
    # Use regular expressions to match the register number and student name
    match_register = re.search(r'(\d{5}[A-Z]\d{5})\s+(.+)', line)

    # Extract and format the matched data
    if match_register:
        register_number, student_name = match_register.groups()
        continue  # Skip to the next iteration if register number and student name are found

    # Split the line into subjects and their details
    subject_details = line.split()
    print(subject_details)

    # Initialize variables for subject data
    subjects = []

    # Ensure that there are at least 4 elements in the subject_details list
    if len(subject_details) >= 4:
        for i in range(0, len(subject_details), 5):
            print(i)
            subject_code = subject_details[i]
            print(subject_code)
            internal_mark = subject_details[i + 1]
            print(internal_mark)
            external_mark = subject_details[i + 2]
            print(external_mark)
            total_mark = subject_details[i + 3]
            print(total_mark)
            status = subject_details[i + 4]
            print(status)

            # Print the extracted information for each subject
            #print(f"Register Number: {register_number}")
            #print(f"Student Name: {student_name}")
            #print(f"Subject Code: {subject_code}")
            #print(f"Internal Mark: {internal_mark}")
            #print(f"External Mark: {external_mark}")
            #print(f"Total Mark: {total_mark}")
            #print(f"Status: {status}")
