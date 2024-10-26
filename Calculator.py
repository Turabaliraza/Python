'''
Python Calculator
'''

a=int(input("Add a First number"))
print("type of number",type(a))

b=int(input("Add a second number"))
print("type of number",type(b))

print("The value of",a,"+",b,"is: ",a+b)
print("The value of",a,"-",b,"is: ",a-b)
print("The value of",a,"*",b,"is: ",a*b)

if b!=0:
    print("the value of",a,"/",b,"is:",a/b)
    print("the value of",a,"//",b,"is:",a//b)
    print("the value of",a,"%",b,"is:",a%b)
else:
    print("Cannot divide by zero!")

