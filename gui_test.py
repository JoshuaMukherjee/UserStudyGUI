from controller import Controller
from pages import ID_page, Text_Page, Response_Page
import time


def f(x):
    old_text = x.into_label['text']
    x.into_label['text'] = 'Scanning...'
    x.update()
    print(1)
    time.sleep(1)
    x.into_label['text'] = old_text


pages = [ID_page, Text_Page, Text_Page, Response_Page]

page_args = [
    {
            "title_label_args":{
                "text":'Haptics BEM GUI test'
            },
            "info_label_args":{
                "text":"Welcome to the Haptics BEM Study..."
            },
            "next_page": 'text_page'
    },
    
    {
        'text_args':{
            "text":"Some instructions..."
            },
        "next_page": 'scan_page'
    }, 

    {
        'text_args':{
            "text":"Press Button when hand is in place..."
            },
        "button_func": lambda x: f(x),
        "next_page": 'response_page'
        
    },
    {
         'text_args':{
            "text":"Rate Intensity & Please enter the number you belive you felt..."
        },
         "next_page": 'start_page'
    }
]


page_names = ['start_page', 'text_page', 'scan_page','response_page']


gui = Controller(pages, page_names, page_args)
gui.mainloop()