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

#declare variables
sum_diagonal_elements = 0
sum_upper_diagonal_elements = 0
sum_lower_diagonal_elements = 0
n = 1000

#store the hilbert matrix where n is 1000
matrix = Hilbert(n)

#calculate sum for diagonal elements(red elements)
for i in range(n):
    sum_diagonal_elements += matrix[i,i]

#calculate sum for upper diagonal elements(blue elements)
for i in range(n):
        if(i< n-1):
            sum_upper_diagonal_elements += matrix[i,i+1]

#calculate sum for lower diagonal elements(green elements)
for i in range(n):
    if(i < n-1):
        sum_lower_diagonal_elements += matrix[i+1,i]

#write function to display all the calculated sums
def display_sum():
    print("The sum for diagonal elements is: " + str(sum_diagonal_elements))
    print("The sum for upper diagonal elements is: " + str(sum_upper_diagonal_elements))
    print("The sum for lower diagonal elements is: " + str(sum_lower_diagonal_elements))

display_sum()

#create the test matrixes
A = np.array([[0,2],
             [2,3]])
x0 = np.array([1,1])

#function to perform power method
def Power_method(A,x0, n):
    for i in range(n):
        x0 =np.dot(A,x0)
        eigenvalue = max(abs(x0))
        x0 = x0/eigenvalue
        eigenvector = x0
    return eigenvalue,eigenvector

n = 8

#display eigenvalue and eigenvector
print("eigenvalue: ", Power_method(A,x0,n)[0])
print("eigenvector: ", Power_method(A,x0,n)[1])