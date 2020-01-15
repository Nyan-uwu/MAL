def read(_filename):
    file  = open(_filename, "r").read()
    sfile = file.split("\n")
    # print(sfile)
    ffile = []
    for line in sfile:
        ffile.append(__cleanline__(line.split(" ")))
    return ffile

def __cleanline__(_lineArr):
    i = len(_lineArr)-1
    while i >= 0:
        if _lineArr[i] == "    " or _lineArr[i] == " " or _lineArr == "":
            _lineArr.remove(i)
        i -= 1
    return _lineArr
