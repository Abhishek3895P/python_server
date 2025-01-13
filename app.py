import threading
import socket
import time


# All Colors
class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"
    RESET = "\033[0m"
    
    # Bright colors
    BRIGHT_BLACK = "\033[1;30m"
    BRIGHT_RED = "\033[1;31m"
    BRIGHT_GREEN = "\033[1;32m"
    BRIGHT_YELLOW = "\033[1;33m"
    BRIGHT_BLUE = "\033[1;34m"
    BRIGHT_MAGENTA = "\033[1;35m"
    BRIGHT_CYAN = "\033[1;36m"
    BRIGHT_WHITE = "\033[1;37m"


helptext='''
    help      :      for help
    list      :      for see all conected devices
    select    :      for select any of clint
    exit      :      for exit
'''


# Start
print(f"[ {Colors.BRIGHT_GREEN}#{Colors.RESET} ] Program Started.")

host = '0.0.0.0'  # Get local machine name
port = 6677  # Reserve a port for your service
print(f"[ {Colors.BRIGHT_GREEN}#{Colors.RESET} ] Port {port}.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"[ {Colors.BRIGHT_GREEN}#{Colors.RESET} ] Server started in {Colors.BRIGHT_YELLOW}{host}{Colors.RESET}:{Colors.BRIGHT_YELLOW}{port}{Colors.RESET}.")


while True:
    client_socket, addr = server_socket.accept()
    print()
    print(f"[ {Colors.BRIGHT_GREEN}#{Colors.RESET} ] New clint connected from .")
       
