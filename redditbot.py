# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:31:45 2018

@author: billy
"""
"""
Reddit bot for qidanunderground warning when a new chapter of RTW is out
ATM all this does is search a subreddit for a string and stores that url relevent in
the dictonary title.

Plan to make this open up the url tired to the dictonary and automate it a bit more

"""
import praw
import re
import datetime
import time
import webbrowser as wb

#just function pretty much looks for a value which you can define need to make more abstract
def searchSub(value,limitVal,mem):#value is search term in title as a string, limit is how far you wana search
    for submission in subreddit.hot(limit=(limitVal)):
        
        a = submission.title  
        clen = re.sub('[^0-9]','', a) 
        
        if clen in mem:
            #print("from mem")
            return mem[clen]
        
        elif value in submission.title:
            
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print(submission.url)
            
            print(datetime.datetime.fromtimestamp(
            int(submission.created)).strftime('%Y-%m-%d %H:%M:%S'))            
            print("---------------------------------\n")
            #i wanted my diconary key in numbers only this removes everything but the numbers
            mem[clen] = submission.url
            
   
            
# links to my praw.ini

#emptylist
title = {}
ititle = {}
reddit = praw.Reddit("bot1")
# the subreddit you wana use in this case qidianunderground
subreddit = reddit.subreddit("QidianUnderground")
#examples of this search
for i in range(2):
    print("loop ",i)
    
    print("searching sub")
    searchSub("Release That Witch",20,title)
    searchSub("RTW",20,title)
       
    if len(title) > len(ititle):
        d=[]
        for keys in title.keys():
            d.append(keys)
            d.sort()
            if d[0]>d[len(d)-1]:
                newURL = title[d[0]]
                
            else:
                newURL = title[d[len(d)-1]]
                
        ititle = title
        
        print("new chatper")
        wb.open(newURL)
    elif len(title) == len(ititle):
        print("no new chapter")
        
    print("sleeping for 10 seconds")    
    time.sleep(10)
    



"""    
    


for submission in subreddit.hot(limit=20):
    if "Release That Witch" in submission.title:
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print(submission.url)
        print(submission.visited)
        print("---------------------------------\n")
        
        title[submission.title] = submission.url
    if "RTW" in submission.title:
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print(submission.url)
        print(submission.visited)
        print("---------------------------------\n")
        
        title[submission.title] = submission.url
        
"""        
    
    
        
      
