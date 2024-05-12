import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLineEdit, QLabel
import re
import pdfplumber
import pandas as pd

class PDFParserApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Parser App')
        self.setGeometry(100, 100, 400, 200)

        self.label1 = QLabel("Enter the month_year:")
        self.month_year_input = QLineEdit()

        self.label2 = QLabel("Enter the Status:")
        self.status_input = QLineEdit()

        self.label3 = QLabel("Enter Excel file name:")
        self.excel_name_input = QLineEdit()

        self.process_button = QPushButton('Process PDF')
        self.process_button.clicked.connect(self.process_pdf)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.month_year_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.status_input)
        layout.addWidget(self.label3)
        layout.addWidget(self.excel_name_input)
        layout.addWidget(self.process_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def process_pdf(self):
        pdf_path, _ = QFileDialog.getOpenFileName(self, 'Open PDF File', '', 'PDF Files (*.pdf)')
        if pdf_path:
            with pdfplumber.open(pdf_path) as pdf:
                month_year = self.month_year_input.text()
                status = self.status_input.text()
                excel_name = self.excel_name_input.text()
                documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')
                excel_path = os.path.join(documents_dir, f"{excel_name}.xlsx")
                print(excel_path)
                all_student_data = []
                lines_buffer = []

                for page in pdf.pages:
                    page_text = page.extract_text()
                    lines = page_text.splitlines()
                    for line in lines:
                        match_register = re.search(r'(\d{5}[A-Z]\d{5})\s+(.+)', line)
                        if match_register:
                            if lines_buffer:
                                all_student_data.extend(self.extract_student_data(lines_buffer, month_year, status))
                                lines_buffer = []
                            lines_buffer.append(line)
                        elif lines_buffer:
                            lines_buffer.append(line)

                if lines_buffer:
                    all_student_data.extend(self.extract_student_data(lines_buffer, month_year, status))

            df_list = []
            for student_data in all_student_data:
                register_number = student_data['Register Number']
                student_name = student_data['Student Name']
                exam = student_data['Exam']
                status = student_data['Status']
                for subject_data in student_data['Subjects']:
                    subject_code = subject_data['Subject Code']
                    semester = extract_semester_from_subject(subject_code)
                    internal_mark = normalize_mark(subject_data['Internal Mark'])
                    external_mark = normalize_mark(subject_data['External Mark'])
                    total_mark = normalize_mark(subject_data['Total Mark'])
                    df_list.append([register_number, student_name, subject_code, semester, internal_mark, external_mark, total_mark, exam, status])

            df = pd.DataFrame(df_list, columns=["Register No", "Student", "Course Code", "Semester", "Internal", "External", "Total", "Exam", "Status"])
            df.to_excel(excel_path, index=False)  # Save to the desktop directory         
            print("Success")

    def extract_student_data(self, lines, month, status):
        student_data_list = []
        register_number = ""
        student_name = ""
        subjects = []

        for line in lines:
            if should_skip_line(line):
                continue
            match_register = re.search(r'(\d{5}[A-Z]\d{5})\s+(.+)', line)
            if match_register:
                register_number, student_name = match_register.groups()
                continue
            subject_matches = re.findall(r'(\d*[A-Z]+\s?\d+\s?[A-Z]*\s?\d*)\s+(-{1,3}|\d+|A{3}|WHE|WHI|NC)\s+(-{1,3}|\d+|AAA|WHE|WHI|NC)\s+(-{1,3}|\d+|AAA|WHE|WHI|NC)\s+(PASS|RA|(?:AAA|WHE|WHI|NC))', line)
            if subject_matches:
                for match in subject_matches:
                    subject_code = match[0].replace(" ", "")
                    semester = extract_semester_from_subject(subject_code)
                    subject_data = {
                        "Subject Code": subject_code,
                        "Semester": semester,
                        "Internal Mark": match[1],
                        "External Mark": match[2],
                        "Total Mark": match[3]
                    }
                    subjects.append(subject_data)

        if subjects:
            student_data_list.append({
                "Register Number": register_number,
                "Student Name": student_name,
                "Subjects": subjects,
                "Exam": month,
                "Status": status,
            })

        return student_data_list


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
    elif mark in ('WHI', 'WHE', 'AAA','NC'):
        return mark
    else:
        return str(mark).zfill(3)


def extract_semester_from_subject(subject_code):
    semester = ""
    for char in reversed(subject_code):
        if char.isdigit():
            semester = char
        elif semester:
            # If a digit was found before encountering a character, return the semester
            return semester
    # If no digit was found, return a default value
    return "Unknown"


def main():
    app = QApplication(sys.argv)
    window = PDFParserApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
