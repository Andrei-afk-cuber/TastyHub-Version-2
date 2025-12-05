# importing necessary libraries
import pathlib

# config variables
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
ICON_PATH = PROJECT_ROOT / 'app' / 'images' / 'icon.ico'
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432

theme = {
    'fg_color':'#e06b04',
    'hover_color':'#b55604',
    'text_color':'#ffffff',
    'textbox_bg_color':"#171717",
    'recipe_card_fg_color':"#333333"
}

day_theme = {
    'background_color':'#ffcca1', # foreground color
    'frame_background_color':'#ffe0c6', # frame bg color
    'button_color':'#ffcca1', # color of buttons
    'hover_color':'#ffb373', # color of active buttons
    'text_color':'#000000', # color of text
    'textbox_bg_color':"#ffcca1", # textbox bg color
    'recipe_card_fg_color':"#333333",
    'textbox_text_color': '#000000'
}

