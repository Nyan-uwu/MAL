import sys

sys.path.insert(1, './_script/classes')
import file
import tokens

def main(inp):
    tokenFile = file.File()
    # print(inp)

    line = 0
    indx = 0

    while line < len(inp):
        linetok = inp[line]
        # print(linetok)
        while indx < len(linetok):
            values = {
                "name":None,
                "params":[]
            }
            tok = linetok[indx].lower()

            if tok == "mov":
                values["name"] = "mov"
                # Param 1
                indx += 1
                tok = linetok[indx].lower()
                if tok[0] == "$":
                    values["params"].append(tokens.MemLoc({"name":"memloc", "value":int(tok[1:])}))
                else:
                    values["params"].append(tokens.Int({"name":"int", "value":int(tok)}))

                # Param 2
                indx += 1
                tok = linetok[indx].lower()
                if tok[0] == "$":
                    values["params"].append(tokens.MemLoc({"name":"memloc", "value":int(tok[1:])}))
                else:
                    res = response.create("601", "Cannot move value to a non-memorylocation")
                    print(res)
                    raise Exception(res["message"])

                tokenFile.tokens.append(tokens.Mov(values))
            indx += 1
        indx = 0
        line += 1

    return tokenFile