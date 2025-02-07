# Extract TXT

Extract TXT is a simple Python script for extracting text from various file types. It is designed to be lightweight and easy to use from the command line.

> **Note:** This project is a work in progress. Contributions, feedback, and suggestions are welcome!

## Features

- **Simple Text Extraction:** Quickly extract text from input files.
- **Command-Line Interface:** Easily run the tool from your terminal.
- **Lightweight:** Minimal dependencies for a streamlined experience.

## Prerequisites

- **Python 3.6+**  
  Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

- **Required Python Libraries:**  
  The dependencies are listed in the `requirements.txt` file. Install them using:

  ```bash
  pip install -r requirements.txt
  ```

## Additional Tools (Optional)
If you plan to extract text from images using OCR, you might need Tesseract OCR installed on your system.

- **Ubuntu:**
  ```bash
  sudo apt-get install tesseract-ocr
  ```
- **macOS (Homebrew):**
  ```bash
  brew install tesseract
  ```

## Installation

### Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/MathoAvito/extract_txt.git
cd extract_txt
```

### (Optional) Create a Virtual Environment

It is recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```bash
python extract_txt.py <path_to_input_file>
```

For example:

```bash
python extract_txt.py sample_image.png
```

The script will process the specified file and output the extracted text to the console. Modify the script as needed to save the output to a file or perform further processing.

## Repository Structure

```
extract_txt/
├── extract_txt.py      # Main script for text extraction
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── (other files)       # Additional modules or configurations, if any
```
