import csv

def read(fl: str):
    content: list[str] = []
    
    f = open(fl,"r")
    lines = csv.reader(f)

    for ln in lines:
        content += ln

    return content

def search(sr: str,cont: list):
    content: list[str] = []

    res = ''
    into = False
    for i in cont:
        res = ''
        into = False
        for itr in range(len(i)-2):
            if into == True:
                res += i[itr]
            if i[itr] == sr:
                if into == True:
                    into = False
                if into == False:
                    into = True
        content.append(res)

    return content

def write(cont: list,flr: str,sr: str):
    
    f = open(flr,'w')

    cont.remove('')

    for i in cont:
        if i == '':
            continue
        if i == cont[len(cont)-1]:
            f.write(sr+i+sr)
            break
        f.write(sr+i+sr+"\n")
    
    f.close()
