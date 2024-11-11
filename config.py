# Path to the CSV file containing student data (e.g., student ID, name, blood group, etc.)
# Update this path if the data file location changes
data_file_path = r'data\FirstYearList.csv'

# Path to the template image file for ID card background
# Replace this path if using a different template image
template_path = r'templates\template3.png'

# Directory where the generated ID card images will be saved
# Update the folder name or path if you want to save outputs elsewhere
output_dir = r'outputs\2427batch'

# Path to the font file used for writing text on the ID card
# Change this path if a different font style is desired
font_style_path = r'fonts\CENTURY.TTF'

# Font size for the text on the ID card
# Adjust the font size based on the readability on the template
font_size = 53

# Set to True to make text bold on ID cards
bold = False

# Academic batch year displayed on the ID card
# Update this to the relevant batch year as necessary
batch_year = '2024-2027'

# Position coordinates for each text item on the ID card
# These coordinates control the exact placement of each detail on the template.
# Modify these if the template changes or to adjust spacing.

# Coordinates for the YRC ID
yrc_id_x_cord = 548
yrc_id_y_cord = 899

# Coordinates for the name of the individual
name_x_cord = 548
name_y_cord = 1012

# Coordinates for the blood group
blood_group_x_cord = 548
blood_group_y_cord = 1123

# Coordinates for the batch year
year_x_cord = 548
year_y_cord = 1239

# Coordinates for the phone number
phone_number_x_cord = 548
phone_number_y_cord = 1352
