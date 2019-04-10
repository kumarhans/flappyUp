import serial


ser = serial.Serial('/dev/ttyACM0')

ser.baudrate = 9600

def isfloat(value):
  try:
    int(value)
    return True
  except ValueError:
    return False


#x = (ser.readline()).strip()   # read one byte
while True:
	x = ser.readline().strip()
	if isfloat(x):
		print(int(x))

