import sys
import math
while 1:
        try:
            number1=int(input('Input first number:'))
        except:
            print('Enter only number!')
            sys.exit()
        operation=input('Input operator:')
        if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '**':
            print('Enter correct operator')
            sys.exit()
        else:
            try:
                number2=int(input('Input second number:'))
            except:
                print('Enter only number!')
                sys.exit()
            if operation=='+':
                b=number1+number2
                print(b)
            elif operation=='-':
                b = number1 -number2
                print(b)
            elif operation=='*':
                b=number1*number2
                print(b)
            elif operation=='**':
                b=number1**number2
                print(b)
           # elif operation == '***':
              #  b = sqrt(number1)
              #  print(b)
            elif operation=='/' and number2!=0:
                b=number1/number2
                print(b)
            elif operation=='/' and number2==0:
                print('Divide by zero')
