import tkinter as tk
from tkinter import *
from textscraper import *
from classifierprogram import *
from UIanalysisOutput import *

class SecondaryWindow(tk.Toplevel):

    alive = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Social Media Sentiment Analysis Results")
        self.minsize(800,400)

        #(following 5 functions): functionality for the buttons in secondary window
        def displaySentiment():
            resultsLabel.configure(text=sentimentAnalysis(sentiments))
            explanation.configure(text="Scale: -100 to 100. \nThe more positive the number, the more positive the sentiment. \nThe more negative the number, the more negative the sentiment.")

        def displayEmotion():
            resultsLabel.configure(text="This is the emotion")
            explanation.configure(text="This explains the emotion")

        def displayStrength():
            resultsLabel.configure(text=strengthAnalysis(prepredictions))
            explanation.configure(text="Scale: 0 to 100, larger the number, stronger the feeling")

        def displaySubjectivity():
            resultsLabel.configure(text="This is the subjectivity")
            explanation.configure(text="This explains the subjectivity")

        def displayKeywords():
            resultsLabel.configure(text="This is the keyword cloud")
            explanation.configure(text="This explains the keyword cloud")

        displaysentiment = Button(self, width=50, text="Sentiment", command=displaySentiment)
        displayemotion = Button(self, width=50, text="Emotion", command=displayEmotion)
        displaystrength = Button(self, width=50, text="Strength of sentiment", command=displayStrength)
        displaysubjectivity = Button(self, width=50, text="Subjectivity", command=displaySubjectivity)
        displaykeywords = Button(self, width=50, text="Keywords", command=displayKeywords)

        #only displays label if user chose it
        if analysesOptions[0] == 1:
            displaysentiment.grid(column=0,row=0)
        if analysesOptions[1] == 1:
            displayemotion.grid(column=0,row=1)
        if analysesOptions[2] == 1:
            displaystrength.grid(column=0,row=2)
        if analysesOptions[3] == 1:
            displaysubjectivity.grid(column=0,row=3)
        if analysesOptions[4] == 1:
            displaykeywords.grid(column=0,row=4)
        

        resultsLabel = Label(self, text="", width=50)
        resultsLabel.grid(column=1,row=5)

        explanation=Label(self, text="",width=50,pady=20)
        explanation.grid(column=0,row=6)

        self.back=Button(self,width=20,text="Back to Search",command=lambda:[self.destroy()])
        self.back.grid(column=1,row=6,pady=50)
        self.focus()
        
        self.__class__.alive = True

    def destroy(self):
        
        self.__class__.alive = False
        return super().destroy()


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Social Media Sentiment Analysis")
        self.searches = []
        self.sentiments = []
        self.prepredictions = []
        self.minsize(800,400)

        def runanalysis():
            success = False
            q1ans = [var1.get(), var2.get(),var3.get()]
            q2ans = [var4.get(),var5.get(), var6.get(), var7.get(), var8.get()]
            if 1 not in q1ans:
                errormessage.configure(text="Please tick at least one option for Question 1",fg="red")
            elif 1 not in q2ans:
                errormessage.configure(text="Please tick at least one option for Question 2",fg="red")
            elif len(searchterm.get())==0:
                errormessage.configure(text="Please enter a search query in the search box",fg="red")
            else:
                errormessage.configure(text="Successful input",fg="green")
                success = True
                self.searches = q1ans,q2ans,searchterm.get(),success
                return success

        searchlabel = Label(self, text = "Enter search terms", pady = 10)
        searchlabel.grid(column=1, row=0)

        advice1 = Label(self, text="Enter search terms in the search box", pady=20, padx = 3, fg="blue")
        advice1.grid(column=0, row=0)

        errormessage=Label(self,text="",width=50)
        errormessage.grid(column=0,row=8)

        advice2=Label(self, text="Tick at least one box for Social Media",pady=20, fg="blue")
        advice2.grid(column=0, row=1)

        advice3=Label(self,text="Tick at least one box for Analyses",pady=20,padx = 11, fg="blue")
        advice3.grid(column=0, row=2)

        searchterm=tk.StringVar()
        searchedterm = Entry(self, width=75, textvariable=searchterm)
        searchedterm.grid(column=1, row=1)

        question1=Label(self,text="(1) Which text would you like to analyse?",pady=30)
        question1.grid(column=0,row=3)

        var1=IntVar()
        Checkbutton(self,text="Youtube Comments", variable=var1).grid(column=0,row=4, sticky="w")
        var2=IntVar()
        Checkbutton(self,text="Tumblr Posts", variable=var2).grid(column=0,row=5, sticky="w")
        var3=IntVar()
        Checkbutton(self,text="Twitter Posts", variable=var3).grid(column=0,row=6, sticky="w")

        question1=Label(self,text="(2) What would you like information on?")
        question1.grid(column=1,row=3)

        var4=IntVar()
        Checkbutton(self,text="Sentiment", variable=var4).grid(column=1,row=4, sticky="w")
        var5=IntVar()
        Checkbutton(self,text="Emotion", variable=var5).grid(column=1,row=5,sticky="w")
        var6=IntVar()
        Checkbutton(self,text="Strength of sentiment", variable=var6).grid(column=1,row=6,sticky="w")
        var7=IntVar()
        Checkbutton(self,text="Subjectivity", variable=var7).grid(column=1,row=7,sticky="w")
        var8=IntVar()
        Checkbutton(self,text="Keywords", variable=var8).grid(column=1,row=8,sticky="w")

        self.run=Button(self, text="RUN ANALYSIS",command=lambda:[runanalysis(),self.open_secondary_window(runanalysis())])
        self.run.grid(column=1,row=2)

    def open_secondary_window(self, success):
        if not SecondaryWindow.alive and success:
            scraper0 = textScraper()
            scraper0.setsocials(self.searches[0])
            #makes the analyses options global
            global analysesOptions
            analysesOptions = self.searches[1]
            scraper0.setkeywords(self.searches[2])
            scraper0.setfilename("extractedtext.csv")
            #performs text scraping
            scraper0.refreshCSV()
            scraper0.extractText()
            scraper0.langToEn()
            scraper0.removeDuplicates()
            #creates feature matrix from extracted text
            Matrix = textToMatrix("selectedtrainingexamples.csv","extractedtext.csv")
            sentimentpredictions = predictSentiment(Matrix, "theta.csv")[0]
            strengthpredictions = predictSentiment(Matrix, "theta.csv")[1]
            global sentiments 
            sentiments = sentimentpredictions
            global prepredictions
            prepredictions = strengthpredictions
            self.secondary_window = SecondaryWindow()
            #prints simgoid and binary predictions
            print(sentimentpredictions, strengthpredictions)

main_window = MainWindow()
main_window.mainloop()
