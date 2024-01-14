("""addition,
subtraction,
multiplication,
division""")

num1= int(input("enter the value of number 1"))
num2= int(input("enter the value of number 2"))
print ("press + for addition/npress - for subtrraction/npress * for multiplication/npress / for division") 
opt= input("enter opt +-*/")
if  opt == "+":
    print (num1 + num2)
elif  opt == "-":
    print (num1 - num2)
elif  opt == "*":
    print (num1 * num2)
elif  opt == "/":
    print (num1 / num2)
else:
    print ("bye")
    
    

