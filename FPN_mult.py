import numpy as np
import os,sys,struct,random
try:
	v1 = sys.argv[1]
	v2 = sys.argv[2]
except:
	print("Value and format must be provided in format: python ", os.path.basename(__file__), " val1 val2")
	print("val1 and val2 are any positive or negative fractional values")
	exit()

v1 = eval("np.half({val})".format(val=v1))
v2 = eval("np.half({val})".format(val=v2))

def fpn_mult(v1,v2):
	# Fields extraction #
	sb1 = v1>>15
	mnt1 = (v1&0x3FF)
	exp1 = (v1>>10)&0x1F
	sb2 = v2>>15
	mnt2 = (v2&0x3FF)
	exp2 = (v2>>10)&0x1F

	# Implicit bit concatenation #
	mnt1|=0x400
	mnt2|=0x400

	print("value 1: ", "{:01b}".format(sb1), " ", "{:05b}".format(exp1), " ", "{:010b}".format(mnt1))
	print("value 2: ", "{:01b}".format(sb2), " ", "{:05b}".format(exp2), " ", "{:010b}".format(mnt2))

	# Exponent & mantissa calculation #	
	exp3 = exp1+exp2-15
	mnt3 = mnt1*mnt2

	if(mnt3>>21): # overflow detected, i.e. multiplication result >= 2
		rounding = 1 if ((mnt3>>10)&1) else 0
		mnt3>>=11
		mnt3+=rounding
		exp3+=1		# exponent adjusting
	else:
		rounding = 1 if((mnt3>>9)&1) else 0
		mnt3>>=10
		mnt3+=rounding
		if(mnt3>>11):
			exp3+=1
	# Sign bit computation #
	sb3 = sb1^sb2
	# Mantissa mask #
	mnt3&=0x3FF
	print("Function result: ","{:01b}".format(sb3), " ", "{:05b}".format(exp3), " ", "{:010b}".format(mnt3))
	return sb3,exp3,mnt3
	
sb3,exp3,mnt3 = fpn_mult(struct.unpack('<H',v1)[0],struct.unpack('<H',v2)[0])
vout = v1*v2
vout = struct.unpack('<H',vout)[0]
sbout = vout>>15
mntout = (vout&0x3FF)
expout = (vout>>10)&0x1F
print("Python result:   ","{:01b}".format(sbout), " ", "{:05b}".format(expout), " ", "{:010b}".format(mntout))
