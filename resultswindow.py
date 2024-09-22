import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("Social Media Sentiment Analysis Results")
window.minsize(800,400)

def displaySentiment():
    resultsLabel.configure(text="This is the sentiment")
    explanation.configure(text="This explains the sentiment")

def displayEmotion():
    resultsLabel.configure(text="This is the emotion")
    explanation.configure(text="This explains the emotion")

def displayStrength():
    resultsLabel.configure(text="This is the strength of feeling")
    explanation.configure(text="This explains the strength of feeling")

def displaySubjectivity():
    resultsLabel.configure(text="This is the subjectivity")
    explanation.configure(text="This explains the subjectivity")

def displayKeywords():
    resultsLabel.configure(text="This is the keyword cloud")
    explanation.configure(text="This explains the keyword cloud")

def backToSearch():
    pass

displaysentiment = Button(window, width=50, text="Sentiment", command=displaySentiment)
displaysentiment.grid(column=0,row=0)
displayemotion = Button(window, width=50, text="Emotion", command=displayEmotion)
displayemotion.grid(column=0,row=1)
displaystrength = Button(window, width=50, text="Strength of sentiment", command=displayStrength)
displaystrength.grid(column=0,row=2)
displaysubjectivity = Button(window, width=50, text="Subjectivity", command=displaySubjectivity)
displaysubjectivity.grid(column=0,row=3)
displaykeywords = Button(window, width=50, text="Keywords", command=displayKeywords)
displaykeywords.grid(column=0,row=4)

resultsLabel = Label(window, text="", width=50)
resultsLabel.grid(column=1,row=5)

explanation=Label(window, text="",width=50,pady=20)
explanation.grid(column=0,row=6)

back=Button(window,width=20,text="Back to Search",command=backToSearch)
back.grid(column=1,row=6,pady=50)

window.mainloop()
