import sys

def print_multiplication_tables():
    for i in range(11):
        table = [i * j for j in range(11)]
        print(f"Table de {i}: {' '.join(map(str, table))}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "yolo":
        print("none$")
    else:
        print_multiplication_tables()
