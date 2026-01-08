def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def mod(num1, num2):
    return num1 % num2

def div(num1, num2):
    try:
        return num1/num2
    except as e :
        print(e)

print(calculator(3, 4))
print("shijith")