from flet import *
from Data import get_users_id

#init_Tb()

def dash(page:Page):
    page.title='Real time db update'
    page.scroll='auto'
    id=page.session.get('user')[1]

    user_table=DataTable(
        columns=[
            #DataColumn(Text('ID')),
            DataColumn(Text('Name')),
            DataColumn(Text('Breed')),
            DataColumn(Text('Type')),
            DataColumn(Text('Price(Ksh)')),
            DataColumn(Text('Age')),
            DataColumn(Text('Quantity')),
            DataColumn(Text('')),
            DataColumn(Text('')),
        ],
        rows=[]
    )
    users=get_users_id('Poultry', id)
    for user in users:
            user_table.rows.append(
                DataRow(
                    cells=[
                        #DataCell(Text(str(user[0]))),
                        DataCell(Text(str(user[10]))),
                        DataCell(Text(str(user[4]))),
                        DataCell(Text(str(user[8]))),
                        DataCell(Text(str(user[6]))),
                        DataCell(Text(str(user[7]))),
                        DataCell(Text(str(user[5]))),
                        DataCell(IconButton(icon=icons.EDIT)),
                        DataCell(IconButton(icon=icons.DELETE, icon_color='red'))
                    ]
                )
            )
    
    user_table2=DataTable(
        columns=[
            #DataColumn(Text('ID')),
            DataColumn(Text('Name')),
            DataColumn(Text('Breed')),
            DataColumn(Text('Type')),
            DataColumn(Text('Price(Ksh)')),
            DataColumn(Text('Age')),
            DataColumn(Text('Quantity')),
            DataColumn(Text('')),
            DataColumn(Text('')),
        ],
        rows=[]
    )
    users1=get_users_id('Livestock', id)
    for user in users1:
            user_table2.rows.append(
                DataRow(cells=[
                        #DataCell(Text(str(user[0]))),
                        DataCell(Text(str(user[10]))),
                        DataCell(Text(str(user[4]))),
                        DataCell(Text(str(user[8]))),
                        DataCell(Text(str(user[6]))),
                        DataCell(Text(str(user[7]))),
                        DataCell(Text(str(user[5]))),
                        DataCell(IconButton(icon=icons.EDIT)),
                        DataCell(IconButton(icon=icons.DELETE, icon_color='red'))
                    ]))

    name_input=TextField(label='Name')
    age_input=TextField(label='Age')#, input_type=TextFieldType.NUMBER)

    def add_user_click(e):
        name=name_input.value
        age=int(age_input.value)
        #add_user(name, age)
        user_table2.rows.append(
             DataRow(cells=
                     [
                        DataCell(Text(users[-1][0]+1)),
                        DataCell(Text(name)),
                        DataCell(Text(age))
                     ]))
        page.add(Container(Row([OutlinedButton(text=name), ]), bgcolor=colors.BLACK26))
        name_input.value=''
        age_input.value=''
        page.update()

    return View('/dash',[
        Row([ElevatedButton(text='back',color='red', icon=icons.ARROW_BACK, on_click=lambda e: page.go('/home')),
             IconButton( icon=icons.ADD, bgcolor=colors.WHITE24, on_click=lambda e: page.go('/add_item'))
             ]),
        Text('Poultry', weight='bold', size=15),
        Divider(),
        user_table,
        Text('Livestock', weight='bold', size=15),
        Divider(),
        user_table2,], auto_scroll='auto', scroll='auto')

