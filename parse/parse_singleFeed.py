# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 21:50:51 2018

@author: maxga
"""
import xml.etree.ElementTree as ET
import sqlite3
import urllib
import datetime

# ENTRY CLASS
class Entry:
    
    def __init__(self):
        self.title = "None"  
        self.author = "None"
        self.pubDate = "None"
        self.source = "None"
        self.link = "None"
        self.description = "None"
        
        
class Source:
    
    def __init__(self):
        self.name = "None"
        self.xml_url = "None"
        self.language = "None"
        

# STEP 1: PARSE FEED
xml_url = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
feed = urllib.request.urlopen(xml_url)
tree = ET.parse(feed)
root = tree.getroot()

SourceName = root[0][0].text
entry_list = [ Entry() for i in range(len(root[0]))]

# STEP 2: CLEAN DATA
indexA = 0
for xml_entry in root[0]:
    if xml_entry.tag == "item":

        # For each PARAM of ENTRY
        indexB = 0
        for entry_param in xml_entry:
            if indexA == 8:
                print(entry_param.tag)
                print('     ', entry_param.text)

            # Title
            if entry_param.tag == "title":
                entry_list[indexA].title  = entry_param.text
            # Link
            if entry_param.tag == "link":
                entry_list[indexA].link = entry_param.text
            # pubDate
            if entry_param.tag == "pubDate":
                entry_list[indexA].pubDate = entry_param.text
            # description
            if entry_param.tag == "description":
                entry_list[indexA].description = entry_param.text
            # Author
            if "creator" in entry_param.tag:
                entry_list[indexA].author = entry_param.text
            # Source
            entry_list[indexA].source = SourceName
    indexA += 1
                
    
    
# STEP 3: ADD TO DATABASE
conn = sqlite3.connect('db1_test2.sqlite')
cur = conn.cursor()

for entry in entry_list:
    
    # add new ITEM
    cur.execute('''SELECT * FROM items WHERE title=?''', (entry.title,))
    if len(cur.fetchall()) == 0:
        cur.execute('''INSERT INTO Items 
            (title, link, desc, date) 
            VALUES(?, ?, ?, ?)''',
            (entry.title, entry.link, entry.description, entry.pubDate))
        print('New Entry!')
        print('     ', entry.title)
        
    # Add new SOURCE
    cur.execute('''SELECT * FROM Sources WHERE name=?''', (SourceName,))
    if len(cur.fetchall()) == 0:
        cur.execute('''INSERT INTO Sources 
            (name, feedURL, lastUpdate) 
            VALUES(?, ?, ?)''',
            (SourceName, xml_url, datetime.datetime.now(),))
        print('New Source!')
        print('     ', entry.SourceName)
        
    # Add new AUTHOR
    cur.execute('''SELECT * FROM Authors WHERE name=?''', (entry.author,))
    if len(cur.fetchall()) == 0:
        cur.execute('''INSERT INTO Authors 
            (name)
            VALUES(?)''',
            (entry.author,))
        print('New Author!')
        print('     ', entry.author)


conn.commit()
cur.close()
print("\nDONE!")
