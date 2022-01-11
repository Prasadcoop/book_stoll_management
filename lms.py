import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",passwd="Prasad@14",database="book_stoll")
print("\t")
print("*"*90)
print(' '*25,end=" ")
print("Book Stoll Management")
print("*"*90)

cursor=con.cursor()

def add():
    bid=int(input("Enter Book B_Id:"))
    name=input("Enter Book Name:")
    writer=input("enter Writer name:")
    qty=int(input("Enter qty:"))
    price=int(input("Enter Book price:"))
    query="insert into details(bid,name,writer,qty,price)value({},'{}','{}',{},{})".format(bid,name,writer,qty,price)
    qry="insert into info(bid,name,writer) values({},'{}','{}')".format(bid,name,writer)
    cursor.execute(query)
    cursor.execute(qry)
    con.commit()
    print("Data insert successfully...")
    main()

def find():
    title=input("Enter the Book details :")
    b="select bid,name,writer from info where name='{}'".format(title)

    cursor.execute(b)
    result=cursor.fetchone()
    print("+"*90,"\n"," "*26,title,"book details is")
    print("\t")
    for i in result:
        
        print(i,end="\t|\t")
    main()

def update():
    title=input("Enter the book Name :")
    u=int(input("Enter the qty :"))
    
    query="select qty from details where name='{}'".format(title) #SELECT DATA FROM TABLE
    cursor.execute(query)
    result=cursor.fetchone() #MATCHING WITH INPUT
    b=result[0]
    up_date=b-u
    qry="update details set qty={} where name='{}'".format(up_date,title) #UPDATE QTY FROM TABLE 
    cursor.execute(qry)
    con.commit()
    print("Collecting Your Order...")
    main()
def price():
    title=input("Enter Book Name :")
    query="select price from details where name='{}'".format(title)
    cursor.execute(query)
    result=cursor.fetchone()
    b=result[0]
    print("\t")
    print('[','Book Price of',title,'is',b,']')
    main()
def main():
     print("\n")
     print("+"*90)

     print(" "*6,"[]"*10,"M A I N_M E N U","[]"*10)
     print("\t")
    
     print(" "*26,"1.ADD BOOK\n"," "*25,"2.FINDING BOOK\n"," "*25,"3.BUYING BOOK\n"," "*25,"4.PRICE\n"," "*25,"5.CLOSE")
     print("+"*90)
     choice=input("Enter Your Choice :")
     print("+"*90)
     if(choice=='1'):

         add()
     elif(choice=='2'):
         find()
     elif(choice=='3'):
         update() 
     elif(choice=='4'):
         price()  
     elif(choice=='5'):
         print("T H A N K S___Y O U....\t")
         exit() 
         
     else:
         print("Invalid Choice.....") 
         main()
main()

