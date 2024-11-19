num = input( "Enter number : " )

try:
    if num > 0:
        print("positive.")
    elif num < 0:
        print("negative.")
except:
    print("inn don't know.")