#!/usr/bin/env python2.7
# coding=utf-8 
#################################################################################
#################################################################################
#                    		VIPERSYNC                                       #
#                    	  nathanbooth@gmail.com                                 #
# 	                                                                        #
#	     This tool creates incremental snapshots using rsync                #
#                      Created By: Nathan Booth 2015                            #
#                                                                               #
#################################################################################
#################################################################################
#coding: utf-8
import os, errno
import time
import re
import subprocess
import datetime
from datetime import timedelta

###########
# Globals #
###########

backuproot ='/Users/nathanbooth/backups'
hostnames = ['/Users/nathanbooth/backup1', '/Users/nathanbooth/backup2', '/Users/nathanbooth/backup3']

########################################
# Create destination from server input #
########################################

def CreateDest(hostnames):
    #Read input from hostnames and create list of destinations based on backup root
    today = datetime.datetime.now()
    my_new_list = [backuproot + today.strftime("/%m%Y") + today.strftime("/%d") + x for x in hostnames]
    return my_new_list

def CheckExist(dirname):
    #Check to make sure destinations exsist before syncing if not create them if they do except silent error and continue making dirs
    try:
        for i in dirname:
            os.makedirs(i)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise Exception('Error!')

def CreateDict():
    # Create dictionary that pairs up source with destination
    hostname = dict(zip(hostnames, CreateDest(hostnames)))
    return hostname

###################################################################
# Assign list to rsync commands and launch them one after another #
###################################################################

def assignment():
                          # Master key = the day you first runt the program. This will be out full back up day that happens once a month. 
    master = '13'
    t = datetime.datetime.now()
    assign = CreateDict()
    #Run our dir creation function
    CheckExist(CreateDest(hostnames))
    # if day = master then run full backup rsync command
    if t.strftime("%d") == str(1):
	for k, v in assign.items():
	    rcommand = 'rsync -aH --progress %s %s' % (k, v)
	    #rcommand = re.sub(r'[^/]*$', ' ', rcommand)
	    scom = subprocess.Popen(rcommand, shell=True).wait()
	    print rcommand
    else:
	                             # if day doesn't equal master do incremental
	for k, v in assign.items():
	    rcommand = 'rsync -a --delete --log-file=[test] --link-dest=%s/%s/%s %s %s' % (backuproot, t.strftime("%m%Y"), master, k, v)
            #rcommand = re.sub(r'([^/]*/[^/]*)$', '%s' % t.strftime("%d"), rcommand)
	    rcommand = re.sub(r'[^/]*$', ' ', rcommand)
	    #rcommand = re.sub(r'([^/]*/[^/]*)$', '%s' % t.strftime("%d"), rcommand)
            scom = subprocess.Popen(rcommand, shell=True).wait()
    return 0
       
#################
# main function #
#################

def main():
    #print assignment()
    #print IncSource()
    assignment()
    #print IncDict()
    #print CreateDest(hostnames)

if __name__ == '__main__':
   main()
