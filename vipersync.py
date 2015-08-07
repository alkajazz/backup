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

###################################
# Database connection and queries #
###################################

def Query():
    db = MySQLdb.connect("localhost", "root", "testing1", "backup")
    cursor = db.cursor()
    cursor.execute("INSERT YOUR QUERY HERE")
    data = cursor.fetchall()
    for row in data :
        return(data)

######################################
# Clean up strings and create a list #
######################################

def cleanup():
    cleaner = Query()
    rx = re.findall(r'(?<={)([^}]+)', str(cleaner))
    return rx

###################################################################
# Assign list to rsync commands and launch them one after another #
###################################################################

def assignment():
    #rcommand = 'rsync --progress %s' % (i)
    assign = cleanup()
    for i in assign:
        rcommand = 'rsync --progress %s' % (i)
        subprocess.Popen(rcommand, shell=True).wait()
    return 0
        
#################
# main function #
#################

def main():
    assignment()

if __name__ == '__main__':
    main()
