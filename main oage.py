import customtkinter as ctk 
root= ctk.CTk( )
root.geometry('500x800')

from random import randint
current_theme_index = 0

global settings_frame
settings_frame= ctk.CTkFrame (root,width =500, height=800, )
settings_frame.theme=  {'fg_color': '#FF0', 'text_color': '#000'}

settings_frame.pack(side='left',fill='x')

page_1= ctk.CTkFrame(settings_frame )
label_main=ctk.CTkLabel(page_1,text='Welcome , press ''Next Quiz''to Start')
label_main.pack()
page_1_lb = ctk.CTkLabel(settings_frame, text ='MAin page', font=('Bold',20))
page_1_lb.pack()

#=========++=================PAGE @ SETUP ==========================================================================================================
page_2= ctk.CTkFrame(settings_frame )



entry2= ctk.CTkEntry(page_2, placeholder_text='Enter answer')
entry2.pack()

physics_questions = [
    ("How many laws of motion are there ", "3"),
    ("How many planets in our solar system", "8"),
    ("What is the push or pull on an object that can cause it to accelerate called?", "Force"),
    ("What is the unit of measure for force?", "Newton"),
    ("What is the sum of all forces acting on an object called?", "Net force"),
    ("In a tug of war, when one team is pulling with a force of 100 N and the other 80 N, what is the net force?", " 20 N"),
    ("Newton's First Law of Motion is also called:", "Law of Inertia"),
    ("Newton's first Law of Motion states that if there is no net force acting on an object it will:", " remain at rest"),
    (" In the equation F = ma, what does m represent?", "Mass"),
    ("How much net force is required to accelerate a 2000 kg car at 3.00 m/s2?", " 6000 N"),
    ("If you apply a net force of 3 N on 100 g-box, what is the acceleration of the box?", "30 m/s2"),
    ("Are mass and weight the same?", "No")
]
count1 = len(physics_questions)
current_question_index = count1-1  # Initialize to an invalid index



def submit():
    if current_question_index >= 0 and current_question_index < count1:
        answer = entry2.get().strip().capitalize()
        correct_answer = physics_questions[current_question_index][1].capitalize()
        if answer == correct_answer:
            answer_label.configure(text='Correct answer!')
        else:
            answer_label.configure(text=f'Incorrect answer! The correct answer is {correct_answer}')
    else:
        answer_label.configure(text='No question to answer')

def hint():
    global current_question_index
    if current_question_index >= 0 and current_question_index < count1:
        hint_label.configure(text=f'Hint: {physics_questions[current_question_index][1]}')
    else:
        hint_label.configure(text='No question to get a hint')

def next_question():
    global current_question_index
    current_question_index = randint(0, count1 - 1)
    my_label1.configure(text=physics_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label.configure(text='')
    entry.delete(0, ctk.END)
    answer_label.configure(text='')

answer_label = ctk.CTkLabel(page_2, text='a')
answer_label.pack(pady=20)

my_label1 = ctk.CTkLabel(page_2, text='question', font=('Helvetica',24))
my_label1.pack(pady=40)

enter_button = ctk.CTkButton(page_2, text='Enter', command=submit)
enter_button.pack(padx=10, pady=10)



hint_button = ctk.CTkButton(page_2, text='Hint', command=hint)
hint_button.pack(pady=15, padx=30)

next_button = ctk.CTkButton(page_2, text='Next Question', command=next_question)
next_button.pack(pady=15, padx=30)

hint_label = ctk.CTkLabel(page_2, text='', font=('Helvetica', 12))
hint_label.pack()


def submit():
    if current_question_index >= 0 and current_question_index < count1:
        answer = entry2.get().strip().capitalize()
        correct_answer = physics_questions[current_question_index][1].capitalize()
        if answer == correct_answer:
            answer_label.configure(text='Correct answer!')
        else:
            answer_label.configure(text=f'Incorrect answer! The correct answer is {correct_answer}')
    else:
        answer_label.configure(text='No question to answer')

def hint():
    global current_question_index
    if current_question_index >= 0 and current_question_index < count:
        hint_label.configure(text=f'Hint: {biology_questions[current_question_index][1]}')
    else:
        hint_label.configure(text='No question to get a hint')

def next_question():
    global current_question_index
    current_question_index = randint(0, count1 - 1)
    my_label1.configure(text=physics_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label.configure(text='')
    entry.delete(0, ctk.END)
    answer_label.configure(text='')

buttons1 = [next_button ,  enter_button, hint_button]


#==========================PAGE 3======================================================================================
page_3= ctk.CTkFrame(settings_frame )



entry = ctk.CTkEntry(page_3, placeholder_text='Enter answer')
entry.pack()

biology_questions = [
    ("What is the basic unit of life?", "Cell"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("What is the process by which plants make their own food called?", "Photosynthesis"),
    ("What are the tiny blood vessels where gas exchange occurs in the lungs called?", "Capillaries"),
    ("Which organ in the human body produces insulin?", "Pancreas"),
    ("What is the function of white blood cells?", "Fight infections"),
    ("What is the process of breaking down food into simpler substances called?", "Digestion"),
    ("What is the longest bone in the human body?", "Femur"),
    ("What is the function of the cerebellum?", "Movement/Coordination"),
    ("What is the main function of red blood cells?", "Transport oxygen "),
    ("What is the process of cell division called?", "Mitosis"),
    ("What are the main components of the central nervous system?", "Brain and Spinal Cord")
]
count1 = len(biology_questions)
current_question_index = count1 -1


def submit():
    if current_question_index >= 0 and current_question_index < count1:
        answer = entry.get().strip().capitalize()
        correct_answer = biology_questions[current_question_index][1].capitalize()
        if answer == correct_answer:
            answer_label.configure(text='Correct answer!')
        else:
            answer_label.configure(text=f'Incorrect answer! The correct answer is {correct_answer}')
    else:
        answer_label.configure(text='No question to answer')

def hint():
    global current_question_index
    if current_question_index >= 0 and current_question_index < count:
        hint_label.configure(text=f'Hint: {biology_questions[current_question_index][1]}')
    else:
        hint_label.configure(text='No question to get a hint')

def next_question():
    global current_question_index
    current_question_index = randint(0, count1 - 1)
    my_label.configure(text=biology_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label.configure(text='')
    entry.delete(0, ctk.END)
    answer_label.configure(text='')

answer_label = ctk.CTkLabel(page_3, text='Biology quiz ')
answer_label.pack(pady=20)

my_label = ctk.CTkLabel(page_3, text='', font=('Helvetica',24))
my_label.pack(pady=40)

enter_button = ctk.CTkButton(page_3, text='Enter', command=submit)
enter_button.pack(padx=10, pady=10)



hint_button = ctk.CTkButton(page_3, text='Hint', command=hint)
hint_button.pack(pady=15, padx=30)

next_button = ctk.CTkButton(page_3, text='Next Question', command=next_question)
next_button.pack(pady=15, padx=30)

hint_label = ctk.CTkLabel(page_3, text='', font=('Helvetica', 12))
hint_label.pack()


buttons2 = [next_button ,  enter_button, hint_button]


#=====================================PAGE  3  END ========================================================================================================================

settings_frame.pack(fill=ctk.BOTH, expand=True)

pages=[page_1, page_2, page_3]
count=0

def move_next_page():
    global count 
    if not count >len(pages)-2:
        for p in pages:
            p.pack_forget()

        count += 1
        page=pages[count]
        page.pack(pady=100)

def back_next_page():
    global count 
    if not count == 0:
        for p in pages:
            p.pack_forget()

        count -= 1
        page=pages[count]
        page.pack(pady=100)


bottom_frame= ctk.CTkFrame(root)

back_btn = ctk.CTkButton(bottom_frame, text='Exit',font =('Helvetica', 12), width=8, command=back_next_page)
back_btn.pack(side=ctk.LEFT, padx=5, pady=10)

next_btn= ctk.CTkButton(bottom_frame, text='Next Quiz ', font=('Helvetica', 12),width=8,command=move_next_page )
next_btn.pack(side=ctk.BOTTOM, padx=10,pady=10)



bottom_frame.pack(side=ctk.BOTTOM,pady=10)
#===========================================================Side   Page   ===================================================================
Side_frame= ctk.CTkFrame(root)


root.theme = {'fg_color': '#FF0', 'text_color': '#000'}

languages = ['Spanish', 'German', 'Hindi', 'Arabic']
current_language_index = 0
#===============change langauge =======================#




label= ctk.CTkLabel(root, text= 'hello')

languages = ['Spanish', 'German', 'Hindi', 'Arabic']
current_language_index = 0

themes = [
    {'bg': 'black', 'fg': 'white', 'text': 'Light Theme'},
    {'bg': 'white', 'fg': 'black', 'text': 'Dark Theme'},
    {'bg': 'red', 'fg': 'blue', 'text': 'eyestrain'},
    {'bg': 'blue', 'fg': 'blue', 'text': 'Cool 1 '},
    {'bg': 'blue', 'fg': 'blue', 'text': 'easy on the eyes '}
]


def switch_theme():
    global current_theme_index
    current_theme_index = (current_theme_index + 1)
    current_theme_index = (current_theme_index + 1) % len(themes)
    theme = themes[current_theme_index]
    settings_frame.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    page_1.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    root.configure(bg_color=theme['bg'], fg_color=theme['fg'], )
    Side_frame.configure(bg_color=theme['bg'], fg_color=theme['fg'], )


    
root.minsize(height=300, width=500)

#=====change font size========
current_font_size_index = 0

font_sizes = [12, 16, 20, 24]

def increase_font_size():
    global current_font_size_index
    current_font_size_index = (current_font_size_index + 1) % len(font_sizes)
    update_fonts()

def update_fonts():
    selected_font_size = font_sizes[current_font_size_index]
    for button in buttons2:
        button.configure(font=('Helvetica', selected_font_size))
    for button in buttons1:
        button.configure(font=('Helvetica', selected_font_size))
    for button in buttons:
        button.configure(font=('Helvetica', selected_font_size))
    page_1_lb.configure(font=('Helvetica',selected_font_size))
    



languages = ['Spanish', 'German', 'Hindi', 'Arabic']
current_language_index = 0
def create_widgets():
    global buttons, labels

    
    

    change_button = ctk.CTkButton(Side_frame, text="Change Language",)
    change_button.pack(pady=5, padx=12)
    button2 = ctk.CTkButton(Side_frame,  text='Change theme', fg_color=root.theme['fg_color'], text_color=root.theme['text_color'], command=switch_theme)
    button2.pack(pady=5, padx=6) 
    
    font_button = ctk.CTkButton( Side_frame, text="Increase Font Size", command=increase_font_size)
    font_button.pack(pady=5,padx=20)
    


    buttons = [change_button , button2, font_button]

   

create_widgets()

Side_frame.pack(side=ctk.LEFT,pady=5, padx=20)


root.mainloop()