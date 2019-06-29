from fundefin import *
while True:
    print('''
        WELCOME IN EXPENDITURE CALCULATOR
            Press W to Note
                Press R to read
                    press S to Admin Services''')
    response=input('\t').upper()
    if response=='W':expend_note()
    elif response=='R':expend_read()
    elif response=='S':admin()
    else:print('Wrong Entry!')