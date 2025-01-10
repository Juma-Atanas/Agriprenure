import bcrypt
from flet import *
from Data import account_user
# import uuid

def loginpg(page: Page):
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.bgcolor=colors.BLUE_200
    page.window_icon=icons.CABIN

    def handle_login(e):
        # if page.session_id not in user_sessions:
        #     user_sessions[page.session_id] = {'logged_in': False, 'username': None}
        username=(C.content.controls[1].value).lower()
        password= C.content.controls[2].value
        status=C.content.controls[0]
        user=account_user(username)
        #print((user[2]).lower()== (username).lower())
        if not username or not password:
            status.value= 'Fill in to login!'
            status.color='red'
        else:
            try:
                Password=bcrypt.checkpw(password.encode(), user[1])
                if username == user[2] and Password:
                    page.session.set('user', [user[2:], user[0]])
                    status.value='Successful'
                    status.color='green'
                    page.go('/home')
                    # page.snack_bar = SnackBar(Text(f"Hello {(user[0][1:3])} welcome!"), bgcolor='red')#use --->Page.overlay.append(snack_bar)
                    # page.snack_bar.open=True
                    username=''
                    password=''
                    page.clean()
                if username == user[2] and not Password:
                    status.value = 'Incorrect Password'
                    status.color='red'
            except TypeError as E:
                status.value = "Account not found, register!!"
                status.color='red'
        page.update()

    C=Container(content=Column([
        Text(value='Login to your Account'),
        TextField(label='Email', width=300),
        TextField(label='Password', width=300, can_reveal_password=True, password=True),
        Row([
            ElevatedButton(text='Login', color='green', on_click=handle_login),
            ElevatedButton(text='Cancel', color='red', on_click=lambda e: page.go("/home"))
        ],alignment='center', ),
        TextButton(text='Forgot password', on_click=lambda e: page.go("/recover"))
    ], horizontal_alignment='center', alignment=MainAxisAlignment.CENTER
    ),
        width=350,bgcolor=colors.BLACK12,border_radius=10,padding=5, border=border.all(1, 'blue'))
    S=Container(Column([Text('Create with a Social media site', color='black'), Row([Text('fb', color='blue'), Text('YouTube', color='red'), Text('Google', color='orange'), Text('GitHub') ],alignment='center', spacing=50),
                        ElevatedButton('Create Account',color='green', bgcolor='white', on_click=lambda e: page.go('/create_account')),], 
                        horizontal_alignment='center'), bgcolor=colors.WHITE12, width=350, border_radius=5, padding=5, border=border.all(1, 'green'))
    k=Container(Text('Aj-0724641931', size=10, color='blue'), alignment=alignment.bottom_center)

    #page.add(C,S,k)
    return View('/login', [C,S,k], horizontal_alignment='center', vertical_alignment='center')
    #page.on_route_change=route_change
    #page.go("/")
    #print(C.content.controls[0].value)
#app(loginpg)