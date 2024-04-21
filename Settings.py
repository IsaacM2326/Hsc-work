import customtkinter as ctk
ctk.set_appearance_mode('dark') 
ctk.set_default_color_theme('blue')

#window 
window = ctk.CTk()
window.title ('customtkinter app')
window.geometry('600x400')

button = ctk.CTkButton(window, text = 'change theme  ',
                       fg_color= '#FF0',
                       text_color= '#000',
                       command = lambda: ctk.set_appearance_mode('light','dark'))
button.pack(pady=80)
window.mainloop()