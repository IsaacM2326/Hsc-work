 #, HSC-assignment
import customtkinter as ctk
from random import randint

# Set mode
ctk.set_appearance_mode('dark') 
ctk.set_default_color_theme('blue')
# Window 
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('600x400')

entry = ctk.CTkEntry(window, placeholder_text='Enter answer')
entry.pack()

biology_questions = [
    ("What is the basic unit of life?", "Cell"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("What is the process by which plants make their own food called?", "Photosynthesis"),
    ("What are the tiny blood vessels where gas exchange occurs in the lungs called?", "Capillaries"),
    ("Which organ in the human body produces insulin?", "Pancreas"),
    ("What is the function of white blood cells?", "Fight infections/Immune response"),
    ("What is the process of breaking down food into simpler substances called?", "Digestion"),
    ("What is the longest bone in the human body?", "Femur"),
    ("What is the function of the cerebellum?", "Coordination of movement/Balance"),
    ("What is the main function of red blood cells?", "Transport oxygen (to tissues)"),
    ("What is the process of cell division called?", "Mitosis"),
    ("What are the main components of the central nervous system?", "Brain and Spinal Cord")
]
count = len(biology_questions)
current_question_index = -1  # Initialize to an invalid index

def clear():
    entry.delete(0, ctk.END)
    answer_label.configure(text='')

def submit():
    if current_question_index >= 0 and current_question_index < count:
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
    current_question_index = randint(0, count - 1)
    my_label.configure(text=biology_questions[current_question_index][0])
    answer_label.configure(text='')
    hint_label.configure(text='')

answer_label = ctk.CTkLabel(window, text='')
answer_label.pack(pady=20)

my_label = ctk.CTkLabel(window, text='', font=('Helvetica',24))
my_label.pack(pady=40)

enter_button = ctk.CTkButton(window, text='Enter', command=submit)
enter_button.pack(padx=10, pady=10)

clear_button = ctk.CTkButton(window, text='Clear', command=clear)
clear_button.pack(pady=15, padx=30)

hint_button = ctk.CTkButton(window, text='Hint', command=hint)
hint_button.pack(pady=15, padx=30)

next_button = ctk.CTkButton(window, text='Next Question', command=next_question)
next_button.pack(pady=15, padx=30)

hint_label = ctk.CTkLabel(window, text='', font=('Helvetica', 12))
hint_label.pack()

window.mainloop()
