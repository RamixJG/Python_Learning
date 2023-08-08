import os

def createdir(name):
    if not os.path.exists(name):
        os.mkdir(name)
    else:
        print("Directory already exists")


# Create the directories
createdir("images")
os.chdir("images")
createdir("images_png")
createdir("images_jpg")

for root, dirs, files in os.walk(os.getcwd()):
    print(root)