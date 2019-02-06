pd=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
cb=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]


def int2bin(x, n=0):
	return format(x, 'b').zfill(n)

def leftShift(x,y):
    x = x[y:] + x[:y]
    return x

a = input("Enter the string: ")
a = a.replace(' ','')
n = len(a)

if n > 8:
    choice = int(input("Enter the choice 1 or 2: "))
elif n <8:
    print("ERROR: Enter atleast 8 characters")

if choice == 1:
    a=a[:8]
else:
    a=a[n-8:]

temp=""
for i in a:
    temp += int2bin(ord(i),8)
a=temp

opd=""
for i in range(56):
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


