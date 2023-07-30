import os

# Define function to get only lastsix characters
def red_name(name):
    return name[-6:]


# Create paths
paths = [
    os.path.join(os.getcwd(), f'dir_{str(i).zfill(2)}')
    for i in range(1, 14)
]

# Create directories
for path in paths:
    os.mkdir(path)

# Remove the last directory
os.rmdir(paths[-1])

# # Modify in order to get only the last 6 characters of the list
# paths_mod = [red_name(path) for path in paths[:-1]]

# print(paths_mod)

fnames = [fname for fname in sorted(os.listdir()) if len(fname) == 6]
print(fnames)