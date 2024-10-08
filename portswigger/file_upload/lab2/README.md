# Lab: Web shell upload via Content-Type restriction bypass

Description :  This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

End Goal : Upload PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`  (RCE)

CREDS : `wiener:peter`
