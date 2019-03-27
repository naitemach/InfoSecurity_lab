import math
def int2bin(x, n=0):
	return format(x, 'b').zfill(n)

def findRInv(r, n) : 
    n0 = n 
    y = 0
    x = 1
    if (n == 1) : 
        return 0
    while (r > 1) : 
        q = r // n 
        t = n
        n = r % n 
        r = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + n0 
    return x 

p = int(input("Enter a prime number P: "))
q = int(input("Enter another prime number q: "))
e = int(input("Enter public key e: "))
r = int(input("Enter r: "))
plaintext = input("Enter the plain text: ")


# plaintext = "NITK"
# p=349
# q=353
# e=13
# r = 13

n = p * q
phi = (p-1) * (q-1)
ri = findRInv(r,n)

a=e
b=phi
x = 0
y = 1
lx = 1
ly = 0
oa = a
ob = b  
while b != 0:
    q = a // b
    (a, b) = (b, a % b)
    (x, lx) = ((lx - (q * x)), x)
    (y, ly) = ((ly - (q * y)), y)
if lx < 0:
    lx += ob  
if ly < 0:
    ly += oa  

d = lx
if d==1:
	print("e inverse doesn't exist")
	exit()

chun = [1]*65
for i in range(16,65):
	chun[i] = i//8
chunSize = chun[int(math.log2(n))]
pSize = len(plaintext)
ptarr = []
for i in range(0,pSize,chunSize):
	ptarr.append(plaintext[i:i+chunSize])

while len(ptarr[-1]) < chunSize:
	ptarr[-1] = ptarr[-1] + ' '


bi = 1
print()
for block in ptarr:
	print("Block " + str(bi) + " :")
	bi += 1
	print("The message is : ",end="'")
	print(block, end="'\n") 
	char=""
	for i in block:
		char += int2bin(ord(i),8)
	char = int(char,2)	
	mp = (char * (r ** e)) % n
	print("Message sent m' is : ",end="")
	print(mp)
	sp = (mp ** d) % n
	print("Blinded signature s' is : ",end="")
	print(sp)
	s = (sp * ri) % n
	print("Signature s is : ",end="")
	print(s)
	plain =  (s ** e) % n
	print("Plain text p is : ",end="")
	print(plain)
	plain = int2bin(plain,8*chunSize)
	plainarr = []
	for i in range(0,8*chunSize,8):
		plainarr.append(chr(int(plain[i:i+8],2)))
	plain = ''.join(plainarr)
	print("The plain text is : ",end="")
	print(plain)
	print()
