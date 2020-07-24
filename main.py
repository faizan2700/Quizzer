import tkinter as tk

def show_question(n:int) -> None:
    if(n == len(l)):
        print('done')
    else:
        l[n].tkraise()

class Question(tk.Frame):
    def __init__(self, *args,Question = None, Answer = None, num = None, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.Question = Question
        self.Answer = Answer
        self.num = num

        
        self.label = tk.Label(self, text = Question)
        self.label.pack(side = 'top', fill = 'x')

        self.entry = tk.Entry(self)
        self.entry.bind('<Return>', self.Enter)
        self.entry.pack()
        
        self.button = tk.Button(self, text = 'Submit', command = self.submit)
        self.button.pack()
        
    def submit(self):
        s = self.entry.get()
        if(s == self.Answer):
            print('next')
            show_question(self.num + 1)
        else:
            print('try again')
    
    def Enter(self, event):
        self.submit()

if __name__ == '__main__':
    def go_second():
        f1.tkraise()
    def go_first():
        f2.tkraise()

    def first_q():
        show_question(0)

    W = 500
    H = 500
    s = str(W) + 'x' + str(H)
    app = tk.Tk()
    app.title('Quizzzer')
    app.geometry(s)
    app.resizable(False, False)



    welcome = tk.Frame(app)
    welcome.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    label = tk.Label(welcome, text = 'Welcome to Quizzes by faizan', bg = '#CCCCCC')
    label.place(relx = 0.5, rely = 0.5, anchor = 'center')

    button = tk.Button(welcome, text = 'Get Started', command = first_q)
    button.pack(side = tk.BOTTOM)

    q = [('Question1', 'Answer1'),
         ('Question2', 'Answer2'),
         ('Question3', 'Answer3'),
         ('Question4', 'Answer4'),
         ('Question5', 'Answer5')
         ]

    global l
    l = []
    for i in range(len(q)):
        f = Question(app,Question = q[i][0], Answer = q[i][1], num = i)
        f.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        l.append(f)

    
    end = tk.Frame(app)
    end.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    label = tk.Label(end, text = 'Congratulations You have completed the ultimate quest\n made by legendary witches and wizards', bd = 30)
    label.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

    button = tk.Button(end, text = 'Celebrate!!!', command = app.quit)
    button.pack(side = tk.BOTTOM)
    
    l.append(end)
    
    end.tkraise()
    app.mainloop()
        

    
'''
    f1 = tk.Frame(app)
    f2 = tk.Frame(app)

    b1 = tk.Button(f1, text = 'first page', command = go_first)
    l1 = tk.Label(f1, text = 'Second Page')
    l1.pack()
    b1.pack()

    b2 = tk.Button(f2, text = 'second page', command = go_second)
    l2 = tk.Label(f2, text = 'First Page')
    l2.pack()
    b2.pack()

    f1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    f2.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)


    f3 = Question(app, Question = 'Question1')
    f3.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
'''
