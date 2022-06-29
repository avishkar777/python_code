A=[]
n=int(input("Enter N for N x M matrix: "))
m=int(input("Enter M for N x M matrix: "))
print("Enter the element ::>")
for i in range(n): 
   row=[]                                      
   for j in range(m): 
      row.append(int(input()))          
   A.append(row)                    
print(A)
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(m):
      print(A[i][j], end=" ")
   print()                                        
B=[]
n1=int(input("Enter N for N x M matrix: "))
m1=int(input("Enter M for N x M matrix: "))
print("Enter the element ::>")
for i in range (n1): 
   row=[]                                      
   for j in range(m1): 
      row.append(int(input()))
   B.append(row)                       
print(B)
print("Display Array In Matrix Form")
for i in range(n1):
   for j in range(m1):
      print(B[i][j], end=" ")
   print()                                           
result = [[0,0],[0,0]] 
for i in range(len(A)): 
   for j in range(len(B[0])): 
      for k in range(len(B)): 
         result[i][j] += A[i][k] * B[k][j] 
print("The Resultant Matrix Is ::>")
for r in result: 
   print(r)

print("***Abhay Garg_01***")
