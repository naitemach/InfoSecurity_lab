ip = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
fp = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
ebox = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
sp = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
sbox = [
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],
[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],
[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],
[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  
[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 
[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 
[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
] 
pd=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
cb=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

def leftShift(x,y):
	x = x[y:] + x[:y]
	return x

def int2bin(x, n=0):
	return format(x, 'b').zfill(n)

def xor(a,b,l):
	c=''
	for i in range(l):
		if a[i]==b[i]:
			c+='0'
		else:
			c+='1'
	return c

def genRk(a):
	global pd,cb


	temp=""
	for i in a:
		temp += int2bin(ord(i),8)
	a=temp

	opd=""
	for i in range(56):
		opd = opd + a[pd[i]-1]

	left = opd[0:28]
	right = opd[28:]

	routeKeys = []

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
		#print("key " + str(i) + "  : " + ocb)
		routeKeys.append(ocb)
	return routeKeys




# tc = int(input("Enter the test case: "))
# ptfile="PT-TC" + str(tc) + ".txt"
# rkfile="RK-TC" + str(tc) + ".txt"
# f=open(rkfile,'r')
# contents  = f.read()
# keys = contents.split('\n')[:16]
# f.close()

# blocks=[]
# f=open(ptfile,'r')
# contents  = f.read()
# text = contents
# f.close()

# blocks=[]
# blocks.append(text)




def main():
	a = input("Enter the PlainText: ")
	a = a.replace(' ','')
	if len(a) > 40:
		printf("Error: Plaintext should be max 40 bytes!")
		return 0
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

	a = input("Enter the Key: ")
	print()
	a = a.replace(' ','')
	n = len(a)

	# if n > 8:
	# 	choice = int(input("Enter the choice 1 or 2: "))
	# elif n <8:
	# 	print("ERROR: Enter atleast 8 characters")

	# if choice == 1:
	# 	a=a[:8]
	# else:
	# 	a=a[n-8:]

	if n != 8:
		print("Error: Key size shoulld be 8 bytes!")
		return 0
	keys=genRk(a)

	ofile=''
	for block in blocks:
		#input
		# print("Input: ",end="")
		# for l in range(0,64,8):
		# 	print(block[l:l+8],end=" ")
		# print()
		# print()

		print("Input : ",end="")
		for i in range(0,64,8):
			print(chr(int(block[i:i+8],2)),end="")
		print()
		print("block : "+block)
		print()

		#Initial Permutation	
		oip = ''	
		for i in range(64):	
			oip = oip + block[ip[i]-1]	
		print("output of initial permutation : "+oip)	
		print()
		
		block = oip

		#16 Rounds of DES
		left = block[:32]
		right = block[32:64]
		for i in range(16):
			key = keys[i]
			temp = right

			#mixer
			#expansion box
			oeb = ''
			for j in range(48):
				oeb=oeb + right[ebox[j]-1]
			right = oeb

			#xor
			right = xor(right,key,48)

			#substitution box
			osbox = ''
			j = 0
			for k in range(0,48,6):
				sinput = right[k:k+6]
				row = int(sinput[0]+sinput[5],2)
				col = int(sinput[1:5],2)
				osbox += int2bin(sbox[j][row][col],4)
				j += 1
			right = osbox


			#straight permutation
			osp = ''
			for j in range(32):
				osp = osp+right[sp[j]-1]
			right = osp

			#Swapper
			if i == 15:
				left = xor(left,right,32)
				right = temp
				block = left+right
				ofile += block
			else:
				right = xor(left,right,32)
				left = temp
			if i>=9:
				print("output of round " + str(i+1) + " :-",end="")
			else:
				print("output of round  " + str(i+1) + " :-",end="")
			outtext = left+right
			for l in range(0,64,8):
				print(outtext[l:l+8],end=" ")
			print()

		#Final Permutation
		print()	
		ofp = ''	
		for i in range(64):	
			ofp = ofp + block[fp[i]-1]	
		print("output of final permutation : "+ofp)
		print()
		block = ofp

		#output
		# print("output: ",end="")
		# for l in range(0,64,8):
		# 	print(block[l:l+8],end=" ")
		# print()

		# print("output : ",end="")
		# for i in range(0,64,8):
		# 	print(chr(int(ofp[i:i+8],2)),end="")
		# print()
		# print()


	f = open('Output-Program-4.txt',"w+")
	f.write(ofile)
	f.close()



if __name__ == '__main__':
	main()