

def main():
    print(' This is a math helper')

    # list creator
    yeslist = 'yes', 'y', 'yeah', 'yea'
    nolist = 'no', 'n'

    a=input('  ')
    b=input('+  -   *  /\n')
    c=input('  ')
    ctd = a
    e = '$'


    if b == '*':
        print (int(a) * int(c))

    elif b == '/':
        print(int(a) / int(c))

    elif b == '-':
        print(int(a) - int(c))

    elif b == '+':
        print(int(a) + int(c))

    if b == '/' or '*' or '-' or '+':
        print('good')

    else: print('ERROR') + exit()
    question1 = input('Would you like to see how we got that? (y) (n) \n')

    if question1 in nolist:
        print('ok good luck \n Good bye') + exit()

    print ('thats great!\n' + '\nI will try to show you' )

    print('we will use the $ symbol to help explain\n')


    if b == '*':
        print('When multiplying pretend the first number is that many $ signs \n')




        def firstloop():

            while int(ctd) > 0:
                     int(ctd)==int(ctd)-1
                     print (e,end=' ')
                #while int(ctd)<10:
                #    print(e, end=' ')
                #print('\n')
                     while int(ctd)>9 and int(ctd) <20:
                         print(e, end=' ')
                         firstloop()
                #print('\n')
                #while int(ctd)>19 and int(ctd) <30:
                 #   print(e, end=' ')
                #print('\n')

        if int(ctd) >1:
            firstloop()

main()