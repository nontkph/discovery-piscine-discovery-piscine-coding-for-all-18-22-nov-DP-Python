password = input()
verify = "Python is awesome"

try:
    if password == verify:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
except:
    print("error")