from html.parser import HTMLParser
from time import time

stime = time()
avgChars = 3860

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

f = open('prilikResume.txt',"r")

lines = f.readlines()


prilikTokens = lines[0].split(' ')

L1 = []

for x in range(len(prilikTokens)):
    a = prilikTokens[x].replace(',','')
    b = a.replace('.','')
    c = b.replace('-','')
    d = c.replace('/','')
    e = d.replace('(','')
    f = e.replace(')','')
    f = f.strip()
    L1.append(f.lower())

resume = ' '.join(x for x in L1)
resume = " "+resume+" "

j = open('moretools2.txt',"r")
pword = open('personalitywords2.txt', "r")

lines = j.readlines()
lines2 = pword.readlines()

L2 = []
L7 = []

for x in lines:
    L2.append(x[:-1])

for x in lines2:
    L7.append(x[:-1])
    
L3 = [] #contains all keywords in resume + keyword list
L8 = []

for x in L2:
    if x in resume:
        L3.append(x)

for x in L7:
    if x in resume:
        L8.append(x)

k = open('datanohtml.txt',"r", encoding = 'utf-8')

lines = k.readlines()

L4 = []

for x in lines:
    L5 = x.split("$%^&")
    for y in range(len(L5)):
        k = L5[y].strip()
        L5[y] = k
    L4.append(L5)

for x in range(len(L4)):
    if L4[x] == ['']:
        L4[x] = 0
        
L4 = list(filter(None,L4))

def getJobMatchScore(jobDescription, L3, L8):
    descriptList = jobDescription.split(' ')
    parsedList = []
    for x in range(len(descriptList)):
        a = descriptList[x].replace(',','')
        b = a.replace('.','')
        c = b.replace('-','')
        d = c.replace('/','')
        e = d.replace('(','')
        f = e.replace(')','')
        g = f.replace('?','')
        h = g.replace('*','')
        h = h.strip()
        h = h.lower()
        parsedList.append(h)
    description = ' '.join(x for x in parsedList)
    description = " " + description + " "
    count = 0
    LMatches = []
    for x in L8:
        z = " "+x+" "
        if z in description:
            LMatches.append(x)
            count += 0.5
            
    for x in L3:
        k = " "+x+" "
        if k in description:
            LMatches.append(x)
            count += 1
    if 3860/len(jobDescription) < 1.15 and 3860/len(jobDescription) > 0.85:
        count = count * 3860/(len(jobDescription))
    elif 3860/len(jobDescription) > 1.15:
        count = count * 1.15
    else:
        count = count * 0.85
    return LMatches, count

LScore = []

for x in L4:
    if 3 == len(x)-1:
        LScore.append([getJobMatchScore(x[3],L3,L8)[1],L4.index(x)])
    else:
        LScore.append([0,0])

LScore = sorted(LScore)
LScore.reverse()
LScore = LScore[:10]
LTopTen = []

for x in LScore:
    LTopTen.append(L4[x[1]][:3])

print(time()-stime)
