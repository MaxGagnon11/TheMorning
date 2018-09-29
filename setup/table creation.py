# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:25:15 2018

@author: maxga

Need table to keep track of the xml locations and their source information
"""

import sqlite3

# Open Database
conn = sqlite3.connect('db1_test2.sqlite')
cur = conn.cursor()



# Create Table for the source information
# This
cur.execute('DROP TABLE IF EXISTS Sources')
cur.execute('''CREATE TABLE Sources
	(name TEXT, homePage TEXT, feedURL TEXT, lastUpdate TEXT)''')



# Create Table for the author  information
# This
cur.execute('DROP TABLE IF EXISTS Authors')
cur.execute('''CREATE TABLE Authors
	(name TEXT)''')




conn.commit()
cur.close()