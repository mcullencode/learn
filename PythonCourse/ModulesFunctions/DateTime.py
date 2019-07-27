import time
print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\t Daylight Saving Time is in effect for this location")
    print("\t The DST timezone is " + time.tzname[1])

print("Local time is" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

#datetime module and datetime class so import it via

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
