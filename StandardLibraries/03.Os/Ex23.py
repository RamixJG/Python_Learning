import os 

# Create file names
fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
paths = []

# Create and print paths
for name in fnames:
    paths.append(os.path.join(os.getcwd(),name))

print(paths)