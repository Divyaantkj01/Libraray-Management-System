import mysql.connector
import matplotlib.pyplot as plt
import datetime


db=mysql.connector.connect(host="localhost",user="root",password="msql007ID1029", database="test")
cursor=db.cursor()

#create following tables in mysql
cursor.execute("create table books (Bno int (5) primary key , BName varchar (30) , BAuthor varchar (30) , BPublisher varchar (30) , BEdition int (4))")
cursor.execute("create table member (Mno int (5) primary key, MName varchar (30) , MPhoneNo varchar(20) , MActive varchar (10))")
cursor.execute("create table reg (admin varchar(30),password varchar(30))")


def booksmenu():
    print()
    print("-" * 30)
    print("         BOOKS MENU       ")
    print("-" * 30) 
    print("1. Add a Book Record ")
    print("2. Update Record of a Book ")
    print("3. Delete a Book ")
    print("4. Search a Book ")
    print("5. View Book Records ")
    print("6. Exit")
    print("-" * 30)
    print()
    

def membermenu():
    print()
    print("-"*30)
    print("         MEMBER MENU       ")
    print("-"*30)
    print("1. Add Member Record ")
    print("2. Update Member Record ")
    print("3. Delete Member Record ")
    print("4. View Member Records")
    print("5. Issue Book To Member ")
    print("6. Author-Wise Book Issue Data ")
    print("7. Exit")
    print("-" * 30)
    print()
    
def usermenu():
    print()
    print("-"*30)
    print("          USER MENU      ")
    print("-" * 30)
    print("1. Search Book ")
    print("2. Display Books Record ")
    print("3. Author-Wise Book Issue Data ")
    print("4. Exit ")
    print("-"*30)
    print()


def viewbooks():
    cursor.execute("Select * from books")
    result1=cursor.fetchall()
    print("-"*106)
    print("{0:8}{1:^25}{2:^18}{3:^35}{4:^20}".format("Book Number","Book Name","Book Author","Book Publisher","Book Edition"))
    print("-"*106)
    for i in result1:
        print("{0:8}{1:^30}{2:^10}{3:^42}{4:^15}".format(i[0],i[1],i[2],i[3],i[4]))
    print("-"*106)

    
    
def addbook():
    n=int(input("Enter how many records you want to enter: "))
    i=0
    while i<n:
        a=int(input("Enter Book Number: "))
        b=input("Enter Book Name: ")
        c=input("Enter Book Author: ")
        d=input("Enter Book Publisher: ")
        e=int(input("Enter Book Edition: "))
        q1=("Insert into books(Bno, BName ,BAuthor, BPublisher , BEdition ) values(%s,%s,%s,%s,%s)")
        data=(a,b,c,d,e)
        cursor.execute(q1,data)
        db.commit()
        i=i+1
        print()
    print("Book Record Added !")
     
def upbook():
    viewbooks()
    print()
    b=int(input("Enter book number you want to update: "))
    print("Book Details : ")
    q2="Select * from books where Bno=%s"%(b)
    cursor.execute(q2)
    result1=cursor.fetchall()
    for i in result1:
        print(i)
    print()
    c=input("Enter New Book Name : ")
    d=input("Enter New Author : ")
    e=input("Enter Publisher: ")
    f=int(input("Enter Book Edition : "))
    q3="Update books set BName = '%s' , BAuthor = '%s' , BPublisher = '%s', BEdition = %s where Bno=%s" % (c,d,e,f,b)
    cursor.execute(q3)
    db.commit()
    print("Updated Book Record! ")
    
def delbook():
    print()
    print("Delete Book by :- ")
    print()
    print("1. Book Number")
    print("2. Book Name")
    print("3. Book Author")
    print()
    w=int(input("Enter Option: "))
    print()
    if w==1:
        b=int(input("Enter book number : "))
        d="Delete from books where Bno=%s" %(b)
        cursor.execute(d)
        db.commit()
        print("This Book Record has been Deleted !")
    if w==2:
        c=input("Enter book name : ")
        d="Delete from books where BName='%s' " %(c)
        cursor.execute(d)
        db.commit()
        print("This Book Record has been Deleted !") 
    if w==3:
        d=input("Enter book author : ")
        a="Delete from books where BAuthor= '%s' " %(d)
        cursor.execute(a)
        db.commit()
        print("This Book Record has been Deleted !")
            
def searchbook():
    print()
    print("Search Book by :- ")
    print()
    print("1. Book Number")
    print("2. Book Name")
    print("3. Book Author")
    print()
    w=int(input("Enter Option: "))
    print()
    
    if w==1:
        b=int(input("Enter book number : "))
        print("Book Details : ")
        q6="Select * from books where Bno=%s"%(b)
        cursor.execute(q6)
        result1=cursor.fetchall()
        print("-"*93)
        print("{0:8}{1:^15}{2:^18}{3:^25}{4:^8}".format("Book Number","Book Name","Book Author","Book Publisher","Book Edition"))
        print("-"*93)
        for i in result1:
            print("{0:5}{1:^24}{2:^3}{3:^30}{4:^15}".format(i[0],i[1],i[2],i[3],i[4]))
        print("-"*93)
        
    if w==2:
        c=input("Enter book name : ")
        print("Book Details : ")
        q7="Select * from books where BName='%s'"%(c)
        cursor.execute(q7)
        result1=cursor.fetchall()
        print("-"*93)
        print("{0:8}{1:^15}{2:^18}{3:^25}{4:^8}".format("Book Number","Book Name","Book Author","Book Publisher","Book Edition"))
        print("-"*93)
        for i in result1:
            print("{0:5}{1:^24}{2:^3}{3:^30}{4:^15}".format(i[0],i[1],i[2],i[3],i[4]))
        print("-"*93)
        
    if w==3:
        d=input("Enter book author : ")
        print("Book Details : ")
        q8=("Select * from books where BAuthor='%s'")%(d)
        cursor.execute(q8)
        result1=cursor.fetchall()
        print("-"*93)
        print("{0:8}{1:^15}{2:^18}{3:^25}{4:^8}".format("Book Number","Book Name","Book Author","Book Publisher","Book Edition"))
        print("-"*93)
        for i in result1:
            print("{0:5}{1:^24}{2:^3}{3:^30}{4:^15}".format(i[0],i[1],i[2],i[3],i[4]))
        print("-"*93)

    


   
def addmember():
    n=int(input("Enter how many records you want to enter: "))
    i=0
    while i<n:
        a=int(input("Enter Member Number: "))
        b=input("Enter Member Name: ")
        c=int(input("Enter Member Phone No: "))
        d=input("Enter Membership Acivity (Active/Non-Active): ")
        q1=("Insert into member(Mno, MName, MPhoneNo, MActive) values(%s,%s,%s,%s)")
        data=(a,b,c,d)
        cursor.execute(q1,data)
        db.commit()
        i=i+1
        print()
    print("Member Record Added !")

    
def upmember():
    b=int(input("Enter member number whose record you want to update: "))
    print("Member Details : ")
    q2="Select * from member where Mno=%s"%(b)
    cursor.execute(q2)
    result1=cursor.fetchall()
    for i in result1:
        print(i)
    print()
    c=input("Enter New Member Name : ")
    d=input("Enter New Phone Number : ")
    f=input("Enter Membership Activity : ")
    q3="Update member set MName = '%s', MPhoneNo = '%s', MActive = '%s' where Mno=%s" % (c,d,f,b)
    cursor.execute(q3)
    db.commit()
    print("Updated Member Record ! ")


def delmember():
    print("Delete Member by :- ")
    print()
    print("1. Member Number")
    print("2. Member Name")
    print()
    w=int(input("Enter Option: "))
    print()
    if w==1:
        b=int(input("Enter member number : "))
        d="Delete from member where Mno=%s" %(b)
        cursor.execute(d)
        db.commit()
        print("This Member Record has been Deleted !")        
    if w==2:
        c=input("Enter member name : ")
        d="Delete from member where MName='%s' " %(c)
        cursor.execute(d)
        db.commit()
        print("This Member Record has been Deleted !")


def viewmembers():
    cursor.execute("Select * from member")
    result1=cursor.fetchall()
    print("-"*90)
    print("{0:8}{1:^15}{2:^22}{3:^20}".format("Member Number","Member Name","Member PhoneNo","Membership Status"))
    print("-"*90)
    for i in result1:
        print("{0:8}{1:^25}{2:^2}{3:^28}".format(i[0],i[1],i[2],i[3]))
    print("-"*90)

    
def searchmember():
    print("Search Member by :- ")
    print()
    print("1. Member Number")
    print("2. Member Name")
    print()
    w=int(input("Enter Option: "))
    print()
    if w==1:
        b=int(input("Enter member number : "))
        print("Member Details : ")
        q6="Select * from member where Mno=%s"%(b)
        cursor.execute(q6)
        result1=cursor.fetchall()
        print("-"*90)
        print("{0:8}{1:^15}{2:^6}{3:^25}".format("Member Number","Member Name","Member PhoneNo","Membership Status"))
        print("-"*90)
        for i in result1:
            print("{0:8}{1:^25}{2:^2}{3:^28}".format(i[0],i[1],i[2],i[3]))
        print("-"*90)       
    if w==2:
        c=input("Enter member name : ")
        print("Member Details : ")
        q7="Select * from member where MName=%s"%(c)
        cursor.execute(q7)
        result1=cursor.fetchall()
        print("-"*90)
        print("{0:8}{1:^15}{2:^6}{3:^25}".format("Member Number","Member Name","Member PhoneNo","Membership Status"))
        print("-"*90)
        for i in result1:
            print("{0:8}{1:^25}{2:^2}{3:^28}".format(i[0],i[1],i[2],i[3]))
        print("-"*90)

def issuebook():
    viewmembers()
    c=int(input("Enter Member Number whom you want to issue book: "))
    d=int(input("Enter Book Number you want to issue to this member: "))
    print()
    print("Issued Book Status")
    print()
    j=datetime.date.today()
    print("Issue Date: ",j)
    k=datetime.datetime.today() + datetime.timedelta(days=7)
    g=str(k)
    f=g.split()
    h=f[0]
    print("Return Date:",h)
    print()
    q="select member.Mno,member.MName,books.Bno,books.BName,books.BAuthor,member.MActive from member,books where member.Mno=%s and books.Bno=%s"%(c,d)
    cursor.execute(q)
    result3=cursor.fetchall()
    print("-"*90)
    print("{0:8}{1:^15}{2:^8}{3:^15}{4:^8}{5:^25}".format("Member Number","Member Name","Book Number","Book Name","Book Author","Membership Status"))
    print("-"*90)
    for i in result3:
        print("{0:8}{1:^25}{2:^2}{3:^21}{4:^8}{5:^20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print("-"*90)



def graph():
    print()
    c=[]
    d=[]
    cursor.execute("Select distinct(BAuthor)from books")
    result=cursor.fetchall()
    for i in result:
        for j in i:
            c.append(j)
    for m in c:
        q="Select count(BAuthor) from books where BAuthor = '%s' "%(m)
        cursor.execute(q)
        f=cursor.fetchall()
        for n in f:
            for o in n:
                d.append(o)
    plt.bar(c,d,width=.45)
    plt.title("Author-Wise Issue Of Books")
    plt.xlabel("Author Name")
    plt.ylabel("Number of books issued")
    plt.show()





    
def books():
    while True:
        booksmenu()
        c=int(input("Enter Option:"))
        if c==1:
            print()
            addbook()
        if c==2:
            print()
            upbook()
        if c==3:
            print()
            delbook()
        if c==4:
            print()
            searchbook()
        if c==5:
            print()
            viewbooks()
        if c==6:
            librarianoptions()

        
def member():
    while True:
        print()
        membermenu()
        c=int(input("Enter Option: "))
        if c==1:
            print()
            addmember()
        elif c==2:
            print()
            upmember()
        elif c==3:
            print()
            delmember()
        elif c==4:
            print()
            viewmembers()
        elif c==5:
            print()
            issuebook()
        elif c==6:
            graph()
        elif c==7:
            librarianoptions()


def user():
    while True:
        print()
        usermenu()
        f=int(input("Enter Option: "))
        if f==1:
            searchbook()
        if f==2:
            viewbooks()
        if f==3:
            graph()
        if f==4:
            library()
            

def librarianoptions():
        print("-"*24)
        print("     LIBRARIAN MENU    ")
        print("-"*24)
        print("1. Books")
        print("2. Member")
        print("3. Exit")
        print("-"*24)
        print()
        c=int(input("Enter your option: "))
        if c==1:
            books()
        if c==2:
            member()
        if c==3:
            library()


            

def lib_reg():
    a=input("Enter an admin name: ")
    p=input("Enter a password: ")
    
    q1=("Insert into reg(admin, password) values(%s,%s)")
    data=(a,p)
    cursor.execute(q1,data)
    db.commit()
    
    print()
    print("Registraion successful")
    print()
    librarian()



    
def login():
    b = input("Enter admin name : ")
    c = input("Enter password: ")
    print()
    
    q = "Select * from reg where admin ='%s'"%(b)
    cursor.execute(q)
    result1=cursor.fetchall()
    
    for i in result1:
        if i[1] == c:
            print()
            print("Logged in as Librarian! ")
            print()
            print()
            librarianoptions()
        else:
            print("Entered admin id or password is wrong! Please Type Again...")
            print()
            librarian()

    
def librarian():
    print("-"*24)
    print("1. Login")
    print("2. New registration")
    print("3. Exit")
    print("-"*24)
    
    ch = int(input("Enter your choice: "))

    if ch == 1:
        login()
        print()

    elif ch == 2:
        lib_reg()
        print()
        
    elif ch == 3:
        library()

        
def library():
    print()
    print("-"*19)
    print("     MAIN MENU    ")
    print("-"*19)
    print("1. Librarian")
    print("2. User")
    print("3. Exit")
    print("-"*19)
    print()
    p=int(input("Enter Option :"))
    print()          
    if p==1:
        librarian() 
    if p==2:
        user()
    else:
        exit()
        
print()
print("WELCOME TO LIBRARY MANAGEMENT SYSTEM !!")
print()

library()



