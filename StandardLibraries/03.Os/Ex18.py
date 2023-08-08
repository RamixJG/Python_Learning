import os

# Create image directory and path
os.mkdir("images")
path = "/".join([str(os.getcwd()),"images"])

os.chdir(path)
# os.chdir('images')  -> could have use directly this relative path to change to the image folder

# Print path
print(os.getcwd())