str=input("Enter Your String:")sub_str=str.split(" ")maxInd=0max=0max = len(sub_str[0])for inn in range(0,len(sub_str)):  len1 = len(sub_str[inn])  if len1 > max:    max=len1    maxInd=innprint("Longest Substring(Word) is ",sub_str[maxInd])