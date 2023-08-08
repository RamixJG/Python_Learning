import os 

# Create file names
fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]
paths = []

# Create and print paths
for name in fnames[:12]:
    name = "/2020/" + name
    paths.append(os.path.join(os.getcwd(),name))
for name in fnames[-12:]:
    name = "/2021/" + name
    paths.append(os.path.join(os.getcwd(),name))

for path in paths:
    print(path)

# Better alternative way using enumerate
# paths = [
#     os.path.join(os.getcwd(), '2020', fname) 
#     if idx < 12 else os.path.join(os.getcwd(), '2021', fname) 
#     for idx, fname in enumerate(fnames)
# ]