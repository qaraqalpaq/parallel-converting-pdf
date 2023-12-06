import os
import shutil
from pdf2image import convert_from_path
import pytesseract
from concurrent.futures import ThreadPoolExecutor

# Specify the folders
pdf_folder = "./input-pdf/"
output_folder = "./output/"  # Folder to store extracted text files
processing_folder = "./processing/"  # Temporary folder for processing PDFs
processed_folder = "./processed/"  # Folder to move processed PDFs
skipped_folder = "./skipped/"  # Folder to move skipped PDFs

# Make sure all folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(processing_folder, exist_ok=True)
os.makedirs(processed_folder, exist_ok=True)
os.makedirs(skipped_folder, exist_ok=True)

# Language data packs
language_data = {
    "_qqr.pdf": "kaa",
    "_uzb.pdf": "uzb",
    "_rus.pdf": "rus",
    "_qozoq.pdf": "kaz",
    "_qirgiz.pdf": "kir",
    "_turkman.pdf": "tur",
    "_tojik.pdf": "tgk",
}

# Function to process a single PDF file
def process_pdf(pdf_file):
    pdf_path = os.path.join(pdf_folder, pdf_file)
    processing_path = os.path.join(processing_folder, pdf_file)

    # Move the PDF to the processing folder
    shutil.move(pdf_path, processing_path)

    # Determine the language pack
    language_pack = None
    for suffix, traineddata in language_data.items():
        if pdf_file.endswith(suffix):
            language_pack = traineddata
            break

    if language_pack:
        images = convert_from_path(processing_path)
        combined_text = "".join([pytesseract.image_to_string(image, lang=language_pack) for image in images])

        # Save the extracted text
        output_txt_file = os.path.join(output_folder, pdf_file.replace(".pdf", ".txt"))
        with open(output_txt_file, "w") as txt_file:
            txt_file.write(combined_text)

        print(f"Converted {pdf_file} to {output_txt_file} using {language_pack}")

        # Move the processed PDF to the processed folder
        shutil.move(processing_path, os.path.join(processed_folder, pdf_file))
    else:
        print(f"No language pack found for {pdf_file}. Moving to skipped folder.")
        # Move the skipped PDF to the skipped folder
        shutil.move(processing_path, os.path.join(skipped_folder, pdf_file))

# Get all PDF files in the folder
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

# Using ThreadPoolExecutor to process files in parallel
with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(process_pdf, pdf_files)
