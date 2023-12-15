import fitz  # PyMuPDF
from summa import summarizer

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def generate_summary(text):
    summary = summarizer.summarize(text)
    return summary

def summarize_pdf(pdf_path):
    pdf_text = extract_text_from_pdf(pdf_path)
    summary = generate_summary(pdf_text)
    return summary

# Example usage
pdf_path = "path/to/your/file.pdf"
pdf_summary = summarize_pdf(pdf_path)
print(pdf_summary)
