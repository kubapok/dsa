import socket
from Crypto.Signature import DSS
from Crypto.PublicKey import DSA
from Crypto.Hash.SHA256 import SHA256Hash

m = 'Ala ma kota i psa.'

prywatny = DSA.importKey(str(open('prywatny', 'rb').read(), 'utf-8'))
dss_pr = DSS.new(prywatny, 'deterministic-rfc6979')

hash_1 = SHA256Hash(bytes(m, 'utf-8'))
signature = dss_pr.sign(hash_1)


server_address = ('localhost', 5001)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)
print('waiting for a connection')
connection, client_address = sock.accept()

connection.sendall(bytes(m, 'utf-8'))
connection.sendall(bytes(':', 'utf-8'))
print('wyslano wiadomosc pierwszą')

connection.sendall(signature)
print('wyslano wiadomosc druga')
connection.shutdown(0)
connection.close()
