import sys, os

try: 
	val = sys.argv[1]
except:
	print("A value must be passed as argument, format is: python "+ os.path.basename(__file__) + "15")
	exit()
print("The value " + val + " in hexadecimal is: " + hex(int(val)) + " in binary is: " + bin(int(val)))
