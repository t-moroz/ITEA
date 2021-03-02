
while True:
        try:
            x=int(input('Enter integer number, please:'))
            if x <= 0:
                print('Enter integer number>0')
            else:
                for a in range(1,x):
                    for b in range(1,a+1):
                        print('*', end='')
                    print()
                while x>0:
                      x=x-1
                      print('*', end='')
            print()
        except:
            print('Enter number!')
