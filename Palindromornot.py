num= int(input("Enter Number :"))
re=0
ori=num
while num>0:
    ld= num %10
    re=re*10+ld
    num=num//10
    
if ori==re:
    print("Palindrom")
else:
    print("Not palindrom")
