arr=[]size = int(input("Enter the size of the array: "))print("Enter the Element of the array:")for i in range(0,size):  num = int(input())  arr.append(num)sum=int(input("Enter the Sum Value:"))flag=0for i in range(0,size-1):  for j in range(i+1, size):    if arr[i]+arr[j]==sum:      flag=1      print("Given sum pairs of elements are ", arr[i]," and ", arr[j],".\n")if flag==0: print("Given sum Pair is not Present.")