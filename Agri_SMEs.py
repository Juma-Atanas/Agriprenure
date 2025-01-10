from flet import *

def SMEs(page:Page):
    #page.auto_scroll=True
    #Page.window_width
    page.padding=5
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    
    def check(e):
        e.control.bgcolor='purple'
        e.control.update()

    def color(e):
        e.control.icon_color='yellow'
        e.control.update()

    def back(e):
        for i in P.content.controls[1].content.controls[::]:
            i.bgcolor='None'
        page.update()

    def highlight(e):
        P.content.controls[1].content.controls[1].bgcolor='white12'
        page.update()


    P=Container(content=Column([Text('Profile'),
                    Container(Column([Row([ElevatedButton(text='Back', icon=icons.ARROW_BACK, on_click=lambda e: page.go('/cancel')),
                        Text('Personal details', color='white', text_align='top'), IconButton(icons.DELETE, icon_color='white', visible=False)], alignment=MainAxisAlignment.SPACE_BETWEEN),
                        Container(
                            ListTile(content_padding=0, 
                                    title=Row([Icon(icons.DOUBLE_ARROW, color='white'),Text("Full Name", color="white"),]),
                                    subtitle=Column([Row([Icon(icons.NOTIFICATION_IMPORTANT_SHARP, color='yellow'),Text("Address", color="white")]), Text('Message', color='white')], spacing=0),
                                    leading=CircleAvatar(Image(src="D:/Data/Game/Flet/hse.PNG",fit=ImageFit.CONTAIN)),
                                    trailing=Column([Text("Date", color="white"), IconButton(icons.STAR_OUTLINE, on_click=color),]),
                                    hover_color=colors.BLACK,
                                    
                                    ),border=border.all(1, 'white12'), border_radius=10,padding=padding.only(top=-10, bottom=-5, left=2, right=2),
                       on_click=check, on_long_press=color),
                       Container(
                            ListTile(content_padding=0, 
                                    title=Row([Icon(icons.DOUBLE_ARROW, color='white'),Text("Full Name", color="white"),]),
                                    subtitle=Column([Row([Icon(icons.NOTIFICATION_IMPORTANT_SHARP, color='yellow'),Text("Address", color="white")]), Text('Message', color='white')], spacing=0),
                                    leading=CircleAvatar(Image(src="D:/Data/Game/Flet/hse.PNG",fit=ImageFit.CONTAIN)),
                                    trailing=Column([Text("Date", color="white"), IconButton(icons.STAR_OUTLINE, on_click=color),]),
                                    hover_color=colors.BLACK,
                                    
                                    ),border=border.all(1, 'white12'), border_radius=10,padding=padding.only(top=-10, bottom=-5, left=2, right=2),
                       on_click=check, on_hover=highlight),
                 
                                   
                                                  ],alignment=alignment.top_center, scroll='auto', spacing=5),
                                          width=380, height=580,border_radius=40, bgcolor=colors.PURPLE_300,
                                          gradient=LinearGradient(colors=['blue', colors.PURPLE_300],
                                                                  begin=alignment.bottom_right, end=alignment.top_left), padding=10,expand=True, on_click=back),
                                                                  Text('All rights reserved')], 
                               alignment=MainAxisAlignment.CENTER, horizontal_alignment='center'),
        bgcolor=colors.PURPLE, width=400, height=800, border_radius=40, expand=True,)
    
    #page.add(P)
    return View('/Agri_SME', [P])
#app(main)