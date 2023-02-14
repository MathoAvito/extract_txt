import os
import pytesseract
from PIL import Image
import yaml

# Path to the folder containing image files
image_folder = '/home/develeap/Documents/extract_text/photos_to_extract'

# String to hold the concatenated text from all images
text = ''

# Loop through each image file in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):
        # Open the image file
        img = Image.open(os.path.join(image_folder, filename))

        # Extract the text from the image
        image_text = pytesseract.image_to_string(img)

        # Append the extracted text to the string
        text += image_text

# Write the concatenated text to a file
with open('output.txt', 'w') as f:
    f.write(text)