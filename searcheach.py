#encoding="utf8"

from pathlib import Path
import sys
from msvcrt import getch

def search(sr: str = "",ssr = None, fl: str = ""):
    """
    Search text between a character or two in the given file
    """
    
    #Result
    res = ""
    j = -1

    #Two characters case
    if ssr:
        #K is used for know when there are searched text inside searched text
        #Example (text(inside text))
        k = 1
        for i in range(len(fl)):
            if j == -1 and fl[i] == sr:
                j = i
            elif fl[i] == sr:
                k += 1
            elif not j == -1 and fl[i] == ssr:
                k -= 1
                if k == 0:
                    res += fl[j:i+1] + "\n"
                    k = 1
                    j = -1
                    
        return res[:-1]
    
    #One character case
    for i in range(len(fl)):
        if j == -1 and fl[i] == sr:
            j = i
        elif fl[i] == sr:
            res += fl[j:i+1] + "\n"
            j = -1

    return res[:-1]

def main():

    if len(sys.argv) == 4:
        #fl = file
        #sr = searching
        #flr file result
        fl = sys.argv[1]
        sr = sys.argv[2]
        flr = sys.argv[3]
    
        if sr == "strings":
            sr = '"'

        res = search(sr=sr,fl=Path(fl).read_text())

    elif len(sys.argv) == 5:
        #fl = file
        #sr = searching
        #ssr second searching
        #flr file result
        fl = sys.argv[1]
        sr = sys.argv[2]
        ssr = sys.argv[3]
        flr = sys.argv[4]

        res = search(sr=sr,ssr=ssr,fl=Path(fl).read_text())

    else:
        print("searcheach FILE CHARACTER [CHARACTER2] FILE_RESULT\n"+
        "\tFILE = The file to check\n"+
        "\tCHARACTER = The character used for searching texts between it\n"+
        "\tCHARACTER2 = (Optional) Texts will be searched between CHARACTER and CHARACTER2\n"+
        "\tFILE_RESULT = The name of the file where the results will be writen\n\n"+
        "Press any key to exit...")
        getch()
        return

    Path(flr).write_text(res)

if __name__ == "__main__":
    main()
