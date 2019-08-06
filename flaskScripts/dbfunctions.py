from dbconnection import *
import json

# FUNCTION TO RUN THE QUERIES WITH SQL COMMANDS
def runSqlcommand(sql,status):
    mydict = {}
    conncur, conn, constatus = connecttodb()
    try:
        conncur.execute(sql)
        conn.commit()
        mydict['status'] = status
    except:
        status = "Error while pushing the data"
    mydict['status'] = status
    return mydict

# FUCNTION TO CREATE AND UPDATE THE USER ON DUPLICATE KEY
def createUpdateUser(inputData):
    sql = "insert into customernewdata (customerid,fname,mname,lname,dob,mobnumber,gender,resaddtype) \
values (%d,'%s','%s','%s','%s','%s','%s','%s')" %(int(inputData['custnumber']),str(inputData['fname']),str(inputData['mname']),\
str(inputData['lname']),str(inputData['dob']),str(inputData['mobnumber']),str(inputData['gender']),str(inputData['resaddtype']))
    status = "Created the user"
    returndict = runSqlcommand(sql,status)  # calling another function to execute the sql commands
    return returndict

# FUCTION TO DELETE THE USER
def deleteUser(inputData):
    sql = ("delete from customerdata where custnumber = {}".format(inputData['custid']))
    print sql
    status = "Delele user data"
    returndict = runSqlcommand(sql,status)  # calling another function to execute the sql commands
    return returndict

# FUNCTION TO FETCH THE USER DETAILS
def getUser(inputData):
    conncur, conn, constatus = connecttodb()
    conncur = conn.cursor(pymysql.cursors.DictCursor)
    myrellist = {}
    sql = "select * from customernewdata where customerid = %d" %(int(inputData['custid']))
    conncur.execute(sql)
    myrellist = conncur.fetchall()
    return myrellist[0]
