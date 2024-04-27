import customtkinter as ctk
root = ctk.CTk()


themes = [
    {'bg': 'black', 'fg': 'white', 'text': 'Light Theme'},
    {'bg': 'white', 'fg': 'black', 'text': 'Dark Theme'},
    {'bg': '#333', 'fg': 'white', 'text': 'Custom Theme 1'},
    {'bg': '#FF5733', 'fg': 'black', 'text': 'Custom Theme 2'},
    {'bg': '#4287f5', 'fg': 'white', 'text': 'Custom Theme 3'}
]

current_theme_index=0
def switch_theme():
    global current_theme_index
    if current_theme_index >= len(themes):
        current_theme_index = 0
    theme = themes[current_theme_index]
    root.configure(bg=theme['bg'], fg=theme['fg'])
    button1.config(text=theme['text'])


 


#root 
root = ctk.CTk()
root.title ('customtkinter app')
root.geometry('600x400')

button1 = ctk.CTkButton(root, text = 'change theme  ',
                       fg_color= '#FF0',
                       text_color= '#000',
                       command = lambda: switch_theme()) 
button1.pack(pady=80)
root.mainloop()
