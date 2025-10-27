# HTTP 1.0 Server and Client

## Requirements
- Python 3.x
- Both server and client must run on the same machine (localhost)

## How to Run

1. Open terminal

2. In the terminal, start the server: server.py

   You should see: Server listening on 127.0.0.1:8082

3. In the terminal, run the client: client.py

   The client will:
   - Send HTTP/1.0 requests to the server
   - Print request, response content, and delay for each
   - Print the average delay at the end

4. To test in a browser:
   - Visit http://127.0.0.1:8082/3148 (for example) and you should see the Collatz sequence displayed.
   - Try http://127.0.0.1:8082 (no number) to see “Invalid Request”.

## Additional Notes
- The server adds a simulated delay: 0.1 seconds * sequence length.
- The client calculates round-trip delay for each request.

