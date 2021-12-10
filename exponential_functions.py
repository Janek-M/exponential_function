import time

print('hello, and welcome to the exponential function calculator')
time.sleep(2)
while True:
    print('what type of funtion would you like to calculate?')
    func = input('for key, type "key" - ')

    if len(func) < 1:
        print('Goodbye')
        break


    if func == 'eg':
        #y = a(1+r)^t
        try:
            a = float(input('please input the original amount - '))
            r = float(input('please input the rate of growth (as a percentage) - '))
            t = float(input('please input the total time that you would like to calculate - '))
            r = r/100
            par = (1+r)**t
            ans = par*a
            print('answer: ', ans, '\n')
        except:
            print('error: please try again and enter a number\n')
            continue

    elif func == 'ed':
        #y = a(1+r)^t
        try:
            a = float(input('please input the original amount - '))
            r = float(input('please input the rate of decay (as a percentage) - '))
            t = float(input('please input the total time that you would like to calculate - '))
            r = r/100
            par = (1-r)**t
            ans = par*a
            print('answer: ', ans, '\n')
        except:
            print('error: please try again and enter a number\n')
            continue

    elif func == 'ci':
        #y = P(1+(r/n))^nt
        try:
            a = float(input('please input the investment - '))
            r = input('''please input the monthly interest rate (as a percentage) \nor press enter for annual interest rate - ''')
            if len(r) < 1:
                r = float(input('please input the annual interest rate (as a percentage) - '))
            else:
                r = float(r)*12
            t = float(input('please input the total number of years that you would like to calculate - '))
            n = float(input('please input the number of times interest is compounded each year - '))
            r = r/100
            par = 1+(r/n)
            exp = n*t
            p1 = par**exp
            ans = a*p1
            print('answer: ', ans, '\n')
        except:
            print('error: please try again and enter a number\n')

            continue

    elif func == 'key':
        print('\n')
        print('exponential growth - "eg"')
        print('exponential decay - "ed"')
        print('compound interest - "ci"')
        print('\n')

    else:
        print(func,'is an invalid function name\nplease type key in the next box to find valid inputs\n')
        continue
