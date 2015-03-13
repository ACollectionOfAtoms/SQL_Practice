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
                self.audit = audit(self.id)
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
            return None
        elif option == "2":
            self.plan()
            return None
        elif option == "3":
            self.play()
            return None
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
                print '\t' + i[0]
        print ''
        print 'I found these albums that match your request:'
        for i in titles:
            if search.lower() in i[0].lower():
                print '\t' + i[0]
        print ''
        print 'I found these songs that match your request:'
        for i in songs:
            if search.lower() in i[0].lower():
                print '\t' + 'Song ID: ' + str(i[2]) + '\t' + 'Song Name: ' + i[0].ljust(15) + '\t' + 'ALBUM ONLY?' + ': ' + i[1]
        print ''
        print 'Of these songs found, you have listened to:'
        for i in listened:
            for j in songs:
                if search.lower() in j[0].lower() and i[0] == j[2]:
                    print '\t' + j[0]
        print '***'
        print 'Would you like to search again?'
        print "(1) Yes"
        print "(2) No"
        choice = 0
        while choice != "1" or choice != "2":
            choice = raw_input("Enter your choice: ")
            if choice == "1":
                self.search()
                return None
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
                        con.commit()
                        cur.execute('DELETE FROM DAILY WHERE CUSTOMER_ID =' + self.id)
                        con.commit()
                        print ('*** Plan Successfully changed. ***')
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
                        cur.execute('DELETE FROM DAILY WHERE CUSTOMER_ID =' + self.id)
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
            
    def play(self):
        print '***'
        #Get the newest Stream_ID and increment it by 1.
        cur.execute('SELECT STREAM_ID FROM STREAMS WHERE STREAM_ID = (SELECT MAX(STREAM_ID) FROM STREAMS)')
        s_id = cur.fetchall()
        s_id = s_id[0][0] + 1
        
        #Inquire.
        choice = raw_input("Please type the Song ID to play a song: ")

        # Gather 0 Songname, 1 Album ID, 2 Album Title,  3 Artist
        cur.execute('SELECT s.song_name, i.item_id, i.title, i.artist from songs s left join items i on s.item_id = i.item_id where song_id = ' + choice)
        info = cur.fetchall()
        #extract tuple from list.
        info = info[0]
        
        # Check if Song Id is valid.
        if len(info) == 0:
            print 'Sorry, that was an invalid Song I.D'
            self.play()


        # Is it album only?
        cur.execute('SELECT SONG_ALBUM_ONLY FROM SONGS WHERE SONG_ID = ' + choice )
        albumonly = cur.fetchall()
        # Extract string. 
        albumonly = albumonly[0][0]
        
        # Check if there is a stream that is already active.
        cur.execute('SELECT STREAM_ID FROM STREAMS WHERE CUSTOMER_ID = ' + self.id + " and STREAM_STATUS = 'ACTIVE'")
        check = cur.fetchall()

        #if none found... Continue to play
        if len(check) == 0:
            if albumonly == 'YES':
                #Get album id
                cur.execute('SELECT ITEM_ID FROM SONGS WHERE SONG_ID = ' + choice)
                itemid = cur.fetchall()
                itemid = str(itemid[0][0])
                #Get songs on album
                cur.execute('SELECT SONG_ID FROM SONGS WHERE ITEM_ID = ' + itemid)
                album = cur.fetchall()
                #Store last song, then gather all songs but the last.
                lastsong = album[-1]
                lastsong = str(lastsong[0])
                songs = album[:-1]
                tally = len(album)

                #use audit to check if songs can be played
                if self.audit.add(tally):
                    pass
                else:
                    print 'Sorry, Playing This Song Would Exceed your Daily Limit!'
                    print '(1) Main Menu (2) Exit'
                    opt = raw_input('Select: ')
                    if opt == "1":
                        self.menu()
                        return None
                    if opt == "2":
                        return None

                for song in songs:
                    cur.execute('SELECT s.song_name, i.item_id, i.title, i.artist, s.song_album_only from songs s left join items i on s.item_id = i.item_id where song_id = ' + str(song[0]))
                    info = cur.fetchall()
                    info = info[0]
                    #make the song active
                    sql = "INSERT INTO STREAMS VALUES (:s_id, :self_id, :choice, 'ACTIVE')"
                    cur.execute(sql, s_id=s_id,self_id=int(self.id),choice=int(song[0]))
                    con.commit()
                    print 'Now playing %s, on %s, by %s' % (info[0],info[2],info[3])
                    #Deactivate it
                    cur.execute('SELECT STREAM_ID FROM STREAMS WHERE CUSTOMER_ID = ' + self.id + " and STREAM_STATUS = 'ACTIVE'")
                    check = cur.fetchall()
                    cur.execute("UPDATE STREAMS SET STREAM_STATUS = 'INACTIVE' WHERE STREAM_ID = " + str(check[0][0]) )
                    con.commit()
                    #increment Stream ID!
                    s_id += 1

                #play last song. 
                cur.execute('SELECT s.song_name, i.item_id, i.title, i.artist, s.song_album_only from songs s left join items i on s.item_id = i.item_id where song_id = ' + lastsong)
                info = cur.fetchall()
                #extract tuple from list.
                info = info[0]

                sql = "INSERT INTO STREAMS VALUES (:s_id, :self_id, :choice, 'ACTIVE')"
                cur.execute(sql, s_id=s_id,self_id=int(self.id),choice=int(lastsong))
                con.commit()
                print '(1) Main Menu (2) Play Another Song (3) Exit'
                opt = raw_input('Select: ')
                if opt == "1":
                    self.menu()
                    return None
                if opt == "2":
                    self.play()
                    return None
                if opt == "3":
                    return None

            else:
                tally = 1
                if self.audit.add(tally):
                    pass
                else:
                    print 'Sorry, You Have No More Plays Available Today!'
                    print '(1) Main Menu (2) Exit'
                    opt = raw_input('Select: ')
                    if opt == "1":
                        self.menu()
                        return None
                    if opt == "2":
                        return None

                sql = "INSERT INTO STREAMS VALUES (:s_id, :self_id, :choice, 'ACTIVE')"
                cur.execute(sql, s_id=s_id,self_id=int(self.id),choice=int(choice))
                con.commit()
                print '(1) Main Menu (2) Play Another Song (3) Exit'
                opt = raw_input('Select: ')
                if opt == "1":
                    self.menu()
                    return None
                if opt == "2":
                    self.play()
                    return None
                if opt == "3":
                    return None

        # If an active stream is found, set it to inactive, and then play.
        else:
            cur.execute("UPDATE STREAMS SET STREAM_STATUS = 'INACTIVE' WHERE STREAM_ID = " + str(check[0][0]) )
            con.commit()
            if albumonly == 'YES':
                cur.execute('SELECT ITEM_ID FROM SONGS WHERE SONG_ID = ' + choice)
                itemid = cur.fetchall()
                itemid = str(itemid[0][0])
                cur.execute('SELECT SONG_ID FROM SONGS WHERE ITEM_ID = ' + itemid)
                #get album
                album = cur.fetchall()
                #Store last song, then gather all songs but the last.
                lastsong = album[-1]
                lastsong = str(lastsong[0])
                songs = album[:-1]
                tally = len(album)

                #use audit to check if songs can be played
                if self.audit.add(tally):
                    pass
                else:
                    print 'Sorry, You Have No More Plays Available Today!'
                    print '(1) Main Menu (2) Exit'
                    opt = raw_input('Select: ')
                    if opt == "1":
                        self.menu()
                        return None
                    if opt == "2":
                        return None

                for song in songs:
                    cur.execute('SELECT s.song_name, i.item_id, i.title, i.artist, s.song_album_only from songs s left join items i on s.item_id = i.item_id where song_id = ' + str(song[0]))
                    info = cur.fetchall()
                    info = info[0]
                    sql = "INSERT INTO STREAMS VALUES (:s_id, :self_id, :choice, 'ACTIVE')"
                    cur.execute(sql, s_id=s_id,self_id=int(self.id),choice=int(song[0]))
                    con.commit()
                    print 'Now playing %s, on %s, by %s' % (info[0],info[2],info[3])
                    cur.execute('SELECT STREAM_ID FROM STREAMS WHERE CUSTOMER_ID = ' + self.id + " and STREAM_STATUS = 'ACTIVE'")
                    check = cur.fetchall()
                    cur.execute("UPDATE STREAMS SET STREAM_STATUS = 'INACTIVE' WHERE STREAM_ID = " + str(check[0][0]) )
                    con.commit()
                    s_id += 1
                songs = songs[-1]
                cur.execute('SELECT s.song_name, i.item_id, i.title, i.artist, s.song_album_only from songs s left join items i on s.item_id = i.item_id where song_id = ' + lastsong)
                info = cur.fetchall()
                #extract tuple from list.
                info = info[0]

                sql = "INSERT INTO STREAMS VALUES (:s_id, :self_id, :choice, 'ACTIVE')"
                cur.execute(sql, s_id=s_id,self_id=int(self.id),choice=int(lastsong))
                con.commit()
                print 'Now playing %s, on %s, by %s' % (info[0],info[2],info[3])
                print '(1) Main Menu (2) Play Another Song (3) Exit'
                opt = raw_input('Select: ')
                if opt == "1":
                    self.menu()
                    return None
                if opt == "2":
                    self.play()
                    return None
                if opt == "3":
                    return None
            else:
                tally = 1
                if self.audit.add(tally):
                    pass
                else:
                    print 'Sorry, You Have No More Plays Available Today!'
                    print '(1) Main Menu (2) Exit'
                    opt = raw_input('Select: ')
                    if opt == "1":
                        self.menu()
                        return None
                    if opt == "2":
                        return None

                sql = "INSERT INTO STREAMS VALUES (:s_id, :self_id, :choice, 'ACTIVE')"
                cur.execute(sql, s_id=s_id,self_id=int(self.id),choice=int(choice))
                con.commit()
                print 'Now playing %s, on %s, by %s' % (info[0],info[2],info[3])
                print '(1) Main Menu (2) Play Another Song (3) Exit'
                opt = raw_input('Select: ')
                if opt == "1":
                    self.menu()
                    return None
                if opt == "2":
                    self.play()
                    return None
                if opt == "3":
                    return None

class audit:
    def __init__(self,id):
        if id == 0:
            pass
        else:
            self.id = id
            self.custid = self.id
            cur.execute('SELECT C.CUSTOMER_ID, C.CUSTOMER_PLAN, P.PLAN_PLAYS FROM CUSTOMERS C LEFT JOIN PLANS P ON C.CUSTOMER_PLAN = P.PLAN_NAME WHERE CUSTOMER_ID = ' + self.custid)
            self.limit = cur.fetchall()
            self.limit = self.limit[0][2]

    def daycheck(self):
        print 'day check running'
        cur.execute('SELECT CURRENT_DATE FROM DUAL')
        today = cur.fetchall()
        print today 
        cur.execute('SELECT TODAY FROM DAILY WHERE DAILY_ID = 1')
        check = cur.fetchall()
        print check
        if today != check:
            cur.execute('TRUNCATE TABLE DAILY')
            con.commit()
            cur.execute('INSERT INTO DAILY VALUES (1,0,0,CURRENT_DATE)')
            con.commit()
            print 'Days checked!'
            return None
        else:
            return None
    # fetches number of total daily plays
    def fetch_plays(self):
        cur.execute('SELECT DAILY_PLAYS FROM DAILY WHERE CUSTOMER_ID = ' + self.custid)
        plays = cur.fetchall()
        if len(plays) == 0:
            return 0
        else:
            plays = plays[0][0]
            return plays


    def add(self, n):
        #id of the customer_id and n is the number of plays)
        cur.execute('SELECT DAILY_ID FROM DAILY WHERE DAILY_ID = (SELECT MAX(DAILY_ID) FROM DAILY)')
        d_id = cur.fetchall()
        d_id = d_id[0][0] + 1
        d_id = str(d_id)


        if (self.fetch_plays() + n) < self.limit:
            cur.execute('SELECT * FROM DAILY WHERE CUSTOMER_ID = ' + self.custid)
            info = cur.fetchall()
            if len(info) == 0:
                sql = "INSERT INTO DAILY VALUES(:DAILY_ID,:CUSTOMER_ID,:DAILY_PLAYS,CURRENT_DATE)"
                cur.execute(sql,DAILY_ID=d_id,CUSTOMER_ID=self.custid,DAILY_PLAYS=n)
                con.commit()
                return True
            else:
                sql = "UPDATE DAILY SET DAILY_PLAYS = (DAILY_PLAYS + :n ) WHERE CUSTOMER_ID =:id"
                cur.execute(sql,n=str(n),id=self.custid)
                con.commit()
                return True
        else:
            return False
            



def main():
    print '***'
    print "Welcome to Groovy-Pandorify-Shark!"
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    print '***'
    u = User(username,password)
    #ping server to verify date
    ping = audit(0)
    ping.daycheck()
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
