import time

# #specifies the number of seconds to zero, start of epoch. gmtime always works in UTC
# print(time.gmtime(0))
# #also a tuple
# print(time.localtime())
# #printed out number of seconds since start of epoch
# print(time.time())
#
# time_here = time.localtime()
# #print(time_here)
# print("Year:", time_here[0], time_here.tm_year)

from time import time as my_timer
import random
input("press enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

print("started at" + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))

#from time import perf_counter as timer
#from time import monotonic as timer
#perf counter is most precise clock. most useful for benchmarking code.
# its used as a trace to get performance of functions.
#monotonic similar to perf_counter. monotonic means times cant go backwards.
#the two have allowed us to calculate elapsed time.
#processed_time returns the time taken by CPU to process the code.

#to deal with realtimes rather than measuring durations, use time function.

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t\t\t", time.get_clock_info('perf_counter'))
print("monotonic():\t\t\t", time.get_clock_info('monotonic'))
print("process_time():\t\t\t", time.get_clock_info('process_counter'))
