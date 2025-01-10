from flet import *
#from db import data
data=data()

def L(C, page):
        if C.content.controls[1].value == '' or C.content.controls[2].value == '':
            #print("Email and Password Can't be empty!!")
            C.content.controls[0].value="Email and Password Can't be empty!!"
            C.content.controls[0].color='red'
            authentication=False
            page.update()
            return authentication

        elif C.content.controls[1].value != data['Username'] or C.content.controls[2].value != data['Password']:
            print(data['Username'], data['Password'])
            #print("incorect username/ password")
            C.content.controls[0].value='Incorrect credentials, Create Account!!!'
            C.content.controls[0].color='red'
            authentication=False
            page.update()
            return authentication

        elif C.content.controls[1].value == data['Username'] and C.content.controls[2].value == data['Password']:
            #print('correct credentials')
            C.content.controls[0].value='Correct credentials'
            C.content.controls[0].color='green'
            authentication=True
            page.update()
            #page.go('/')
            # authentication=True
            return authentication
            
        
        # elif C.content.controls[1].value not in data.items()# or C.content.controls[2].value == '':
        #         C.content.controls[0].value='Not found, create account!!'
        #         C.content.controls[0].color='green'
        #         #return page.go('/')
        #return Login(e)