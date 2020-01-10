import sys

sys.path.insert(1, './_script/functions')
import response

def run(memory, tokenFile):
    indx = 0
    while indx < len(tokenFile.tokens):
        tok = tokenFile.tokens[indx]
        memory = tok.run(memory)
        indx += 1

    return memory