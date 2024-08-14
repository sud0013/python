# Find even and odd numbers from a list, and store them separately in a new list

n=[0,1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list=",even)
print("odd list=",odd)


