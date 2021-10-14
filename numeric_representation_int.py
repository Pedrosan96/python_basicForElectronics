import numpy as np
import sys, os, struct

try: 
	val = sys.argv[1]
	frmt = sys.argv[2]
except:
	print("Value and format must be provided in format: python ", os.path.basename(__file__), " val format")
	print("Val is any negative or positive integer and format can be: int8, uint8, int16, uint16, int32, uint32, int64 and uint64")
	exit()
v = eval("np.{format}({val})".format(format=frmt, val=val))
size_in_bytes=v.nbytes
print("Value is: ",str(v), " in hexadecimal: ", "{:0{}x}".format(v,size_in_bytes*2), " and in binary: {:0{}b}".format(v,size_in_bytes*8))
