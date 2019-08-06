import pymysql

# Open database connection
def connecttodb():
    keyname = '##########'
    hstnm = '##########'
    unm = 'appadminuser'
    dbnm = 'appserverrds'
    try:
        constatus = 1
        db = pymysql.connect(hstnm,unm,keyname,dbnm)
        cursor = db.cursor()
    except pymysql.error as constatus:
        print constatus
    return cursor,db,constatus

if __name__ == "__main__":
    cursor,db,constatus = connecttodb()
    print cursor,db,constatus
