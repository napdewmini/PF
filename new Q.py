
#Q1
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))

temp =num1
num1 =num2
num2=temp
print (num1)
print(num2)

#Q2
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))

if num1>num2:
    print(num1)
else:
    print(num2)

    
#Q3

num = int(input("Enter number :"))

if num > 0:
    print("This is a positive number")
else:
    print("This is a negative number")

#Q4

marks = int(input("Enter your mark :"))

if marks > 50:
    print("Pass")
else:
    print("Fail")

#Q5
age = int(input("Enter your age :"))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

#Q6
num = int(input("Enter number :"))

if num % 2 == 0:
    print("This number is an even number")
else:
    print("This number is a odd number")

#Q7

num = int(input("Enter number :"))

if num >0:
    print ("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#Q8
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
num3 = int(input("Enter number3 :"))

if num1>num2 and num1>num3:
    print("Largest number is",num1)
elif num2>num1 and num2>num3:
    print("Largest number is",num2)
else:
    print("Largest number is",num3)

#Q9

mark = int(input("Enter your mark :"))
if  90 <= mark <= 100:
    print("A")
    
elif 80 <= mark <= 89:
    print("B")

elif 70 <= mark <= 79:
    print("C")
    
elif 60 <= mark <= 69:
    print("D")
    
elif 50 <= mark <= 59:
    print("E")
else:
    print("F")

    
#Q10
num1=float(input("Enter number1:"))
num2=float(input("Enter number2:"))
opt = str(input("Enter the operator(+,-,*o,/):"))

if opt == "+":
    result=num1+num2
   
elif opt == "-":
    result=num1-num2
    
elif opt == "*":
    result=num1*num2
   
elif opt == "/":
    if num2 !=0:
        result=num1/num2
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


#display result
print("Result =  ",result)
    








        


