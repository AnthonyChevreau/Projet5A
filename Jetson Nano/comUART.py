import time
import serial

serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

def recievefromOpenMV():
	try:

	   	 while True:
	        	if serial_port.inWaiting() > 0:
	        	    data = serial_port.read()
	        	    print(data)	
	except Exception as exception_error:
		print("Error occurred. Exiting Program")
		print("Error: " + str(exception_error))

	finally:
		pass

def sendtoOpenMV(code):
	try:
		serial_port.write(code.encode())

       
	except Exception as exception_error:
		print("Error occurred. Exiting Program")
		print("Error: " + str(exception_error))

	finally:
		pass



