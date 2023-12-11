 '''
Assignment No. 1 : In a second year computer engineering class, group A students play cricket, group B students play
badminton and group C students play football.
Write a python program using functions to compute following:
a) List of students who play both cricket and badminton.
b) List of students who play either cricket or badminton but not both.
c) Number of students who play neither cricket nor badminton.
d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)
'''
# Function for removing duplicate entries from the group
def removeduplicates(d):
list1=[]
for i in d:
if(i not in list1):
list1.append(i)
return list1
# Function for finding union of two sets (A|B)
def Union(cricket,badminton):
list3=cricket.copy()
for val in badminton:
if val not in list3:
list3.append(val)
return(list3)
# Function for finding difference between two sets (A-B)
def Difference(cricket,badminton):
list3=[]
for val in cricket:
if val not in badminton:
list3.append(val)
return(list3)
# Function for finding symmetric difference of two sets (A^B)
def SymmetricDiff(cricket,badminton):
list3=[]
d1=Difference(cricket,badminton)
print("Difference between Cricket and Badminton (C-B) is : ", d1)
d2=Difference(badminton,cricket)
print("Difference between Badminton and Cricket (B-C) is : ", d2)
list3=Union(d1,d2)
return(list3)
# Functon for finding List of students who play both cricket and badminton
def CB(cricket,badminton):
list3=Union(cricket,badminton)
print("\n\nList of students who play both cricket and badminton is : ", list3)
return(len(list3))
# Function for finding List of students who play either cricket or badminton but not both
def eCeB(cricket,badminton):
list3=SymmetricDiff(cricket,badminton)
print("\nList of students who play either cricket or badminton but not both is : ",list3)
return(len(list3))
# Function for finding Number of students who play neither cricket nor badminton
def nCnB(SEcomp,cricket,badminton):
list4=Difference(SEcomp,Union(cricket,badminton))
print("\n\nList of students who play neither cricket nor badminton is : ",list4)
return(len(list4))
# Function for finding Number of students who play cricket and football but not badminton
def CFnB(cricket,football,badminton):
list4=Difference(Union(cricket,football),badminton)
print("\n\nList of students who play cricket and football but not badminton is : ",list4)
return(len(list4))
# Creating an empty list for SE COMP
SEcomp=[]
n=int(input("Enter number of students SEcomp:"))
for i in range(0,n):
ele=input("please enter name of students")
SEcomp.append(ele)
print("The original list of SEcomp student:"+str(SEcomp))
# Creating an empty list for Cricket
Cricket=[]
n=int(input("Enter number of student playing Cricket"))
for i in range(0,n):
name=input("please enter the name of student")
Cricket.append(name)
print("The original list of student playing cricket:",Cricket)
Cricket=removeduplicates(Cricket)
print("List of student play Cricket",Cricket)
# Creating an empty list for Badminton
Badminton=[]
n=int(input("Enter number of student playing Badminton"))
for i in range(0,n):
name=input("please enter the name of student")
Badminton.append(name)
print("The original list of student playing Badminton:",Badminton)
Badminton=removeduplicates(Badminton)
print("List of student play Badminton",Badminton)
# Creating an empty list for Football
Football=[]
n=int(input("Enter the number of student playing Football"))
for i in range(0,n):
name=input("please enter the name of student")
Football.append(name)
print("The original list of student playing Football",Football)
Football=removeduplicates(Football)
print("List of student play Football",Football)
flag=1
while flag==1:
print("\n\n--------------------MENU--------------------\n")
print("1. List of students who play both cricket and badminton")
print("2. List of students who play either cricket or badminton but not both")
print("3. List of students who play neither cricket nor badminton")
print("4. Number of students who play cricket and football but not badminton")
print("5. Exit\n")
ch=int(input("Enter your Choice (from 1 to 5) :"))
if ch==1:
print("Number of students who play both cricket and badminton : ", CB(Cricket,Badminton))
a = input("\n\nDo you want to continue (y/n) :")
if a == "y":
flag = 1
else:
flag = 0
print("Thanks for using this program!")
elif ch==2:
print("Number of students who play either cricket or badminton but not both : ", eCeB(Cricket, Badminton))
a = input("\n\nDo you want to continue (y/n) :")
if a == "y":
flag = 1
else:
flag = 0
print("Thanks for using this program!")
elif ch==3:
print("Number of students who play neither cricket nor badminton : ", nCnB(SEcomp,Cricket,Badminton))
a = input("\n\nDo you want to continue (y/n) :")
if a == "y":
flag = 1
else:
flag = 0
print("Thanks for using this program!")
elif ch==4:
print("Number of students who play cricket and football but not badminton : ", CFnB(Cricket,Football,Badminton))
a = input("\n\nDo you want to continue (y/n) :")
if a == "y":
flag = 1
else:
flag = 0
print("Thanks for using this program!")
elif ch==5:
flag=0
print("Thanks for using this program!")
else:
print("!!Wrong Choice!! ")
a=input("\n\nDo you want to continue (y/n) :")
if a=="y":
flag=1
else:
flag=0
print("Thanks for using this program!")
#<---------------------------------------------END OF PROGRAM--------------------------------------->
