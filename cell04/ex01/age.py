age = int(input("Enter Age : "))

try:
    print(f"Currently {age} yeaar old.")
    for i in range(1, 4):
        num = i *10
        print(f"In { num } years, you'll be {age + (num)} years old.")
except:
    print("Error please try again.")
