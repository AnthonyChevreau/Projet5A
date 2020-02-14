# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!


import pyb, time

s1 = pyb.Servo(3)   # create a servo object on position P7
i = -10;



while(1):

     s1.angle(i)        # move servo 1 to 45 degrees
     time.sleep(10)
     i=i+1
     if i > 2000 :
        i=0
     print('i = ',i)


