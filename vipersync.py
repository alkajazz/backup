#!/usr/bin/env python2.7

###################################################################################
###################################################################################
#  Python Backup Utility that Schedules Rsync commands based on database entries. #
###################################################################################
###################################################################################

import os
import MySQLdb
import time
import re
import subprocess

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
    return rx

def assignment():
    #rcommand = 'rsync --progress %s' % (i)
    assign = cleanup()
    for i in assign:
        rcommand = 'rsync --progress %s' % (i)
        subprocess.Popen(rcommand, shell=True).wait()
    return 0
        



def displayquery():
    assignment()

displayquery()
