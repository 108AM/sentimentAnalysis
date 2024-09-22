from googleapiclient.discovery import build as builder
import csv

#the key which authorises me to access Youtube via the API
api_key = 'AIzaSyDsolWG02ro5RM0nrqv9i0vczfO_IMhXJM'
#creates a builder object
youtube = builder(
    'youtube', 'v3', developerKey = api_key
)

#the main function of interest; scrapes comments to a csv file based on the input argument 
def scrapeYoutubeComments(input, filename):
    
    #uses the .search() method of the builder object to return a dataframe of videos matching the parameters
    videoresponse = youtube.search().list(part="snippet", q=input, maxResults = 5).execute()

    #initialising a list to store the video ids
    ids = []

    videos = videoresponse.get("items")

    #iterates through the videos in the videoresponse dataframe and appends the video id to ids
    for item in videos:

        #the item is a compound dictionary data structure, which is unpacked using .get()
        if item.get('id').get('videoId') is not None:
            ids.append(item.get('id').get('videoId'))

    #initialising a list for comments which stores scraped comments from each video id
    comments = [] 

    #for each video id, a commentresponse object is created
    for id in ids:
        commentresponse0 = youtube.commentThreads().list(part = "snippet", videoId = id, maxResults = 5, textFormat="plainText")

        try:
            commentresponse = commentresponse0.execute()

            #comment is a compound dictionary. Unpacking it using .get() 4 times gives the desired comment text
            for comment in commentresponse['items']:

                #this appends only the desired comment text for each comment to the list
                comments.append(comment.get('snippet').get('topLevelComment').get('snippet').get('textDisplay'))

            #opens the csv in append mode
            with open(filename, 'a', newline='', encoding='utf-8') as file:

                #creates an object whose .writerow() method allows it to append text to the csv
                writer = csv.writer(file)

                for comment in comments:
                    writer.writerow([comment])

        #this exception will be raised if the video has comments disabled
        except:
            pass
