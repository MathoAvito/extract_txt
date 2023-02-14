import os
import pytesseract
from PIL import Image
import yaml

# Path to the folder containing image files
image_folder = '/home/develeap/Documents/extract_text/photos_to_extract'

# Dictionary to hold the extracted text for each image
yaml_data = {}

# Loop through each image file in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):
        # Open the image file
        img = Image.open(os.path.join(image_folder, filename))

        # Extract the text from the image
        image_text = pytesseract.image_to_string(img)

        # Add the extracted text to the dictionary
        yaml_data[filename] = image_text

# Write the dictionary to a YAML file
with open('output.yaml', 'w') as f:
    yaml.dump(yaml_data, f)