import sys
import response
sys.path.insert(1, './_script/recources')
import syntax

def run(memory, tokenFile):
    indx = 0
    intrue = False
    infalse = False
    
    while indx < len(tokenFile.tokens):
        tok = tokenFile.tokens[indx]
        # print(tok)
        # print(str(intrue) + ":" + str(infalse))
        if tok.name == "jmp":
            indx = tok.run(tokenFile)
        elif tok.name == "out":
            tokenFile.outString += str(chr(tok.run(memory)))
        elif tok.name == "trueend":
            intrue = False
        elif tok.name == "truestart":
            if intrue:
                # print("running true")
                pass
            elif not intrue:
                indx = tok.value
        elif tok.name == "falseend":
            infalse = False
        elif tok.name == "falsestart":
            # print("running false")
            if infalse:
                pass
            elif not infalse:
                indx = tok.value
        elif tok.name in syntax.tests:
            result = tok.run(memory)
            # print("RESULT = {}".format(result))
            if result == True:
                intrue = True
                infalse = False
            elif result == False:
                intrue = False
                infalse = True
        else:
            memory = tok.run(memory)
        indx += 1

    return memory