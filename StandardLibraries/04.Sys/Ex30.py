import sys

sum = 0

if len(sys.argv) == 1:
    print("No arguments were given.")
else:
    args = sys.argv[1:]
    for value in args:
        sum = sum + int(value)

    print("Average: ",round((sum/len(args)),4))