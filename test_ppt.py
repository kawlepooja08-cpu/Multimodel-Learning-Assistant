import os
from file_processing.ppt_processor import PPTProcessor

ppt_file = "sample.pptx"

print("File Exists:", os.path.exists(ppt_file))
print("File Size:", os.path.getsize(ppt_file))

text = PPTProcessor.extract_text(ppt_file)

print("Extracted Characters:", len(text))
print(text[:500])