from docxtpl import DocxTemplate
from dotenv import load_dotenv
from docx2pdf import convert
import os
import asyncio


load_dotenv()


async def generate_doc(company_name: str, position_name: str, template_path: str, output_path: str | None) -> bool:
    try:
        doc = DocxTemplate(template_path)
        context = {'company_name': company_name,
                   'position_name': position_name}
        doc.render(context)
        docx_filename = f"{company_name.replace(' ', '_').lower()}-{position_name.replace(' ', '_').lower()}-cover-letter.docx"
        doc.save(docx_filename)

        pdf_filename = docx_filename.replace('.docx', '.pdf')
        convert(docx_filename, pdf_filename)

        if output_path:
            os.rename(docx_filename, os.path.join(output_path, docx_filename))
            os.rename(pdf_filename, os.path.join(output_path, pdf_filename))
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True


async def get_templates() -> list:
    templates = []
    path = os.getenv("template_dir_path")
    for file in os.listdir(path):
        if file.endswith(".docx") and not file.startswith("~$"):
            templates.append({
                "name": file,
                "path": os.path.join(path, file)
            })
    return templates


async def main():
    print("Welcome to the Cover Letter Generator")
    company_name = input("Enter the company name: ")
    position_name = input("Enter the position you are applying for: ")
    templates = await get_templates()
    print("Select a template from the list below")
    for template in templates:
        print(f"{templates.index(template)+1}. {template['name']}")
    template_index = int(
        input("Enter the index of the template you want to use: "))

    if os.getenv("output_dir_path") is not None:
        coverValid = await generate_doc(
            company_name, position_name, templates[template_index-1]["path"], os.getenv("output_dir_path"))
    else:
        coverValid = await generate_doc(
            company_name, position_name, templates[template_index-1]["path"])

    if coverValid:
        print("Cover letter generated successfully")

    else:
        print("Error generating cover letter")


if __name__ == "__main__":
    asyncio.run(main())
