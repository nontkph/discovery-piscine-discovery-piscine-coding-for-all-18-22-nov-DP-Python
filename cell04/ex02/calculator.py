first = int( input("Enter First Number: ") )
second = int( input("Enter Second Number: ") )

try:
    print("thank.")
    print(f"{first} + {second} = { first + second }")
    print(f"{first} - {second} = { first - second }")
    print(f"{first} ÷ {second} = { first / second }")
    print(f"{first} x {second} = { first * second }")
except:
    print("Error please try again.")