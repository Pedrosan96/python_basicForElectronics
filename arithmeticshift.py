import numpy as np
import os,sys

try:
	v = sys.argv[1]
	direction = sys.argv[2]
except:
	print("Value and shift direction must be provided in format: python ", os.path.basename(__file__), " val direction")
	print("val is any negative value and format can be: l (for left shifting) and r (for right shifting)")
	exit()

original = "{0:08b}".format(np.int8(v))
if direction == "r":
	shifted = np.int8(v)>>1
elif direction == "l":	
	shifted = np.int8(v)<<1

orig = format(np.uint8(v), '08b')
s = format(np.uint8(shifted), '08b')
print("Original: ",np.int8(v), " in binary: ",  orig)
print("Shifted: ",np.int8(shifted), " in binary: ", s)
exit()
