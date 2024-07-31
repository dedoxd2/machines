# Access control vulnerabilities

## Lab: Unprotected admin functionality

just check the `robots.txt`, then access the admin panel and delete the user

## Lab: Unprotected admin functionality with unpredictable URL

read the page source and serch for word admin
or in the site map section you would notice that there is an `admin-somestring`
append it to the orignal , pam -> lab is done

## Lab: User role controlled by request parameter

there is a cookie `admin=false` just change it

## Lab: User role can be modified in user profile

change the email as a ligimite request, notice the reponse
there is a "roleid":1
submit the request again but in this time add "roleid":2

## Lab: User ID controlled by request parameter

in the get profile request change the parameter to carlose
/profile?username=weiner
