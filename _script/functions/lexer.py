import sys

sys.path.insert(1, './_script/classes')
import file
import tokens
import response

sys.path.insert(1, './_script/resources')
import syntax

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
            
            if tok[0] == syntax.comment:
                break
            elif tok == syntax.mov:
                values["name"] = "mov"
                # Param 1
                indx += 1
                tok = linetok[indx].lower()
                if tok[0] == syntax.memloc:
                    values["params"].append(tokens.MemLoc({"name":"memloc", "value":int(tok[1:])}))
                else:
                    values["params"].append(tokens.Int({"name":"int", "value":int(tok)}))

                # Param 2
                indx += 1
                tok = linetok[indx].lower()
                if tok[0] == syntax.memloc:
                    values["params"].append(tokens.MemLoc({"name":"memloc", "value":int(tok[1:])}))
                else:
                    res = response.create("601", "Cannot move value to a non-memorylocation")
                    print(res)
                    raise Exception(res["message"])

                tokenFile.tokens.append(tokens.Mov(values))

            elif tok[0] == syntax.label:
                tokenFile.labels.append([tok[1:], len(tokenFile.tokens)])
                tokenFile.tokens.append(tokens.Label({"name":"label", "value":tok[1:]}))

            elif tok == syntax.jump:
                indx += 1
                tok = linetok[indx].lower()
                tokenFile.tokens.append(tokens.Jump({"name":"jmp", "value":tok}))

            elif tok in syntax.tests:
                values["name"] = tok
                # Value 1
                indx += 1
                tok = linetok[indx].lower()
                if tok[0] == syntax.memloc:
                    values["params"].append(tokens.MemLoc({"name":"memloc", "value":int(tok[1:])}))
                else:
                    values["params"].append(tokens.Int({"name":"int", "value":int(tok)}))

                # Value 2
                indx += 1
                tok = linetok[indx].lower()
                if tok[0] == syntax.memloc:
                    values["params"].append(tokens.MemLoc({"name":"memloc", "value":int(tok[1:])}))
                else:
                    values["params"].append(tokens.Int({"name":"int", "value":int(tok)}))
            
                tokenFile.tokens.append(tokens.Test(values))

            elif tok == syntax.ontrue:
                tokenFile.tokens.append(tokens.IfTrueBlockStart({"name":"truestart", "value":None}))
            elif tok == syntax.ontrueend:
                tokenFile.tokens.append(tokens.IfTrueBlockEnd({"name":"trueend", "value":len(tokenFile.tokens)}))
                tokens.findRelatedStartBlock_True(tokenFile.tokens, len(tokenFile.tokens)-1)
            elif tok == syntax.onfalse:
                tokenFile.tokens.append(tokens.IfFalseBlockStart({"name":"falsestart", "value":None}))
            elif tok == syntax.onfalseend:
                tokenFile.tokens.append(tokens.IfFalseBlockEnd({"name":"falseend", "value":len(tokenFile.tokens)}))
                tokens.findRelatedStartBlock_False(tokenFile.tokens, len(tokenFile.tokens)-1)
                    
            indx += 1
        indx = 0
        line += 1

    return tokenFile