'''Write a code that generates the following pattern based on True or
False conditions.
'''

n = int(input("Enter number of rows = "))
f = input("Enter True or False = ")
if (f == "true"):
    for i in range(1,n+1):
        for j in range(1,(n+1)-i):
            print(end="  ")
        for j in range(1,2*i):
            print("*",end=' ')
        print('\n')

else:
    for i in range(1,n+1):
        for j in range(0,i):
            print(end='  ')
        for j in range(1,2*(n-i)+2):
            print("*",end=' ')
        print('\n') 
