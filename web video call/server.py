import socket,cv2,pickle,struct

#Creating the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Host IP: ", host_ip)
port = 9999
socket_address = (host_ip, port)

#Socket Binding
server_socket.bind(socket_address)
#Socket Listening
server_socket.listen(7)
print("Listening on: ",socket_address)

#Socket Accepting
while True:
    client_socket, server_address = server_socket.accept()
    print("Got a connection from: ",server_address)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while (vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a)) +a
            client_socket.sendall(message)
            cv2.imshow("Transmitting the video",frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
            
            
            
            
            
            
            
        