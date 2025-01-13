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


# Lists
connobjlist=[]
addrlist=[]

def listner():
    print(f"[ {Colors.BRIGHT_GREEN}#{Colors.RESET} ] Wating for to clint to connect....")

    while True:
        client_socket, addr = server_socket.accept()
        print()
        print(f"[ {Colors.BRIGHT_GREEN}#{Colors.RESET} ] New clint connected from : {Colors.YELLOW}{addr[0]}{Colors.RESET}:{Colors.YELLOW}{addr[1]}{Colors.RESET}.")
        connobjlist.append(client_socket)
        addrlist.append(addr)

stop_clint_recv=False
def clint_recv(obj):
    global stop_clint_recv
    while not stop_clint_recv:
        data = obj.recv(1024)
        try:
            data=data.decode().replace("1b1n33","\n")
        except Exception as e:
            print(e)
        print(data)
        if ""==data:
        	stop_clint_recv=True

def clint_operation(idno):
    global stop_clint_recv
    stop_clint_recv=False
    cliobj=connobjlist[idno]
    cliadd=addrlist[idno]
    thread=threading.Thread(target=clint_recv,args=(cliobj,))
    thread.start()
    contnue=True
    while contnue:
        try:
            inp=input(f"{Colors.BRIGHT_CYAN}{cliadd}{Colors.RESET}~/: ")
            cliobj.sendall((inp+"\n").encode())
            if "exit" in inp:
                print(f"[ {Colors.RED}#{Colors.RESET} ] Exit.")
                stop_clint_recv=True
                cliobj.close()
                connobjlist.pop(idno)
                addrlist.pop(idno)
                contnue=False
        except Exception as e:
            print(f"[ {Colors.RED}#{Colors.RESET} ] Connection closed.")
            cliobj.close()
            connobjlist.pop(idno)
            addrlist.pop(idno)
            contnue=False


listner_thread = threading.Thread(target=listner,daemon=True)
listner_thread.start()

contnue=True
while contnue:
    print()
    inp=input(f"[{Colors.BRIGHT_CYAN}Server@Pi~/: {Colors.RESET}")
    if "help" in inp:
        print(helptext)
    elif "list" in inp:
        i=0
        for address in addrlist:
            print(f"    [ {Colors.BRIGHT_GREEN}{i}{Colors.RESET} ] {Colors.YELLOW}{address[0]}{Colors.RESET}:{Colors.YELLOW}{address[1]}{Colors.RESET}")
            i=i+1

    elif "select" in inp:
        try:
            idno=int(inp.split(" ")[1])
            clint_operation(idno)
        except Exception as el:
            print(f"[{Colors.RED} ? {Colors.RESET}] {el}")
    elif "exit" in inp:
        for obj in connobjlist:
            obj.sendall("exit".encode())
            obj.close()
        server_socket.close()
        print(f"[ {Colors.RED}#{Colors.RESET} ] Exit.")
        print()
        print(f" {Colors.BRIGHT_YELLOW}(∗ ･‿･)ﾉ゛{Colors.RESET} Goodbye.")

        contnue=False
    else:
        print(f"[{Colors.RED} ? {Colors.RESET}] Command not found.")



