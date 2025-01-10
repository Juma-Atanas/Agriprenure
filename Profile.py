from flet import *
from typing import Dict
from Data import user_image
def farmer(page: Page):
    auser=page.session.get('user')
    if auser != None:
        id=auser[1]
        Name=str((f'{auser[0][1:3]}').replace('(','').replace(')','').replace("'", '').replace(',', ''))
        Phone=f'0{auser[0][3]}'#.replace('(','').replace(')','').replace("'", '').replace(',', '')
        County=f'{auser[0][4]}'
        location=f'{auser[0][5]}'
        Nearest_School=f'{auser[0][6]}'
        img=auser[0][7]
    elif auser == None:
         Name=None
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
            loc.append(f'uploaded_images/{i.name}')
            user_image(id, f'uploaded_images/{i.name}')
        #profl.controls.controls[1].Controls[1].visible=False
        #print(profl.controls[1].controls[])
        #print(profl.controls[1].controls[0])
        profl.controls[1].controls[0]=CircleAvatar(Image(src=f'uploaded_images/{i.name}'),radius=50, bgcolor='white')
        
        page.update()
    # hide dialog in a overlay
    page.overlay.append(file_picker)

    #------------------------------------------------------------------------------------------------------------
    y=Column([IconButton(icon=icons.EDIT,
            on_click=lambda _: file_picker.pick_files(allow_multiple=False, allowed_extensions=['jpeg', 'png']),
        ),
        Column(ref=files),
        ElevatedButton("Upload", ref=upload_button, icon=icons.UPLOAD, on_click=upload_files, disabled=True,
        )])

    Profile_image=CircleAvatar(Image(src=str(img), fit=ImageFit.COVER), radius=40, bgcolor='white')
    profl=Column([
                    Text('Profile', size=20),
                    Row([Stack([Profile_image, y]),
                        Column([
                        Row([Icon(name=icons.PERSON),Text(f'{Name}',)]),
                        Row([Icon(name=icons.CALL),Text(f'{Phone}', selectable=True), IconButton(icon=icons.EDIT)]),
                        Row([Icon(name=icons.LOCATION_CITY),Text(f'{County},{location}')]),
                        Row([Icon(name=icons.LOCATION_CITY),Text(f'{Nearest_School}')]),
                        ElevatedButton(text='back',color='red', icon=icons.ARROW_BACK, on_click=lambda e: page.go('/cancel'))
                    ], spacing=5)
                    ], spacing=4)
            ], spacing=2)
    # page.add(profl)
    return View('/profile', [profl])
# app(farmer)