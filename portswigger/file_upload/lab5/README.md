# Lab: Web shell upload via obfuscated file extension

Description : Certain file extensions are blacklisted, but this defense can be bypassed using a classic obfuscation technique.

creds : `wiener:peter`

Target : `cat /home/carlos/secret` (RCE)

payload : shell.php%00.jpg -> null byte technique
