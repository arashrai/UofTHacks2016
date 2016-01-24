k = open('datanohtml.txt',"r", encoding = 'utf-8')

lines = k.readlines()

L4 = []

for x in lines:
    L5 = x.split("$%^&")
    for y in range(len(L5)):
        k = L5[y].strip()
        L5[y] = k
    if len(L5) == 4:
        L4.append(L5[3])


parsedList = []

for x in range(len(L4)):
    a = L4[x].replace(',','')
    b = a.replace('.','')
    c = b.replace('-','')
    d = c.replace('/','')
    e = d.replace('(','')
    f = e.replace(')','')
    g = f.replace('?','')
    h = g.replace('*','')
    h = h.strip()
    h = h.lower()
    h = " " +h+" "
    parsedList.append(h)

tools = []

j = open('moretools2.txt',"r")

lines = j.readlines()

for x in lines:
    tools.append([0,x[:-1]])

for x in tools:
    for y in parsedList:
        string = " "+x[1]+" "
        if string in y:
            x[0] += 1

tools = sorted(tools)
tools.reverse()

with open("count.txt","w") as text_file:
    for x in tools:
        print(x[1] + " ", x[0], file = text_file)

with open("wordMap.txt","w") as text_file:
    for x in tools:
        print((x[1]+" ")*int(x[0]/10), file = text_file)
