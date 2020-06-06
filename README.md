# Reverse-Me
Reverse-me is a reverse shell generator for use in Capture-The-Flag (CTF) competitions.  Like many other reverse shell generators, reverse-me offers a menu-driven script that generates a reverse shell one-liner for both Nix and Windows boxes.  Where reverse-me departures from other reverse shell generators is that it uses a *fast* option to quickly generate reverse shell commands based on an easily configurable configuration script, skipping the menu altogether.   

Reverse-me is fully extensible and customizable.  Users are encouraged to add thier own shell scripts.  This is done by creating a file in the correct platform directory.  

## Dependencies 
netifaces
termcolor

## Installation

## Usage
```
python3 reverse-me.py 
```
or
```
python3 reverse-me.py --fast
```

## Available Shell Commands
Note: shell commands are agregated from many different sources.
### Nix
```
- [1. awk](https://www.nostarch.com/carhacking)
1. awk
2. bash_TCP
3. bash_UDP
4. c
5. golang
6. java
7. lua
8. nc
9. nc_fifo
10. perl
11. php
12. php_exec
13. php_passthru
14. php_popen
15. php_shell_exec
16. php_system
17. python_TCP
18. python_cmd
19. python_exports
20. ruby
21. socat
22. telnet
23. template
24. xterm
```
### Windows
```
1. lua
2. powershell
3. python
4. ruby
```
## Future Additions

Encoding options

Command-line options

Integration with SQLMap tamper scripts

