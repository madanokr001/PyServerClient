import socket

def server_logo():
    print("""
 ____  _____ ______     _______ ____  
/ ___|| ____|  _ \ \   / / ____|  _ \ 
\___ \|  _| | |_) \ \ / /|  _| | |_) |
 ___) | |___|  _ < \ V / | |___|  _ < 
|____/|_____|_| \_\ \_/  |_____|_| \_\
          
          """)
    
server_logo()

s = socket.socket()
print('Socket successfully created')

port = 56789

s.bind(('', port))
print(f'Socket bound to port {port}')

s.listen(5)
print('Socket is listening')

message = input('Enter the message to send to clients : ')

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(message.encode())
    c.close()
