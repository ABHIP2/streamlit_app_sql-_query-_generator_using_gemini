import sqlite3

#Connectt to SQlite
#Our database name: Naresh_it_student
connection=sqlite3.connect("Naresh_it_employee.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

#create the table
#Our table name student
#Columns names are: name, course
table_info="""
Create table Naresh_it_employee(employee_name varchar(30),
                    employee_role varchar(50),
                    employee_salary FLOAT,
                    employee_address varchar (20));
"""
cursor.execute(table_info)

#Insert the records

cursor.execute('''Insert Into Naresh_it_employee values('Omkar Nallagoni','Data Science',75000,'hyd')''')
cursor.execute('''Insert Into Naresh_it_employee values('Naresh','Data Science',90000,'blr')''')
cursor.execute('''Insert Into Naresh_it_employee values('Phani','Data Science',88000,'mum')''')
cursor.execute('''Insert Into Naresh_it_employee values('Naga babu','Data Engineer',50000,'pune')''')
cursor.execute('''Insert Into Naresh_it_employee values('Ajay','Data Engineer',35000,'hubli')''')
cursor.execute('''Insert Into Naresh_it_employee values('Pawan','Data Engineer',60000,'dhl')''')
cursor.execute('''Insert Into Naresh_it_employee values('Abhi','Data Scientist',100000,'Tas')''')
cursor.execute('''Insert Into Naresh_it_employee values('Punit','Data Scientist',100000,'ayd')''')


#Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from Naresh_it_employee''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()