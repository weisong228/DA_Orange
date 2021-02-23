import socket
import requests

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(1)
    print(f'Listening on port {SERVER_PORT} ...')

    while True:
        # Wait for client connections
        client, client_address = s.accept()
        print(f"{client_address} has connected!")

        # Get the client request
        with client as c:
            request = c.recv(1024).decode()
            print(request)

            # Send HTTP response
            response = """ \n
<!DOCTYPE html>
<html>
<body>

<h1>Team Orange is here!</h1>

<p>Do u like annoying oranges?This is the webpage to it.</p>
<img src="https://i.quotev.com/img/q/u/10/11/29/69614128-Annoying-Orange-2.jpeg" alt="quotev.com" width="460" height="345">
<img src="https://i.quotev.com/img/q/u/15/5/23/2522b0bbf1-image.jpg" alt="quotev.com" width="500" height="375">
<img src="https://i.quotev.com/img/q/u/10/10/31/36755915-Screen_shot_2010-10-31_at_5_16_47_PM.jpg" alt="quotev.com" width="500" height="375">
<p>Orange can be annoying at times but it taste sour too Darren is an orange.</p>


</body>
</html>

"""
            #send response to client
            c.sendall("HTTP/1.1 200 OK".encode())
            c.sendall(response.encode())