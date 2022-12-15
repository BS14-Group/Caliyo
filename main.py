# Code for the main requests for things we want to monitor

#Uptime
import psutil
import time

print(psutil.cpu_times())

# physical cores of the cpu
print("The number of physical cores in the system is %s" % (psutil.cpu_count(logical=False),))

# logical cores of the cpu
print("The number of logical cores in the system is %s" % (psutil.cpu_count(logical=True),))

## Output current CPU load as a percentage
def get_cpu_usage_pct():
 """
 Obtains the system's average CPU load as measured over a period of 500 milliseconds.
 :returns: System CPU load as a percentage.
 :rtype: float
 """

 return psutil.cpu_percent(interval=0.5)

# Output current CPU load as a percentage.
while True:
    print('System CPU load is {} %'.format(get_cpu_usage_pct()))
    time.sleep(1)
