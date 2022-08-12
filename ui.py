from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self, quiz_brain: QuizBrain ):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)


        self.false_image = PhotoImage(file="images/false.png")
        self.true_image = PhotoImage(file="images/true.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0, width=100, command=quiz_brain.answer_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_image, highlightthickness=0, width=100, command=quiz_brain.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)


