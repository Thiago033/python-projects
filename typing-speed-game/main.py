from words import words
from tkinter import *
import random
from tkinter import messagebox


score=0
missed=0
  
time=60

def timer_function():
    global time, score, missed
        
    if time>0:
        time -=1
        timer_counter.configure(text=time)
        timer_counter.after(1000,timer_function)
    else:
        start_label.configure(text=f'Hit = {score} | Miss = {missed} | Total Score = {score - missed}')
        rr = messagebox.askretrycancel('Notification','Do you want to play again?')
        
        if rr == True:
            score=0
            missed=0
            time=60
            start_label.configure(text='Typing Speed Game')
            timer_counter.configure(text=time)
            word.configure(text=random.choice(words))
            score_counter.configure(text=score)
            word_entry.delete(0, END)


def game(event):
    global score, missed
    
    if time==60:
        timer_function()
    
    if word_entry.get() == word['text']:
        score +=1
        score_counter.configure(text=score)
    else:
        missed +=1
    
    word.configure(text=random.choice(words))
    
    word_entry.delete(0,END)

# Window Setup
window = Tk()
window.geometry('800x600')
window.title('Typing Speed Game')
window.config(bg="gray")

# ---------------------------- LABELS ------------------------------- #
start_label = Label(window, text='Typing Speed Game', font=('arial', 30, 'bold'), bg='gray', fg='black')
start_label.place(x=220, y=50)

score_label = Label(window, text='Score:', font=('arial', 25, 'bold'), bg='gray', fg='black')
score_label.place(x=70, y=180)
score_counter = Label(window, text=score, font=('arial', 25, 'bold'), bg='gray', fg='black')
score_counter.place(x=100, y=230)

time_left_label = Label(window, text='Time Left:', font=('arial', 25, 'bold'), bg='gray', fg='black')
time_left_label.place(x=580, y=180)
timer_counter = Label(window, text=time, font=('arial', 25, 'bold'), bg='gray',fg='black')
timer_counter.place(x=650, y=230)

word = Label(window, text=random.choice(words), font=('arial', 45, 'bold'),fg='green')
word.config(padx=10, pady=10)
word.place(x=290, y=300)

word_entry = Entry(window, font=('arial', 30, 'bold'), justify='center', bd=3)
word_entry.place(x=180, y=400)
word_entry.focus_set()

game_label = Label(window, text='Press "Enter" To type a word', font=('arial', 25, 'bold'), fg='black', bg='white')
game_label.config(padx=10, pady=10)
game_label.place(x=180, y=500)

#call game function when enter is pressed
window .bind('<Return>', game)

mainloop()
