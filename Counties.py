from flet import *
Counties={"Kakamega":["Malava", "Lurambi", "Shinyalu", "Navakholo", "Likuyani", "Khwisero", "Matungu", "Ikolomani", "Mumias West", ],
"Nairobi":["Embaskasi East", "Embakasi South", "Juja", "Kasarani"],
}

# def main(page: Page):
#     def subcounties(e):
#         L.options.clear()
#         for i in Counties[e.control.value]:
#                 L.options.append(dropdown.Option(i))
#         page.update()

#     k= Dropdown(label='County', on_change=subcounties, width=300)
    
#     L= Dropdown(label='Sub-County',width=300 )
    
#     for i in Counties:
#         k.options.append(dropdown.Option(i))
#     page.add(k, L)
# app(main)