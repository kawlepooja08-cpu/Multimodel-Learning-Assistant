import os
from file_processing.pdf_processor import PDFProcessor

pdf_file = "sample.pdf"

print("File Exists:", os.path.exists(pdf_file))
print("File Size:", os.path.getsize(pdf_file))

text = PDFProcessor.extract_text(pdf_file)

print(text[:1000])

text = PDFProcessor.extract_text(pdf_file)

print("Extracted Characters:", len(text))
print(text[:500])