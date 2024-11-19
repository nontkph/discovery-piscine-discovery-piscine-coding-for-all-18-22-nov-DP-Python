num = float( input("Enter number : ") )

try:
    if num.is_integer():
         print("This number is an integer.")
    else:
         print("This number is a decimal.")
        
except:
    print("error please try aggain.")