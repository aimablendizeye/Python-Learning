## calculator  program 

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Enter the operator you want (+,-,*,/):")

if operator == "-":
     result = num1 - num2

elif operator == "+":
     result = num1 + num2

elif operator == "*":
     result = num1 * num2 

elif operator == "/":
     result = num1 / num2
else:
     result = "Invalid input"
              

print ("The answer is:",result);

