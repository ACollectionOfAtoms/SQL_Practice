import cx_Oracle
import sys
con = cx_Oracle.connect('dah3227_om/Oradah3227@//net6.cs.utexas.edu:1521/orcl')
cur = con.cursor()

class User:
    def __init__(self,login,password):
        self.login = login
        self.password = password
        
    def connect(self):
        cur.execute('SELECT CUSTOMER_LOGIN, CUSTOMER_PASSWORD FROM CUSTOMERS')
        info = cur.fetchall()
        if (self.login,self.password) in info:
            print 'Login Succesful'
        else:
            print 'Login Failed'

def main():
    print "Welcome to Pandorify-Shark!"
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    u = User(username,password)
    u.connect()
main()
cur.close()
con.close()

