#Impor Libraries
import numpy as np

#create a function that creates a Hilbert matrix
def Hilbert(n):
    H = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            H[i][j] = 1/(i+1)+(j+1) -1
    return H
n = 3
#test the function
print(Hilbert(n))
