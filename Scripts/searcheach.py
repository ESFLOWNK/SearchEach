#encoding="utf8"

import funcs
import sys
from msvcrt import getch

def main():

    if len(sys.argv) > 3:
        #fl = file
        #sr = searching
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

    cont = funcs.read(fl)

    ress = funcs.search(sr,cont)

    funcs.write(ress,flr,sr)

if __name__ == "__main__":
    main()
