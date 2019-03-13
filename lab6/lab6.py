#p = input("Enter a prime number P: ")
#q = input("Enter another prime number q: ")
#e = input("Enter public key e: ")

p=173
q=149
e=3


n = p * q
phi = (p-1) * (q-1)

#finding d
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


plaintext = "NITK575025"
ciphertext = [(ord(char) ** e) % n for char in plaintext]
print("Encrpting ...\nThe cipher text is: ",end="")
print(ciphertext)
plain = [chr((char ** d) % n) for char in ciphertext]
plain = ''.join(plain)
print("Decrypting..\nThe plaintext is: ",end="")
print(plain)
