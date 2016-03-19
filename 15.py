#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/return/uzi.html
import datetime
for i in xrange(1006,1996,10):
    d = datetime.date(i,1,26)
    if d.weekday() == 0 and i%4 == 0:
        print d

print  "the second most recent date of our list :","1756-01-26"
print  "The next day is 1756-01-27 , which is the birthdate of Mozart"

