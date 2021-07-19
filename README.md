# Reverse-Me
Reverse-me is a reverse shell generator for use in Capture-The-Flag (CTF) competitions.  Like many other reverse shell generators, reverse-me offers a menu-driven script that generates a reverse shell one-liner for both Nix and Windows boxes.  Where reverse-me departures from other reverse shell generators is that it uses a *fast* option to quickly generate reverse shell commands based on an easily configurable configuration script, skipping the menu altogether.   

Reverse-me is fully extensible and customizable.  Users are encouraged to add thier own shell scripts.  This is done by creating a file in the correct platform directory.  

## Dependencies 
- [netifaces](https://pypi.org/project/netifaces/)
- [termcolor](https://pypi.org/project/termcolor/)


## Installation
```
git clone https://github.com/serialwaffle/reverse-me.git
```

## Usage
```
python3 reverse-me.py 
```
or
```
python3 reverse-me.py --fast
```

## Available Shell Commands
Note: shell commands are aggregated from many different sources.
### Nix

- [1. awk](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/awk)
- [2. bash_Local_SUID](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/bash_Local_SUID)
- [3. bash_TCP](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/bash_TCP)
- [4. bash_UDP](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/bash_UDP)
- [5. bash_UDP](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/bash_curl)
- [6. c](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/c)
- [7. golang](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/golang)
- [8. java](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/java)
- [9. lua](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/lua)
- [10. nc](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/nc)
- [11. nc_fifo](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/nc_fifo)
- [12. perl](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/perl)
- [13. php](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/php)
- [14. php_exec](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/php_exec)
- [15. php_passthru](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/php_passthru)
- [16. php_popen](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/php_popen)
- [17. php_shell_exec](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/php_shell_exec)
- [18. php_system](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/php_system)
- [19. python_TCP](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/python_TCP)
- [20. python_cmd](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/python_cmd)
- [21. python_exports](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/python_exports)
- [22. ruby](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/ruby)
- [23. ruby_shell](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/ruby_shell)
- [24. socat](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/socat)
- [25. telnet](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/telnet)
- [26. template](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/template)
- [27. xterm](https://github.com/serialwaffle/reverse-me/blob/master/cmds/nix/xterm)

### Windows
- [1. lua](https://github.com/serialwaffle/reverse-me/blob/master/cmds/win/lua)
- [2. powershell](https://github.com/serialwaffle/reverse-me/blob/master/cmds/win/powershell)
- [3. python](https://github.com/serialwaffle/reverse-me/blob/master/cmds/win/python)
- [4. ruby](https://github.com/serialwaffle/reverse-me/blob/master/cmds/win/ruby)


## Future Additions
- Encoding options
- Command-line options
- Integration with SQLMap tamper scripts

## Feedback and issues?
If you have any feedback, anything that you want to see implemented or running into issues using reverse-me, please feel free to file an issue on https://github.com/serialwaffle/reverse-me/issues


## Support
If you appreciate my work and HackTheBox, feel free to give me some respect:

<a href="https://www.hackthebox.eu/profile/5305"><img src="https://www.hackthebox.eu/badge/image/5305" width="150"></a>

