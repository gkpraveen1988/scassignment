import pymysql

# Open database connection
def connecttodb():
    keyname = 'password123'
    hstnm = ''
    unm = 'admin'
    dbnm = ''
    try:
        constatus = 1
        db = pymysql.connect(hstnm,unm,keyname,dbnm)
        cursor = db.cursor()
    except pymysql.error as constatus:
        print constatus
    return cursor,db,constatus