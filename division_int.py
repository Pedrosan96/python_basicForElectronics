import numpy as np
import os,sys

try:
	dtype = sys.argv[3]
	a = eval("np."+dtype+"("+sys.argv[1]+")")
	b = eval("np."+dtype+"("+sys.argv[2]+")")
except:
	print("Operands and format must be provided in format: python ", os.path.basename(__file__), " op1 op2 format")
	print("op1 and op2 are any negative or positive integer and format can be: int8,int16,int32,int64,uint8,uint16,uint32, and uint64")
	exit()

c = eval("np."+dtype+"(a/b)")
d = eval("np.u"+dtype+"(c)") if dtype[0] == 'i' else c
rr = abs(a)%abs(b)
size_in_bytes=c.nbytes
print("Division result is: ",str(c), " in hexadecimal: ", "{:0{}X}".format(d,size_in_bytes*2), " and in binary: {:0{}b}".format(d,size_in_bytes*8), " and remainder is: ",str(rr))
