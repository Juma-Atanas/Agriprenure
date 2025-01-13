from flet import *
from item import home
from homepg import loginpg
from Add_product import add
from signup import create_account
from Agri_SMEs import SMEs
from Chatspg import Chats
from passrecovery import recover_account
from Profile import farmer
from Dash import dash

def main(page:Page):
    def route_change(route):
        #auser=page.session.get('user')
        # if auser != None:
        #     Name=(f'{auser[0][1:3]}').replace('(','').replace(')','').replace("'", '').replace(',', '')
        #     print(Name)
        # elif auser == None:
        #     Name=None
        if page.route =='/home':
            page.views.append(home(page))
            page.update()
        if page.route =='/login':
            page.views.append(loginpg(page))
            page.update()
        if page.route =='/add_item':
            page.views.append(add(page))
            page.update()
        if page.route=='/cancel':
            page.views.pop()
            page.update()
        if page.route == '/create_account':
            page.views.append(create_account(page))
            page.update()
        # if page.route == '/SMEs':
        #     page.views.append(SMEs(page))
        #     page.update()
        # if page.route == '/Chats':
        #     page.views.append(Chats(page))
        #     page.update()
        if page.route == '/recover':
            page.views.append(recover_account(page))
            page.update()
        if page.route == '/profile':
            page.views.append(farmer(page))
            page.update()
        if page.route == '/dash':
            page.views.append(dash(page))
            page.update()
    page.on_route_change=route_change
    page.go(home(page))
    page.padding=0
if __name__=="__main__":
    app(target=main, assets_dir="assets", upload_dir='uploaded_images', web_renderer=(WebRenderer.HTML), view=WEB_BROWSER, base_path="/home")
