import apiinteractortumblr as tu
import apiinteractortwitter as tw
import apiinteractoryoutube as yt
import languagedetection as ld
import duplicationremoval as dr
import csv

class textScraper:

    def __init__(self):
        self.socials = []
        self.keywords = ""
        self.filename = ""

    def setsocials(self, socials):
        self.socials = socials

    def setkeywords(self, keywords):
        self.keywords = keywords

    def setfilename(self, filename):
        self.filename = filename

    def extractText(self):
        if self.socials[0] == 1:
            yt.scrapeYoutubeComments(self.keywords, self.filename)
        if self.socials[1] == 1:
            tu.scrapeTumblr(self.keywords, self.filename)
        if self.socials[2] == 1:
            tw.scrapeTweets(self.keywords, self.filename)

    def refreshCSV(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            #gets rid of all rows
            file.truncate()

    def readCSV(self):
        #initialises list of text strings
        all_text = []
        #opens input file with utf8 encoding
        with open(self.filename, "r+", encoding="utf8") as input_file:
            for row in csv.reader(input_file):
                #appends entire row (not comma separated) to all_text
                all_text.append(",".join(row))
        return all_text

    def langToEn(self):
        ld.onlyEnglishText(self.filename)

    def removeDuplicates(self):
        dr.removingDuplicates(self.filename)






        
        


