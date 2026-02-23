#Write A Program To Create A List And Perform Vaarious Operation List Using Menu.

"""List=[10,20,30]
List.reverse
List.append(40)
List[2]=100
print(List)"""


List = []

while True:
    print("1. Add element")
    print("2. Remove element")
    print("3. Display list")
    print("4. Sort list")
    print("5. Search element")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        element = input("Enter element to add: ")
        List.append(element)
        print("Element added!")
    elif choice == '2':
        element = input("Enter element to remove: ")
        if element in List:
            List.remove(element)
            print("Element removed!")
        else:
            print("Element not found!")
    elif choice == '3':
        print(f"List: {List}")
    elif choice == '4':
        List.sort()
        print("List sorted!")
    elif choice == '5':
        element = input("Enter element to search: ")
        if element in List:
            print(f"Element found at index {List.index(element)}")
        else:
            print("Element not found!")
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")