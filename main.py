from docxtpl import DocxTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def generate_doc(company_name: str, position_name: str, job_type: str):
    try:
        doc = DocxTemplate(os.getenv("tempelate_path"))
        context = { 'company_name' : company_name, 'position_name': position_name}
        doc.render(context)
        doc.save("generated_doc.docx")
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True


def main():
    print("Welcome to the Cover Letter Generator")
    company_name = input("Enter the company name: ")
    position_name = input("Enter the position you are applying for: ")
    job_type = input("Enter the job type: ")
    coverValid = generate_doc(company_name, position_name, job_type)
    if coverValid:
        print("Cover letter generated successfully")
    else:
        print("Error generating cover letter")

if __name__ == "__main__":
    main()
    