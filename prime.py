number = int(input('Pick a number! '))
if number > 0:
    for i in range(2, number):
        if number%i == 0:
            print('Not a Prime number')
            break

    else:
        print('Prime number')
else:
    print('Not a prime number')
        
