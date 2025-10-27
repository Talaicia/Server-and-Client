import socket
import time
import re

HOST = '127.0.0.1'
PORT = 8082

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request:\n{request}")

    match_num = re.search(r'GET /(\d+)', request)
    if match_num:
        number = int(match_num.group(1))
        sequence = collatz_sequence(number)
        sequence_str = ' '.join(map(str, sequence))
        
        # Add processing delay: 0.1 seconds x length of sequence
        time.sleep(0.1 * len(sequence))
        
        response_body = (f"<!DOCTYPE html>\n"
                        f"<html>\n"
                        f"<p>\n"
                        f"[{sequence_str}]\n"
                        f"</p>\n"
                        f"</html>")
        
        response = (f"HTTP/1.0 200 OK\r\n"
                    f"Content-Type: text/html\r\n"
                    f"\r\n"
                    f"{response_body}")
    else:
        response_body = (f"<!DOCTYPE html>\n"
                        f"<html>\n"
                        f"<p>\n"
                        f"Invalid Request\n"
                        f"</p>\n"
                        f"</html>")
        
        response = (f"HTTP/1.0 400 Bad Request\r\n"
                    f"Content-Type: text/html\r\n"
                    f"\r\n"
                    f"{response_body}")

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        handle_client_connection(client_socket)

if __name__ == "__main__":
    start_server()




