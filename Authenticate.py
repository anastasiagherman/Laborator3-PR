import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://andys.md/ru/login"
s = requests.Session()

values = {'email': 'testingemailacount@gmail.com',
                  'password': 'testingAccount01'
        }
r = s.post(url, data=values)

c = r.cookies

print(c)
r = s.get('https://andys.md/ru/account', cookies = c, verify = False)
print(r.text)
