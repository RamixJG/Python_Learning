import os

# Create and change the directory to documents
os.mkdir("documents")
os.chdir("documents")

# Create a directory for each month
for i in range(1,13):
    os.mkdir(f"{str(i).zfill(2)}_sales")

# List directories in alphabetical order and print
print(sorted([name for name in os.listdir()]))