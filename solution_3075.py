n=int(input("Enter the range of number:"))sum=0.0fact=1for i in range(1,n+1):  fact *= i  sum+=1.0/factprint("The sum of the series = ",sum)