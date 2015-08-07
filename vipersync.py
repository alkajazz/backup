#!/usr/bin/env python2.7

###################################################################################
###################################################################################
#  Python Backup Utility that Schedules Rsync commands based on database entries. #
###################################################################################
###################################################################################

import os
import MySQLdb
import time
import getpass
import configparser
import re

#db = MySQLdb.connect("localhost", "root", "testing1", "backup" )

#cursor = db.cursor()

#cursor.execute("SELECT * from altigen")

#data = cursor.fetchall()

#for row in data :
#    return(row [0], row[1])


#db.close()

###################################
# Database connection and queries #
###################################

def Query():
    db = MySQLdb.connect("localhost", "root", "testing1", "backup")
    cursor = db.cursor()
    cursor.execute("SELECT * from altigen union all select * from crystal union all select * from equipment union all select * from etisql")
    data = cursor.fetchall()
    for row in data :
        return(data)

def cleanup():
    cleaner = Query()
    rx = re.findall(r'(?<={)([^}]+)', str(cleaner))
    for row in rx :
        return(rx)

def assignment():
    assign = cleanup()
    print assign





def displayquery():
    print(cleanup())

displayquery()
