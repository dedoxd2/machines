# Lab: Blind OS command injection with output redirection

Target : exploit command injection and redirect the output from `whoami` command to `/var/www/images/`

Analysis :

the vulnerable parameter is email
the payload `ayahaga%40gmail.com+%26+ls+>+/var/www/images/file.txt+%23`
