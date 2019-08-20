import xlrd
import xlwt
import xlutils
from xlutils.copy import copy
import smtplib
import random
import time
bb=0
def mail_system():
    global bb
    print("WELCOME TO MAIL SYSTEM\n\nPRESS 1 for signup\nPRESS 2 for signin")
    a=int(input("ENTER NOW"))
    if a==1:
        name=input("enter name")
        dob=input("enter dob")
        email=input("enter your email")
        psedo_email=email[::-1]
        if psedo_email[:10]=='moc.liamg@':
            print("Email is correct")
        else:
            print("invalid email")
            return
        phone=input("Enter number")
        if len(phone)<10 or len(phone)>10:
            return
        user=input("enter username")
        password=input("enter password")
        if bb>1 or bb==1:
            #print("heelo")
            rb=xlrd.open_workbook('user_details.xls')
            wb=copy(rb)
            ws1=wb.get_sheet('user')
            ws1.write(bb,0,name)
            ws1.write(bb,1,dob)
            ws1.write(bb,2,email)
            ws1.write(bb,3,phone)
            ws1.write(bb,4,user)
            ws1.write(bb,5,password)
        else:
            #print("hi")
            wb=xlwt.Workbook()
            ws1=wb.add_sheet('user')
            ws1.write(bb,0,name)
            ws1.write(bb,1,dob)
            ws1.write(bb,2,email)
            ws1.write(bb,3,phone)
            ws1.write(bb,4,user)
            ws1.write(bb,5,password)
        wb.save('user_details.xls')
        print("Hello {},You have successfully signed up in our mail system".format(name))
        bb=bb+1
        print("If signed up please sign in again")
        mail_system()
    elif a==2:
        count=0
        flag=0
        flag1=0
        data=0
        t=0
        u=input("enter username")
        wb=xlrd.open_workbook('user_details.xls')
        ws1=wb.sheet_by_index(0)
        l=ws1.col_values(4)
        print(l)
        for item in l:
            if u==item:
                break
            else:
                data=data+1
        if u in l:
            print("Welcome {}".format(u))
            while count<3:
                p=input("please provide password")
                l=ws1.col_values(5)
                print(l)
                if p in l:
                    flag=1
                    break
                else:
                    print("Password incorrect !!! Please try again")
                    count=count+1
            if flag==1:
                print("generating one time otp at your email id")
                eml=ws1.cell(data,2).value
                print(eml)
                list1=['0','1','2','3','4','5']
                random.shuffle(list1)
                string1=""
                for items in list1:
                    string1=string1+items
                a=string1
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("paramchattani@gmail.com",'param@28')
                print("sending otp")
                server.sendmail("paramchattani@gmail.com",eml,a)
                print("otp succesfully sent")
                b=input("enter your otp")
                while t<3:
                    if a==b:
                        flag1=1
                        break
                    else:
                        print("wrong otp !!!try again")
                        b=input("enter your otp")
                        t=t+1
                if flag1==1:
                    print("SUCCESSFULLY LOGGED IN")
                    server.quit()
                else:
                    print("too many attempts. PLEASE try again after 1 min")
                    time.sleep(15)
                    server.quit()
                    mail_system()
            else:
                print("too many attempts to login")
                return
    else:
        print("please input no 1 or 2 only")
        a=input("enter yes to try again else enter no")
        if a=="yes":
            mail_system()
        else:
            pass
            
        
            
        
        
