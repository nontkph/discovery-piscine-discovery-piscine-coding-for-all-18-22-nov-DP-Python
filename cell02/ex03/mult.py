firstNumber = float(input("enter first number : "))
lastNumber = float(input("enter last number : "))

result = float(firstNumber * lastNumber)

print( f"{firstNumber} x {lastNumber} = {result}" )
try:
    if result > 0:
        print("result is positive.")
    elif result < 0:
        print("result is negative.")
    else:
        print("what ;-;")
except: 
    print("error")