import time

def meta_sum(tree_sequence, index):
    nb_child_nodes = int(tree_sequence[index])
    nb_meta_entries = int(tree_sequence[index+1])
    # print("nb of child", nb_child_nodes)
    # print("nb of meta", nb_meta_entries)
    msum = 0
    if nb_child_nodes == 0:
        for i in range(index + 2, index + 2 + nb_meta_entries):
            msum += int(tree_sequence[i])
        return msum, index + 2 + nb_meta_entries
    else:
        ind = index + 2
        for n in range(nb_child_nodes):             
            (s, ind) = meta_sum(tree_sequence, ind)
            msum += s
        # print(ind)
        # time.sleep(1)
    for i in range(ind, ind + nb_meta_entries):
        msum += int(tree_sequence[i])
    return (msum, ind + nb_meta_entries)

def node_value(tree_sequence, index):
    nb_child_nodes = int(tree_sequence[index])
    nb_meta_entries = int(tree_sequence[index+1])
    # print("nb of child", nb_child_nodes)
    # print("nb of meta", nb_meta_entries)
    nval = 0
    if nb_child_nodes == 0:
        for i in range(index + 2, index + 2 + nb_meta_entries):
            nval += int(tree_sequence[i])
        return nval, index + 2 + nb_meta_entries
    else:
        ind = index + 2
        child_values = []
        for n in range(nb_child_nodes):             
            (s, ind) = node_value(tree_sequence, ind)
            child_values.append(s)

    for i in range(ind, ind + nb_meta_entries):
        el_ind = int(tree_sequence[i]) - 1
        if el_ind < nb_child_nodes:
            nval += child_values[el_ind]
    
    return (nval, ind + nb_meta_entries)


def main():

    f = open("input.txt", "r")
    line = f.readline()

    tree_sequence = line.split(" ")
    print("Tree length is:", len(tree_sequence))


    # metadata_sum = meta_sum(tree_sequence, 0)
    # print("Metadata sum is: ", metadata_sum)

    root_val = node_value(tree_sequence, 0)
    print("Root value is: ", root_val)
    

if __name__ == '__main__':
    main()