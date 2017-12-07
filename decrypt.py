from Crypto.Signature import DSS
from Crypto.PublicKey import DSA
from Crypto.Hash.SHA256 import SHA256Hash
import socket


publiczny = DSA.importKey(str(open('publiczny', 'rb').read(), 'utf-8'))
dss_pu = DSS.new(publiczny, 'deterministic-rfc6979')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
server_address = ('localhost', 5001)
sock.connect(server_address)

zaszyfrowana = bytes()
while 1:
    buf = sock.recv(1024)
    zaszyfrowana += buf
    if len(buf) == 0:
        break


delimiter_pos = zaszyfrowana.find(b':')
m, signature = zaszyfrowana[:delimiter_pos], zaszyfrowana[delimiter_pos + 1:]
hash_m = SHA256Hash(m)
m = str(m, 'utf-8')
print(m)
print(signature)

try:
    dss_pu.verify(hash_m, signature)
    print('authentic')
except ValueError:
    print('not authentic')
