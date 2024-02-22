
import socket

def relay_messages(server_socket):
    data, receiver_addr = server_socket.recvfrom(1024)  # Получаем данные и адрес клиента
    print(f"Received message from {receiver_addr}: {data.decode()}")
    receiver_message = "Waiting data from transmitter..."
    print("Waiting data from transmitter...")
    server_socket.sendto(receiver_message.encode(), receiver_addr)

    while True:
        data, addr = server_socket.recvfrom(265*4*4)  # Получаем данные и адрес клиента
        #print(f"Received message from {addr}: {len(data)} bytes")
        print(".", end='', flush=True)
        
        server_socket.sendto(data, receiver_addr)
        #print(f"Relayed message to {receiver_addr}")
        print("+", end='', flush=True)
                    

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('', 11373))  
        print("Relay Server is running. Waiting for test message from receiver...")
        relay_messages(server_socket)
