import numpy as np
print("Create an array of zeros")
x = np.zeros((1,2))
print("Default type is float")
print(x)
print("Type changes to int")
x = np.zeros((1,2), dtype = np.int)
print(x)
print("Create an array of ones")
y= np.ones((1,2)) 
print("Default type is float")
print(y)
print("Type changes to int")
y = np.ones((1,2), dtype = np.int)
print(y)
