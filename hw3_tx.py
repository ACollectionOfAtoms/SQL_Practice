import cx_Oracle
import sys
con = cx_Oracle.connect('dah3227_om/Oradah3227@//net6.cs.utexas.edu:1521/orcl')
cur = con.cursor()

class User:

    def __init__(self,login,password):
        self.login = login
        self.password = password
        
    def connect(self):
        cur.execute('SELECT CUSTOMER_LOGIN, CUSTOMER_PASSWORD, CUSTOMER_ID FROM CUSTOMERS')
        info = cur.fetchall()
        for i in info:
            if i[0] == self.login and i[1] == self.password:
                self.id = str(i[2])
                return True
            else:
                pass

    def menu(self):
        print '***'
        print 'Welcome %s, what would you\nlike to do today?' % (self.login)
        print '(1) Search for a song'
        print '(2) Plan Options'
        print '(3) Play Music'
        print '(4) Exit'
        option = 0
        option = raw_input('Please Select: ')
        print '***'
        if option == "1":
            self.search()
        elif option == "2":
            self.plan()
        elif option == "3":
            self.play()
        elif option == "4":
            return None
    
    def search(self):
        search = raw_input('Please type the name of the song or album you wish to find: ')
        print '***'
        cur.execute('SELECT TITLE FROM ITEMS')
        titles = cur.fetchall()

        cur.execute('SELECT SONG_NAME, SONG_ALBUM_ONLY, SONG_ID FROM SONGS')
        songs = cur.fetchall()

        cur.execute('SELECT ARTIST FROM ITEMS')
        artist = cur.fetchall()

        cur.execute('SELECT SONG_ID FROM STREAMS WHERE CUSTOMER_ID ='+self.id)
        listened = cur.fetchall()

        print 'I found these artist that match your request:'
        for i in artist:
            if search.lower() in i[0].lower():
                print i[0]
        print ''
        print ''
        print 'I found these albums that match your request:'
        for i in titles:
            if search.lower() in i[0].lower():
                print i[0]
        print ''
        print ''
        print 'I found these songs that match your request:'
        for i in songs:
            if search.lower() in i[0].lower():
                print i[0] + '\t\t\t\t\t' + 'ALBUM ONLY?' + i[1]
        print ''
        print ''
        print 'Of these songs found, you have listened to:'
        for i in listened:
            for j in songs:
                if i[0] == j[2]:
                    print j[0]
        print '***'
        print 'Would you like to search again?'
        print "(1) Yes"
        print "(2) No"
        choice = 0
        while choice != "1" or choice != "2":
            choice = raw_input("Enter your choice: ")
            if choice == "1":
                self.search()
            elif choice == "2":
                self.menu()
                return None
    
    def plan(self):
        cur.execute('SELECT CUSTOMER_PLAN FROM CUSTOMERS WHERE CUSTOMER_ID ='+self.id)
        plan = cur.fetchall()
        plan = plan[0][0]
        plans = ['GOLD','SILVER','BRONZE']
        plans.pop(plans.index(plan))

        print 'Your current plan is: %s' % (plan)
        print 'Would you like to switch to one of these plans ?'
        for i in range(len(plans)):
            print '('+str(i + 1)+')' + ' ' + plans[i]
        print '(3) No, take me back to the main menu!'
        choice = 0
        while choice != "1" or choice != "2" or choice != "3":
            choice = raw_input("Enter your choice: ")

            if choice == "1":
                print "You've chosen the %s plan" %(plans[0])
                cur.execute('SELECT PLAN_PLAYS, PLAN_FEE FROM PLANS WHERE PLAN_NAME = ' + '\''+plans[0]+'\'')
                info = cur.fetchall()
                print "This plan grants you %i plays, and cost $%s" % (info[0][0],info[0][1])
                opt = 0
                print "(1) Yes, I would like to change my plan."
                print "(2) No, I'll keep my current plan."
                while opt != "1" or opt != "2":
                    opt = raw_input("Are you sure you want to choose this plan?: ")
                    if opt == "1":
                        cur.execute('UPDATE CUSTOMERS SET CUSTOMER_PLAN = ' + '\''+plans[0]+'\'' + 'WHERE CUSTOMER_ID =' + self.id)
                        print ('Plan Successfully changed.')
                        con.commit()
                        self.plan()
                        return None
                    else:
                        self.plan()
                        return None
                    

            elif choice == "2":
                print "You've chosen the %s plan" %(plans[1])
                cur.execute('SELECT PLAN_PLAYS, PLAN_FEE FROM PLANS WHERE PLAN_NAME = ' + '\''+plans[1]+'\'')
                info = cur.fetchall()
                print "This plan grants you %i plays, and cost $%s" % (info[0][0],info[0][1])
                opt = 0
                print "(1) Yes, I would like to change my plan."
                print "(2) No, I'll keep my current plan."
                while opt != "1" or opt != "2":
                    opt = raw_input("Are you sure you want to choose this plan?: ")
                    if opt == "1":
                        cur.execute('UPDATE CUSTOMERS SET CUSTOMER_PLAN = ' + '\''+plans[1]+'\'' + 'WHERE CUSTOMER_ID =' + self.id)
                        con.commit()
                        print ('Plan Successfully changed.')
                        self.plan()
                        return None
                    else:
                        self.plan()
                        return None

            elif choice == "3":
                self.menu()
                return None

def main():
    print '***'
    print "Welcome to Groovy-Pandorify-Shark!"
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    print '***'
    u = User(username,password)
    if u.connect():
        print '___________________________'
        print '*** - Login Succesful - ***'
        print '***                     ***'
        u.menu()
    else:
        print 'Login Failed'
        

main()
cur.close()
con.close()
