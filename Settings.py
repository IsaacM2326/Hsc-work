import customtkinter as ctk

root = ctk.CTk()

themes = [
    {'bg': 'black', 'fg': 'white', 'text': 'Light Theme'},
    {'bg': 'white', 'fg': 'black', 'text': 'Dark Theme'},
    {'bg': '#333', 'fg': 'white', 'text': 'white dove'},
    {'bg': 'black', 'fg': 'light green', 'text': 'Custom Theme 2'},
    {'bg': '#grey', 'fg': 'grey', 'text': 'east eyes  3'}
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

button1 = ctk.CTkButton(root, text='change theme', command=switch_theme)
button1.pack(pady=80)

root.mainloop()
