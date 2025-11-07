num1 = int(input("Please enter a number.\n"))
num2 = int(input("Please enter another number.\n"))
op = input("Which arithmetic operation would you like to perform? * / + -\n")

output = f"{num1} {op} {num2} = "
result = 0

if op == "-":
    result = num1 - num2
elif op == "+": 
    result = num1 + num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "undefined"

output += str(result)

print(output)