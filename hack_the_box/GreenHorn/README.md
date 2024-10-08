# GreenHorn machine

- i tried first to get the machine but after i just went to the github app there i was stuck , now i new that i should try to add the ip to my hosts and i have tried again so let's how far we can go this time

- when i tried to access the home page it required a password and told me hat the version of this service is `pluck 4.7.18`
- horrayy ... there is a already exploit on `https://www.exploit-db.com/exploits/51592`
- let's try it
- actually i didn't manage to exploit this vulnerability successfully , but i managed to log in by uncracking the hash i found in `./GrennHorn/data/settings/pass.php` using this site <https://passwordrecovery.io/sha512/>
- i was stuck  in exploiting the vulnerability on `pluck` cuz i didn't noitce that i should customize the authentication phase :"//

## Take Aways from this machine

- after getting a shell access on the victim machine we could transfer files from and to the victim machine using simple http servers by python from example `python3 -m http.server`
- we could turn pixeled pdf files into (ppm:Portable Pixmap ,pgm:Portable Graymap ,pbm:Portable Bitmap,jpeg) -> for more info check `[check](https://www.xpdfreader.com/pdfimages-man.html)
- when dealing with pixeled images check this great tool [Depix](https://github.com/spipm/Depix)
- `nc -lvnp 4444` i want to save this command tho cus i always forget it xd
