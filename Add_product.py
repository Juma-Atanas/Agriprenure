from flet import * 
import os
from Data import init_Tb, add_item
from typing import Dict
from Counties import Counties

assets_dir=os.path.abspath('assets')
init_Tb()
secret_key='mine'
def add(page: Page, secret_key=secret_key):
    page.assets_dir='assets'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.bgcolor=colors.GREEN

    def details(e):
        button.visible=True
        fields[0].value=e.control.key
        page.update()
    #------------------------------------------------------------------------
    prog_bars: Dict[str, ProgressRing] = {}
    files = Ref[Column]()
    upload_button = Ref[ElevatedButton]()

    def file_picker_result(e: FilePickerResultEvent):
        #assets_dir=os.path.abspath('assets')
        upload_button.current.disabled = True if e.files is None else False
        prog_bars.clear()
        files.current.controls.clear()
        #k.controls.clear()
        if e.files is not None:
            # print(e.files)
            for f in e.files:
                prog = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(Row([prog, Text(f.name)]))
        page.update()

    def on_upload_progress(e: FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress,)
    image_display=Row([], wrap=True, scroll='auto')
    uf = []
    loc=[]
    def upload_files(e):
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600),))
            file_picker.upload(uf)
            #upload_files=request
        for i in uf:        
            image_display.controls.append(Image(src=f'uploaded_images/{i.name}', width=300, height=300, border_radius=20))
            loc.append(f'uploaded_images/{i.name}')
            image_display.visible=True
            #shutil.copy(destpath, k.controls[0].src)
        page.update()
    # hide dialog in a overlay
    page.overlay.append(file_picker)
    #------------------------------------------------------------------------------------------------------------
    y=[ElevatedButton(
            "Select files...",
            icon=icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True, allowed_extensions=['jpeg', 'png']),
        ),
        Column(ref=files),
        ElevatedButton("Upload", ref=upload_button, icon=icons.UPLOAD, on_click=upload_files, disabled=True,
        ),
        #page.overlay.append(file_picker),
        image_display, Image(src='icons/icon.png', width=300, height=300),]

    choice=Dropdown(label='Type of a product',
                    options=[
                        #dropdown.Option(text='Farm item', on_click=details, key='Farm item'),
                        dropdown.Option('Poultry',on_click=details,),
                        dropdown.Option('Livestock',on_click=details),
                        #dropdown.Option('Seedling', on_click=details)
                    ])
    age=Dropdown(label='Dys/Wks/yrs',
                    options=[
                        dropdown.Option(text='Days', on_click=details),
                        dropdown.Option(text='Weeks', on_click=details),
                        dropdown.Option('Months',on_click=details),
                        dropdown.Option('Years', on_click=details)
                    ],width=150)
    Gender=Dropdown(label='Gender',
                    options=[
                        dropdown.Option(text='Female', on_click=details),
                        dropdown.Option('Male',on_click=details),
                        dropdown.Option('male & female', on_click=details)
                    ],width=150)
    Poultry1=Dropdown(label='Poultry',
                    options=[
                        dropdown.Option(text='Chicken', on_click=details),
                        dropdown.Option('Duck',on_click=details),
                        dropdown.Option('Pegion', on_click=details),
                        dropdown.Option('Geese', on_click=details),
                        dropdown.Option('Other', on_click=details)
                    ],width=150)
    Livestock1=Dropdown(label='Livestock',
                    options=[
                        dropdown.Option(text='Cattle', on_click=details),
                        dropdown.Option('Pig',on_click=details),
                        dropdown.Option('Goat', on_click=details),
                        dropdown.Option('Sheep', on_click=details),
                        dropdown.Option('Other', on_click=details)
                    ],width=150)
    breed=Dropdown(label='breed',
                    options=[
                        dropdown.Option(text='Exortic', on_click=details),
                        dropdown.Option('Indigenious',on_click=details),
                        dropdown.Option('Cross breed', on_click=details)
                    ],width=150)
    
    fields=[choice,
        Column(controls=y, scroll='auto', alignment='center'),
        Column([breed, Livestock1, Poultry1, TextField(label='Type', width=150)]),
        TextField(label='Quantity Available', width=180,),
        TextField(label='Price for each', width=180),
        Column([TextField(label='Approx Age', width=150),age]),
        Gender,
        #TextField(label='Available', width=150),
        TextField(label='Total Births', width=150),
        ]
    #auser=page.session.get('user')
    auser=page.session.get('user')

    k=Text(value='0', visible=False)
    j=''
    def add(e):
        Add.content.controls.clear()
        nonlocal k
        nonlocal j
        if fields[0].value== 'Poultry':
                fields[2].controls[3].visible=True
                fields[2].controls[1].visible=False
                j='Poultry'
             
        if fields[0].value == 'Livestock':
                fields[2].controls[2].visible=False
                fields[2].controls[1].visible=True
                j= 'Livestock'
        print(j)
        # if fields[6].value=='Male' or fields[6].value=='male':
        #     fields[-1].value='0'
        #     #fields[-1].visible=False
        if int(k.value)>=len(fields):
            k.visible=False
            #.visible=False
            Add.content.controls.append(Text(f'Check out the {fields[0].label} you added', text_align='center', size=20))
            for i in fields:
                if fields.index(i) !=1:
                    Add.content.controls.append(Row([Text(i.label), Text(i.value)],alignment=MainAxisAlignment.SPACE_BETWEEN))
                    #continue
                else:
                    Add.content.controls.append(Row([Text('Image Source'), Text(image_display.src)],alignment=MainAxisAlignment.SPACE_BETWEEN))
            button.visible=False
            Submit.visible=True
        else:
            if auser==None:
                Add.content.controls.clear()
                Add.content.controls=[Text('Log in to add your item', color='red', weight='bold')]
                button.visible=False
                login.visible=True
                upload_button.visible=False
                fields[1].visible=False
                #Submit.visible=True
            elif auser != None:
                if int(k.value)>=0:
                    if int(k.value)==0:
                        #button.text+str(k.value)
                        button2.visible=True
                    else:
                        button.text+str(k.value)
                        button2.visible=True

                elif int(k.value)<1:
                    button2.visible=False
                    k.visible=True
                    
            if int(k.value)>=len(fields)-2:
                    Submit.visible=True
                    Submit.color='blue'
                    button.visible=False
            k.value=int(k.value)+1
            Add.content.controls.append(fields[int(k.value)])
            button.text=f'Next {int(k.value)}'
            page.update()
   
    def Sent(e):
        nonlocal j
        nonlocal auser
        nonlocal uf
        user=auser[1]
        Item = j
        image=loc[0]#image_display.controls.src#image_display=Row([], wrap=True, scroll='auto')
        breed=fields[2].controls[0].value
        if fields[2].controls[1].value != None:
            Product=fields[2].controls[1].value
        else:
            Product=fields[2].controls[2].value
        Type=fields[2].controls[3].value
        Quantity=str(fields[3].value,)
        Price=fields[4].value
        Age=fields[5].controls[0].value + fields[5].controls[1].value
        Gender=fields[6].value
        Births=fields[7].value
        image2=loc[1]
        add_item(Item, image, breed, Quantity,  Price, Age, Type, Births, Product, user, image2)#
        page.snack_bar = SnackBar(Text("Your product saved!"), bgcolor='red')#use --->Page.overlay.append(snack_bar)
        page.snack_bar.open=True
        Submit.visible=False
        button2.visible=False
        # #result_text.value = " User added successfully!"
        #page.views.clear()
        page.views.pop()
        page.update()

    def back(e):
        Add.content.controls.clear()
        nonlocal k
        k.value=int(k.value)-1
        Add.content.controls.append(fields[int(k.value)])
        if int(k.value)<=len(fields):
            Submit.visible=False
            
        if int(k.value)<=0:
                button2.visible=False
                page.update()
        
        button.visible=True
        if int(k.value)==0:
            #button.text+str(k.value)
            button.text='Next'
        else:
            button.text=f'Next {int(k.value)}'

        page.update()

    button=ElevatedButton(text='Start', icon=icons.NEXT_PLAN, on_click=add, visible=False)
    button2=ElevatedButton(text='Back', icon=icons.SKIP_PREVIOUS, on_click=back, visible=False)
    Submit=ElevatedButton(text='Submit', icon=icons.CHECK, on_click=Sent, visible=False,)
    canceladd=ElevatedButton(text='Cancel',color='red', icon=icons.CANCEL, on_click=lambda e: page.go('/cancel'))
    login=ElevatedButton(text='Login', color='green', on_click=lambda e: page.go('/login'), visible=False)
    Add=Container(
        content=Row([Text('Hello, you can add a product that you disire to sell, choose a related product to start'),fields[0],
        ],alignment='center', wrap=True),
        width=500, height=500, bgcolor=colors.GREEN_300,border_radius=20, padding=5,alignment=alignment.center
    )
    #page.add(canceladd,Add,Row([button2, button, Submit],alignment='center', scroll='auto'))
    return View('/add_item', [Row([canceladd,login], alignment=MainAxisAlignment.CENTER), Add, Row([button2, button, Submit],alignment='center', scroll='auto', wrap=True)],auto_scroll=True, horizontal_alignment='center', )
#app(add, view=AppView.WEB_BROWSER, assets_dir='assets', web_renderer=WebRenderer.HTML)