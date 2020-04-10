import socket
s=socket.socket()
print('socket created')
 # one argument so bind consist of ip address and
# port number
s.bind(('localhost',9999))
s.listen(3)
print('waiting for the connection')
while True:
  c, addr = s.accept()
  # here server received the request from the client side
  name=c.recv(1024).decode()
  print("conected with",addr,name)
  c.send(bytes('welcome to python','utf-8'))
  c.close()
