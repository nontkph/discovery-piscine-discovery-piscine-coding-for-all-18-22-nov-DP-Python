import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    count_z = string.count("z")

    if count_z == 0:
        print("none")
    else:
        print("z" * count_z)
