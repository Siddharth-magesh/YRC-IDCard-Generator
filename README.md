# ID Card Generator

This tool is designed to automate the process of generating ID cards from a list of student data. It reads student information from a CSV file and overlays it onto a pre-designed ID card template. The output is a set of customized ID card images saved to a designated folder.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuring `config.py`](#configuring-configpy)
- [CSV Data Preparation](#csv-data-preparation)

## Features

- Automatically generates ID cards with student information.
- Customizable template and font style.
- Easy configuration for batch year, font size, and text positions on the template.

## Project Structure

```

.
├── config.py # Configuration file for font, template paths, text positions
├── data/ # Directory for storing CSV data files
├── fonts/ # Directory for storing font files
├── generate.py # Main script to generate ID cards
├── LICENSE # License file
├── outputs/ # Directory for storing generated ID card images
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── templates/ # Directory for storing ID card template images

```

## Installation

Follow these steps to set up and use the ID Card Generator.

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) (or Python 3.8+)
- The necessary packages listed in `requirements.txt`

### Step 1: Set Up the Environment

1. Open Anaconda Prompt (or your preferred terminal).
2. Navigate to the project directory.
3. Create a new environment for this project and install dependencies:

   ```bash
   conda create -n id_card_env python=3.8
   conda activate id_card_env
   pip install -r requirements.txt
   ```

### Step 2: Project Directory Setup

1. **data/**: Place the CSV data file here (e.g., `data/FirstYearList.csv`).
2. **fonts/**: Store any custom fonts here (e.g., `fonts/bahnschrift.ttf`).
3. **templates/**: Place the ID card template image here (e.g., `templates/template1.jpg`).
4. **outputs/**: Generated ID cards will be saved here. Ensure this folder exists before running the script.

## Usage

1. Update `config.py` to customize font style, size, and text positioning. Detailed instructions are below.
2. Run the `generate.py` script:

   ```bash
   python generate.py
   ```

3. The script will output individual ID card images in the `outputs` directory.

## Configuring `config.py`

The `config.py` file controls the text content, positions, font style, and batch year for the ID cards. Below is an overview of each setting in `config.py`:

```python
# Path to the CSV data file
data_file_path = r'data\FirstYearList.csv'

# Path to the ID card template image
template_path = r'templates\template1.jpg'

# Directory to save generated ID cards
output_dir = r'outputs\2427batch'

# Path to the font file
font_style_path = r'fonts\bahnschrift.ttf'

# Font size for text on the ID card
font_size = 30

# Batch year to display on the ID card
batch_year = '2024-2027'

# Text positioning (x and y coordinates) for different elements on the template
yrc_id_x_cord = 314
yrc_id_y_cord = 628

name_x_cord = 314
name_y_cord = 679

blood_group_x_cord = 314
blood_group_y_cord = 730

year_x_cord = 314
year_y_cord = 781

phone_number_x_cord = 314
phone_number_y_cord = 832
```

### Key Configurations

- **data_file_path**: Update this to the path of your CSV file if located elsewhere.
- **template_path**: Update to the path of your ID card template if using a different image.
- **output_dir**: Specify the output directory for the generated ID cards.
- **font_style_path**: Change this to use a different font. Make sure to place new fonts in the `fonts/` directory.
- **font_size**: Adjust based on template design and readability.
- **batch_year**: Update this with the current batch years.
- **x and y coordinates**: Modify each text position (`yrc_id`, `name`, `blood_group`, etc.) as per your template’s layout.

## CSV Data Preparation

The script expects the student data in a CSV format. Ensure that your CSV file includes the following columns in this order:

1. YRC ID (column 0)
2. Name (column 1)
3. Blood Group (column 8)
4. Phone Number (column 5)

### Excel to CSV Conversion

If your data is in Excel format, you can easily convert it to CSV using this [conversion tool](https://cloudconvert.com/). Simply upload your Excel file, select CSV as the output format, and download the converted file. Place this file in the `data/` directory.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
