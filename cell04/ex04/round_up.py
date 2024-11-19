import math

try:
    num = float( input("Enter Number: ") )
    result = math.ceil( num )
    
    print(result)
except:
    print("Error please try again.")