
print("Enter the row and column size:")
row_size=input()
for out in range(ord(row_size),ord('A')-1,-1):
  for i in range(ord(row_size)-1,out-1,-1):
    print(" ",end="")
  for p in range(ord('A'), out+1):
    print(chr(p),end="")
  print("\r")
