import numpy as np
import os,sys,struct

try:
	val = sys.argv[1]
	frmt = sys.argv[2]
except:
	print("Value and format must be provided in format: python ", os.path.basename(__file__), " val format")
	print("val is any negative or positive fractional value and format can be: half,single, and double")
	exit()
v = eval("np.{format}({val})".format(format=frmt,val=val))
size_in_bytes=v.nbytes
fc = '<I' if frmt == "single" else '<H' if frmt == "half" else '<Q'
print("Value is: ",str(v), " in hexadecimal: ", "{:0{}X}".format(struct.unpack(fc, v)[0],size_in_bytes*2), " and in binary: {:0{}b}".format(struct.unpack(fc, v)[0],size_in_bytes*8))
