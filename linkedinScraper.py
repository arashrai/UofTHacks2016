import urllib.request
import requests
from bs4 import BeautifulSoup

payload={
    'session_key' : 'arashrai17@gmail.com',
    'session_password' : 'jatinder5'
}

URL='https://www.linkedin.com/uas/login-submit'
s=requests.session()
s.post(URL,data=payload)

r = s.get('https://www.linkedin.com/vsearch/f?type=all&keywords=software&orig=GLHD&rsid=&pageKey=oz-winner&trkInfo=tarId%3A1453520431435&search=Search')

print(r)

html = r.read()

html = str(html)

html = html.encode('utf-8')

