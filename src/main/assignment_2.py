import numpy as np

#question 1 

row= 3
col= 3 
w =  3.7
x_points = [3.6,3.8,3.9]
y_points = [1.675,1.436,1.318]
matrix = np.zeros((row,col))
for i in range(row):
  matrix[i][0] = y_points[i]
for l in range(1,row):
  for k in range(1,l+1):
    T1 = (w -x_points[l-k])*matrix[l][k-1]
    T2 = (w-x_points[l]) * matrix[l-1][k-1]

    matrix[l][k] = (T1 -T2)/ (x_points[l]-x_points[l-k])
print(matrix[row-1][col-1])
print("\n")


#question 2
row = 4
col = 4 
x_points = [7.2,7.4,7.5,7.6]
y_points = [23.5492,25.3913,26.8224,27.4589]

matrix2= np.zeros((row,col))

for i in range(row): 
  matrix2[i][0] = y_points[i]

for l in range(row):
  for k in range(1,l+1):
    matrix2[l][k] = (matrix2[l][k-1]-matrix2[l-1][k-1])/(x_points[l]-x_points[l-k])


new = np.zeros(row-1)
for l in range(1,row):
  new[l-1]=matrix2[l][l]
print(new)
print("\n")

#question 3 
row = 4
col = 4 
w = 7.3
x_points = [7.2,7.4,7.5,7.6]
y_points = [23.5492,25.3913,26.8224,27.4589]

matrix3 = np.zeros((row,col))

for i in range(row): 
  matrix3[i][0] = y_points[i]

for l in range(1,row):
  for k in range(1,l+1):
    T1 = (w -x_points[l-k])*matrix3[l][k-1]
    T2 = (w-x_points[l]) * matrix3[l-1][k-1]

    matrix3[l][k] = (T1 -T2)/ (x_points[l]-x_points[l-k])
print(matrix3)
print(matrix3[row-1][col-1])
print("\n")

#question 4
row = 6
col = 6 
x_points = [3.6,3.6,3.8,3.8,3.9,3.9]
y_points = [1.675,1.675,1.436,1.436,1.318,1.318]
deriv_points = [0,-1.195,0,-1.188,0,-1.182]

matrix4 = np.zeros((row,col))

for i in range(row): 
  matrix4[i][0] = x_points[i]
  matrix4[i][1] = y_points[i]
  matrix4[i][2] = deriv_points[i]


for l in range(row):
  for k in range(2,l+1):
    T1 = (x_points[l] -x_points[l-k])*matrix4[l][k-1]
    T2 = (x_points[l-1]-x_points[l]) * matrix4[l-1][k-1]

    matrix4[l][k] = deriv_points[l]*(T1 -T2)/ (x_points[l]-x_points[l-k])
print(matrix4)
