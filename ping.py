import serial
import httplib

ser = serial.Serial('/dev/ttyACM2')
ser.baudrate = 9600
distance = ''
while True:
	ch = ser.read(1)
	if ch == '\n':
		print distance
		conn = httplib.HTTPConnection('184.106.153.149')
		conn.request("GET","https://api.thingspeak.com/update?api_key=P80UYHN4H4W0CFMO&field1=%s\n" %(distance))
		res = conn.getresponse()
		print res.status, res.reason
		conn.close()
		distance = ''
	else:
		distance += ch
