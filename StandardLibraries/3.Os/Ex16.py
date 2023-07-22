import os

names = os.listdir()
enames=[]

# Filter only files and directories beginning with e
for name in names:
    if name[0] == 'e':
        enames.append(name)


print(sorted(enames))



# import os
# names = sorted([name for name in os.listdir() if name.startswith('e')])
# print(names)