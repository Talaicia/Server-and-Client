import socket
import time
from datetime import datetime
import re

HOST = '127.0.0.1'
PORT = 8082

numbers = [3148, 3744, 1237, 112, 56, 12328, 99, 104, 9999]


def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def send_collatz_request(number):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request = f"GET /{number} HTTP/1.0\r\nHost: {HOST}:{PORT}\r\n\r\n"
        
        # Print the request
        print(f"GET /{number} HTTP/1.0")
        print(f"Host: {HOST}:{PORT}")
        
        start_time = time.time()
        s.sendall(request.encode('utf-8'))
        
        response = b""
        while True:
            part = s.recv(1024)
            if not part:
                break
            response += part
        
        end_time = time.time()
        delay = end_time - start_time
            
    return response.decode('utf-8'), delay

def parse_response(response):
    # Extract content between <p> and </p> tags
    match = re.search(r'<p>\s*(.*?)\s*</p>', response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def main():
    delays = []
    
    for number in numbers:
        response, delay = send_collatz_request(number)
        
        # Parse and print the content from <p> tags
        content = parse_response(response)
        if content:
            print(content)
        
        # Print delay information
        print(f"delay for request {number} is {delay} seconds")
        print()  # Empty line between requests
        
        delays.append(delay)
    
    # Calculate and print average delay
    average_delay = sum(delays) / len(delays)
    print(f"average delay is {average_delay} seconds")

if __name__ == "__main__":
    main()


