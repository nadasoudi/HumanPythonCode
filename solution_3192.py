def swap_Element(arr,i,j):  temp = arr[i]  arr[i] = arr[j]  arr[j] = tempdef sort_element(arr,n):  if(n>0):    for i in range(0,n):      if (arr[i] >= arr[n - 1]):        swap_Element(arr, i, n - 1)    sort_element(arr, n - 1)def printArr(arr,n):  for i in range(0, n):    print(arr[i],end=" ")arr=[]n = int(input("Enter the size of the array: "))print("Enter the Element of the array:")for i in range(0,n):  num = int(input())  arr.append(num)sort_element(arr,n)print("After ascending order sort Array Elements are:")printArr(arr, n)