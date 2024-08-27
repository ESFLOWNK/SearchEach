
def search(sr: str, fl: str):
    """
    Search text between a character or more in the given file
    """

    #if "--and" in sr:
    #   Add code
    #   return

    #Result
    res = ""
    
    j = -1
    for i in range(len(fl)):
        if j == -1 and fl[i] == sr:
            j = i
        elif fl[i] == sr:
            res += fl[j:i+1] + "\n"
            j = -1

    return res[:-1]