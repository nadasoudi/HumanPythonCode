str=input("Enter Your String:")str1=input("Enter your Searching word:")out = 0i=0j=0while out< len(str1):  for i in range(len(str)):    for j in range(len(str1)):      if (str[i] == str1[j]):        j+=1      else:        j=0  out+=1if(j==out):  print("Searching word is Found.")else:  print("Searching Word is not Found.")