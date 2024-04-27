import customtkinter as ctk
root 
ctk.set_appearance_mode('dark','light') 
ctk.set_default_color_theme('blue')
 
def set_appearance_mode('dark','light')
#window 
root = ctk.CTk()
root.title ('customtkinter app')
root.geometry('600x400')

button = ctk.CTkButton(root, text = 'change theme  ',
                       fg_color= '#FF0',
                       text_color= '#000',
                       command = lambda: ctk.set_appearance_mode('light','dark'))
button.pack(pady=80)
root.mainloop()