from flet import *
#import sqlite3
#import mysql.connector
#from Session import Sessions
import datetime
#from Data import account_user
#import bcrypt

#'INSERT INTO (email, password) VALUES ( Atanas, ())'

# conn= sqlite3.connect('Task.db')
# cursor = conn.cursor()
# cursor.execute("SELECT UseriD, Phone1, email FROM Users")#ADD IMAGE COLUMN
# user=cursor.fetchall()


def Chats(page: Page):
    def send(e):
        page.add(You)
        #file_picker.pick_files(allow_multiple=True, file_type=FilePickerFileType.IMAGE)
        #T.content.content.Controls[0]==''
        page.update()
        
    import os
    import base64
    upload_dir="uploaded_images"
    os.makedirs(upload_dir, exist_ok=True)
    # k=Row([image_display=Image(src='', width=300, height=300, fit=ImageFit.CONTAIN, visible=False),
    # image_display=Image(src='', width=300, height=300, fit=ImageFit.CONTAIN, visible=False),
    # image_display=Image(src='', width=300, height=300, fit=ImageFit.CONTAIN, visible=False)])
    image_display=Image(src='', width=300, height=300, fit=ImageFit.CONTAIN, visible=False)
    def on_file_picked(e:FilePickerUploadEvent):
        if e.files:
            file = e.files[0]
            print(file)
            with open(file.path, 'rb') as f:
                file_content =f.read()

            image_path= os.path.join(upload_dir, file.name)
            with open(image_path, "wb") as f:
                f.write(file_content)

            image_base64 = base64.b64encode(file_content).decode("utf-8")
            image_displayimage_display=f"data:image/ {file.name.split('.')[-1]}; base64, {image_base64}"
                  

            page.snack_bar = SnackBar(Text(f"Image saved to {image_path}"), bgcolor='red')#use --->Page.overlay.append(snack_bar)
            AlertDialog(title='Hello')
            page.snack_bar.open=True
            image_display.src=image_path
            image_display.visible=True
            page.update()
    def upload(e):
         page.add(image_display)
         page.add(file_picker.pick_files(allow_multiple=True, file_type=FilePickerFileType.IMAGE))
         page.update()
        #lambda _ : file_picker.pick_files(allow_multiple=True, file_type=FilePickerFileType.IMAGE)
    file_picker = FilePicker(on_result=on_file_picked)

    page.overlay.append(file_picker)
    #------------------------------------------------------------------------------------------------------------
    y=[ElevatedButton('upload image',bgcolor='red', on_click = lambda _ : file_picker.pick_files(allow_multiple=True, file_type=FilePickerFileType.IMAGE)),
                    image_display,
                ],

    Others=Row([Row([CircleAvatar()]),Column([Text('A.j', weight='bold'),Container(Text('Blablabla too', color='white', expand=True), bgcolor=colors.GREEN_700, border_radius=5, padding=2),Text(f'{datetime.datetime.now()}', size=10)],spacing=0)])
    You=Row([Column([Text('You', weight='bold'),
                     Container(Text('i did manage to deliver the plan?', color='white'), 
                               bgcolor=colors.GREEN_300, border_radius=5, padding=2,),Text(f'{datetime.datetime.now()}', size=10)],spacing=0),
                               Row([CircleAvatar()],),], alignment=MainAxisAlignment.END,)

    Topbar=AppBar(ElevatedButton(text='Back', icon=icons.ARROW_BACK, on_click=lambda e: page.go('/cancel')))
    B=BottomAppBar(Container(Row([TextField(label='Message...',expand=True), IconButton(icon=icons.FILE_PRESENT, on_click =upload), 
                                  IconButton(icon=icons.SEND, on_click=send, visible=False,)],alignment=alignment.bottom_center, expand=True), expand=True))
    auser=page.session.get('user')
    if auser==None:
            B.content.content.controls[-1].visible=False
            B.content.content.controls[0].lable='Login to send a message'

            #page.update()
    elif auser !=None:
            B.content.content.controls[-1].visible=True
            You.controls[-1]=Image(src=str(auser[0][7]), fit=ImageFit.COVER)
            
    #page.add(Column([Others], You))
    return View('/Chats', [Topbar, Column([Others])],You,  bottom_appbar=B)
#app(Chats)