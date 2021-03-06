import socket

# 전송할 메시지를 설정해둔다.
msgFromClient = "n1.jpg"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
# bufferSize = 1024
bufferSize = 10 # 버퍼사이즈 줄임
# 클라이언트 쪽에서 UDP 소켓 생성
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 생성된 UDP 소켓을 사용하여 서버로 전송
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)


