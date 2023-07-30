import os
import random

def file_end(file_name):
    # Get the file extension using os.path.splitext()
    _, file_extension = os.path.splitext(file_name)
    
    # Check if the file extension is ".jpg" (case-insensitive)
    return file_extension.lower()

# Generate random image names
random.seed(30)
images = [
    f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}"
    for i in range(1, 20)
]

# Create directories
base_dir = 'images'

if not os.path.exists(base_dir):
    os.mkdir(base_dir)
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(png_dir):
    os.mkdir(png_dir)
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)
    
# Create file for each image name in the correct folder
for image in images:

    if file_end(image) == ".jpg":
        jpg_path = os.path.join(jpg_dir, image)
        with open(jpg_path, 'x'):
            pass

    elif file_end(image) == ".png":
        png_path = os.path.join(png_dir, image)
        with open(png_path, 'x'):
            pass
    

for root, dirs, files in os.walk(base_dir):
    print(root)
    for file in sorted(files):
        print(f'\t{file}')
