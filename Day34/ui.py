from email.mime import base
from msilib.schema import Font
from tkinter import *
from tkinter import font
from turtle import color, width
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface: 
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()#Object                            # Self. yapinca O class'in bir property'si oluyor unutma!#
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        #TEXT LABEL
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR) #FG YI YAZ! COLOR 
        self.score_label.grid(row=0,column=1)
           
        #CANVAS
        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, 
            text= " Some Question Text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")
            ) # TEXT RENGI DEGISTIR
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)
        
        #BUTTON
          #TRUE 
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_command) #Highlightthickness yazinin ustundeki cizgileri siliyor.
        self.true_button.grid(row=2,column=0)
        
          #False
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_command) #Highlightthickness yazinin ustundeki cizgileri siliyor.
        self.false_button.grid(row=2,column=1)
        
        
        self.get_next_question()
        
        self.window.mainloop()#Runs the program.
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz. GG")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_command(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_command(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
        
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        