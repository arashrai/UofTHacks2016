# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from time import time
from time import sleep
from random import randint

stime = time()

def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

def getJobLocation(html):
    if 'itemprop="description">' in html:
        n = html.index('itemprop="description">')
        n += len('itemprop="description">')
        if "</span>" in html[n:]:
            k = html[n:].index("</span>")
        else:
            return ['UNKNOWN',0]
        return [html_decode(html[n:n+k]),n]
    return ['UNKNOWN',0]

def getJobTitle(html):
    if 'itemprop="title">' in html:
        n = html.index('itemprop="title">')
        n += len('itemprop="title">')
        if "</h1>" in html[n:]:
            k = html[n:].index("</h1>")
        else:
            return ['UNKNOWN',0]
        return [html_decode(html[n:n+k]),n]
    return ['UNKNOWN',0]  

def getCompanyName(html):
    if 'itemprop="name">' in html:
        n = html.index('itemprop="name">')
        n += len('itemprop="name">')
        if "</span>" in html[n:]:
            k = html[n:].index("</span>")
        else:
            return ['UNKNOWN',0]
        return [html_decode(html[n:n+k]),n]
    return ['UNKNOWN',0]


def getJobDescription(html):
    if 'itemprop="description">' in html:
        n = html.index('itemprop="description">')
        n += len('itemprop="description">')
        if "similar-jobs-module" in html[n:]:
            k = html[n:].index("similar-jobs-module")
        else:
            return ['UNKNOWN',0]
        return [html_decode(html[n:n+k]),n]
    return ['UNKNOWN',0]


client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'(login email)',
    'session_password':'(password)',
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)

searchPage = 'https://www.linkedin.com/vsearch/j?keywords=computer+science&distance=50&locationType=I&countryCode=ca&postalCode=M5S+1A1&openFacets=L%2CC&page_num=1'

page_count = 1

while page_count < 41:

    searchPage = searchPage[:searchPage.index("num=")+4]
    searchPage = searchPage + str(page_count)
    
    response = client.get(searchPage)

    html = response.text

    links = []

    for x in html:
        if "https://www.linkedin.com/jobs2/view/" not in html:
            break
        n = html.index("https://www.linkedin.com/jobs2/view/")
        k = html[n+3:].index('",')
        if "vsrp_jobs_res_photo" in html[n:n+k]:
            print(html[n:n+k+3])
            links.append(html[n:n+k+3])
        html = html[n+4:]

    jobTitle = []
    companyName = []
    jobLocation = []
    jobDescription = []

    for x in links:
        sleep(randint(4,8))
        response = client.get(x)
        html = response.text
        store = getJobTitle(html)
        jobTitle.append(store[0])
        html = html[store[1]:]
        store = getCompanyName(html)
        companyName.append(store[0])
        html = html[store[1]:]
        store = getJobLocation(html)
        jobLocation.append(store[0])
        html = html[store[1]:]
        store = getJobDescription(html)
        jobDescription.append(store[0])
        html = html[store[1]:]
        with open('CompSciSearchPart1.txt', 'a', encoding='utf-8') as text_file:
            print("Job Title: ", jobTitle[-1], "  $%^& Company Name: ", companyName[-1], "  $%^&   Job Location: ", jobLocation[-1], "  $%^&   Job Description: ", jobDescription[-1], file = text_file)
            print("Job Title: ", jobTitle[-1], "  printed.")

    sleep(randint(4,15))
    print("SOMETHING SHOULDVE PRINTED")
    page_count += 1

print(time()-stime)
