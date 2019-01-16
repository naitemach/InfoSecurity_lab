ip=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
fp=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]



def int2bin(x, n=0):
	return format(x, 'b').zfill(n)


a = input("Enter the string: ")
print()
a = a.replace(' ','')
b = []
for i in a:
	b.append(i)
c = 8-(len(b) % 8)
for i in range(c):
	b.append(' ')
l = len(b)
for i in range(l):
	b[i] = int2bin(ord(b[i]),8)
blocks=[]
for i in range(0,l,8):
	temp=''
	for j in range(8):
		temp = temp + b[i+j]
	blocks.append(temp)

for block in blocks:
	print("Input : ",end="")
	for i in range(0,64,8):
		print(chr(int(block[i:i+8],2)),end="")
	print()
	print("block : "+block)
	oip = ''
	for i in range(64):
		oip = oip + block[ip[i]-1]
	print("output of initial permutation : "+oip)
	ofp = ''
	for i in range(64):
		ofp = ofp + oip[fp[i]-1]
	print("output of final permutation : "+ofp)
	for i in range(64):
		if block[i] != ofp[i]:
			break
		if i==63:
			print("Output of final permutation is same as respective 64bits input block")
	print("output : ",end="")
	for i in range(0,64,8):
		print(chr(int(ofp[i:i+8],2)),end="")
	print()
	print()


