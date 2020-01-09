import os
import sys

sys.path.insert(1, './_script/functions')
import setup
import malfilereader
import response
import lexer

def main():
    _response = setup.main()
    if _response["status"] != 200:
        raise Exception(_response["message"])
    
    _file = malfilereader.read(sys.argv[1])
    # print(_file)
    tokenFile = lexer.main(_file)

    return response.create(200)

exitresponse = main()
print(exitresponse)