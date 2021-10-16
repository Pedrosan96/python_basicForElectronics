import numpy as np
import os,sys,struct

try:
	v1 = sys.argv[1]
	v2 = sys.argv[2]
except:
	print("Value and format must be provided in format: python ", os.path.basename(__file__), " val1 val2")
	print("val1 and val2 are any positive fractional values")
	exit()

v1 = eval("np.half({val})".format(val=v1))
v2 = eval("np.half({val})".format(val=v2))

def fnp_add(v1,v2):
	vmax = v1 if v1>v2 else v2
	vmin = v2 if v1>v2 else v1
	# Fields extraction #
	sb1 = vmax>>15
	sb2 = vmin>>15
	mnt1 = (vmax&0x3FF)
	mnt2 = (vmin&0x3FF)
	exp1 = (vmax>>10)&0x1F
	exp2 = (vmin>>10)&0x1F
	
	sb3 = sb1

	print("vmax fields:     ","{:01b}".format(sb1), " ", "{:05b}".format(exp1), " ", "{:010b}".format(mnt1))	
	print("vmin fields:     ","{:01b}".format(sb2), " ", "{:05b}".format(exp2), " ", "{:010b}".format(mnt2))	
	
	# mantissa implicit bit concatenation #
	mnt1|=0x400
	mnt2|=0x400

	# mantissa of larger value is shifted #
	mnt1<<=(exp1-exp2)

	# mantisa addition #
	mnt3 = mnt1+mnt2
	rounding = (mnt3>>(exp1-exp2))&1
	mnt3>>=(exp1-exp2)
	if(mnt3>>11):	# if result >= 2, normalization is required
		print("normalization required")
		exp3 = exp1+1
		mnt3 = mnt3>>1
	else:
		exp3 = exp1
	if(exp1 != exp2):
		mnt3+=rounding
	mnt3&=0x3FF
	print("Function result: ","{:01b}".format(sb3), " ", "{:05b}".format(exp3), " ", "{:010b}".format(mnt3))	
	
fnp_add(struct.unpack('<H',v1)[0],struct.unpack('<H',v2)[0])
vout = np.half(v1+v2)
vout = struct.unpack('<H',vout)[0]
sbout = vout>>15
mntout = (vout&0x3FF)
expout = (vout>>10)&0x1F
print("Python result:   ","{:01b}".format(sbout), " ", "{:05b}".format(expout), " ", "{:010b}".format(mntout))	
