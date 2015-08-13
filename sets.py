#!/usr/bin/env python2.7

import os
import datetime

timetrack = datetime.datetime.today().weekday()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


print days[timetrack]
