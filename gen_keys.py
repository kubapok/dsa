from Crypto.PublicKey import DSA

key = DSA.generate(2048)
with open('prywatny', 'wb') as f:
    f.write(key.exportKey())
with open('publiczny', 'wb') as f:
    f.write(key.publickey().exportKey())


# zaszyfrować jedno zdanie

# literatura  Kutyłowski Kryptografia i praktyka 
# william stallings cryptography and network security
