p1 = float(input("Enter Price:"))
p2 = float(input("Enter Price:"))

sum = p1 + p2


print("Select Option")
print("1.Totle Bill")
print("2.Discount")
print("3.Quntity")

choice = input("Enter choice: ")
if choice == "1":
    totle = p1 + p2
    print("Totle Bill=", totle)

elif choice == "2":
    totle = p1 + p2
    discount = float(input("Enter Discouunt %:"))
    final = totle - (totle * discount / 100)
    print("Final Totle After Discount=", final)

elif choice == "3":
    q1 = int(input("Enter Quantity: "))
    q2 = int(input("Enter Quantity: "))
    totle_stock = (p1 * q1) + (p2 * q2)
    print("Totle Quntity Price= ", totle_stock)

else:
    print("Invalid Choice")
