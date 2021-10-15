import numpy as np
import os,sys,struct

try:
	val = sys.argv[1]
except:
	print("Value and format must be provided in format: python ", os.path.basename(__file__), " val")
	print("val is any negative or positive fractional value")
	exit()
v = eval("np.half({val})".format(val=val))
v = struct.unpack('<H',v)[0]
#fnp_add(struct.unpack('<H',v1)[0],struct.unpack('<H',v2)[0])
#size_in_bytes=v.nbytes
#fc = '<I' if frmt == "single" else '<H' if frmt == "half" else '<Q'
#print("Value is: ",str(v), " in hexadecimal: ", "{:0{}X}".format(struct.unpack(fc, v)[0],size_in_bytes*2), " and in binary: {:0{}b}".format(struct.unpack(fc, v)[0],size_in_bytes*8))
# Fields extraction #
sb1 = v>>15
mnt1 = (v&0x3FF)
exp1 = (v>>10)&0x1F
print("Value fields:     ","{:01b}".format(sb1), " ", "{:05b}".format(exp1), " ", "{:010b}".format(mnt1))	
