import time

def getRootNodes(graph, nodeParents):
    roots = []
    for node in graph.keys():
        if node not in nodeParents:
            roots.append(node)
    return roots

def displayNodes(roots, graph, nodeParents, output):
    isVisited = {}
    roots.sort()
    while roots:
           
        node = roots.pop(0)

        # Checking if node is ready for display
        notReady = False
        # print("roots are: ", roots)
        if node in nodeParents:
            # print(node," parents are: ", nodeParents[node])
            for x in nodeParents[node]:            
                if x not in isVisited:
                    notReady = True
                    break
        
        if notReady:
            # print(node," cant be displayed")
            # time.sleep(1)
            roots.append(node)
            continue

        output.append(node)
        isVisited[node] = True
        # time.sleep(1)
        # print(''.join(output))
        if node in graph:
            for x in graph[node]:
                if x not in roots:
                    roots.append(x)
        roots.sort()
    return output

def getCompletionTime(roots, graph, nodeParents, nb_workers):
    max_time = 1000
    avail_work = roots
    avail_workers = range(nb_workers)
    
    # Map each task to duration
    work_units = {}
    incr = 1
    for unit in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        work_units[unit] = {'duration': 60 + incr}
        incr += 1

    current_tasks = []
    worker_task_map = {}
    completed_tasks = []
    avail_child_work = []
    
    for t in range(max_time):

        while avail_work:
            if avail_workers:
                unit = avail_work.pop(0)
                current_tasks.append(unit)
                worker = avail_workers.pop(0)
                work_units[unit]['worker'] = worker
                worker_task_map[worker] = unit
            else:
                break
        
        #print(avail_work)
        #print(avail_workers)
        #print(current_tasks)
        # Print progress
        wk_tsk_output = ""
        tsk_completed = ""
        for wk in range(nb_workers):
            if wk in worker_task_map:
                wk_tsk_output += worker_task_map[wk] + " "
        for tsk in completed_tasks:
            tsk_completed += tsk
        print("{} {} {}".format(t, wk_tsk_output, tsk_completed))
        # time.sleep(1)

        # Add children and ready tasks in available work
        for tsk in current_tasks:
            work_units[tsk]['duration'] -= 1
        for tsk in current_tasks:
            if work_units[tsk]['duration'] == 0:
                if tsk in graph:
                    for t in graph[tsk]:
                        if t not in avail_child_work and t not in completed_tasks:
                            avail_child_work.append(t)
        
        
        # Remove task with incomplete dependencies
        tmp_arr = avail_child_work[:]
        while tmp_arr:
            tsk = tmp_arr.pop(0)           
            if tsk in nodeParents:
                isReady = True
                for node in nodeParents[tsk]:
                    if work_units[node]['duration'] != 0:
                        isReady = False
                if isReady:
                    avail_work.append(tsk)
                    avail_child_work.remove(tsk)
        
        # Collect completed tasks
        tmp_arr = current_tasks[:]
        while tmp_arr:
            tsk = tmp_arr.pop(0)
            if work_units[tsk]['duration'] == 0:
                completed_tasks.append(tsk)
                worker = work_units[tsk]['worker']
                avail_workers.append(worker)
                worker_task_map[worker] = '_'
                current_tasks.remove(tsk)
        
        


        # Sort tasks
        avail_work.sort()
        avail_workers.sort()

        if not current_tasks and not avail_work:
            break
    return t+1        
        





def main():

    f = open("input.txt", "r")
    lines = f.readlines()
    graph = {}
    nodeParents = {}
    output = []
    for line in lines:
        arr = line.split(" ")
        node1 = arr[1]
        node2 = arr[7]
        if node1 not in graph:
            graph[node1] = []
        graph[node1].append(node2)
        if node2 not in nodeParents:
            nodeParents[node2] = []
        nodeParents[node2].append(node1)

    roots = getRootNodes(graph, nodeParents)
    print("Roots: ", roots)
    # output = displayNodes(roots, graph, nodeParents, output)
    # print(''.join(output))
    nb_workers = 3
    completion_time = getCompletionTime(roots, graph, nodeParents, nb_workers)
    print("work completed in: ", completion_time)


if __name__ == '__main__':
    main()