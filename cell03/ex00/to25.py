try:
    num = int(input("Enter a number less than 25\n"))
    
    if num > 25:
        print("Error")
    else:
        while num <= 25:
            print(f"Inside the loop, my variable is {num}")
            num += 1

except 10:
    print("Error: Please enter a valid number.")
