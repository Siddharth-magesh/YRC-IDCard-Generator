from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import config
import warnings
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

warnings.simplefilter(action='ignore', category=FutureWarning)

def generate_id_card():
    # Load template and font settings
    template_path = config.template_path
    font_path = config.font_style_path
    font_size = config.font_size
    font = ImageFont.truetype(font_path, font_size)

    # Load data from CSV
    print(Fore.CYAN + "Loading data from CSV file...")
    data = pd.read_csv(config.data_file_path)
    print(Fore.GREEN + f"Successfully loaded {len(data)} records from {config.data_file_path}\n")

    # Generate each ID card
    for index, row in data.iterrows():
        # Create a new template for each card
        template = Image.open(template_path).copy()

        # Extract user details
        yrc_id = str(row[0])
        name = row[1]
        blood_group = row[8]
        year = config.batch_year
        phone_number = str(row[5])

        # Display progress
        print(Fore.YELLOW + f"Processing ID card for {name} (YRC ID: {yrc_id})...")

        # Define details and positions on the card
        text_details = [
            (yrc_id, (config.yrc_id_x_cord, config.yrc_id_y_cord)),
            (name, (config.name_x_cord, config.name_y_cord)),
            (blood_group, (config.blood_group_x_cord, config.blood_group_y_cord)),
            (year, (config.year_x_cord, config.year_y_cord)),
            (phone_number, (config.phone_number_x_cord, config.phone_number_y_cord))
        ]

        # Draw text onto the template
        draw = ImageDraw.Draw(template)
        for text, position in text_details:
            draw.text(position, text, font=font, fill='black')

        # Save the generated ID card
        file_name = f"{yrc_id}_IDCARD.png"
        file_path = os.path.join(config.output_dir, file_name)
        template.save(file_path)

        # Confirm successful save
        print(Fore.GREEN + f"ID card for {name} saved as {file_name}.\n")

    # Final message
    print(Fore.MAGENTA + Style.BRIGHT + "ID card generation complete.")

if __name__ == '__main__':
    generate_id_card()
