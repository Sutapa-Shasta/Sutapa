import xlrd
import MYSQLdb

excell_sheet= open_workbook("https://docs.google.com/spreadsheets/d/1cnPUhCbUm5p3DMWw6wcSu4li7qChBrhd-UyRkW2RSUg/edit?usp=sharing")
s=excell_sheet.sheet_by_name("beginner_assignment01")
database= MYSQLdb.connect(host: "localhost",user: "root", passwd: "", db = MysqlPython)
cursor=database.cursor()
sqlquery= """insert into NEW_PRODUCTLIST (Product_Name, Model_Name, Product_Serial_no, Group_Associated, Product_MRP) VALUES (%s, %s, %s, %s, %s )"""
for i in range (1,s.nrows):
    Product_Name = s.cell(i,0).value
    Model_Name = s.cell(i,1).value
    Product_Serial_no = s.cell(i,2).value
    Group_Associated = s.cell(i,3).values
    Product_MRP = s.cell(i,4).value
    values = (Product_Name, Model_Name, Product_Serial_no, Group_Associated, Product_MRP)
    cursor.execute(sqlquery,values)
cursor.close()
database.commit()
database.close()


#import xlrd - to import excell sheet
#import MYSQLdb - to easily connect to the database
#excell_sheet= open_workbook - used to open the given excell sheet
#s=excell_sheet.sheet_by_name - used to define the excell sheet
#database= MYSQLdb.connect - used to establish a database connection
#host - used for the local host 
#user - used for the user name 
#passwd - used for the password
#db - used for the database name
#cursor=database.cursor - used to read the excell sheet line by line
#sqlquery = insert into NEW_PRODUCTLIST(...) VALUES (...) - used to insert values into the table NEW_PRODUCTLIST
#for loop is used to insert data 
#cursor.execute - used to execute the sql query 
#cursor.close - used to close the previously opened cursors
#database.commit - used to save the data permanently into the database by commit
#database.close - used to close the database
