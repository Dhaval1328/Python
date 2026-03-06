# WAP to display exception handling

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a/b
    print("Result is:", result)
    
except ValueError:
    print("Error: Please enter valid integer number!")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
except Exception as e:
    print("Unexpected Error:",e)
    
else:
    print("Division Succesful!")
    
finally:
    print("Program executed successfuly")
    