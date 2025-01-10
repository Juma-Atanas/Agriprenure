#from flet import *
import sqlite3
#import mysql.connector
import bcrypt
# account_user()
#from Session import Sessions

def init_Tb():
    conn= sqlite3.connect('Task.db')
    cursor = conn.cursor()
    #Item, image, Quantity, Price, Age, Gender, Product, Births, Phone1, Phone2,  name1, name2, email, location
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    UseriD INTEGER PRIMARY KEY AUTOINCREMENT, Phone1 INTEGER(10), Phone2 INTEGER(10), name1 
                   VARCHAR(15) NOT NULL, name2 VARCHAR(15) NOT NULL, email VARCHAR(80), Password VARCHAR(10), 
                   County VARCHAR(55), Sub_County VARCHAR(255), Nearest_School VARCHAR(90),image VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''') 
    cursor.execute('''CREATE TABLE IF NOT EXISTS Poultry (
                        Productid INTEGER PRIMARY KEY AUTOINCREMENT, UseriD INTEGER, Item VARCHAR(10), image VARCHAR(255), breed VARCHAR(50), 
                       Quantity INTEGER NOT NULL, Price INTEGER NOT NULL, Age VARCHAR(10), Gender VARCHAR(20), Product VARCHAR(200), 
                       Births INTEGER,  image2 VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (UseriD) REFERENCES Users(UseriD))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Livestock (
                        Productid INTEGER PRIMARY KEY AUTOINCREMENT, UseriD INTEGER, Item VARCHAR(10), image VARCHAR(255), breed VARCHAR(50), 
                       Quantity INTEGER NOT NULL, Price INTEGER NOT NULL, Age VARCHAR(10), Gender VARCHAR(20), Product VARCHAR(200), 
                       Births INTEGER, image2 VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (UseriD) REFERENCES Users(UseriD))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Favorite (
                        User INTEGER, Item VARCHAR(10), Productsid VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (User) REFERENCES Users(UseriD))''')
   
    conn.commit()
    conn.close()

def add_item(Item, image, breed, Quantity, Price, Age, Gender, Product, Births, user, image2):
    if Item=='Poultry':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute('''INSERT INTO Poultry (Item, image, breed, Quantity, 
                Price, Age, Gender, Product, Births, UseriD, image2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                (Item, image, breed, Quantity, Price, Age, Gender, Product, Births, user, image2))
        conn.commit()
        conn.close()

    if Item == 'Livestock':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute('''INSERT INTO Livestock (Item, image, breed, Quantity, 
                Price, Age, Gender, Product, Births, UseriD, image2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                (Item, image, breed, Quantity, Price, Age, Gender, Product, Births, user, image2))
        conn.commit()
        conn.close()
        
    if Item == 'Farmitem':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute('''INSERT INTO Farmitem (Item, image, breed, Quantity, 
                Price, Age, Gender, Product, Births, UseriD, image2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                (Item, image, breed, Quantity, Price, Age, Gender, Product, Births, user, image2))
        conn.commit()
        conn.close()

def get_users(Item):
    if Item == 'Livestock':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Livestock")
        users=cursor.fetchall()
        cursor.execute("SELECT * FROM Users")
        details=cursor.fetchall()
        conn.close()
        return [users, details]
    
    elif Item == 'Poultry':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Poultry")
        users=cursor.fetchall()
        cursor.execute("SELECT * FROM Users")
        details=cursor.fetchall()
        conn.close()
        #print(details)
        return [users, details]
    elif Item == 'Farmitem':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Farmitem")
        users=cursor.fetchall()
        conn.close()
        return [users, details]
    
def get_users_id(Item, id):
    if Item == 'Livestock':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Livestock WHERE UseriD = ?", (id,))
        details=cursor.fetchall()
        conn.close()
        return  details
    
    elif Item == 'Poultry':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Poultry WHERE UseriD = ?", (id,))
        details=cursor.fetchall()
        conn.close()
        return details
    
    elif Item == 'Farmitem':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Farmitem WHERE UseriD = ?", (id,))
        users=cursor.fetchall()
        conn.close()
        return details
    
def account_user(Email):
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()#dictionary=True)
        cursor.execute('''SELECT UseriD, Password, email, name1, name2, Phone1, County, Sub_County, 
                       Nearest_School, image FROM Users WHERE email = ?''', (Email,))
        user=cursor.fetchone()
        cursor.close()
        conn.close()
        return user

def register_user(Phone1, Phone2,  name1, name2, email, Password, County, Sub_county, Nearest_School):
    conn = sqlite3.connect('Task.db')
    cursor=conn.cursor()
    cursor.execute('''SELECT email, name1 FROM Users WHERE email = ? or phone1 = (?)''', (email, Phone1))
    exist=cursor.fetchone()
    try:
        if email in exist or Phone1 in exist:
            print('User Exist',email, Phone1)
    
    except TypeError as T:
        cursor.execute('''INSERT INTO Users (Phone1, Phone2,  name1, name2, email, Password, County, Sub_county, 
                    Nearest_School) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        ( Phone1, Phone2,  name1, name2, email, Password, County, Sub_county, Nearest_School))
        print(f'{name1, name2} added')
        conn.commit()
    cursor.close()
    conn.close()

def recover_password(Phone1, name1, email, Password, County):
    conn = sqlite3.connect('Task.db')
    cursor=conn.cursor()
    cursor.execute('SELECT  Phone1, name1, email, County FROM Users WHERE email = ?', (email,))
    user=cursor.fetchone()
    if str(Phone1)=='0' + str(user[0]) and (name1).lower() == (user[1]).lower() and (County).lower() == (user[3]).lower():
        cursor.execute('UPDATE Users SET Password = ?  WHERE email = ?',
                        (Password, email))
        conn.commit() 
        cursor.close()
        conn.close()
        return 'Success'              
    else:
        print(user[0],Phone1,  user[2], name1, email, Password, user[3],County)
        return 'Failed'
        
    #print('added')

def user_image(id, image):
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()#dictionary=True)
        cursor.execute('UPDATE Users SET image = ? WHERE UseriD = ?', (image, id))
        #user=cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

def check_user(email, Phone):
    conn = sqlite3.connect('Task.db')
    cursor=conn.cursor()
    try:
        cursor.execute('''SELECT email, name1, Phone1 FROM Users WHERE email = ? or phone1 = (?)''', (email, Phone))
        exist=cursor.fetchall()
        # cursor.execute('''SELECT email, name1 FROM Users WHERE phone1 = (?)''', (Phone,))
        # phone_exist=cursor.fetchone()
    except TypeError as T:
        exist='Non'
    cursor.close()
    conn.close()
    return exist

def add_favorite(User, Item, Product):
    if Item=='Poultry':
        conn = sqlite3.connect('Task.db')
        cursor=conn.cursor()
        cursor.execute('''INSERT INTO Poultry (Item, image, breed, Quantity, 
                Price, Age, Gender, Product, Births, UseriD, image2) VALUES (?, ?)''', 
                (Item, Product))
        conn.commit()
        conn.close()
        #return user
#validate_user('reeergr')
        # username=username.value
        # password= password.value
        
        # if not username or not password:
        #     status.value= 'Fill in to login'
        #     status.color='amber'
        #     #username.error_text='fill'
        # else:
        #     if username == Email and password==Password:
        #         status.value='Successful'
        #         status.color='green'
        #     else:
        #         status.value = 'Invalid, please try again!!'
        #         status.color='red'
        # page.update()
        # if user and crypt.checkpw(Password.encode(), 
        #     user['Password'].encode()):
        #     return user
        #return None
# if __name__=='__main__':
#     app(main)