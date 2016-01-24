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

j = open('programmingTools.txt',"r")

lines = j.readlines()

toolTokens = lines[0].split("', '")

toolTokens[0] = toolTokens[0][2:]
toolTokens[-1] = toolTokens[-1][:-2]

resume = ' '.join(x for x in L1)
resume = " "+resume+" "

L2 = []

for x in range(len(toolTokens)):
    a = toolTokens[x].replace(',','')
    b = a.replace('.','')
    c = b.replace('-','')
    d = c.replace('/','')
    d = d.strip()
    k = " "+d+" "
    if k in resume:
        L2.append([d,1])
    L2.append([d,0])
    
