# HTTP Requests

![](https://github.com/aditya109/designs-for-software-designers/raw/main/assets/http-request.svg)

# HTTP AJAX Polling

**A**synchronous **J**avaScript **A**nd **X**ML

Downsides:

- Empty responses
- Regular intervals
- Unnecessary network calls
- Delay in response

Process:

1. Client opens connection and requests data from the server using regular HTTP.
2. Requested webpage sends requests to the server at regular intervals.
3. Server calculates response and sends it back, just like regular HTTP traffic.
4. Receive updates from server. 

## HTTP Long-Polling (Hanging GET)

- If the server does not have any data available for the client, instead of sending an empty response, the server holds the request and waits until some data is available.
- Once data is available, a full response is sent to the client. (<span style="color:orange">*Long-Polling request + timeout*</span>)
- Client almost immediately re-request information from the server, so the server will almost always have an available waiting request that it can use to deliver data in response to an event.

# Web Sockets

A bidirectional persistent TCP/IP connection, client can send data to server and vice versa.

# Server Sent Events (SSE)

Server sends data whenever it is available, client sends data only via HTTP requests.