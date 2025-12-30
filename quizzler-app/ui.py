from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #score label
        self.score_label = Label(text=f"Score: 0", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        #canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quiz_txt = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="This is a question?", fill="black", 
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=35)        

        #buttons
        #----------Buttons
        right_mark_img = PhotoImage(file="images/true.png")
        cross_mark_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=right_mark_img, command=self.check_true)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=cross_mark_img, command=self.check_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.score_label.config(text=f"Score: {self.quiz.score}")
            ques_text =self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_txt, text=ques_text)
        else:
            self.canvas.itemconfig(self.quiz_txt, text="You have completed all the questions.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def check_true(self):
        is_right =self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):       
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
