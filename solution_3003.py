arr=[]size = int(input("Enter the size of the array: "))print("Enter the Element of the array:")for i in range(0,size):  num = int(input())  arr.append(num)count=0print("All the inversions are:")for i in range(0,size-1):  for j in range(i+1, size):    if arr[i]>arr[j]:      print("(",arr[i],",",arr[j],")")      count+=1if count==0:  print("(0)")elif count==0:  print("\nNumber of Inversions is ",count)else:  print("\nNumber of Inversions are ",count)