import requests
import re
import time
from urllib3.exceptions import InsecureRequestWarning
import base64
import os

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def logout():
    rp = requests.get('https://192.168.193.1:1442/logout?030403030f050d06',verify=False)
    print("[*] Logged out!..")

while(True):
    try:
        resp = requests.get("http://www.speedtest.net/",allow_redirects=False)
        rt = resp.text
        m = re.findall('<a href="([^"]+)">Click here',rt)
        print(m)
        url = 'https://192.168.193.1:1442/login?a=b'
        rsp = requests.get(url,verify=False)
        magic = re.findall('name="magic" value="([^"]+)">',rsp.text)[0]
        username = os.environ('USER')
        pwd = os.environ('PASS')
        data = '4Tredir=http%3A%2F%2Fspeedtest.net%2F&magic='+magic+'&username='+ username +'&password=' + pwd
        hdrs = {'referer':url}
        rp = requests.post('https://192.168.193.1:1442/',verify=False,data=data,headers=hdrs)
        keepalive = re.findall('location.href="([^"]+)"',rp.text)[0]
        
        while True:
            requests.get(keepalive,verify=False)
            print(keepalive)
            time.sleep(10)
        
    except KeyboardInterrupt:
        print("[*] Logging Out!!")
        logout()
        exit()
    except requests.exceptions.ConnectionError:
        print("[*] Connection  Error!!")
        logout()
    except:
        pass