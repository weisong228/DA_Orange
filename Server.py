#First HTTP Server
import socket
#Define the host as a tuple
HOST, PORT = "", 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(True)

print("Serving HTTP on port %s...." %PORT)

while True:
    client_connection, client_address = s.accept()
    request = client_connection.recv(1024) #Buffer Size
    print(request.decode("utf-8")) #Display the HTTP request
    #Define the Web response message
    #http_reponse = """"\HTTP/1.0 200 OK Content-Type: text/html; charset=UTF-8 Welcome This is my first webpage, GREAT!"""
    http_reponse = 'HTTP/1.0 200 OK\n\nHello World Darren_jaslyn_weisong'
    client_connection.sendall(bytes(http_reponse, "utf-8"))
    #http_reponse = 'HTTP/1.0 200 OK\n\nHello World'
    #client_connection.sendall(http_reponse.encode())
    client_connection.close()

<!DOCTYPE html>
<html>
<body>

<h2>Alternative text</h2>

<p>:Are you annoying like him?</p>

<img src="https://i.quotev.com/img/q/u/10/11/29/69614128-Annoying-Orange-2.jpeg" alt="quotev.com" width="460" height="345">
<img src="https://i.quotev.com/img/q/u/15/5/23/2522b0bbf1-image.jpg" alt="quotev.com" width="500" height="375">


</body>
</html>
