import tkinter as tk
import getpass
import webbrowser
import random
def new():
    win = tk.Toplevel(window)
    win.config(bg="light sky blue")
    win.title("BasicBot")
    name = getpass.getuser()
    text = tk.Label(win, text=f"Hello {name}\nWelcome!!!\nI Can't Understand Your Language. So, You Have To Use Some Commands\nType /cmds For Listing Out The Commands", bg="khaki1", fg="black", width="60")
    text.pack(anchor='nw')

    def ifelse():
        if (entry.get() == '/developedby'):
            msg2 = tk.Label(win, text="/developedby", bg="spring green")
            msg2.pack(anchor='se')
            msg1 = tk.Label(win, text="Visit my Guru", bg="khaki1")
            msg1.pack(anchor='nw')
            web_page="https://www.linkedin.com/in/srikar-kailash-51b560107/"
            webbrowser.open_new(web_page)

        elif(entry.get()=='/cmds'):
            text = tk.Label(win,text="You can ask me the questions\nin the format of commands\n1. Ask /howiwasmade\n2. Ask /tkinter\n3. Ask /python\n"
                                     "4. Ask /mathsolve\n5. Ask /joke\n6. /developedby", bg="khaki1", fg="black")
            text1 = tk.Label(win, text="/cmds", bg="Spring Green", fg="black")
            text1.pack(anchor='se')
            text.pack(anchor='nw')

        elif(entry.get()=='/mathsolve'):
            text1 = tk.Label(win, text="/mathsolve", bg="Spring Green", fg="black")
            text1.pack(anchor='se')
            str = tk.Label(win, text="Hope You Are Enjoying/Enjoyed The Math Solver", bg="khaki1", fg='black')
            str.pack(anchor='nw')
            win2 = tk.Toplevel(window)
            win2.config(bg="light sky blue")
            win2.title("BasicBot(MathSolver)")
            win2.geometry("300x150")

            def eva():
                calc = round(eval(ent.get()), 2)
                result = tk.Label(win2, text=f"       Result is {calc}      ", bg="khaki")
                result.place(x=110,y=100)
            msg = tk.Label(win2, text="Enter A Mathematical Equation Here", bg="spring green")
            msg.pack()
            msg = tk.Label(win2, text="Like 2+3, 15*20+(12/2)%10 & ..... ", bg="spring green")
            msg.pack()
            ent = tk.Entry(win2, width="20", bg="azure4", fg="white")
            ent.pack()
            sol = tk.Button(win2, text="Solve", bg="khaki", command=eva)
            sol.pack()
            win2.mainloop()

        elif(entry.get()=='/howiwasmade'):
            text3 = tk.Label(win, text="/howiwasmade", bg="spring green", fg="black")
            text3.pack(anchor='se')

            text3 = tk.Label(win, text="I was built using python and tkinter. tkinter is a built-in module in python\nIt is used to develop "
                                      "Graphical User Interface(s)(GUIs).", bg="khaki1", fg="black")
            text3.pack(anchor='nw')

        elif(entry.get()=='/tkinter'):
            text3 = tk.Label(win, text="/tkinter", bg="spring green", fg="black")
            text3.pack(anchor='se')
            text4 = tk.Label(win, text="Good Question, I Was Built Using This GUI Only\ntkinter, a module in the Python standard library which serves as an interface to Tk, a simple toolkit.\n"
                                       "There are many other toolkits available, but they often vary across platforms.\n"
                                       "If you learn the basics of tkinter, you should see many similarities should you try to use a different toolkit.", bg="khaki1")
            text4.pack(anchor="nw")

        elif(entry.get()=='/joke'):
            inp = tk.Label(win, text="/joke", bg="spring green")
            inp.pack(anchor="se")
            jokes = ["According to my calculations the problem doesn't exist.",
                     "Any program that runs right is obsolete.",
                     "Any programming language is at its best before it is implemented and used.",
                     "Air conditioned environment - Do not open Windows!",
                     "A computer scientist is someone who fixes things that aren't broken.",
                     "A user friendly computer first requires a friendly user.",
                     "A paperless office has about as much chance as a paperless bathroom.",
                     "COFFEE.EXE Missing---Insert Cup and Press Any Key.",
                     "Beta. Software undergoes beta testing shortly before it's released. Beta is Latin for still doesn't work.",
                     "Computer Science: solving today's problems tomorrow.",
                     "Don't document the program; program the document.",
                     "Bug? That's not a bug, that's a feature."]
            rand_joke = random.choice(jokes)
            joke = tk.Label(win, text=rand_joke, bg="khaki1")
            joke.pack(anchor='nw')

        elif(entry.get()=='/python'):
            inp1 = tk.Label(win, text="/python", bg="spring green")
            inp1.pack(anchor="se")
            hello = tk.Label(win, text="Good Question. I Was Built Using this language.\nPython is created by Guido van Rossum in 1991. It is an Interpreted and High-"
                                       "Level Programming Language.\n Python has good code readability even without the comments. We can do lot of things with Python.\n"
                                       "We Can Create GUIs, Can Create Games, Create ML, AI & Data Science Algorithms, Can Design Web-Pages. \n"
                                       "We Can Also Create Computer Applications and Many More...........\nSo Explore It And Start Learning Python", bg="khaki1")
            hello.pack(anchor="nw")

        else:
            inp = tk.Label(win, text=entry.get(), bg="spring green")
            inp.pack(anchor="se")

            error = tk.Label(win, text="I Can't Understand. Please Use The Commands For Providing You The Information\n"
                                       "Use /cmds To Know The Commands", bg="#A4123F", fg="white")
            error.pack(anchor="nw")


    entry=tk.Entry(win, width="50", bg="azure4", fg="white")
    entry.pack()
    but=tk.Button(win,text="Ask", command=ifelse, bg="peach puff")
    but.pack()
    but2=tk.Button(win,text="NewWin", command=new, bg="peach puff")
    but2.pack()


window = tk.Tk()
window.title("Basic Bot")
window.config(bg="light sky blue")
text = tk.Label(text="Ready To Start The ChatBot??", font="40", bg="khaki")
text.pack(pady=50)

but = tk.Button(text="Start", command=new, bg="spring green")
but.pack(pady=10)

window.mainloop()