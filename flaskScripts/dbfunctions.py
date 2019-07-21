from dbconnection import *
import json

# FUNCTION TO RUN THE QUERIES WITH SQL COMMANDS
def runSqlcommand(sql,status):
    mydict = {}
    conncur, conn, constatus = connecttodb()
    try:
        conncur.execute(sql)
        conn.commit()
    except:
        status = "Error while pushing the data" + sql
    mydict['status'] = status
    return json.dumps(mydict)

# FUCNTION TO CREATE AND UPDATE THE USER ON DUPLICATE KEY
def createUpdateUser(inputData):
    sql = "insert into customerdata(fname,mname,lname,dob,mobnumber,gender,custnumber,cob,cor,customersegment,resaddtype,resline1,\
    resline2,resline3,resline4,rescouncode,reszipcode,resstage,rescity,offaddtype,offline1,offline2,offline3,offline4,offcoucode,\
    offzipcode,offstate,offcity) \
    values ('%s','%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
    '%s','%s','%s','%s','%s','%s','%s') \
    ON DUPLICATE KEY UPDATE fname='%s',mname='%s',lname='%s',dob='%s',mobnumber='%d',gender='%s',custnumber='%s',cob='%s',cor='%s',customersegment='%s',\
    resaddtype='%s',resline1='%s',resline2='%s',resline3='%s',resline4='%s',rescouncode='%s',reszipcode='%s',resstage='%s',rescity='%s',\
    offaddtype='%s',offline1='%s',offline2='%s',offline3='%s',offline4='%s',offcoucode='%s',offzipcode='%s',offstate='%s',offcity='%s'" \
    % (inputData['fname'],inputData['mname'],inputData['lname'],inputData['dob'],inputData['mobnumber'],inputData['gender'],inputData['custnumber'],\
       inputData['cob'],inputData['cor'],inputData['customersegment'],inputData['resaddtype'],inputData['resline1'],\
        inputData['resline2'],inputData['resline3'],inputData['resline4'],inputData['rescouncode'],inputData['reszipcode'],\
        inputData['resstage'],inputData['rescity'],inputData['offaddtype'],inputData['offline1'],inputData['offline2'],\
        inputData['offline3'],inputData['offline4'],inputData['offcoucode'],inputData['offzipcode'],inputData['offstate'],inputData['offcity'], \
        inputData['fname'], inputData['mname'], inputData['lname'], inputData['dob'], inputData['mobnumber'],\
        inputData['gender'], inputData['custnumber'], inputData['cob'], inputData['cor'], inputData['customersegment'],\
        inputData['resaddtype'], inputData['resline1'], inputData['resline2'], inputData['resline3'], inputData['resline4'], \
        inputData['rescouncode'], inputData['reszipcode'], inputData['resstage'], inputData['rescity'], \
        inputData['offaddtype'], inputData['offline1'], inputData['offline2'], inputData['offline3'], \
        inputData['offline4'], inputData['offcoucode'], inputData['offzipcode'],\
        inputData['offstate'], inputData['offcity'])
    status = "Delele user data"
    runSqlcommand(sql,status)  # calling another function to execute the sql commands
    return "Sent to db for executing"

# FUCTION TO DELETE THE USER
def deleteUser(inputData):
    sql = 'delete from customerdata where custnumber = %s'.format(inputData['custnumber'])
    status = "Delele user data"
    runSqlcommand(sql,status)  # calling another function to execute the sql commands
    return "Sent data to delete the user"

# FUNCTION TO FETCH THE USER DETAILS
def getUser(inputData):
    conncur, conn, constatus = connecttodb()
    sql = 'select * from customerdata where custnumber = %s'.format(inputData['custnumber'])
    try:
        conncur.execute(sql)
        myrellist = dict(conncur.fetchall())
    except:
        print "Error", sql
    return json.dumps(myrellist)