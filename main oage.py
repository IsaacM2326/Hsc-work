import customtkinter as ctk
from customtkinter import*
from googletrans import Translator
from random import randint

root = ctk.CTk()
root.geometry('800x800')
root.minsize(300, 300)


root.title('Quiz ')


settings_frame= ctk.CTkFrame (root,width =500, height=800, )
settings_frame.theme=  {'fg_color': '#FF0', 'text_color': '#000'}
settings_frame.pack(fill="both", expand=True)

page_4= ctk.CTkFrame(settings_frame )
def resize():
    w=width_entry.get()
    h=height_entry.get()
    root.geometry(f'{w}x{h}')

width_label = ctk.CTkLabel(page_4,text='Width')
width_label.pack(pady=20)
width_entry=ctk. CTkEntry(page_4)
width_entry.pack()

height_label = ctk.CTkLabel(page_4,text='Height')
height_label.pack(pady=20)

height_entry=ctk.CTkEntry(page_4)
height_entry.pack()

my_button = ctk.CTkButton(page_4, text='Resize', command=resize )
my_button.pack(pady=20)


page_4.pack





current_theme_index = 0
current_lang_index = 0
languages = ['en', 'es', 'de', 'hi','' ]  # Language codes: English, Spanish, German, Hindi, Arabic
translator = Translator()



page_1= ctk.CTkFrame(settings_frame )
label_main=ctk.CTkLabel(page_1,text='Welcome , press ''Next Quiz''to Start')
label_main.pack()
page_1_lb = ctk.CTkLabel(settings_frame, text ='MAin page', font=('Bold',20))
page_1_lb.pack()

#=========++=================PAGE @ SETUP ==========================================================================================================
page_2= ctk.CTkFrame(settings_frame )





physics_questions = [
    ("How many laws of motion are there ", "3", 'less than 5 '),
    ("How many planets in our solar system", "8"),
    ("What is the push or pull on an object that can cause it to accelerate called?", "Force",),
    ("What is the unit of measure for force?", "Newton",'starts with N'),
    ("What is the sum of all forces acting on an object called?", "Net force", 'N--, F----'),
    ("In a tug of war, when one team is pulling with a force of 100 N and the other 80 N, what is the net force?", " 20 N",'--N'),
    ("Newton's First Law of Motion is also called:", "Law of Inertia"),
    ("Newton's first Law of Motion states that if there is no net force acting on an object it will:", " remain at rest",'re---- a- re--'),
    (" In the equation F = ma, what does m represent?", "Mass", 'M---'),
    ("How much net force is required to accelerate a 2000 kg car at 3.00 m/s2?", " 6000 N", '6---'),
    ("If you apply a net force of 3 N on 100 g-box, what is the acceleration of the box?", "30 m/s2",'3-m/s2"'),
    ("Are mass and weight the same?", "No", 'Yes/No')
]

physics_hints = [('less than 5 ', 'less than 9 ','Fo---', 'Ne----', 'N--, F----', '--N', 're---- a- re--','6---','3-m/s2 ', 'Yes/No' )



]
count2 = len(physics_questions)
count2_hint = len(physics_hints)
current_question_index = 1

# Widgets for page 2
entry2 = ctk.CTkEntry(page_2, width=30)
entry2.pack(pady=35)

answer_label = ctk.CTkLabel(page_2, text='', font=('Helvetica', 12))
answer_label.pack(pady=20)

my_label1 = ctk.CTkLabel(page_2, text='Question', font=('Helvetica', 24))
my_label1.pack(pady=40)

hint_label = ctk.CTkLabel(page_2, text='', font=('Helvetica', 12))
hint_label.pack()




def submit():
    if 0 <= current_question_index < count2:
        answer = entry2.get().strip().capitalize()  # Get and clean user input
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
    if 0 <= current_question_index < count2:
        hint_label.configure(text=f'Hint: {physics_questions[current_question_index][2]}')
    else:
        hint_label.configure(text='No question to get a hint')
    



def next_question():
    global current_question_index
    current_question_index = randint(0, count2 - 1)
    my_label1.configure(text=physics_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label.configure(text='')
    entry2.delete(0, ctk.END)

# Buttons for page 2
enter_button = ctk.CTkButton(page_2, text='Enter', command=submit)
enter_button.pack(pady=10)

hint_button = ctk.CTkButton(page_2, text='Hint', command=hint1)
hint_button.pack(pady=15)

next_button = ctk.CTkButton(page_2, text='Next Question', command=next_question)
next_button.pack(pady=15)




buttons1 = [next_button ,  enter_button, hint_button]


#==========================PAGE 3======================================================================================
page_3= ctk.CTkFrame(settings_frame )



entry = ctk.CTkEntry(page_3, placeholder_text='Enter answer')
entry.pack(pady=35)

biology_questions = [
    ("What is the basic unit of life?", "Cell",'C--l'),
    ("What is the powerhouse of the cell?", "Mitochondria",'Mi--------ia'),
    ("What is the process by which plants make their own food called?", "Photosynthesis",'Ph-----------s'),
    ("What are the tiny blood vessels where gas exchange occurs in the lungs called?", "Capillaries",'Ca---------'),
    ("Which organ in the human body produces insulin?", "Pancreas"),
    ("What is the function of white blood cells?", "Fight infections",'F---t inf-----ns'),
    ("What is the process of breaking down food into simpler substances called?", "Digestion",'Di------n'),
    ("What is the longest bone in the human body?", "Femur",'Fe---'),
    ("What is the function of the cerebellum?", "Movement",'Mo------'),
    ("What is the main function of red blood cells?", "Transport oxygen ",'1','Tra------ ox----'),
    ("What is the process of cell division called?", "Mitosis",'Mi-----'),
    ("What are the main components of the central nervous system?", "Brain and Spinal Cord",'Br--- and S----- C---'),
]
count1 = len(biology_questions)
current_question_index = 1


def submit2():
    if 0 <= current_question_index < count1:
        answer = entry.get().strip().capitalize()  # Get and clean user input
        correct_answer = biology_questions[current_question_index][1].capitalize()

        # Case-insensitive comparison (optional)
        if answer.lower() == correct_answer.lower():
            answer_label2.configure(text='Correct answer!')
        else:
            answer_label2.configure(text=f'Incorrect answer! The correct answer is {correct_answer}')
    else:
        answer_label2.configure(text='No question to answer!')

def hint2():
    if 0 <= current_question_index < count1:
        hint_label.configure(text=f'Hint: {biology_questions[current_question_index][2]}')
    else:
        hint_label.configure(text='No question to get a hint')

def next_question():
    entry.delete(0, ctk.END)  # Clear the entry widget's content
    global current_question_index
    global current_question_index
    current_question_index = randint(0, count1 - 1)
    my_label.configure(text=biology_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label.configure(text='')
    

answer_label2 = ctk.CTkLabel(page_3, text='Biology quiz ')
answer_label2.pack(pady=20)

my_label = ctk.CTkLabel(page_3, text='', font=('Helvetica',24))
my_label.pack(pady=40)

enter_button = ctk.CTkButton(page_3, text='Enter', command=submit2)
enter_button.pack(padx=10, pady=10)



hint_button = ctk.CTkButton(page_3, text='Hint', command=hint2)
hint_button.pack(pady=15, padx=30)

next_button = ctk.CTkButton(page_3, text='Next Question', command=next_question)
next_button.pack(pady=15, padx=30)

hint_label = ctk.CTkLabel(page_3, text='', font=('Helvetica', 12))
hint_label.pack()


buttons2 = [next_button ,  enter_button, hint_button]


#=====================================PAGE  3  END ========================================================================================================================

settings_frame.pack(fill=ctk.BOTH, expand=True)

pages=[page_1, page_2, page_3, page_4]
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


#===============change langauge =======================#







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
    
def toggle_language():
    global current_lang_index
    current_lang_index = (current_lang_index + 1) % len(languages)
    update_language()

def update_language():
    lang_type = languages[current_lang_index]
    # Translate the text of labels and buttons
    label_main.configure(text=translator.translate('Welcome, press "Next Quiz" to Start', dest=lang_type).text)
    page_1_lb.configure(text=translator.translate('Main page', dest=lang_type).text)
    my_label1.configure(text=translator.translate('Question', dest=lang_type).text)
    answer_label.configure(text=translator.translate('Biology quiz', dest=lang_type).text)
    answer_label.configure(text=translator.translate('Biology quiz', dest=lang_type).text)

    for button in buttons1:
        button_text = button.cget("text")
        translated_text = translator.translate(button_text, dest=lang_type).text
        button.configure(text=translated_text)
    for button in buttons2:
        button_text = button.cget("text")
        translated_text = translator.translate(button_text, dest=lang_type).text
        button.configure(text=translated_text)
    my_label_text= my_label.cget('text')
    translated_text = translator.translate(my_label_text, dest=lang_type).text
    my_label.configure(text=translated_text)





def create_widgets():
    global buttons, labels

    
    

    global buttons
    change_button = ctk.CTkButton(Side_frame, text="Change Language", command=toggle_language)
    change_button.grid(row=2, column=2)
    button2 = ctk.CTkButton(Side_frame,  text='Change theme', fg_color=root.theme['fg_color'], text_color=root.theme['text_color'], command=switch_theme)
    button2.grid(row=2, column=1)
    
    font_button = ctk.CTkButton( Side_frame, text="Increase Font Size", command=increase_font_size)
    font_button.grid(row=2, column=0)
    

    buttons = [change_button, button2, font_button]

   

create_widgets()

Side_frame.pack()


root.mainloop()
