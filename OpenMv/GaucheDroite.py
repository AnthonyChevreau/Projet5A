# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!


import pyb, time

s1 = pyb.Servo(3)   # create a servo object on position P7
i = 0;



while(1):

    s1.angle(-10)        # move servo 1 to 45 degrees
    time.sleep(2000)

    s1.angle(70)        # move servo 1 to 45 degrees
    time.sleep(2000)

    s1.angle(30)        # move servo 1 to 45 degrees
    time.sleep(2000)



