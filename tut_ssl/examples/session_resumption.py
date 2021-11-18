from __future__ import print_function

import socket
import ssl

HOST = '192.168.210.12'
PORT = 502

# Create TLS context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(certfile="client.crt", keyfile="client.key")
context.load_default_certs()
context.load_verify_locations("ca.crt")
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = False
context.options |= ssl.OP_NO_TICKET

# Create socket and encrypt it using the TLS context
sock = socket.socket()
sock = context.wrap_socket(sock)

# Connect to the server
sock.connect((HOST, PORT))
print(sock.session_reused)

# Save the current session
ssr = sock.session

sock.sendall(b'a')

# Close the connection
# sock = sock.unwrap()
sock.shutdown(socket.SHUT_RDWR)
sock.close()

# Reconnect to the server using the stored session
sock = socket.socket()
sock = context.wrap_socket(sock, session=ssr)
sock.connect((HOST, PORT))
print(sock.session_reused)

# Close the connection
sock = sock.unwrap()
sock.shutdown(socket.SHUT_RDWR)
sock.close()