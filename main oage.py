import customtkinter as ctk 
root= ctk.CTk()
root.minsize(height=500, width = 800)


settings_frame= ctk.CTkFrame (root,bg_color=('red', 'blue'),)
settings_frame.theme=  {'fg_color': '#FF0', 'text_color': '#000'}

page_1= ctk.CTkFrame(settings_frame )
page_1_lb = ctk.CTkLabel(page_1, text ='Settings', font=('Bold',20))
page_1_lb.pack()
page_1.pack(pady=100)

page_2= ctk.CTkFrame(settings_frame )
page_2_lb = ctk.CTkLabel(page_2, text ='Settings', font=('Bold',20))
page_2_lb.pack()


page_3= ctk.CTkFrame(settings_frame )
page_3_lb = ctk.CTkLabel(page_3, text ='Settings', font=('Bold',20))
page_3_lb.pack()


settings_frame.pack(fill=ctk.BOTH, expand=True)



bottom_frame= ctk.CTkFrame(root)

back_btn = ctk.CTkButton(bottom_frame, text='back',font =('Helvetica', 12), width=8)
back_btn.pack(side=ctk.LEFT, padx=10)

next_btn= ctk.CTkButton(bottom_frame, text='Next', font=('Helvetica', 12),width=8)
next_btn.pack(side=ctk.BOTTOM, pady=10)


bottom_frame.pack(side=ctk.BOTTOM,pady=10)

root.mainloop()
