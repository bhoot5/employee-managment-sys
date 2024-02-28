
print ("welcome!")
print ("entering mysql.!!,,please wait!!!")
h=1
import pandas as pd
from datetime import date
today = date.today ()
d=today.strftime("%Y-%m-%d")
import mysql.connector
while h == 1:
 x1 = input ("your username for mysql- ")
 x2 = input ("your password for mysql- ")
 config = {
    'user' : x1,
    'password' : x2,
    'host' : "localhost",
    'database' : 'employees'}
 try:
  m1 = mysql.connector.connect (**config)
  m = m1.cursor ()
  break
 except:
  print('''
opppsss!!something went wrong!!
your errors can be:
1.wrong username 
2.wrong password
3.wrong host
please try again!!''')
  continue

def register():
   m=m1.cursor()
   print("employee registration!!")
   m.execute("select count(*) from office")
   x4=list(m)[0][0]+100
   y=input("name - ")
   z=input("department - ")
   s2=str(d)
   e=None
   m=m1.cursor()
   m.execute("select dept_salary from department where em_dept='%s'"%(z))
   f=m.fetchall()[0][0]
   g2=g3=y
   w=0
   m=m1.cursor()
   m.execute("select * from department")
   m=m.fetchall()
   t=0
   for i in m:
       if i[0]==z:
           m=m1.cursor()
           m.execute("update department set no_of_employees={0} where em_dept='{1}'".format(i[1]+1,i[0]))
           t=1
   if t==0:
       m.execute("insert into department values('{0}',{1})".format(z,1))
   m.execute("insert into performance values({0},'{1}','{2}','{3}')".format(x4,y,z,e))
   m.execute("insert into office values({0},'{1}','{2}',{3},'{4}',{5})".format(x4,y,z,f,s2,w))
   m.execute("insert into login values ({0},'{1}','{2}',{3},'{4}')".format(x4,g2,g3,0,s2))
   m1.commit()
   print('registered')

def update_salary():
    print("update salary!!")
    d=input("enter department")
    b=int(input("new salary - "))
    m.execute("update department set dept_salary ={0} where em_dept='{1}'".format(b,d))
    m1.commit()
    print('salary updated')

def display_list():
    print()
    print("employees list!!")
    a23=("select em_name from office")
    m.execute (a23)
    for i in m :
         print (i[0])
         
def number_employees():
    print()
    print("no. of employees!!")
    a23=("select count(em_no) from office")
    m.execute (a23)
    for i in m :
       print (i[0])
       
def delete_emp():
    c1=int(input("em_no of the employee"))
    m.execute("delete from office where em_no={0}".format(c1))
    m.execute ("delete from performance where em_no={0}".format(c1))
    m.execute ("delete from login where em_no={0}".format(c1))
    m1.commit()
    print("employee dropped")

def attendance(a,c):
    m=m1.cursor()
    m.execute("select attendance,last_login from login where username='{0}' and em_no={1}".format(a,c))
    t=m.fetchall()[0]
    
    if t[1]==today:
       print("attendance already done")
    else: 
      m=m1.cursor()
      
      m.execute("update login set attendance={0} where em_no={1}".format(int(t[0])+1,c))
      m.execute("update login set last_login='{0}' where em_no={1}".format(d,c))
      m=m1.cursor()
      m.execute("select dept_salary from office,department where office.em_dept=department.em_dept and  office.em_no={0}".format(c))
      m=m.fetchall()[0][0]
      
      net_salary=(int(t[0])+1)*int(m)
      m=m1.cursor()
      m.execute("update office set em_salary={0} where em_no={1}".format(net_salary,c))
      m1.commit()
      print("attendance done")
      
   
def update_workyears():
    m=m1.cursor()
    m.execute("select em_doj,em_no from office")
    t=m.fetchall()
    z=0
    for i in t:
        w=today.year-i[0].year
        m=m1.cursor()
        m.execute("update office set em_workyears={0} where em_no={1}".format(w,t[z][1]))
        z+=1
    print('workyears updated')
    m1.commit()

def admin():
    while True:
       m=m1.cursor()
       print ('''
##some predefined queries:
1-employee details
2-employee registration
3-update salary
4-employees list
5-no. of employees
6-drop an employee
7-update workyears
8-exit''')
       x = input ("query- ")
       a_=1
       if x == "1":
           print("employee details!!")
           print ("query ok!!")
           a = input("name - ")
           m.execute('''SELECT office.*,p.em_performance,attendance from office,performance p,login where office.em_no=p.em_no and office.em_no=login.em_no and office.em_name='{0}' '''.format(a))
           h5=m.column_names
           m=m.fetchall()
           table=pd.DataFrame(m)
           table.columns=h5
           pd.set_option('display.max_columns', None)
           print(table)
       elif x == "2":
           register()
       elif x == "3":
           update_salary()
       elif x == "4":
           display_list()
       elif x == "5":
           number_employees()
       elif x == "6":
           delete_emp()
       elif x=="7":
           update_workyears()
       elif x == "8" :
           print ("thank you! exiting!!")
           break
       m1.commit()
        
def personal_details(a,c):
   global m1
   m=m1.cursor()
   m.execute("SELECT office.*,p.em_performance,attendance from office,performance p,login where office.em_no=p.em_no and office.em_no=login.em_no and office.em_name='{0}'and office.em_no={1}".format(a,c))
   header=m.column_names
   m=m.fetchall()
   table=pd.DataFrame(m)
   table.columns=header
   pd.set_option('display.max_columns', None)
   print(table)
   
def login():
   while True:
      g=input("user or admin or exit - ")
      if g == "user":
         a=input("username - ")
         b=input("password - ")
         c=input("em_no-")
         m=m1.cursor()
         m.execute("select em_no,username,password from login where em_no={0} and username='{1}' and password='{2}'".format(c,a,b))
         m=m.fetchall()
         if m==[]:
             print("username/password/em-no invalid")
             continue
         while True:
           print('''##some predefined queries:
           1-attendance
           2-personal details
           3-exit''')
           x = input ("query- ")
           if x=="1":
               attendance(a,c)
               
           elif x=="2":
               personal_details(a,c)
           elif x=="3":
               break
      elif g == "admin":
         a__ =input("admin password - ")
         if a__ == "admin123":
            admin()
      elif g=="exit":
          break
login()
