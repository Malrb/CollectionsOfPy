import os

hostname = "localhost" #example
response = os.system("ping -n 1 " + hostname)
#If OS System is Linux , just use -c param
# use -w (deadline) : 1 ,hold time will decrease
#and then check the response...
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')
