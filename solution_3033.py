row_size=int(input("Enter the row size:"))print_control_x=row_size//2+1for out in range(1,row_size+1):  for inn in range(1,row_size+1):    if (inn==1 or inn==row_size) or (out==1 or out==row_size):      print("*",end="")    else:      print(" ", end="")  print("\r")