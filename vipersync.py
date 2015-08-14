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
import time
import re
import subprocess
import datetime

###########
# Globals #
###########

backuproot ='/Users/nathanbooth/backups'
hostnames = ['/Users/nathanbooth/backup1', '/Users/nathanbooth/backup2', '/Users/nathanbooth/backup3']
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
    #for i in hostnames:
    #	return
    today = datetime.datetime.now()
    days = ['/Monday', '/Tuesday', '/Wednesday', '/Thursday', '/Friday', 'Saturday', 'Sunday']
    my_new_list = [ backuproot + today.strftime("/%m%d%Y") + days[timetrack] + x for x in hostnames]
    return my_new_list

def CheckExist(dirname):
    try:
        for i in dirname:
            os.makedirs(i)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise Exception('Error!')

def CreateDict():
    hostname = dict(zip(hostnames, CreateDest(hostnames)))
    return hostname

###################################################################
# Assign list to rsync commands and launch them one after another #
###################################################################

#re.sub(r'[^/]*$', ' ')
def assignment():
    assign = CreateDict()
    CheckExist(CreateDest(hostnames))
    for k, v in assign.items():
        rcommand = 'rsync -r --progress %s %s' % (k, v)
        rcommand = re.sub(r'[^/]*$', ' ', rcommand)
	scom = subprocess.Popen(rcommand, shell=True).wait()
        #scom = subprocess.Popen(rcommand, shell=True).wait()
        #scom = subprocess.Popen(rcommand, shell=True).wait()
        #scom = subprocess.Popen(rcommand, shell=True).wait()        
        #if scom == 0:
        #    f = open(filename, 'a')
        #    f.write('\nBack up job successful at %s' % (timestamp))
        #    f.close()
        #else:
        #    f = open(filename, 'a')
        #    f.write('\nback up failed at %s please check server to restart jobs' % (timestamp))
        #    f.close()
        #return 0
    return 0
       
#################
# main function #
#################

def main():
    #print assignment()
    assignment()
    

if __name__ == '__main__':
   main()
