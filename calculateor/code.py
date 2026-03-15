
while True:

    number1 = int(input('enter numbar 1 :'))
    operator  = str(input('enter operator :'))
    number2 = int(input('enter number 2 :'))
    if operator == '+':
        n = number1 + number2
    if operator == '-':
        n = number1 - number2 
    if operator == '*' or operator == 'x':
        n = number1 * number2
    if operator == '/':
        n = number1 / number2
    print('output : ',n)               
