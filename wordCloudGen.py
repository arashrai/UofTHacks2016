
f = open('count.txt', "r")

lines = f.readlines()
string = ""

L1 = []

for line in lines:
    print(line)
    k = line[:line.index(':')]
    k = k.replace(' ','')
    n = int(line[line.index(':')+1:])
    L1.append([k,n])


for x in L1:
    string += (x[0]+' ')*int(x[1]/10)

with open("wordMap.txt", "a") as text_file:
    print(string, file = text_file)

    
