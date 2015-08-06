#!/usr/bin/env python3

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
    column = []
    for row in data :
        return(data)

def displayquery():
    print(Query())

displayquery()    
