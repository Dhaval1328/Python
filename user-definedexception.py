# WAP for user-defined exception

class MyError(Exception):
    pass

num = int(input("Enter a number: "))

if num < 0:
    print("Negative number not allowed")
else:
    print("Number is:", num)