from statistics import mean

global seq_set
seq_set = []

def sub_seq_match(arr, numb):
    op = [None for i in range(len(arr))]
    subsequence(arr, op, 0, 0)
    # print(seq_set)
    print("Sequences matching arithmetic mean: ", numb)
    for seq in seq_set:
        if mean(seq) == numb:
            print(seq)


def subsequence(s, op, i, j):
    # print(i,j,op)
    if i == len(s):
        return
    else:
        if j == 0 or op[j-1] == s[i-1]:       
            op[j] = s[i]
        seq_set.append([x for x in op if x])
        op_copy1 = op.copy()
        op_copy2 = op.copy()
        subsequence(s, op_copy1, i+1, j+1)
        subsequence(s, op_copy2, i+1, j)
        return


if __name__ == '__main__':
    arr = [1,2,3]
    numb = 2
    sub_seq_match(arr, numb)