import random
def linear_search(list1,n,key):
    for i in range(0,n):
        if(list1[i]==key):
            return i
    return -1

A=[]
n=int(input("Enter the size of list:"))
for i in range(0,n):
    A.append(random.randint(1,50))
item=int(input("Enter the key you want to search"))
index=linear_search(A,n,item)
if(index==-1):
    print("Element not found")
else:
    print("Element found at index",index)

print("***Avishkar_gautam_33***")
