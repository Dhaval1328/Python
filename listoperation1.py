
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]


list3 = list1 + list2
print("Concatenated List:", list3)


list1.remove(list1[3])
print("After removing list1[3]:", list1)


list1.append("Java")
print("After adding Java:", list1)


list2[3] = 11
print("Updated list2:", list2)

del list2[2]
print("v. After deleting index 2 from list2:", list2)


print("vi.")
for i in range(4):
    print("Welcome to Marwadi University")


print("list1[-2]:", list1[-2])
print("list2[1:3]:", list2[1:3])
print("list1[-1:-3]:", list1[-1:-3])


print("Length of list2:", len(list2))


numeric_list1 = [x for x in list1 if isinstance(x, int)]
print("Maximum element in list1:", max(numeric_list1))


print("Minimum element in list2:", min(list2))


list2.append(100)
print("After appending 100:", list2)


list2.extend([200, 300])
print("After extend operation:", list2)

# xiv. Difference between pop() and remove()
print("xiv.")
temp_list = [10, 20, 30, 40]
print("Original List:", temp_list)

temp_list.pop(1)        # removes element by index
print("After pop(1):", temp_list)

temp_list.remove(30)    # removes element by value
print("After remove(30):", temp_list)

# xv. Perform reverse() on list1
list1.reverse()
print("xv. Reversed list1:", list1)

# xvi. Arrange elements in descending order in list2
list2.sort(reverse=True)
print("xvi. list2 in descending order:", list2)
