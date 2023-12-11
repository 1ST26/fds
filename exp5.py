 def InsertSort(arr,n):
 for index in range(1,len(arr)):
 currentelement= arr[index]
 pos=index
 while((currentelement<arr[pos-1]) and (pos>0)):
 print("Array of pos=>",arr[pos])
 arr[pos] = arr[pos-1]
 print("Array of pos-1=>",arr[pos-1])
 pos=pos-1
 arr[pos] = currentelement
 print("phases==>",arr)
 print("Using Insert Sort Algorithm=>",arr)
def ShellSort(arr,n):
 gap = len(arr)//2
 while gap > 0: 
 for index in range(gap,len(arr)):
 currentelement = arr[index] 
 pos=index
 while(currentelement<arr[pos-gap] and pos >= gap): 
 arr[pos] = arr[pos-gap] 
 pos=pos-gap
 
 arr[pos] = currentelement 
 gap= gap//2
 print("Using Shell Sort Algorithm=>",arr)
 print("Top Five Scores are...")
 for i in range (len(arr)-1,len(arr)-6,-1):
 print(arr[i])
#Driver Code
print("\nHow many students are there?")
n = int(input())
array = []
i=0
for i in range(n):
 print("\n Enter percentage marks")
 item = float(input())
 array.append(item)
print("You have entered following scores...\n")
print(array)
InsertSort(array,n)
ShellSort(array,n)