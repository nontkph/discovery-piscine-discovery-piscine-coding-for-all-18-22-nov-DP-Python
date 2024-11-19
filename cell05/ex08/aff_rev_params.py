import sys

if len(sys.argv) < 2:
    print("none")
else:
    for index in reversed( sys.argv[1:] ):
        print( index )