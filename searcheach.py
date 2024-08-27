#encoding="utf8"

import funcs
from pathlib import Path
import sys
from msvcrt import getch

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

        res = funcs.search(sr=sr,fl=Path(fl).read_text())

    elif len(sys.argv) == 5:
        #fl = file
        #sr = searching
        #ssr second searching
        #flr file result
        fl = sys.argv[1]
        sr = sys.argv[2]
        ssr = sys.argv[3]
        flr = sys.argv[4]

        res = funcs.search(sr=sr,ssr=ssr,fl=Path(fl).read_text())

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
