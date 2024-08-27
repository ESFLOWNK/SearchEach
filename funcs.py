
def search(sr: str = "",ssr = None, fl: str = ""):
    """
    Search text between a character or two in the given file
    """
    
    #Result
    res = ""

    j = -1
    if ssr:
        for i in range(len(fl)):
            if j == -1 and fl[i] == sr:
                j = i
            elif not j == -1 and fl[i] == ssr:
                res += fl[j:i+1] + "\n"
                j = -1

        return res[:-1]
    
    for i in range(len(fl)):
        if j == -1 and fl[i] == sr:
            j = i
        elif fl[i] == sr:
            res += fl[j:i+1] + "\n"
            j = -1

    return res[:-1]