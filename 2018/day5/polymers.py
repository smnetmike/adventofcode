def collapsePolymer(sequence):
    result = ""
    xPred = ""
    for x in sequence.strip():
        if xPred == "":
            xPred = x
            result += x
            # print(result)
            continue

        if xPred != x and xPred.upper() == x.upper():
            result = result[:-1]
            if result != "":
                xPred = result[-1]
            else:
                xPred = ""
        else:
            result += x
            xPred = x
        # print(result)
    #print('string length: ', len(result))
    return len(result)

def main():

    f = open("input.txt", "r")
    sequence = f.readline()
    lengths = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for let in alphabet:
        newSeq = sequence.replace(let, '')
        newSeq = newSeq.replace(let.upper(), '')
        seqLen = collapsePolymer(newSeq)
        print('Collapsing without ', let, ' produce length ', seqLen)
        lengths[let] = seqLen
    optLet = min(lengths.keys(), key=(lambda k: lengths[k]))
    print("Optimal letter is ", optLet, "with collapsing size ", lengths[optLet] )

if __name__ == '__main__':
    main()