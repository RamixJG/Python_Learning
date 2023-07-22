import os

# Create image directory and path
os.mkdir("images")
path = "/".join([str(os.getcwd()),"images"])

os.chdir(path)

# Print path
print(os.getcwd())