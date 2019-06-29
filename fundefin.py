from datetime import datetime as time
#   This is the code for ;Monthly,yearwise Expenditure Calculator.
def month_find(n):
    if n==1:return 'JANUARY'
    elif n==2:return 'FEBRUARY'
    elif n==3:return 'MARCH'
    elif n==4:return 'APRIL'
    elif n==5:return 'MAY'
    elif n==6:return 'JUNE'
    elif n==7:return 'JULY'
    elif n==8:return 'AUGUST'
    elif n==9:return 'SEPTEMBER'
    elif n==10:return 'OCTOBER'
    elif n==11:return 'NOVEMBER'
    elif n==12:return 'DECEMBER'
def secur_password():#this function is built for security purpose
    obj=open('encryption.txt','r')
    curr_pass=obj.read()
    obj.close()
    if input('Enter Desktop Password\t')==curr_pass:return True
    else:print('Wrong Password, Process Failed');return False

def confirmation_passw():
    '''this function is built for confirmation:if user made any mistake,that mistake could be cleared
    before consideration'''
    obj = open('encryption.txt', 'r')
    curr_pass = obj.read()
    obj.close()
    if input('Confirm Desktop Password\t') == curr_pass:
        return True
    else:
        print('Wrong Password, Process Failed');return False
def admin():
    print('Press C to change Your Password\t')
    if input().upper()=='C' and secur_password() and confirmation_passw():change_password()
    else:print('Wrong Entry!')

def change_password():#this function is access when you type "access":if yo forgot password, it handles
    obj=open('encryption.txt','r')
    curr_pwd=obj.read();obj.close()
    if input('Enter Current Password\t')==curr_pwd and transac_server_password() and confirmation_passw():
        new_pwd=input('Enter New Password\t')
        obj=open('encryption.txt','w')
        obj.write(new_pwd)
        return print('Successfully Done!')
    else:print('Wrong Password,Try Again!')
def expend_note():
    if secur_password():
        month_name=month_find(int(str(time.now().month)))
        date=str(time.now().date())[-2:]
        year=str(time.now().year)
        obj=open(month_name+year+'.txt','a')
        type_exp=input('Enter type of expenditure\t').title()
        particul=input('Enter Particulars\t').title()
        amount=input('Enter Amount expended\t')
        if confirmation_passw():
            obj.write(date+' '+month_name+','+year+'%*'+type_exp+'%*'+particul+'%*'+amount+'\n')
            obj.close()
        if obj.closed:print('\n\t\tSuccessfully Done!')
def expend_read():
    if secur_password() and confirmation_passw():
        try:
            month_name=month_find(int(input('Enter Month Number,for example 3 for March\t')))
            year=input('Enter Year,like 2019\t')
            obj=open(month_name+year+'.txt','r')
            month_data=obj.readlines();found_a_line=0;add=0
            print('_=_'*30)
            for i in month_data:
                found_a_line+=1
                j=i.split('%*');add+=int(j[-1])
                print(f'''[{found_a_line}]
        DATE: {j[0]}            TYPE OF EXPENDITURE: {j[1]}
        PARTICULARS: {j[2]}
        EXPENDITURE:{j[3]}\n''')
            if found_a_line!=0:print(f'Total = Rs. {add}')
            print('_=_'*30)
            print('Done') if found_a_line!=0 else print('No Data found for this month!')
        except:print('No Data found For the Month, you entered!')





