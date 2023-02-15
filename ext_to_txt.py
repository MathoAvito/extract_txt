import os
import pytesseract
from PIL import Image

image_folder = './photos_to_extract'

photo_text = ''

# Loop through each image file in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):

        # Open the image file
        img = Image.open(os.path.join(image_folder, filename))

        # Extract the text from the image
        image_text = pytesseract.image_to_string(img, config='-c tessedit_create_txt=1')

        # Remove the first 3 lines of the extracted text
        lines = image_text.split('\n')[3:]

        image_text = '\n'.join(lines)

        # Remove any blank lines from the extracted text
        image_text = '\n'.join([line for line in image_text.split('\n') if line.strip()])

        # Append the extracted text to the photo_text variable
        photo_text += f"==========================================\n{image_text}\n\n"
        # photo_text += f"==== {filename} ====\n{image_text}\n\n"


with open('photo_text.md', 'w') as f:
    f.write(photo_text)