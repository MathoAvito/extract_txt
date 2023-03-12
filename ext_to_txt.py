import os
import pytesseract
from PIL import Image

# The folder that contains the photos to extract the text from
input_folder = './photos_to_extract'

# The name of the *new* file to extract the text to.
# txt/md files would be the best
output_file = 'output.md'

output_text = ''
# Loop through each image file in the folder

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):

        # Open the image file
        img = Image.open(os.path.join(input_folder, filename))

        # Extract the text from the image
        image_text = pytesseract.image_to_string(img, config='-c tessedit_create_txt=1')

        # Remove the first 3 lines of the extracted text
        lines = image_text.split('\n')[3:]

        image_text = '\n'.join(lines)

        # Remove any blank lines from the extracted text
        image_text = '\n'.join([line for line in image_text.split('\n') if line.strip()])

        # Append the extracted text to the output_text variable and separate each by "="
        output_text += f"==========================================\n{image_text}\n\n"

with open(output_file, 'w') as f:
    f.write(output_text)