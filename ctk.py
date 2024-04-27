 #, HSC-assignment
import customtkinter as ctk

#set mode
ctk.set_appearance_mode('dark') 
ctk.set_default_color_theme('blue')

#window 
root = ctk.CTk()
root.title ('customtkinter app')
root.geometry('600x400')

button = ctk.CTkButton(root, text = 'Settings  ',
                       fg_color= '#FF0',
                       text_color= '#000',
                       command = lambda: ctk.set_appearance_mode('light'))
button.pack(pady=20)
my_button = ctk.CTkButton(root, text='Settings',fg_color=('blue', 'green'),height=50, width=50, corner_radius=10, hover_color='gray')
my_button.pack(pady=20)

my_button2 =ctk.CTkButton(root,text='Quiz',fg_color=('blue', 'green'),height=50, width=100, corner_radius=10,hover_color='gray')
my_button2.pack(pady=20)

label = ctk.CTkLabel(root,
                     text = 'choose quiz ',
                     fg_color=('red','blue'),
                     text_color = ('green','yellow'),
                     corner_radius = 10)
label.pack(pady=80)


root.mainloop()

