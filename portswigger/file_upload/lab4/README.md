# Lab: Web shell upload via extension blacklist bypass

Description : Certain file extensions are blacklisted, but this defense can be bypassed due to a fundamental flaw in the configuration of this blacklist.

End Goal : RCE (cat /home/carlos/secret)

Creds : `wiener:peter`

Analysis:

- techniquesi have tried :
- null byte (dedoxd2.php%00.jpg)
- adding # after the extension so that other extension should be treated as a comment (dedoxd2.php#%00.jpg)
- adding a number after the php (dedoxd2.php1#%00.jpg)
- but none of them worked

- using the simple list provided by hacktrickes and the following extensions have been executed as a code
  - .module , .ctp ,  hphp , inc , `phar` ,htaccess shtml , pgif ,php[2-7] ,
- the only extension worked is [phar , phtml] and gave me an RCE

> The solution provided by portswiger is so good
