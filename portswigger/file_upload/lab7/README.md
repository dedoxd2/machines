# Lab: Web shell upload via race condition

Description : This lab contains a vulnerable image upload function. Although it performs robust validation on any files that are uploaded, it is possible to bypass this validation entirely by exploiting a race condition in the way it processes them.

End Goal : `cat /home/carlos/secret` (RCE)
creds : `wiener:peter`

i loved this technique
