num = int(input("Enter Number: "))

original = num
re = 0

while num > 0:
    ld = num % 10
    re = re * 10 + ld
    num = num // 10

if re == original:
    print("Palindrome")
else:
    print("Not Palindrome")