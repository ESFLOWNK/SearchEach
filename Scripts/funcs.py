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

    for i in cont:
        if i.find(sr) != i.rfind(sr):
            content.append(i[i.find(sr):i.rfind(sr)+1])

    return content

def write(cont: list,flr: str,sr: str):
    
    f = open(flr,'w')

    if len(cont) > 0:
        f.write(cont[0])

    for i in cont:
        if i == '' or i == cont[0]:
            continue

        f.write("\n"+i)
    
    f.close()
