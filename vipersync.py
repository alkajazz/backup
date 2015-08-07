#!/usr/bin/env python2.7

###################################################################################
###################################################################################
#  Python Backup Utility that Schedules Rsync commands based on database entries. #
#                              Created By Nathan Booth                            #
#                               nathanbooth@gmail.com                             #
#                                                                                 #
#                                                                                 #
#       Make sure your database entries are inside {} for this to work right      #  
#                                                                                 #
#                          EXAMPLE: {/mnt/test /home/test}                        #
#                                                                                 #
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
    cursor.execute("select * from altigen")
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
    assign = cleanup()
    timestamp = time.strftime('%m-%d-%y-%I-%M-%S')
    filename = 'rsync.log'
    for i in assign:
        rcommand = 'rsync --progress %s' % (i)
        scom = subprocess.Popen(rcommand, shell=True).wait()
        if scom == 0:
            f = open(filename, 'a')
            f.write('\nBack up job successful at %s' % (timestamp))
            f.close()
        else:
            f = open(filename, 'a')
            f.write('\nback up failed at %s please check server to restart jobs' % (timestamp))
            f.close()
        return 0
    #return 0
        
#################
# main function #
#################

def main():
    assignment()

if __name__ == '__main__':
    main()
