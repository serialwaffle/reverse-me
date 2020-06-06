#!/usr/bin/env python3

#  Default configuration file for reverse-me.  This configuration file is used for hte --fast option.    

# Set to the interface of the vpn tunnel if using openvpn to connect to netowrk (aka "tun0")
interface="eth0"

# Port range that should be used for call back. 
rhp_range="30000-65535"

# Target platform.  Choose between "nix" or "win"
target_platform="nix"

#Shell output.  If multiple shells shoud be outputed, comma seperated.
target_shell="perl,python_TCP,nc"

#shell type to be used for nix targets.
default_shelltype = "/bin/sh"

