#!/usr/bin/env python2.7

import os

list1 = list(['dog', 'mouse', 'cat'])

set1 = set(['dog', 'cat', 'mouse', 'monkey'])
set2 = set(['dog', 'monkey', 'mouse'])

matched =  list(set1.intersection(set2))


backup= "/mnt/"
path = "/home/backups"

def listdirs(folder):
    return set([
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ])

print listdirs(path)    
