from flet import *
from Data import register_user
import bcrypt
from Counties import Counties
from Data import check_user 

def create_account(page: Page):
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.bgcolor=colors.BLUE_200
    page.window_icon=icons.CABIN
    
    def register(e):
        name1=C.content.controls[1].value
        name2=C.content.controls[2].value
        Phone1=C.content.controls[3].value
        email=(C.content.controls[4].value).lower()
        County=C.content.controls[5].value
        Sub_county=C.content.controls[6].value
        Nearest_School=C.content.controls[7].value
        Password=C.content.controls[9].value
        
        condition=True
        if len(C.content.controls[3].value) != 10:
            C.content.controls[0].value='Phone number should be 10 characters!'
            C.content.controls[0].color='red'
            condition=False
        if (C.content.controls[3].value).isdigit() !=True:
            C.content.controls[0].value='Phone number should number!'
            C.content.controls[0].color='red'
            condition=False
        if len(C.content.controls[9].value) <8:
            C.content.controls[0].value='Password should be 8 characters!'
            C.content.controls[0].color='red'
            condition=False
        if C.content.controls[9].value != C.content.controls[8].value:
            C.content.controls[0].value='Password not matching!'
            C.content.controls[0].color='red'
            condition=False
        if 'mail.com' not in email:
            C.content.controls[0].value='Email incorrect!'
            C.content.controls[0].color='red'
            condition=False
        if len(check_user(email, Phone1)) >= 1:# or check_user(email, Phone1) != 'Non':
            print(check_user(email, Phone1)!='[]')
            C.content.controls[0].value='Details already used/ Exists!'
            C.content.controls[0].color='red'
            condition=False
        for i in [name1, name2, Phone1, email, County, Sub_county, Nearest_School, Password]:
            if i == '':
                C.content.controls[0].value='Plese fill empty spaces'
                C.content.controls[0].color='red'
                C.content.controls[0].weight='bold'
                condition=False
        #if email == check_user(email, Phone1)[0] or str(Phone1) == str(check_user(email, Phone1)[0][2]):
        
        page.update()

        if condition:
            #print('conditions met',check_user(email, Phone1)[0][0])
            page.snack_bar = SnackBar(Text(f"Account created Successfuly"), bgcolor='red')#use --->Page.overlay.append(snack_bar)
            page.snack_bar.open=True
            register_user(Phone1=Phone1, Phone2=Phone1, name1=name1, name2=name2, email=email, Password=bcrypt.hashpw(Password.encode(), bcrypt.gensalt()), County=County, Sub_county=Sub_county, Nearest_School=Nearest_School)
            page.go('/login')
            
    def subcounties(e):
        L.options.clear()
        for i in Counties[e.control.value]:
                L.options.append(dropdown.Option(i))
        page.update()

    k= Dropdown(label='County', on_change=subcounties, width=300)
    
    L= Dropdown(label='Sub-County',width=300 )
    
    for i in Counties:
        k.options.append(dropdown.Option(i))

    C=Container(content=Column([
        Text(value='Create your Account'),
        TextField(label='First name', width=300),
        TextField(label='Sir name', width=300),
        TextField(label='Phone no: 07...', width=300),
        TextField(label='Email', width=300),
        k,
        L,
        TextField(label='Nearest School', width=300),
        TextField(label='Password', width=300, can_reveal_password=True, password=True),
        TextField(label='Confirm Password', width=300, can_reveal_password=True, password=True),
        Row([
            ElevatedButton(text='Sign up', color='green', on_click=register),
            ElevatedButton(text='Cancel', color='red', on_click=lambda e: page.go("/cancel"))
        ],alignment='center', ),
    ], horizontal_alignment='center', alignment=MainAxisAlignment.CENTER
    ),
        width=350,bgcolor=colors.BLACK12,border_radius=10,padding=5)
    S=Container(Column([Text('Create with a Social media site', color='black'), Row([Text('fb', color='blue'), Text('YouTube', color='red'), Text('Google', color='orange'), Text('GitHub') ],alignment='center', spacing=50),
                        ], horizontal_alignment='center'), bgcolor=colors.WHITE12, width=350, border_radius=5, padding=5, )
    k=Container(Text('Aj', size=10, color='blue'), alignment=alignment.bottom_center)

    #Bck=Container(Image(src="D:/Data/Game/kaggle_evaluation/Frontends/Mail.py/download.jpeg"))
    
    
    #page.scroll='auto'
    #page.add(C,S,k)
    return View('/login', [C,S,k], horizontal_alignment='center', vertical_alignment='center',bgcolor=colors.BLUE_200, scroll='auto')
    #page.on_route_change=route_change
    #page.go("/")

#app(create_account)