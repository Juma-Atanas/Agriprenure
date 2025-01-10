from flet import *
from Data import register_user
import bcrypt
from Data import recover_password

def recover_account(page: Page):
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.bgcolor=colors.BLUE_200
    page.window_icon=icons.CABIN
    
    def update(e):
        # for i in C.content.controls:
        #     if i.value=='':
        #         C.content.controls[0].value='Please fill all fields!'
        name1=C.content.controls[1].value
        Phone1=C.content.controls[2].value
        email=C.content.controls[3].value
        County=C.content.controls[4].value
        #Sub_county=C.content.controls[4].value
        Password=C.content.controls[5].value
        condition=True
        if len(C.content.controls[2].value) <10 or len(C.content.controls[2].value) >10:
            C.content.controls[0].value='Phone number should be 10 Numbers!'
            C.content.controls[0].color='red'
            condition=False
        if len(C.content.controls[2].value) ==10:
            if ' ' in C.content.controls[2].value:
                       condition = False
            try:
                if type(int(C.content.controls[2].value)) is not int:
                    print(type(C.content.controls[2].value))
                    C.content.controls[0].value='Phone number should be Numbers!'
                    condition=False
            except ValueError as E:
                C.content.controls[0].value='Phone number should be Numbers!'
                condition=False
        if len(C.content.controls[-2].value) <8:
            C.content.controls[0].value='Password should be 8 characters!'
            C.content.controls[0].color='red'
            condition=False
        if C.content.controls[6].value != C.content.controls[5].value:
            C.content.controls[0].value='Password not matching!'
            C.content.controls[0].color='red'
            condition=False
        if 'mail.com' not in C.content.controls[3].value or ' ' in C.content.controls[3].value:
            C.content.controls[0].value='Email incorrect'
            C.content.controls[0].color='red'
            condition=False
        for i in [name1, Phone1, email, County, Password]:
            if i == '':
                C.content.controls[0].value='Plese fill empty spaces'
                C.content.controls[0].color='red'
                C.content.controls[0].weight='bold'
                #C.content.controls[i]. error_text='Fill this space'
                condition=False
        page.update()
        if condition:
            C.content.controls[0].value='Sign up!'
            C.content.controls[0].color='green'
            password=bcrypt.hashpw(Password.encode(), bcrypt.gensalt())
            results=recover_password(Phone1,name1, email, password, County)
            if results == 'Success':
                page.go('/login')
                page.snack_bar = SnackBar(Text(f"Password Successfuly recovered"), bgcolor='red')#use --->Page.overlay.append(snack_bar)
                #AlertDialog(title='Hello')
                page.snack_bar.open=True
                page.update()
            elif results == 'Failed':
                C.content.controls[0].value='Details not matching our records'
                C.content.controls[0].color='red'
                C.content.controls[0].weight='bold'
                page.update()
        

    C=Container(content=Column([
        Text(value='Recover your Password', color='red'),
        TextField(label='First name', width=300,),
        TextField(label='Phone no: 07...', width=300),
        TextField(label='Email', width=300),
        TextField(label='County', width=300),
        TextField(label='New Password', width=300, can_reveal_password=True, password=True),
        TextField(label='Confirm Password', width=300, can_reveal_password=True, password=True),
        Row([
            ElevatedButton(text='Reset', color='green', on_click=update),
            ElevatedButton(text='Cancel', color='red', on_click=lambda e: page.go("/cancel"))
        ],alignment='center', ),
        #TextButton(text='Forgot password', )
    ], horizontal_alignment='center', alignment=MainAxisAlignment.CENTER
    ),
        width=350,bgcolor=colors.BLACK12,border_radius=10,padding=5)
    S=Container(Column([Text('Create with a Social media site', color='black'), Row([Text('fb', color='blue'), Text('YouTube', color='red'), Text('Google', color='orange'), Text('GitHub') ],alignment='center', spacing=50),
                        ], horizontal_alignment='center'), bgcolor=colors.WHITE12, width=350, border_radius=5, padding=5, )
    k=Container(Text('Aj', size=10, color='blue'), alignment=alignment.bottom_center)

    #Bck=Container(Image(src="D:/Data/Game/kaggle_evaluation/Frontends/Mail.py/download.jpeg"))
    
    #page.scroll='auto'
    #page.add(C,S,k)
    return View('/recover', [C,S,k], horizontal_alignment='center', vertical_alignment='center',bgcolor=colors.BLUE_200, scroll='auto')
    #page.on_route_change=route_change
    #page.go("/recover")

#app(recover_account)