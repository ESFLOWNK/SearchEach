#encoding="utf8"

import funcs
from pathlib import Path
import sys
from msvcrt import getch

def main():

    if len(sys.argv) > 3:
        #fl = file
        #sr = searching
        #flr file result
        fl = sys.argv[1]
        sr = sys.argv[2]
        flr = sys.argv[3]

        if sr == "strings":
            sr = '"'

    else:
        print("searcheach [FILE] [CHARACTER] [FILE_RESULT]\n"+
        "\tFILE = The file to check\n"+
        "\tCHARACTER = The character that the program will search and show its content\n"+
        "\tFILE_RESULT = The name of the file where the data will be write")
        getch()
        exit()

    res = funcs.search(sr,Path(fl).read_text())

    #funcs.write(res,flr,sr)
    Path(flr).write_text(res)

if __name__ == "__main__":
    main()
