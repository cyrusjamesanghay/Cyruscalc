number1 = int(input("Enter First number : "))
operator = input("pick operator (+,-,*,/) :")
number2 = int(input("enter Second number : "))

if operator == "+":
    plus_total = number1 + number2
    print(plus_total)
elif operator == "-":
    minus_total = number1 - number2
    print(minus_total)
elif operator == "*":
    mul_total = number1 * number2
    print(mul_total)
elif operator == "/":
    div_total = number1 / number2
    print(div_total)
                