from bs4 import BeautifulSoup
import csv
import requests
  
def scrapeTumblr(search_term, filename):

    #defines URL as the url for searching for the argument passed into function
    URL = f"https://www.tumblr.com/search/{search_term}"
    r = requests.get(URL)
    
    #p is a list of elements on the page with url of URL which is contained in <p> tags
    soup = BeautifulSoup(r.content, 'html5lib') 
    p = soup.find_all('p')

    #opens csv file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        try:
            #<p> text is appended to file provided its length is below 200 characters
            for i in p:
                if len(i.text) < 280 and len(i.text) > 50:
                    writer.writerow([i.text])

        except:
            pass
