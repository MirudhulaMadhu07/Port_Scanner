# Port_Scanner
Lightweight multithreaded TCP port scanner with banner grabbing, written in pure Python using only the standard library. Scans a user-defined port range with 100 worker threads, then reconnects to open ports to read service banners. A beginner-friendly learning project covering sockets, concurrency, and recon basics. Use only on authorized systems
scan_port() checks whether a single TCP port is open on a target host by attempting a full TCP connection, which completes the three-way handshake (SYN, SYN-ACK, ACK). If the connection succeeds, the port is open and the function returns (port, True). If it fails, the port is treated as closed and the function returns (port, False).

How it works:

socket.create_connection((host, port), timeout=timeout) is a function from Python’s socket library that opens a TCP connection to another machine.
(host, port) is the address being connected to. The host is a domain name or IP address, and the port is the numbered “door” on that machine.
timeout=timeout is the number of seconds to wait for a response before giving up.
The with keyword is a Python context manager. It automatically closes the socket once the indented block finishes, even if an error occurs, so connections are never left open.
The function returns a tuple containing the port number along with the result, so you can tell which port each result belongs to. This is especially useful when scanning many ports at once.
