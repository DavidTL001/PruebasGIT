#cliente
import socket

HOST = '192.168.1.68'  # Sustituye esto por la IP de tu compañero
PORT = 1060

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(b"Hola servidor, soy el cliente.")
        respuesta = client_socket.recv(1024)
        print("Respuesta del servidor:", respuesta.decode())
except Exception as e:
    print("Error al conectar con el servidor:", e)
