def Add():
 for i in range(0,m):
 for j in range(0,n):
 C[i][j] = A[i][j] + B[i][j]
 display(C)
def Sub():
 for i in range(0,m):
 for j in range(0,n):
 C[i][j] = A[i][j] - B[i][j]
 display(C)
def Mul():
 for i in range(0,m):
 for j in range(0,q):
 for k in range(0,n):
 C[i][j]=C[i][j]+ A[i][k] * B[k][j]
 display(C)
def Transpose():
 for i in range(0,m):
 for j in range(0,n):
 C[i][j] = A[j][i]
 display(C)
def display(C1):
 print('Resultant Matrix is:')
 for i in range(0,m):
 print('\n')
 for j in range(0,n):
 print(' ',C1[i][j],end=" ") 
m = int(input('Enter no. of rows for Matrix 1:'))
n = int(input('Enter no. of columns for Matrix 1:'))
A = [[0 for j in range(0, n)] for i in range(0, m)]
print('Enter Elements of Matrix A')
for i in range(0, m):
 for j in range(0, n):
 A[i][j] = int(input('\nEnter element A{}{}:'.format(i, j)))
display(A)
p = int(input('\nEnter no. of rows for Matrix 2:'))
q = int(input('\nEnter no. of columns for Matrix 2:'))
B = [[0 for j in range(0, q)] for i in range(0, p)]
print('\nEnter Elements of Matrix B')
for i in range(0, p):
 for j in range(0, q):
 B[i][j] = int(input('\nEnter element B{}{}:'.format(i, j)))
display(B)
flag =1
while flag==1:
 print('\n1.Add Matrices\n2.Subtract Matrices\n3.Multiply 
Matrices\n4.Transpose of Matrices\n5.Exit')
 choice = int(input('Enter Choice:'))
 if choice==1:
 if m==p and n==q:
 print('Matrices can be Added')
 C = [[0 for j in range(0, n)] for i in range(0, m)]
 Add()
 a = input("\n\nDo you want to continue (y/n) :")
 if a == "y":
 flag = 1
 else:
 flag = 0
print("Thanks for using this program!")
 
 else:
 print('Matrices cannot be Added')
 elif choice==2:
 if m==p and n==q:
 print('Matrices can be Subtracted')
 C = [[0 for j in range(0, n)] for i in range(0, m)]
 Sub()
 a = input("\n\nDo you want to continue (y/n) :")
 if a == "y":
 flag = 1
 else:
 flag = 0
print("Thanks for using this program!")
 else:
 print('Matrices cannot be Subtracted')
 elif choice==3:
 if n==p:
 print('Matrices can be Multiplied')
 C = [[0 for j in range(0, q)] for i in range(0, m)]
 Mul()
 a = input("\n\nDo you want to continue (y/n) :")
 if a == "y":
 flag = 1
 else:
 flag = 0
print("Thanks for using this program!")
 
 else:
 print('Matrices cannot be Multiplied')
 elif choice==4:
 C = [[0 for j in range(0, n)] for i in range(0, m)]
 Transpose()
a = input("\n\nDo you want to continue (y/n) :")
 if a == "y":
 flag = 1
 else:
 flag = 0
print("Thanks for using this program!")
 elif choice==5:
 flag=0
 print("Thanks for using this program!")
 else:
 print('\nPlease enter a valid choice')
 a = input("\n\nDo you want to continue (y/n) :")
 if a == "y":
 flag = 1
 else:
 flag = 0
 print("Thanks for using this program!")