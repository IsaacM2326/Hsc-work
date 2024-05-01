import customtkinter as ctk

root = ctk.CTk()
root.theme = {'fg_color': '#FF0', 'text_color': '#000'}

themes = [
    {'bg': 'black', 'fg': 'white', 'text': 'Light Theme'},
    {'bg': 'white', 'fg': 'black', 'text': 'Dark Theme'},
    {'bg': '#333', 'fg': 'white', 'text': 'Custom Theme 1'},
    {'bg': '#FF5733', 'fg': 'black', 'text': 'Custom Theme 2'},
    {'bg': '#4287f5', 'fg': 'white', 'text': 'Custom Theme 3'}
]

current_theme_index = 0

def switch_theme():
    global current_theme_index
    current_theme_index = (current_theme_index + 1) % len(themes)
    theme = themes[current_theme_index]
    root.configure(bg=theme['bg'])
    root.configure(fg_color=theme['fg'], text=theme['text'])

root.title('customtkinter app')
root.geometry('600x400')

button1 = ctk.CTkButton(root, text='change theme', fg_color=root.theme['fg_color'], text_color=root.theme['text_color'], command=switch_theme)
button1.pack(pady=80)

root.mainloop()
