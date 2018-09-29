# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:52:51 2018

@author: maxga
"""

import xml.etree.ElementTree as ET

# ENTRY CLASS
class Entry:
    
    def __init__(self):
        self.text = "None"  
        self.title = "None"
        self.type = "None"
        self.xmlUrl = "None"
        self.htmlUrl = "None"

feed = 'SubList.xml'
tree = ET.parse(feed)
root = tree.getroot()

count = 0
for a in root.iter('outline'):
    count += 1
    
print(count) 
entry_list = [Entry() for i in range(count)]

iter = 0
for a in root.iter('outline'):
    entry_list[iter] = a.attrib
    for b in a.attrib.keys():
        if b == "text":
            print(a.attrib["text"])
        if b == "type":
            print('     ', a.attrib["type"])
        if b == "xmlUrl":
            print('     ', a.attrib["xmlUrl"])
        if b == "htmlUrl":
            print('     ', a.attrib["htmlUrl"])
        #print(b)

    iter += 1