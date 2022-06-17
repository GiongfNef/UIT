from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from pwn import *

def _decrypt(ciphertext):
    r.recvuntil("choice: ")
    r.sendline("2")
    r.recvuntil(" ")
    r.sendline(ciphertext)
    pt = r.recvuntil("\nRSA service", drop = True)[83:85]  
    return pt.decode()

r = remote("localhost", 5000) # 0.tcp.ap.ngrok.io:10329
r.recvline()
flag_enc = r.recvline().strip()[31:].decode()
N = int(r.recvline().strip()[20:])
print ("I see your super secret: ", flag_enc)
print ("N: ", N)

e = 65537
upper_limit = N
lower_limit = 0

flag = ""
i = 1

while i <= 1049:
    chosen_ct = long_to_bytes((bytes_to_long(bytes.fromhex(flag_enc))*pow(2**i, e, N)) % N)
    output = _decrypt(chosen_ct.hex())
    print(i)
    if int(output[-1]) == 0:
        upper_limit = (upper_limit + lower_limit)//2
    elif int(output[-1]) == 1:
        lower_limit = (lower_limit + upper_limit)//2
    else:
        break
        print ("Unsuccessfull")
    i += 1

print ("Flag : ", long_to_bytes(lower_limit))