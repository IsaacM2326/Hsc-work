 #, HSC-assignment
import customtkinter as ctk

#set mode
ctk.set_appearance_mode('dark') 
ctk.set_default_color_theme('blue')

#window 
window = ctk.CTk()
window.title ('customtkinter app')
window.geometry('600x400')
label = ctk.CTkLabel(window,
                     text = 'A ctk label',
                     fg_color=('red','blue'),
                     text_color = ('green','yellow'),
                     corner_radius = 10)
label.pack()
button = ctk.CTkButton(window, text = 'A ctk_buttton ',
                       fg_color= '#FF0',
                       text_color= '#000',
                       command = lambda: ctk.set_appearance_mode('light'))
button.pack(pady=80)
my_button = ctk.CTkButton(window, text='Settings',fg_color=('blue', 'green'),height=50, width=50, corner_radius=10, hover_color='gray')
my_button.pack(pady=60)

my_button2 =ctk.CTkButton(window,text='Setting',fg_color=('blue', 'green'),height=50, width=100, corner_radius=10,hover_color='gray')
my_button2.pack()

label = ctk.CTkLabel(window,
                     text = 'choose quiz ',
                     fg_color=('red','blue'),
                     text_color = ('green','yellow'),
                     corner_radius = 10)
label.pack()


window.mainloop()
