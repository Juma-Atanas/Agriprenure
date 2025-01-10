from flet import *
from Data import get_users
from Process_data import details, data1

def home(page: Page):
    page.spacing=0
    page.padding=0
    page.horizontal_alignment='center'
    page.bgcolor='white'
    page.window.icon=Image(src='Backends/icon/Gmail.png', width=10, height=10)
    #page.scroll='auto'
    page.icon=None
    page.title='Agriprenure app'
    auser=page.session.get('user')
    Platform=page.platform
    # download_link={
    #     'windows': 'https://',
    #     'android': 'https://',
    #     'ios': 'https://',
    #     'macos':'https://',
    # }
    # download_url=download_link.get(Platform, 'https://example.com/downloads',)
    # k=Text(f'Detected:', Platform)
    # AlertDialog(f'Download {k} App', url=download_url)


    if auser != None:
        Name=(f'{auser[0][1:3]}').replace('(','').replace(')','').replace("'", '').replace(',', '')
    elif auser == None:
         Name=None

    #user_image=CircleAvatar(Image(src='uploaded_images/Chick.jpeg'))

    def MOREINF(e):
        #print((e.control).content.controls[0].controls[1].icon_color)
        if auser==None:
            MORE.content.controls=[Text('Log in to see more i.e farmers contact, location etc', color='red', weight='bold')]
        if  auser!=None:
            if 'Livestock' in (Body2.content.controls[1].controls[0].content.controls[1].value):
                MORE.content.controls=details[e.control]
                #print(details[e.control])
                
            if 'Poultry' in Body2.content.controls[1].controls[0].content.controls[1].value:
                MORE.content.controls=details[e.control]
                #print(details[e.control])
                
        MORE.visible=True
        page.update()
        return  details[e.control][1]

    def HIDE(e):
        bar2.content.controls[1]=Row([IconButton(icon=icons.NOTIFICATIONS_OUTLINED, icon_color='black', tooltip='Notifications'),
                                     IconButton(icon=icons.SEARCH, icon_color='black',tooltip='Search', on_click=SEARCH_ITEMS ),])
        MORE.visible=False
        page.update()
    
    def SEARCH_ITEMS(e):
        bar2.content.controls[1]=Container(Row([TextField(label='Search for a item...',expand=True, bgcolor='white',text_align=TextAlign.START, border_radius=border_radius.only(top_left=20, bottom_left=20,top_right=0, bottom_right=0), width=250), 
                                                    IconButton(icon=icons.SEARCH, tooltip='Search', icon_color='white', icon_size=25,padding=2)],spacing=0, height=40, alignment='center'), width=300, bgcolor=colors.ORANGE, border_radius=20, expand=True)
        MORE.visible=False
        page.update()
    
    def BOOKMARK(e):
        for i in details.keys():
                if i.content.controls[0].controls[1]==e.control:
                    #print(e.control, i)
                    break
                if i.content.controls[0].controls[1] !=e.control:
                    #print(e.control,'none', i)
                    break
        if e.control.icon_color=='yellow':
            e.control.icon_color='red'
            e.control.icon=icons.BOOKMARK_ADD_OUTLINED
            e.control.update()
                

        elif e.control.icon_color=='red':
            e.control.icon_color='yellow'
            e.control.icon=icons.BOOKMARK
            e.control.update()
            
            #print(details['content'].controls[0])#==e.control)#details[content.controls[0].controls[1]]

    def Show_Livestock(e):
        Body2.content.controls=[Divider(height=1, color='black'),data1(get_users('Livestock'), MOREINF, added, HIDE, BOOKMARK)[0]]#,About]
        MORE.visible=False
        #SEARCH.visible=False
        Tabs.controls[0].bgcolor='white'
        Tabs.controls[0].color='black'
        Tabs.controls[1].bgcolor='black'
        Tabs.controls[1].color='white'
        # Tabs.controls[2].bgcolor='black'
        # Tabs.controls[2].color='white'
        Body2.bgcolor=None#colors.BLACK12
        all.bgcolor=colors.BLACK12
        page.update()

    def Show_Poultry(e):
        Body2.content.controls=[Divider(height=1, color='orange'),data1(get_users('Poultry'), MOREINF,added, HIDE,BOOKMARK)[0]]#, About]
        MORE.visible=False
        #SEARCH.visible=False
        Tabs.controls[1].bgcolor='white'
        Tabs.controls[1].color='black'
        Tabs.controls[0].bgcolor='black'
        Tabs.controls[0].color='white'
        # Tabs.controls[2].bgcolor='black'
        # Tabs.controls[2].color='white'
        Body2.bgcolor=None#colors.BLACK12
        all.bgcolor=colors.BLACK12
        page.update()

    def added(e):
        MORE.content.controls[-1].content=Column([
        TextField(label='Name', width=100, height=30),
        TextField(label='Summary Comment', width=200, height=30),
        TextField(label='Comment', ),
        ElevatedButton(text='Submit')
        ])
        MORE.scroll='auto'
        page.update()

    def show_career(e):
        MORE.content.controls=[Text('No Careers available at the moment, keep checking', color='red', size=20)]
        MORE.visible=True
        #MORE.content.bgcolor='red'
        page.update()

    def Complains(e):
        MORE.content.controls=[Text('Raise you complain hear', color='red', size=20), TextField(label='Your Name', width=200),TextField(label='Contact', width=200),TextField(label='Write...'), ElevatedButton(text='Submit')]
        MORE.visible=True
        MORE.content.border_radius=5
        page.update()

    def show_products(e):
        Show_Livestock(e)
        Tabs.visible=True
        products_but.visible=False
        Body2.bgcolor=None#colors.BLACK12
        all.bgcolor=colors.BLACK12

        page.update()

    def home(e):
        Body2.content.controls=[Text('Hello Welcome to our products'),products_but]#, Image(src='D:/Data/Game/Flet/Pictu/Stone.jpeg')]
        products_but.visible=True
        #SEARCH.visible=False
        Tabs.visible=False
        Body2.bgcolor=None
        all.bgcolor=None

        page.update()

    def RETAIN(e):
        e.control.visible=True
        e.control.update()

    def Quote(e):
        MORE.content.controls=[Text('Fill in the details bellow', color='red', size=20), 
                               TextField(label='Your Name', width=200),TextField(label='Contact', width=200),
                               TextField(label='Write...Land size or No. of products'), 
                               ElevatedButton(text='Submit')]
        MORE.visible=True
        MORE.content.border_radius=5
        page.update()

    def logout(e):
        page.session.clear()
        bar2.content.controls[2].visible=True
        bar2.content.controls[-1].visible=False
        page.go('/home')
        page.update()
    #SEARCH=Container(Row([TextField(label='Search for a item...',expand=True, border_radius=20),IconButton(icon=icons.SEARCH, tooltip='Search',)
        
    #], height=40, alignment='center'), on_click=SEARCH_ITEMS,visible=False, width=300)
    bar=Container(content=Row([Text('INGO Domestic.com', color=colors.BLUE_ACCENT_100, size=30, weight=FontWeight.BOLD), Icon(name=icons.SELL)],
                              alignment=MainAxisAlignment.SPACE_BETWEEN),height=50, bgcolor='white',gradient=LinearGradient(begin=alignment.top_left, end=alignment.bottom_right, colors=['purple', colors.BLUE]), )

    bar2=Container(content=Row([
                                PopupMenuButton(content=Row([Text('Sales', weight='bold', color='black', size=20),
                                                             Text('LTD', weight='bold',bgcolor='purple', color='white', size=25), 
                                                             Icon(name=icons.MENU, color='green', scale=1)],spacing=0 ),
                                                items=[PopupMenuItem(text='Home', icon=icons.HOME, on_click=home),
                                                       PopupMenuItem(text='Products', icon=icons.GPP_GOOD_SHARP,on_click=show_products),
                                                       PopupMenuItem(text='Get a Quote', icon=icons.PRICE_CHANGE,on_click=Quote),
                                                       PopupMenuItem(text='Hire', icon=icons.TIMELAPSE,),
                                                       PopupMenuItem(text='Advertise your service', icon=icons.ROOM_SERVICE),
                                                       PopupMenuItem(text='Careers', icon=icons.CASES,on_click=show_career),
                                                       PopupMenuItem(text='Raise a complain', icon=icons.WAVING_HAND, on_click=Complains),
                                                       PopupMenuItem(text='Chat zone', icon=icons.MESSENGER_SHARP,on_click=lambda e : page.go('/Chats')),
                                                       PopupMenuItem(text='Agri-SMEs', icon=icons.SUPPORT, on_click=lambda e: page.go('/SMEs')),
                                                       PopupMenuItem(text='About us', icon=icons.INFO),
                                                      
                                                       ],menu_position=PopupMenuPosition.UNDER, bgcolor=colors.PURPLE_200,
                                                ), 
                                Row([IconButton(icon=icons.NOTIFICATIONS_OUTLINED, icon_color='black', tooltip='Notifications'),
                                     IconButton(icon=icons.SEARCH, icon_color='black',tooltip='Search', on_click=SEARCH_ITEMS,),]),
                                               
                                TextButton(text='Login',icon_color='purple', icon=icons.LOCK, on_click=lambda e: page.go('/login'), tooltip='Login',
                                               ),
                                PopupMenuButton(content=Row([Icon(icons.PERSON, color='purple'),Text('Profile',color='black')], spacing=0),
                                                items=[
                                    PopupMenuItem(text=f"{Name}", icon=icons.PERSON_2_OUTLINED, on_click=lambda e: page.go('/profile')),
                                    PopupMenuItem(text='settings', icon=icons.SETTINGS),
                                    PopupMenuItem(text='Product Views', icon=icons.WATCH),
                                    PopupMenuItem(text='Messages', icon=icons.MESSAGE),
                                    PopupMenuItem(text='Sales', icon=icons.MONEY),
                                    PopupMenuItem(text='My Dashboard', icon=icons.WALLET, on_click=lambda e: page.go('/dash')),
                                    PopupMenuItem(text='Orders', icon=icons.PRODUCTION_QUANTITY_LIMITS),
                                    PopupMenuItem(text='Logout', icon=icons.LOCK, on_click= logout)
                                ], menu_position=PopupMenuPosition.UNDER, bgcolor=colors.BLUE_200,)
                                ], alignment=MainAxisAlignment.SPACE_BETWEEN),height=40, border=border.all(2,'white12'), padding=2, on_click=HIDE)
    #--------------------------------------------------------------------------------------------------
    if auser==None:
            bar2.content.controls[3].visible=False
            bar2.content.controls[2].visible=True
    
    elif auser!=None:
            bar2.content.controls[-1].visible=True
            bar2.content.controls[2].visible=False
    products_but=ElevatedButton(text='Products', icon=icons.GPP_GOOD_SHARP,on_click=show_products)
    
    #-----------------------------------------------------------------------------------------------------------   

    MORE=Container(Column(scroll='auto', spacing=0, alignment='top'),
    width=550,padding=5, expand=True,bgcolor=colors.WHITE,visible=False, 
    border_radius=20,border=border.all(1,'black12'), shadow=[BoxShadow(blur_radius=20, color='black', )], on_click=RETAIN)

    bar3=BottomAppBar(content=Row([Text('Please do not sent money to a person without direct interaction with a product', size=10),
        Image(src='icon/YouTube.png', border_radius=border_radius.all(50), ),
        Image(src='icon/facebook.png', border_radius=border_radius.all(50)),
        Image(src='icon/Gmail.png', border_radius=border_radius.all(50)),
        #Text('A.J', italic=True, color='white',text_align='center'),
    ], alignment=MainAxisAlignment.CENTER),height=40, bgcolor='green',)
    NEXT=IconButton(icon=icons.ARROW_FORWARD, right=0, top=50)
    BACK=IconButton(icon=icons.ARROW_BACK, left=0, top=50)
    
    items=Row([],scroll='auto', spacing=2)
    

    # About=Container(Column([
    #     Text('About us'),
    #     Text('Contact us')
    # ]),height=150, bgcolor='yellow',alignment=alignment.bottom_center)       
     
    #inheritance in future
    Tabs=Row([
        ElevatedButton('Livestock', on_click=Show_Livestock, bgcolor=colors.BLACK38, color='white',
    style=ButtonStyle(color={ControlState.HOVERED:colors.WHITE, ControlState.FOCUSED:colors.BLUE, ControlState.DEFAULT:colors.BLACK,},
    side={ControlState.HOVERED:BorderSide(1, colors.WHITE), ControlState.DEFAULT:BorderSide(1, 'red'), ControlState.FOCUSED:BorderSide(1, 'blue')},
    shape={ControlState.HOVERED:RoundedRectangleBorder(radius=20), ControlState.DEFAULT:RoundedRectangleBorder(radius=5), ControlState.FOCUSED:RoundedRectangleBorder(20)}
    )),
    ElevatedButton('Poultry', on_click=Show_Poultry,bgcolor=colors.BLACK38, color='white',
    style=ButtonStyle(color={ControlState.HOVERED:colors.WHITE, ControlState.FOCUSED:colors.BLUE, ControlState.DEFAULT:colors.BLACK,},
    side={ControlState.HOVERED:BorderSide(1, colors.WHITE), ControlState.DEFAULT:BorderSide(1, 'red'), ControlState.FOCUSED:BorderSide(1, 'blue')},
    shape={ControlState.HOVERED:RoundedRectangleBorder(radius=20), ControlState.DEFAULT:RoundedRectangleBorder(radius=5), ControlState.FOCUSED:RoundedRectangleBorder(20)}
    )),
    # ElevatedButton('items',color='white', on_click=Show_items, bgcolor=colors.BLACK38,
    # style=ButtonStyle(color={ControlState.HOVERED:colors.WHITE, ControlState.FOCUSED:colors.BLUE, ControlState.DEFAULT:colors.BLACK,},
    # side={ControlState.HOVERED:BorderSide(1, colors.WHITE), ControlState.DEFAULT:BorderSide(1, 'red'), ControlState.FOCUSED:BorderSide(1, 'blue')},
    # shape={ControlState.HOVERED:RoundedRectangleBorder(radius=20), ControlState.DEFAULT:RoundedRectangleBorder(radius=5), ControlState.FOCUSED:RoundedRectangleBorder(20)}
    # ))
    ], scroll='auto', visible=False,)

    BODY=Container(Stack([items,BACK,NEXT]),padding=1)
    Body2=Container(Row([ products_but], scroll='auto', wrap=True,alignment=MainAxisAlignment.CENTER),padding=1,margin=0)
    all=Container(Stack([Body2,MORE],alignment=alignment.top_center, expand=True),expand=True, padding=0, on_click=HIDE)
    b=FloatingActionButton(icon=icons.ADD, bgcolor=colors.WHITE24, on_click=lambda e: page.go('/add_item'))

    return View('/home',controls=[bar2,Tabs, all, b],horizontal_alignment='center', appbar=bar, bottom_appbar=bar3, spacing=0, padding=0)