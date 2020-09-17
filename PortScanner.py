# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:17:10 2020

@author: Malika Perera
"""
#!/usr/bin/python3
import socket
import subprocess
import sys
from datetime import datetime
import threading



print_lock = threading.Lock()

# To Clear the screen
subprocess.call('clear', shell=True)



# Checking start time of scan

t1 = datetime.now()
print("Scan start time:  ", t1, "\n")

#Message to be sent to obtain banner information
msg = 'GET /WhoAreYou HTTP/1.1\r\n\r\n'
msgbt = str.encode(msg)

#Function for portscanner

def portscanner(targetip,port):
    global service, version
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((targetip, port))
        with print_lock:
            if result == 0:
                service = socket.getservbyport(port)
                print("Port {}:      Open".format(port) + "\t-- Service: " + str(service), "\n")
                sock.close()
    except socket.gaierror as e:
        print("Hostname could not be resolved. Exiting")
        print(e)
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
   




def main():
    # Get user
    global port
    Target = input("Enter a target host to scan: ")

    # Translate target to IPv4 format

    targetip = socket.gethostbyname(Target)

    # Display process
    print("--------------------------------")
    print("Scanning target", targetip)
    print("--------------------------------")

    port = 1
    for port in range(1, 65535):
        t = threading.Thread(target=portscanner, kwargs={'targetip':targetip,'port': port})
        port +=1
        t.start()
    
    

    portscanner(targetip,port)


if __name__ == '__main__':
    main()

# Checking the end time
t2 = datetime.now()

# Calculating time taken

print("Scan end time  :  ", t2)

time_taken = t2 - t1

# Printing time taken
print("Scanning completed in:  ", time_taken)
