#!/usr/bin/env python3
# coding=utf-8

import argparse
import os
import netifaces
import ipaddress
import random
import config as cfg

from termcolor import colored 
from string import Template


def fancybanner():
    banner = '''
    .................................................................................
    .%%%%%...%%%%%%..%%..%%..%%%%%%..%%%%%....%%%%...%%%%%%..........%%...%%..%%%%%%.
    .%%..%%..%%......%%..%%..%%......%%..%%..%%......%%..............%%%.%%%..%%.....
    .%%%%%...%%%%....%%..%%..%%%%....%%%%%....%%%%...%%%%....%%%%%%..%%.%.%%..%%%%...
    .%%..%%..%%.......%%%%...%%......%%..%%......%%..%%..............%%...%%..%%.....
    .%%..%%..%%%%%%....%%....%%%%%%..%%..%%...%%%%...%%%%%%..........%%...%%..%%%%%%.
    .By: ⚡s0l3x ⚡..................................................................
    '''
    os.system('clear')
    print(colored(banner,'cyan'))

def menuip():
    iface = {}
    print("[*] Please select an IP/Interface from the options below:")
    print("1. Manual Entry")
    try: 
        cnt = 2 
        for _interface in netifaces.interfaces():
            _ip = netifaces.ifaddresses(_interface)[netifaces.AF_INET][0]['addr']
            iface[cnt] = _interface
            print(("%d. %s %s")%(cnt,_ip,colored(_interface,"green")))
            cnt +=1
        selection = input("[*] Select an option from the options above: ")        
        if int(selection) == 1:
            manual = input("[*] Enter IP address: ")
            while not verifyIP(manual):
                print(("[!] %s is not a valid IP address!")%(manual))
                manual = input("Enter IP address: ")
            _ip = manual
        else:
            _interface = iface[int(selection)]
            _ip = netifaces.ifaddresses(_interface)[netifaces.AF_INET][0]['addr']    
    except:
       print(" [!]  Error getting interfaces")
       exit()
    return _ip

def menuport():
    portlmt = cfg.rhp_range.split("-")
    _port = random.randint(int(portlmt[0]),int(portlmt[1]))
    return _port

def menushell(platform):
    _shell = {}
    cnt = 1
    shelloptions = "./cmds/%s/"%(platform)
    shells = [f for f in os.listdir(shelloptions) if os.path.isfile(os.path.join(shelloptions, f))]
    for s in shells:
       _shell[cnt]=s
       print(("%d. %s")%(cnt,s))
       cnt +=1
    selection = input("[*] Select a reverse Shell technique from the options above: ")
    return _shell[int(selection)]

def menuplatform():
    _platform = {}
    cnt = 1
    path = "./cmds/"
    platform= [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    for p in platform:
        _platform[cnt]=p
        print(("%d. %s")%(cnt,p))
        cnt+=1
    selection = input("[*] Select a platform from the options above: ")
    return _platform[int(selection)]


def fastip():
    try:
        return netifaces.ifaddresses(cfg.interface)[netifaces.AF_INET][0]['addr']
    except:
        print("[!] Error with config file.")

def fastport():
    portlmt = cfg.rhp_range.split("-")
    return menuport()

def fastshell():
    try:
        shell = cfg.target_shell.split(",")
        return shell
    except:
        print("[!] Error invalid value for target_shell in config file")
        exit()

def fastplatform():
    path = "./cmds/"
    platform= [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    if cfg.target_platform in platform:
        return cfg.target_platform
    else:
        print("[!] Error invalid value for target_platform in config file") 
        exit()   

def build(_platform,_shell,_shelltype,_ip,_port):
    base_cmd=("cmds/%s/%s"%(_platform,_shell))
    with open(base_cmd) as c:
        _cmd=Template(c.read())
    _cmd=_cmd.safe_substitute(ip=_ip, port=_port, shell=_shelltype)
    return _cmd
     
def printcmd(_cmd):
    final_cmd = '''
----------------------------------      
%s
----------------------------------
    '''%(_cmd)
    print(colored(final_cmd,"cyan"))

def verifyIP(_ip):
    try:
        ipaddress.ip_address(_ip)
        return True
    except:
        pass
        return False

def fast():
    ip=fastip() 
    port=fastport()
    platform=fastplatform()
    shell=fastshell()
    shelltype=cfg.default_shelltype
    for s in shell:
        cmd=build(platform,s,shelltype,ip,port)
        printcmd(cmd)
    exit()

def menu():
    fancybanner()
    shell="/bin/sh"
    ip=menuip()
    port=menuport()
    platform=menuplatform()
    shell=menushell(platform)
    shelltype=cfg.default_shelltype
    

    print(colored(ip + ":"+str(port),"cyan"))
    print(colored(platform,"cyan"))
    print(colored(shell,"cyan"))


    cmd=build(platform,shell,shelltype,ip,port)
    printcmd(cmd)
    exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
#    parser.add_argument("-i","--ip", help="IP Address used for callback.")
#    parser.add_argument("-p","--port", help="listener port")
#    parser.add_argument("-t","--interface", help="Interface")
#    parser.add_argument("--platform", help="unix or windows")
#    parser.add_argument("--listener", help="Enable netcat listener")
    parser.add_argument("-f","--fast", help="uses values from config settings",action='store_true')

    args=parser.parse_args()


    if args.fast:
        fast()		        
    menu()

