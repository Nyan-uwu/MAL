import sys

sys.path.insert(1, './_script/classes')
import file
import tokens

def main(inp):

    tokenFile = file.File()
    # print(inp)

    line = 0
    indx = 0

    cTok = None

    while line < len(inp):
        linetok = inp[line]
        while indx < len(linetok):
            tok = linetok[indx].lower()

            if tok == "mov":
                indx += 1
                tok = linetok[indx].lower()
                
            
            indx += 1
        line += 1

    return tokenFile