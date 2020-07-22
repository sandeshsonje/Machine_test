'''
5. Write a snippet that resolves ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many
rabbits and how many chickens do we have?

Suggestions: You can use "for loop" to iterate all possible conditions.
'''

numheads = int(input("Enter number of heads= "))
numlegs = int(input("Enter number of legs= "))

for chicken in range(0,numheads):
    rabbit = numheads - chicken
    chicken_Leg = 2*chicken
    rabbit_Leg = 4*rabbit
    
    total_legs = chicken_Leg + rabbit_Leg
 
    if(total_legs == numlegs):
        print("Rabbits = ",rabbit)
        print("Chicken = ",chicken)
