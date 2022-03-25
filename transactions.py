'''
transactions.py is a Object Relational Mapping to the categories table

The ORM will work map SQL rows with the schema
    (rowid,name,description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3

def to_cat_dict(cat_tuple):
    ''' cat is a category tuple (rowid, name, desc)'''
    cat = {'rowid':cat_tuple[0], 'name':cat_tuple[1], 'desc':cat_tuple[2]}
    return cat

def to_cat_dict_list(cat_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_cat_dict(cat) for cat in cat_tuples]

class Transaction():
    ''' Category represents a table of categories'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no int, amount NUMERIC, category text, date text, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_date(self, date):
        ''' summarize via date '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from categories WHERE date(date) =", date)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def select_date(self, month):
        ''' summarize via a month, no particular year '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from categories WHERE month(date) =", month)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def select_month(self):
        ''' summarize via date '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from categories ORDER BY date")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def select_all(self):
        ''' return all of the categories as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def select_one(self,rowid):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from categories where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict(tuples[0])

    #Sanjna
    def add_sb(self,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        #create global variable 
        global item_num
        item_num = 1
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()

        #edit parameters 
        cur.execute("INSERT INTO categories VALUES(?,?,?,?,?)",('item_no', item['amount'],item['category'],
        item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()

        item_num +=1 #increment global variables 
        return last_rowid[0]

    #Sanjna new feature 
    def show(self, amount):
        '''
            shows amount of each transaction 
        '''

    def add_jf(self, tuple):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?, ?, ?, ?, ?)", tuple)
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,rowid,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE categories
                        SET name=(?), desc=(?)
                        WHERE rowid=(?);
        ''',(item['name'],item['desc'],rowid))
        con.commit()
        con.close()

    def delete(self,rowid):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM categories
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()
