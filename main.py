# Code for the main requests for things we want to monitor

#Uptime
import psutil

print(psutil.cpu_times())

# physical cores of the cpu
print("The number of physical cores in the system is %s" % (psutil.cpu_count(logical=False),))

# logical cores of the cpu
print("The number of logical cores in the system is %s" % (psutil.cpu_count(logical=True),))