import os
import pytesseract
from PIL import Image

# Path to the folder containing image files
image_folder = '/home/develeap/Documents/extract_text/photos_to_extract'

# Variable to hold the combined extracted text from all images
all_text = ''

# Loop through each image file in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):
        # Open the image file
        img = Image.open(os.path.join(image_folder, filename))

        # Extract the text from the image
        image_text = pytesseract.image_to_string(img, config='-c tessedit_create_txt=1')

        # Remove the first two lines of the extracted text
        lines = image_text.split('\n')[3:]
        image_text = '\n'.join(lines)

        # Append the extracted text to the all_text variable
        # all_text += f"==== {filename} ====\n{image_text}\n\n"
        all_text += f"==========================================\n{image_text}\n\n"
# Write the combined extracted text to a single text file
with open('all_text.txt', 'w') as f:
    f.write(all_text)