str=input("Enter Your String:")arr=[0]*256for i in range(len(str)):  if str[i]!=' ':    num=ord(str[i])    arr[num]+=1ch=' 'print("First Non-repeating character in a given string is: ",end="")for i in range(len(str)):    if arr[ord(str[i])] ==1:      ch=str[i]      breakprint(ch,end="")