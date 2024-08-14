
# password guess

a=1234
b=int(input("enter password:"))
while a!=b:
    print("it is wrong input")
    b=int(input("enter password:"))
print("it is the password")