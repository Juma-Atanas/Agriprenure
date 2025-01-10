from flet  import *
details={}
def data1(Choice, MOREINFO,added, HIDE, BOOKMARK):
    details.clear()
    data=Row(alignment=MainAxisAlignment.CENTER,scroll='auto', wrap=True)
    for i in Choice[0]:
        num=i[1]
        item=i[2]
        src=i[3]
        breed=i[4]
        quantity=i[5]
        Price=i[6]
        Age=i[7]
        Gender=i[8]
        Product=i[10]
        Births=i[9]
        img2=i[11]
        for j in Choice[1]:
            if  j[0] == num:
                Phone1='0'+str(j[1])
                name1=j[3]
                name2=j[4]
                email=j[5]
                location=j[8]+','+ j[9]
                County=j[7]
                img1=j[10]
        
        if src == '':
            src='uploaded_images/Cow.jpeg'
        else:
            src=src
        img=Image(src=src,fit=ImageFit.CONTAIN, border_radius=5)
        img2=Image(src=img2,fit=ImageFit.CONTAIN, border_radius=5)
        #print(img2)
        details[Container(content=Column([
                     Stack([Image(src=src,fit=ImageFit.FILL, border_radius=5, height=90, width=120),IconButton(icon=icons.BOOKMARK_ADD_OUTLINED, icon_color='red',right=0, on_click=BOOKMARK),]),
                     Text(f'{item}:\n{breed}|{Product[:4]}', weight=FontWeight.BOLD, max_lines=2, size=13),#replace item with type  eg calf, bull, etc
                    Row([Text(f'Age: {Age[:4]}|',size=12),  Text(f'Qty: {quantity}',size=12)], spacing=5,),
                    Row([Text(f'Ksh.{Price}/-', color=colors.AMBER, size=13, weight=FontWeight.BOLD), Text('More', size=10,color='red'),
                    #IconButton(icon=icons.MORE_VERT_OUTLINED,icon_size=20, icon_color='black', bgcolor=colors.WHITE24,)
                    #Icon(name=icons.PASSWORD)
                    ])
                    # Stack([
                    # Row([
                    #     # IconButton(icon=icons.FAVORITE_OUTLINE, icon_size=15, icon_color='red', tooltip='Add to favourite',splash_radius=0),
                    #     # IconButton(icon=icons.STAR_BORDER_OUTLINED, icon_size=15, icon_color='green', hover_color=colors.BLACK12, on_click=Star,tooltip='Rate'),
                    #     CircleAvatar(Image(src='D:/Data/Game/Flet/hse.PNG')),
                    #     Column([ Text(f'{name1} {name2}', size=10), Text(f'{location}', size=10),Text(f'{Phone1}', size=10), ], spacing=0),
                    # ], spacing=0, ),
                    # IconButton(icon=icons.MORE_VERT_OUTLINED,icon_size=20, on_click=MOREINFO,icon_color='black', bgcolor=colors.WHITE24, right=0)
                    # ]),
                    
                    ],horizontal_alignment='left', spacing=0, alignment=MainAxisAlignment.SPACE_BETWEEN),
            width=120,  border_radius=5, on_click=MOREINFO, bgcolor=colors.WHITE70, padding=5, height=180)]=[Row([IconButton(icon=icons.ARROW_BACK,on_click=HIDE,tooltip='Go back', icon_color='red'),Text(f'{breed} {Product}({quantity})',size=30),Column([Text(f'Age= {Age}'), Text(f'Price=Ksh.{Price}/-')], spacing=0)],alignment=MainAxisAlignment.SPACE_BETWEEN, scroll='auto'),
            Row([
            Row([img]),
            Row([img2]),
            Column([
                 Image(src=src,fit=ImageFit.FILL, border_radius=5, height=100, width=100),
                 Image(src=src,fit=ImageFit.FILL, border_radius=5, height=100, width=100)
            ], height=200, spacing=0, scroll='auto'),
            
            ], height=200, alignment='center', scroll='auto'),
            Row([Text('Details',size=20)], alignment=MainAxisAlignment.SPACE_BETWEEN),
            Text(f'Price:Ksh.{Price}/',size=18,color=colors.AMBER, weight='bold'),
            Row([
                Column([
                    Text('Farmer', size=20),
                    Row([CircleAvatar(Image(src=img1,fit=ImageFit.FILL),radius=40, bgcolor='white'), 
                        Column([
                        Row([Icon(name=icons.PERSON),Text(f'{name1} {name2}',)]),
                        Row([Icon(name=icons.CALL),Text(f'{Phone1}', selectable=True)]),
                        Row([Icon(name=icons.LOCATION_CITY),Text(f'{County},{location}')])
                    ])
                    ], spacing=4)
                
            ], spacing=2),

            Column([
            Text(f'Product, Stock={quantity}', size=20),
            Row([CircleAvatar(Image(src=src,border_radius=50),radius=40, bgcolor='white'), 
            Column([
                Row([Icon(name=icons.AGRICULTURE),Text(f'Age: {Age}',)]),
                Row([Icon(name=icons.SUMMARIZE),Text(f'{Product}',)]),
                Row([Icon(name=icons.APPROVAL),Text('Available')])
            ])
            ], spacing=4)
                    ], spacing=2)
                ],wrap=True ),
                Row([Icon(icons.VACCINES), Text('Product', size=20),], spacing=0),#Product
                Row([
                    Column([Column([
                    Text('........'),
                    Text('.........'),
                    Text('.........')
                ]),
                Row([Icon(icons.HEALING), Text('Health', size=20)]),
                Column([
                    Text('Healthy'),
                    Text(f'{Gender}'),
                    Text(f'{Births} births')
                ],alignment='center')]),
                
                ]),
                Row([
                    OutlinedButton(text='Burgain', on_click=added),
                    OutlinedButton(text='Comment', on_click=added),
                    OutlinedButton(text='Rate', on_click=added),
                    OutlinedButton(text='Feedback', on_click=added)
                ], wrap=True),
                Container()
                    #CircleAvatar(Image(src="D:/Data/Game/Flet/hse.PNG",fit=ImageFit.CONTAIN), radius=120),
            ]
    
    for i, v in details.items():
        data.controls.append(i)
            
    return data, details