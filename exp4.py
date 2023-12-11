 def SelectionSort(arr,n): 
 for i in range(n):
 Min = i
 for j in range(i+1,n):
 if(arr[j]<arr[Min]):
 Min = j
 temp=arr[i]
 arr[i]=arr[Min]
 arr[Min]=temp 
 print(arr)
def BubbleSort(arr,n):
 for i in range(len(arr)-1):
 for j in range(len(arr)-1):
 if(arr[j] > arr[j+1]):
 temp = arr[j]
arr[j] = arr[j+1]
 arr[j+1] = temp
 print(arr)
 print("Top Five Scores are...")
 for i in range (len(arr)-1,len(arr)-6,-1):
 print(arr[i])
 
 
#Driver Code
print("\nhow many no. of students in first year ?")
n = int(input())
array = []
i=0
for i in range(n):
 item = float(input("\n Enter percentage marks of student"))
 array.append(item)
print("You have entered following scores...\n")
print(array)
flag =1
while flag==1:
 print("Main Menu \n 1. Selection Sort \n 2. Bubble Sort and display Top 5 scores 
\n 3. Exit")
 choice = int(input("\n Enter your Choice: "))
 if(choice == 1):
 print("\n The sorted Scores are...")
 SelectionSort(array,n)
 a = input("\n\nDo you want to continue (y/n) :")
 if a == "y":
 flag = 1
 else:
 flag = 0
 print("Thanks for using this program!")
 elif choice==2:
 print("\n The sorted Scores are...")
 BubbleSort(array,n)
 a = input("\n\nDo you want to continue (y/n) :")
 if a == "y":
 flag = 1
 else:
 flag = 0
print("Thanks for using this program!")
 elif choice==3:
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