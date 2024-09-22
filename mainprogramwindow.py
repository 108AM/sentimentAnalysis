import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("Social Media Sentiment Analysis")
window.minsize(800,400)

def runanalysis():
    q1ans = [var1.get(), var2.get(),var3.get()]
    q2ans = [var4.get(),var5.get(), var6.get(), var7.get(), var8.get()]
    if 1 not in q1ans:
        errormessage.configure(text="Please tick at least option for Question 1")
    elif 1 not in q2ans:
        errormessage.configure(text="Please tick at least option for Question 2")
    elif len(searchterm.get())==0:
        errormessage.configure(text="Please enter a search query in the search box")
    else:
        errormessage.configure(text="Successful input")
        return q1ans,q2ans,searchterm.get()

searchlabel = Label(window, text = "Enter search terms", pady = 10)
searchlabel.grid(column=1, row=0)

advice1 = Label(window, text="Enter search terms in the search box", pady=20, padx = 3)
advice1.grid(column=0, row=0)

errormessage=Label(window,text="",width=50)
errormessage.grid(column=0,row=8)

advice2=Label(window, text="Tick at least one box for Social Media",pady=10)
advice2.grid(column=0, row=1)

advice3=Label(window,text="Tick at least one box for Analyses",pady=10,padx = 11)
advice3.grid(column=0, row=2)

searchterm=tk.StringVar()
searchedterm = Entry(window, width=75, textvariable=searchterm)
searchedterm.grid(column=1, row=1)

run=Button(window, text="RUN ANALYSIS",command=runanalysis, bg="#20FF50")
run.grid(column=1,row=2)

question1=Label(window,text="(1) Which text would you like to analyse?",pady=25)
question1.grid(column=0,row=3)

var1=IntVar()
Checkbutton(window,text="Youtube Comments", variable=var1).grid(column=0,row=4, sticky="w")
var2=IntVar()
Checkbutton(window,text="Tumblr Posts", variable=var2).grid(column=0,row=5, sticky="w")
var3=IntVar()
Checkbutton(window,text="Twitter Posts", variable=var3).grid(column=0,row=6, sticky="w")

question1=Label(window,text="(2) What would you like information on?")
question1.grid(column=1,row=3)

var4=IntVar()
Checkbutton(window,text="Sentiment", variable=var4).grid(column=1,row=4, sticky="w")
var5=IntVar()
Checkbutton(window,text="Emotion", variable=var5).grid(column=1,row=5,sticky="w")
var6=IntVar()
Checkbutton(window,text="Strength of sentiment", variable=var6).grid(column=1,row=6,sticky="w")
var7=IntVar()
Checkbutton(window,text="Subjectivity", variable=var7).grid(column=1,row=7,sticky="w")
var8=IntVar()
Checkbutton(window,text="Keywords", variable=var8).grid(column=1,row=8,sticky="w")

window.mainloop()