'''Assume some email address like "username@companyname.com",
now write a snippet that extracts the company name of a given email
address.
expected result of code:
Enter your email: shubhamb@techspawn.com
Your company name is: techspawn
'''

myinput = input("Enter Company mail id = ")
index = myinput.find('@')
rindex = myinput.rfind('.')
Name = myinput[index+1:-(len(myinput)-rindex)]
print("Company Name = ",Name)
