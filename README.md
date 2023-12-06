# PDF to Text Converter

This project provides a tool to convert PDF files into text files using Optical Character Recognition (OCR). It processes multiple PDF files in parallel, categorizing them based on language and processing status. The script uses parallel processing to improve efficiency.

## Requirements

- Python 3
- Tesseract OCR

## Installation

Before running the script, ensure you have Python 3 and Tesseract OCR installed on your machine.

### Install Tesseract OCR

Installation of Tesseract OCR varies based on your operating system:

- **macOS**: `brew install tesseract`
- **Ubuntu**: `sudo apt-get install tesseract-ocr`
- **Windows**: Download the installer from the [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).

### Setting up the Python Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install Python Dependencies

Install the required Python libraries using:

```bash
pip3 install -r requirements.txt
```

## Usage
To run the script, navigate to the project directory and execute the following command:

```bash
python3 converter.py
```

The script is configured to process up to 20 files in parallel. You can adjust the number of parallel workers by changing the max_workers parameter in the ThreadPoolExecutor within the script.

## Directory Structure
- input-pdf/: Place your PDF files here for processing.
- output/: Extracted text files are saved here.
- processing/: Temporary folder for processing PDFs.
- processed/: Processed PDFs are moved here.
- skipped/: PDFs with no matching language pack are moved here.

## Language Support
The script currently supports the following languages, identified by file suffix:

- _qqr.pdf: Kazakh
- _uzb.pdf: Uzbek
- _rus.pdf: Russian
- _qozoq.pdf: Kazakh
- _qirgiz.pdf: Kyrgyz
- _turkman.pdf: Turkmen
- _tojik.pdf: Tajik


## Contributing
Feel free to fork the repository and submit pull requests.

MIT License

### Additional Information:

- **Parallel Workers**: The note about parallel workers explains how to change the number of workers for parallel processing.
- **Language Labels**: Adjust the language names according to the actual languages you are processing.
- **License**: Replace `[MIT License](LICENSE)` with the correct license information or remove this section if not applicable.
- **Customization**: Modify any part of this template to better fit the specifics of your project or add additional sections as needed.

To use this, create a `README.md` file in your project directory and copy this content into it. This file will serve as the main documentation for anyone looking to understand or use your project.
