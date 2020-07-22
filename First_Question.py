'''1. Write a program which takes 2 digits, X,Y as input and generates a
2-dimensional array.
Example:
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Note: Values inside array can be any.(it's up to candidate)'''

row = int(input("Enter number of rows = "))
col = int(input("Enter number of cols = "))
arr=[]
for i in range(0,row):
    arr1=[]
    for j in range(0,col):
        arr1.append(i*j)
    arr.append(arr1)

print(arr)
