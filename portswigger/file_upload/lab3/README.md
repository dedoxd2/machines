# Lab: Web shell upload via path traversal

Description : This lab contains a vulnerable image upload function. The server is configured to prevent execution of user-supplied files, but this restriction can be bypassed by exploiting a `secondary vulnerability:lfi`.

End Goal : RCE

- the trick here to escape the directory that the web server uploads ur file into it using the lfi trick
`filename="..%2fdedoxd222.php`
- why we needed to do this trick ?
  - i think because the webserver is configured to not execute code from the `avatars` directory , so the php code get treated as a text not an actull code
