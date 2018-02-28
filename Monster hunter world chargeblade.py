# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:25:21 2018

@author: billy
"""
#basic imports to run bs4
import bs4
from bs4 import BeautifulSoup as soup
import requests

"""Goal for this program was to scrape informatoin of kiranico for 
monster hutner world weapons
really basic stuff using bs4 ( Beautiful soup 4) and python
just for fun and practice!"""

#gets the html adress
html_Adress = requests.get("https://mhworld.kiranico.com/charge-blade")

page_soup = soup(html_Adress.content,"html.parser")

title = page_soup.h1.text

filename = "chargebladekira.csv"
f = open(filename,"w")
headers = "Weapon Name, Attack, True Attack, Special ,Rarity ,Gem1,Gem2,Gem3 \n"

f.write(title +"\n")
f.write(headers)

#i looked though the soup and found the data i wanted was in the table hence calling tr
containersmh = page_soup.findAll("tr")

""" initally I ran a in function for containers(for container in containers:)
discorvered the top tr was bad to use as it was the table heading etc
decided to use the range function with the length o the list instead
thinking i can also just get rid of that data with soup but i decided just to ignore it
or skip it instead
"""
for i in range(1,len(containersmh)):
    containermh = containersmh[i]
    
    try:
        weaponName = containermh.a.text
    except:
        weaponName = "n/a"
 
    
    attackVal = containermh.findAll("td",{"class":"text-center align-middle"})[0].text
    
    trueAttackVal = containermh.findAll("td",{"class":"text-center align-middle text-muted"})[0].text
    
    weaponSpecial = containermh.small.text.replace(" ","").replace("\n"," ").strip()
    
    weaponRarity = containermh.findAll("td",{"class":"text-center align-middle"})[4].text.strip()
    
    gemContainers = containermh.findAll("i")
    
    """ had a issue getting gems off the page in a proper order used a dictonary
    with gem final and used range instead of container in containers again
    seems to work better with what I do most abstract"""
    gemFinal = {}
    for x in range(len(gemContainers)):
        
        gemContainer = gemContainers[x]
    
        gemSlot = gemContainer["class"][1]
        if gemSlot == "zmdi-n-3-square":
            gemFinal[x] = "3 slot"
            
        elif gemSlot == "zmdi-n-2-square":
            gemFinal[x] = "2 slot"
         
        elif gemSlot == "zmdi-n-1-square":
            gemFinal[x] = "1 slot"
        
        else:
            gemFinal[x] = "no slot"
            
    gemSlot1 = gemFinal[0]
    gemSlot2 = gemFinal[1]
    gemSlot3 = gemFinal[2]
        
    print(weaponName)        
    print(attackVal)
    print(trueAttackVal)    
    print(weaponSpecial)
    print(weaponRarity)
    print(gemSlot1)
    print(gemSlot2)
    print(gemSlot3)
    
    f.write(weaponName + ","+ attackVal+ "," + trueAttackVal + ","+weaponSpecial +","+ weaponRarity +","+ gemSlot1 + ","+ gemSlot2 +"," + gemSlot3 +"\n")

f.close()    