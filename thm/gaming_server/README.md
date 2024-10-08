# GamingServer

- consediring the results of nmap the server is running http & ssh
- since there is http server , let's try u see it's dirs
- using the results of dirb , we found private key for ssh
- we should transform it to hash so we can crack it and get the phrase to use it
  - `/usr/share/john/ssh2john.py secretKey > hashedkey`
  - `sudo john hashedkey -w=../server_uploads/dict.lst`

- after cracking the hash we got the passing phrase to use it via authentication
- we had to chang it's mode to 400 -> so we can use it via authentcation  <https://stackoverflow.com/questions/9270734/ssh-permissions-are-too-open>
- after login we got the the user flag
- now we need to escalate our privilage
- using id coomand to investigate more in the environment
- using the results in simple google search with phrase "privalage escalation" lead us to exploit the lxc vulnerability

---

- googling the `OpenSSH 7.6p1` , and found this version is actually vulnerable for user enumeration
- `https://www.exploit-db.com/exploits/46516`

viewing the page source and found this comment
`<!-- john, please add some actual content to the site! lorem ipsum is horrible to look at. -->`
