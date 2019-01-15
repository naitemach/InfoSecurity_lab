pd=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
cb=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]



def int2bin(x, n=0):
	return format(x, 'b').zfill(n)

def leftShift(x,y):
    x = x[y:]
    for i in range(y):
        x = x+'0'
    return x


# a = input("Enter the string: ")
# a = a.replace(' ','')
# b = []
# for i in a:
# 	b.append(i)
# c = 8-(len(b) % 8)
# for i in range(c):
# 	b.append(' ')
# l = len(b)
# for i in range(l):
# 	b[i] = int2bin(ord(b[i]),8)
# blocks=[]
# for i in range(0,l,8):
# 	temp=''
# 	for j in range(8):
# 		temp = temp + b[i+j]
# 	blocks.append(temp)


a="1000101000101011010101000001010010100000101001010010101010101010"

opd=""
for i in range(64):
	opd = opd + a[pd[i]-1]

left = opd[0:28]
right = opd[28:]

for i in range(1,17):
    if i==1 or i==2 or i==9 or i==16:
        left = leftShift(left,1)
        right = leftShift(right,1)
    else:
        left = leftShift(left,2)
        right = leftShift(right,2)
    ocb=""
    icb=left+right
    for j in range(48):
        ocb=ocb+icb[cb[j]-1]
    print("key " + str(i) + "  : " + ocb)




# for block in blocks:
# 	print("block : "+block)
# 	oip = ''
# 	for i in range(64):
# 		oip = oip + block[ip[i]-1]
# 	print("output of initial permutation : "+oip)
# 	ofp = ''
# 	for i in range(64):
# 		ofp = ofp + oip[fp[i]-1]
# 	print("output of final permutation : "+ofp)
# 	for i in range(64):
# 		if block[i] != ofp[i]:
# 			break
# 		if i==63:
# 			print("Output of final permutation is same as respective 64bits input block")
# 	print()


