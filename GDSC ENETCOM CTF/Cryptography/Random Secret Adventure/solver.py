from Crypto.Util.number import inverse,long_to_bytes
import binascii
e = 65537
p=89768529456611589156600297564715535821269053058298172625567973617360300277891
q=88611089061890825503530486834862116736903339656105975489808565421851461797841
n=p*q
phi=(p-1)*(q-1)
d=inverse(e,phi)
with open ("ciphertext.txt",'rb') as file:
    hexdata=binascii.hexlify(file.read())

print(hexdata)
ct=int(hexdata,16)
print("ct : ",ct)
message=pow(ct,d,n)
print(long_to_bytes(message))