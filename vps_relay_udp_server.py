
import socket

def relay_messages(server_socket):
    data, receiver_addr = server_socket.recvfrom(1024)  # Получаем данные и адрес клиента
    print(f"Received message from {receiver_addr}: {data.decode()}")
    print("Waiting data from transmitter...")

    while True:
        data, addr = server_socket.recvfrom(256*4*4)  # Получаем данные и адрес клиента
        print(f"Received message from {addr}: {len(data)} bytes")
        
        server_socket.sendto(data, receiver_addr)
        print(f"Relayed message to {receiver_addr}")
                    

if __name__ == "__main__":
    # Запрос номера порта у пользователя
    # port = input("Please enter the port number to bind to: ")
    # port = int(port)  # Преобразование введенного значения в целое число
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('', 11373))  
        print("Relay Server is running. Waiting for test message from receiver...")
        relay_messages(server_socket)
