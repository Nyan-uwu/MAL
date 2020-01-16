import os
import sys

sys.path.insert(1, './_script/functions')
import setup
import malfilereader
import response
import lexer
import run

sys.path.insert(1, './_script/classes')
import memory

def main():
    _response = setup.main()
    if _response["status"] != 200:
        raise Exception(_response["message"])
    
    _file = malfilereader.read(sys.argv[1])
    # print(_file)
    tokenFile = lexer.main(_file)
    # print(tokenFile)
    # for t in tokenFile.tokens:
    #     print(t)

    mem = memory.Memory()
    mem = run.run(mem, tokenFile)
    print(tokenFile.outString)
    print(mem.mem)
    print(tokenFile.labels)

    return response.create(200, "Run Successful")

exitresponse = main()
print(exitresponse)