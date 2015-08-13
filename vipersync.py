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

import os, errno
import MySQLdb
import time
import re
import subprocess
import datetime

###########
# Globals #
###########

backuproot ='/home/backups/'
hostnames = ['mnt/mybox/nbooth/Desktop/fileserver1', 'mnt/mybox/nbooth/Desktop/fileserver2', 'fart/fileserver3', 'test2', 'test3', 'test4']
''' 0-6 monday-sunday '''
timetrack = datetime.datetime.today().weekday()
########################################
# Create destination from server input #
########################################

def time():
    
    f = open("paritytracker.txt", "r+")
    parity = f.read()

    if parity == timetrack:
        pass
    elif timetrack == 5:
        print timetrack + -5
    elif timetrack == 6:
        print timetrack + -5
    else:
        f = open("paritytracker.txt", "w")
        f.write(str(timetrack + 1))
        f.close()

def CreateDest(hostnames):
    
    days = ['Monday/', 'Tuesday/', 'Wednesday/', 'Thursday/', 'Friday/', 'Saturday/', 'Sunday/']
    my_new_list = [ backuproot + days[timetrack] + x for x in hostnames]
    return my_new_list

def CheckExist(dirname):
     
    print dirname
    try:
        for i in dirname:
            os.makedirs(i)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise Exception('Error!')


#hostname = dict(zip(hostnames, my_new_list))
#    return hostname


###################################
# Database connection and queries #
###################################

def Query():
    #db = MySQLdb.connect("localhost", "root", "testing1", "backup")
    #cursor = db.cursor()
    #cursor.execute("select * from altigen")
    #data = cursor.fetchall()
    #for row in data :
    #    return(data)
    source = '{/mnt/mybox/nbooth/Desktop/fileserver1}'

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
    filename = '/mnt/mybox/nbooth/Desktop/rsync.log'
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
    
    time()
    
    #DayTrack(backuproot)

    #CheckExist(CreateDest(hostnames))
    
    #assignment()

if __name__ == '__main__':
    main()
