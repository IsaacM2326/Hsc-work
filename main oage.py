
#improting required libaries 
import customtkinter as ctk
from customtkinter import*
from random import randint
# setting root 
root = ctk.CTk()
root.minsize(800, 800)
root.state('zoomed')

root.title('Quiz ')

current_font_index = 0
current_font_size_index = 0
font_sizes = [12, 16, 20, 24]
selected_font_size = font_sizes[current_font_size_index]
fonts = ['Helvetica', 'Arial', 'Times New Roman', 'Courier']
selected_font = fonts[current_font_index]

# Whenre the quiz  pages will be connected to 
main_frame= ctk.CTkFrame (root)
main_frame.theme=  {'fg_color': '#FF0', 'text_color': '#000'}
main_frame.pack()


current_font_index =0 
font_size=12

current_theme_index = 0



start_page= ctk.CTkFrame(main_frame)
label_main=ctk.CTkLabel(start_page,text='Press Next Quiz to start ')
label_main.pack()
start_page.pack()

#=========++=================PAGE @ SETUP ==========================================================================================================
physics_page= ctk.CTkFrame(main_frame , width =2000, height =2000)





physics_questions = [
    ("How many laws of motion are there ", "3", 'less than 5 '),
    ("How many planets in our solar system", "8",'more than 7'),
    ("What is the push or pull on an object that can cause it to accelerate called?", "Force",'F--ce'),
    ("What is the unit of measure for force?", "Newton",'starts with N'),
    ("What is the sum of all forces acting on an object called?", "Net force", 'N--, F----'),
    ("Is light faster than sound  ?", "Yes ",'yes or no '),
    ("Newton's First Law of Motion is also called:", "Law of Inertia",'Law of I--rt--'),
    ("Newton's first Law of Motion states that if there is no net force acting on an object it will:", " remain at rest",'re---- a- re--'),
    (" In the equation F = ma, what does m represent?", "Mass", 'M---'),
    ("How much net force is required to accelerate a 2000 kg car at 3.00 m/s2?", " 6000 N", '6---'),
    ("If you apply a net force of 3 N on 100 g-box, what is the acceleration of the box?", "30 m/s2",'3-m/s2"'),
    ("Are mass and weight the same?", "No", 'Yes/No')
]


physics_count = len(physics_questions)
current_question_index = 0

# Widgets for page 2
physics_entry = ctk.CTkEntry(physics_page, width=300)
physics_entry.place (relx=.45,rely=.3)

answer_label = ctk.CTkLabel(physics_page, text='', font=('Helvetica', 12))
answer_label.place (relx=.5,rely=.1)

physics_label = ctk.CTkLabel(physics_page, text='Question', font=('Helvetica', 24))
physics_label.place (relx=.2,rely=.2)

hint_label1 = ctk.CTkLabel(physics_page, text='', font=('Helvetica', 12))
hint_label1.place (relx=.5,rely=.25)




def submit():
    if 0 <= current_question_index < physics_count:
        answer = physics_entry.get().strip().capitalize()  # Get and clean user input
        correct_answer = physics_questions[current_question_index][1].capitalize()

        # Case-insensitive comparison (optional)
        if answer.lower() == correct_answer.lower():
            answer_label.configure(text='Correct answer!')
        else:
            answer_label.configure(text=f'Incorrect answer! The correct answer is {correct_answer}')
    else:
        answer_label.configure(text='No question to answer!')
# start the loop from zero for if condition 


def hint1():
    if 0 <= current_question_index < physics_count:
        hint_label1.configure(text=f'Hint: {physics_questions[current_question_index][2]}')
    else:
        hint_label1.configure(text='No question to get a hint')
    


# increments the question index and reset the labels 
def next_question_physics():
   
    global current_question_index
    current_question_index = randint(0, physics_count - 1)
    physics_label.configure(text=physics_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label1.configure(text='')
    quiz_label1.configure(text='')
    physics_entry.delete(0, ctk.END)

# Buttons for page 2
enter_button = ctk.CTkButton(physics_page, text='Enter', command=submit)
enter_button.place (relx=.5,rely=.35)

hint_button = ctk.CTkButton(physics_page, text='Hint', command=hint1)
hint_button.place (relx=.5,rely=.4)

next_button = ctk.CTkButton(physics_page, text='Next Question', command=next_question_physics)
next_button.place(relx=.5,rely=.45)

quiz_label1 = ctk.CTkLabel(physics_page, text='Physics quiz ')
quiz_label1.place (relx=.5,rely=.1)


quiz_buttons_1 = [next_button ,  enter_button, hint_button]


#==========================PAGE 3======================================================================================
biology_page= ctk.CTkFrame(main_frame ,width =1500, height =1000)



biology_entry = ctk.CTkEntry(biology_page, placeholder_text='Enter answer', width=300)
biology_entry.place(relx=.45,rely=.3)

biology_questions = [
    ("What is the basic unit of life?", "Cell",'C--l'),
    ("What is the powerhouse of the cell?", "Mitochondria",'Mi--------ia'),
    ("What is the process by which plants make their own food called?", "Photosynthesis",'Ph-----------s'),
    ("What are the tiny blood vessels where gas exchange occurs in the lungs called?", "Capillaries",'Ca---------'),
    ("Which organ in the human body produces insulin?", "Pancreas",'Pa----as'),
    ("What is the function of white blood cells?", "Fight infections",'F---t inf-----ns'),
    ("What is the process of breaking down food into simpler substances called?", "Digestion",'Di------n'),
    ("What is the longest bone in the human body?", "Femur",'Fe---'),
    ("What is the function of the cerebellum?", "Movement",'Mo------'),
    ("What is the main function of red blood cells?", "Transport oxygen ",'Tra------ ox----'),
    ("What is the process of cell division called?", "Mitosis",'Mi-----'),
    ("What are the main components of the central nervous system?", "Brain and Spinal Cord",'Br--- and S----- C---'),
]
biology_count = len(biology_questions)
current_question_index = 0

#======================defining quiz commands =============================================================================
#compares the input fro entry to the array 
def biology_submit():
    if 0 <= current_question_index < biology_count:
        answer = biology_entry.get().strip().capitalize()  # Get and clean user input
        correct_answer = biology_questions[current_question_index][1].capitalize()

        # Case-insensitive comparison (optional)
        if answer.lower() == correct_answer.lower():
            quiz_label2.configure(text='Correct answer!')
        else:
            quiz_label2.configure(text=f'Incorrect answer! The correct answer is {correct_answer}')
    else:
        quiz_label2.configure(text='No question to answer!')

def biology_hintss():
    if 0 <= current_question_index < biology_count:
        hint_label.configure(text=f'Hint: {biology_questions[current_question_index][2]}')
    else:
        hint_label.configure(text='No question to get a hint')

def next_question_biology():
    biology_entry.delete(0, ctk.END)  # Clear the entry widget's content
    global current_question_index
    global current_question_index
    current_question_index = randint(0, biology_count - 1)
    biology_label.configure(text=biology_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label.configure(text='')
    quiz_label2.configure(text='')

#======================defining quiz commands ======================================   

quiz_label2 = ctk.CTkLabel(biology_page, text='Biology quiz ')
quiz_label2.place (relx=.5,rely=.1)

biology_label = ctk.CTkLabel(biology_page, text='', font=('Helvetica',24))
biology_label.place(relx=.35,rely=.2)


enter_button = ctk.CTkButton(biology_page, text='Enter', command=biology_submit)
enter_button.place (relx=.5,rely=.35)



hint_button = ctk.CTkButton(biology_page, text='Hint', command=biology_hintss)
hint_button.place (relx=.5,rely=.4)

next_button = ctk.CTkButton(biology_page, text='Next Question', command=next_question_biology)
next_button.place(relx=.5,rely=.45)


hint_label = ctk.CTkLabel(biology_page, text='', font=('Helvetica', 12))
hint_label.place (relx=.5,rely=.25)


quiz_buttons_2 = [next_button ,  enter_button, hint_button]


#=====================================PAGE  3  END ========================================================================================================================
#==========================PAGE $ START==================================================================================================================================================== 

settings_page= ctk.CTkFrame(main_frame ,width =1500, height =800)





width_label = ctk.CTkLabel(settings_page,text='Width')
width_label.place(relx=.5,rely=.1)
width_entry=ctk. CTkEntry(settings_page)
width_entry.place(relx=.5,rely=.3)

height_label = ctk.CTkLabel(settings_page,text='Height')
height_label.place(relx=.5,rely=.4)

height_entry=ctk.CTkEntry(settings_page)
height_entry.place(relx=.5,rely=.45)
#to set a limit in resizing so that gui maintains functionality 




themes = [
    {'bg': 'black', 'fg': 'black', 'text': 'Dark Theme'},
    {'bg': 'silver', 'fg': 'silver', 'text': 'Dark Theme'},
    {'bg': 'brown', 'fg': 'brown', 'text': 'eyestrain'},
    {'bg': 'grey', 'fg': 'grey', 'text': 'Cool 1 '},
    {'bg': 'orange', 'fg': 'orange', 'text': 'easy on the eyes '}
    
]



def switch_theme():
    global current_theme_index
    current_theme_index = (current_theme_index + 1)
    current_theme_index = (current_theme_index + 1) % len(themes)
    theme = themes[current_theme_index]
    start_page.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    physics_page.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    biology_page.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    settings_page.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    main_frame.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    bottom_frame.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    root.configure(bg_color=theme['bg'], fg_color=theme['fg'], )

    

#=====change font size========
# Font style and size change functionality
def change_font_style():
    global current_font_index, selected_font
    current_font_index = (current_font_index + 1) % len(fonts)
    selected_font = fonts[current_font_index]
    update_fonts()

def increase_font_size():
    global current_font_size_index, selected_font_size
    current_font_size_index = (current_font_size_index + 1) % len(font_sizes)
    selected_font_size = font_sizes[current_font_size_index]
    update_fonts()

def update_fonts():
    # Update the fonts in all labels
    physics_label.configure(font=(selected_font, selected_font_size))
    hint_label1.configure(font=(selected_font, selected_font_size))
    biology_label.configure(font=(selected_font, selected_font_size))
    hint_label.configure(font=(selected_font, selected_font_size))
    height_label.configure(font=(selected_font, selected_font_size))
    width_label.configure(font=(selected_font, selected_font_size))
    warning_label.configure(font=(selected_font, selected_font_size))
    quiz_label1.configure(font=(selected_font, selected_font_size))
    quiz_label2.configure(font=(selected_font, selected_font_size))
    for button in quiz_buttons_1:
        button.configure(font=(selected_font, selected_font_size))
#changing buttons for each frame and quiz 
    for button in quiz_buttons_2:
        button.configure(font=(selected_font, selected_font_size))
    for button in quiz_buttons_3:
        button.configure (font=(selected_font, selected_font_size))
    for button in setting_buttons:
        button.configure(font=(selected_font, selected_font_size))
        
        





#=====================================================Creating Widgets  ==============================================================================================================================================


def create_widgets():
    global buttons, labels

    
    

    global setting_buttons
    change_button = ctk.CTkButton(settings_page, text="Change Style", command=change_font_style)
    change_button.grid(row=2, column=2)
    change_theme_button = ctk.CTkButton(settings_page,  text='Change theme',  command=switch_theme)
    change_theme_button.grid(row=2, column=1)
    
    font_button = ctk.CTkButton( settings_page, text="Increase Font Size", command=increase_font_size)
    font_button.grid(row=2, column=0)
    


    setting_buttons = [change_button, change_theme_button, font_button]



settings_page.place(relx=.5,rely=2)

#=========================================PAGE 4 END ======================================================================================
#=========================================SWITCH PAGES ===================================

pages=[start_page, physics_page, biology_page, settings_page]
count=0

def move_next_page():
    global count 
    if not count >len(pages)-2:
        for p in pages:
            p.pack_forget()#deletes page 

        count += 1
        page=pages[count]
        page.pack(padx=50, pady=100)#displays  next page 

def back_next_page():
    global count 
    if not count == 0:
        for p in pages:     
            p.pack_forget()#deletes page 


        count -= 1
        page=pages[count]
        page.pack(padx=50, pady=100)# displays back page

def settings_page1():
        
    for p in pages:
        p.pack_forget()

    settings_page.pack(pady=100)

bottom_frame= ctk.CTkFrame(root,width=1000,height =400)

back_btn = ctk.CTkButton(bottom_frame, text='Exit',font =('Helvetica', 12), width=8, command=back_next_page)
back_btn.grid(row=2, column=1)

next_btn= ctk.CTkButton(bottom_frame, text='Next Quiz ', font=('Helvetica', 12),width=8,command=move_next_page )
next_btn.grid(row=2, column=2)

settings_button=ctk.CTkButton(bottom_frame, text='Settings', font=('Helvetica',12),width=8, command=settings_page1)
settings_button.grid(row=2, column=3)
quiz_buttons_3= [next_btn,back_btn]

bottom_frame.place(rely=.9, relx=0.45)
#===========================================================Side   Page   ===================================================================



   

create_widgets()




root.mainloop()

