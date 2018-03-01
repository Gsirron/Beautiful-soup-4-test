# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:31:45 2018

@author: billy
"""
"""
version 2.0
Reddit bot for qidanunderground warning when a new chapter of RTW is out
ATM all this does is search a subreddit for a string and stores that url relevent in
the dictonary title.

added storage so it doesnt need to redefine a ditonary each time looks for the file "RTW_TITLES_DICT.txt"
if not it writes a file

cleaned up alot of redundent code and fluff
mainly the checking for a new chapter function and opening it


"""
import praw
import re
import datetime
import time
import webbrowser as wb
import os
import json

def sub_info():
    
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print(submission.url)   
    print(datetime.datetime.fromtimestamp(
    int(submission.created)).strftime('%Y-%m-%d %H:%M:%S'))            
    print("---------------------------------\n")

#just function pretty much looks for a value which you can define need to make more abstract
def searchSub(value,limitVal,mem):#value is search term in title as a string, limit is how far you wana search
    for submission in subreddit.hot(limit=(limitVal)):
        
        a = submission.title  #i wanted my diconary key in numbers only this removes everything but the numbers
        clen = re.sub('[^0-9]','', a) 
        
        if clen in mem: #returns from memory so program isnt searching reddit allt he time if its already stored
            #print("from mem") was just a test to see if it was working properly
            print("No new chapters matching search = "+ value)
            return mem[clen]
        
        
        elif value in submission.title:
            #the print is all optional i liked to see what chapters etc
            sub_info()
            
            mem[clen] = submission.url
            with open("RTW_TITLES_DICT.txt","a") as f:
                f.write(str(mem) +"\n")
                d=[]
                for keys in mem.keys():# my method of finding the newest chapter aka highest value , I pretty much convert the dict keys into a list, sort it then return the higehst value
                    d.append(keys)
                    d.sort
                    if d[0]>d[len(d)-1]:#checks the new list which is the higher number, made an assumption that the key values will be acending
                        newURL = title[d[0]]
                
                    else:
                        newURL = title[d[len(d)-1]]
                print("new chatper")
                wb.open(newURL)
            
def get_saved_titles(): #function to see if the text file for the array is presnet in directory
    if not os.path.isfile("RTW_TITLES_DICT.txt"):# 
        title = {} #returns empty ditronary
    else:
        with open("RTW_TITLES_DICT.txt","r") as f: #if file with the name is found it, Proceeds to clean the file and convert from a string to dic with JSON
             titlebad = f.read().strip()
             jsonformattitle = titlebad.replace("'", "\"")
             title = json.loads(jsonformattitle)
             
             
    return title    
        
            


#
title = get_saved_titles()
# links to my praw.ini
reddit = praw.Reddit("bot1")
# the subreddit you wana use in this case qidianunderground
subreddit = reddit.subreddit("QidianUnderground")
#examples of this search
for i in range(2): # just the duration of program and how long you need to run in need to make it into a function
    print("loop ",i+1)# shows the current loop
    
    print("searching sub")# just to tell that the program is running
    searchSub("Release That Witch",20,title) 
    searchSub("RTW",20,title)
    print("sleeping for 10 seconds")    # just a timer so that program isnt spamming all the time
    time.sleep(10)
    
    
"""    
    if len(title) > len(ititle): # does a test to see if a new chapter is up in the case if the program is always running, If a new chapter is out it will open it in the web page
        d=[]
        for keys in title.keys():# chose this method as I'm too dumb to figure out a better method
            # pretty much converts all the ditonarys keys in title into a list, and sorts them
            
            d.append(keys)
            d.sort()
            
            if d[0]>d[len(d)-1]:#checks the new list which is the higher number, made an assumption that the key values will be acending
                
                newURL = title[d[0]]
                
            else:
                newURL = title[d[len(d)-1]]
                
        ititle = title
        
        print("new chatper")
        wb.open(newURL)
    elif len(title) == len(ititle): # tell the user that there is no new chapter
        print("no new chapter")
 
    


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
    
    
        
      
