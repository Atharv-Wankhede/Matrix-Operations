N=int(input("Enter the no. of rows : "))
M=int(input("Enter the no. of Columns : "))
MATRIX_1=[]    
 for i in range(N):
    row=[]
    for j in range(M):
      num=int(input("Enter the elements : "))
      row.append(num)
    MATRIX_1.append(row)
 print("Resultant matrix is : ")
 for i in range(N):
   for j in range(M):
     print(MATRIX_1[i][j],end="")
   print()   
   MATRIX_2=[]    # Second matrix
 for i in range(N):
    row=[]
    for j in range(M):
      num=int(input("Enter the elements : "))
      row.append(num)
    MATRIX_2.append(row)
 print("Resultant matrix is : ")
 for i in range(N):
   for j in range(M):
     print(MATRIX_2[i][j],end="")
   print()
MATRIX_3=[]         #For sum of both matrices
 for i in range(N):
    row=[]
    for j in range(M):
      num=MATRIX_1[i][j]+MATRIX_2[i][j]
      row.append(num)
    MATRIX_3.append(row)
 print("Resultant sum of matrices is : ")
 for i in range(N):
   for j in range(M):
     print(MATRIX_3[i][j],end="")
   print()
   MATRIX_4=[]         
 for i in range(N):
    row=[]
    for j in range(M):
      num=MATRIX_1[i][j]-MATRIX_2[i][j]
      row.append(num)
    MATRIX_4.append(row)
 print("Resultant difference of matrices is : ")
 result=[[0,0,0], [0,0,0], [0,0,0]] 
 for i in range(N):
   for j in range(M):
     print(MATRIX_4[i][j],end="")
   print()
for i in range(len(MATRIX_1)): 
   for j in range(len(MATRIX_2[0])):          
      for k in range(len(MATRIX_1)): 
         result[i][j] += MATRIX_1[i][k] * MATRIX_2[k][j] 
print("The Resultant Matrix MULTIPLICATION Is ::>")
for r in result: 
   print(r)