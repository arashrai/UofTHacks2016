f = open('personalitywords.txt','r')

lines = f.readlines()

L1 = []

L2 = []

for x in lines:
    L1.append(x[:-1])

for x in L1:
    y = x.strip()
    z = y.lower()
    a = z.replace(',','')
    b = a.replace('.','')
    c = b.replace('-','')
    d = c.replace('/','')
    L2.append(d)

L2 = list(set(L2))

with open("personalitywords2.txt","a") as text_file:
    for x in L2:
        print(x, file = text_file)

