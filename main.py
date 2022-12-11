# -*- coding: utf-8 -*-
import multiprocessing
import subprocess
import os
import logging
if __name__ == '__main__':
    multiprocessing.freeze_support()
    if os.getenv('CLIENT') == None:
        data=input('Please insert the client data: ')
        os.environ["CLIENT"] = data
        logging.warning("Added client")    
    else:
        logging.warning("Client finded")    
    hosts_location="C:\\Windows\\System32\\drivers\\etc\\hosts"
    with open(hosts_location,"r+") as file:
        content=file.read()
        file.write('	127.85.170.2    viewer.enerion')
    netshcmd=subprocess.Popen('netsh interface portproxy add v4tov4 listenport=80 listenaddress=127.85.170.2 connectport=8080 connectaddress=127.0.0.1', 
    shell=True, 
    stderr=subprocess.PIPE, 
    stdout=subprocess.PIPE )
    output, errors =  netshcmd.communicate()
    if errors: 
        print("WARNING: ", errors)
    else:
        print("SUCCESS ", output)
    logging.warning("Reboot is necessary")