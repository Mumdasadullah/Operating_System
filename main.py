# SJF IMPLEMENTED
class SJF:
    def __init__(self):
        self.Id = 0,
        self.arrivalTime = 0,
        self.executionTime = 0,
        self.startTime = 0,
        self.endTime = 0,
        self.turnaroundTime = 0,
        self.waitTime = 0,
        self.utlization = 0,
        self.isVisited = False

Process_SJF = []
Visited_SJF = []

#def print_func_SJF():
#    for i in range (len(Process_SJF)):
#        print(f"{Process_SJF[i].Id}  {Process_SJF[i].arrivalTime}  {Process_SJF[i].executionTime}")
#        print()

def print_gantt_chart_SJF():
    print("\nGantt Chart")
    print("---------------------------------")
    #for j in range (len(Visited)):
    j = 0
    while (j < len(Visited_SJF)):
        if (j == 0):
            if(Visited_SJF[j].arrivalTime != 0):
                #Visited[j].isVisited == False
                print("|  Idle  ", end="")
                print(f"|  {Visited_SJF[j].Id}  ", end="")
                #j-=1
                #continue
                #print(f"|  {Visited[j].Id}  ", end="")
            else:
                print(f"|  {Visited_SJF[j].Id}  ", end="")
        else:
            print(f"|  {Visited_SJF[j].Id}  ", end="")

        j+=1
    print("|")
    print("---------------------------------")
    z = 0
    #for z in Visited:
    while (z < len(Visited_SJF)):
        if(z==0):
            if(Visited_SJF[z].arrivalTime != 0):
                print("0         ", end="")
                print(f"{Visited_SJF[z].startTime}    ", end="")
            else:
                print(f"{Visited_SJF[z].startTime}    ", end="")
        else:
            print(f"{Visited_SJF[z].startTime}    ", end="")
        z+=1
    print(f"{Visited_SJF[-1].endTime}")

def print_table_SJF():
    print("\nTable")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("| Process | Arrival Time | Execution Time | Start Time | End Time | Turnaround Time | Waiting Time | Utilization", end="")
    print(" |")
    print("--------------------------------------------------------------------------------------------------------------------")
    for u in Process_SJF:
        print("|   P{:d}    |     {:3d}      |    {:3d}         |   {:3d}      |   {:3d}    |      {:3d}        |      {:3d}     |      {:3}  |".format(
            u.Id, u.arrivalTime, u.executionTime, u.startTime, u.endTime, u.turnaroundTime, u.waitTime, u.utilization))
        #print(f"  {u.Id}  |  {u.arrivalTime}  |  {u.executionTime}   |   {u.startTime}  |  {u.endTime}  |  {u.turnaroundTime}  |  {u.waitTime}  |  {u.utilization}")
    print("--------------------------------------------------------------------------------------------------------------------")
    print_gantt_chart_SJF()
    
def take_no_of_process_SJF():
    n = int(input("Enter the Number of Processes : "))
    take_arr_exe_input_SJF(n)

def take_arr_exe_input_SJF(n):
    for i in range (n):
        proc = SJF()
        proc.Id = i + 1
        proc.arrivalTime = int(input(f"Enter the Arrival Time of Process {i + 1} : "))
        proc.executionTime = int(input(f"Enter the Execution Time of Process {i + 1} : "))
        Process_SJF.append(proc)
    #sort_func_SJF(Process)

def sort_func_SJF(Process):
    for i in range (len(Process_SJF)-1,0,-1):
        #j = i + 1
        for j in range (i):
            if (Process_SJF[j].arrivalTime > Process_SJF[j+1].arrivalTime):
                #print("ASAD")
                temp = SJF()
                temp = Process_SJF[j+1]
                Process_SJF[j+1] = Process_SJF[j]
                Process_SJF[j] = temp
                #swap(Process[i].executionTime,Process[i+1].executionTime)
    #print_func()

def ShortestJobFirst():
    st_time = Process_SJF[0].arrivalTime
    end_time = Process_SJF[0].arrivalTime
    t = 0
    while (t < len(Process_SJF)):
        if (Process_SJF[t].isVisited == False):
            y = t
            while (y < len(Process_SJF)-1):
                if (Process_SJF[t].executionTime == Process_SJF[y+1].executionTime and Process_SJF[t].isVisited == False and Process_SJF[y+1].isVisited == False):
                    if (Process_SJF[t].arrivalTime < Process_SJF[y+1].arrivalTime):
                        Process_SJF[t].startTime = end_time
                        Process_SJF[t].endTime = st_time + Process_SJF[t].executionTime
                        Process_SJF[t].turnaroundTime = Process_SJF[t].endTime - Process_SJF[t].arrivalTime
                        Process_SJF[t].waitTime = Process_SJF[t].turnaroundTime - Process_SJF[t].executionTime
                        Process_SJF[t].utilization = round(((Process_SJF[t].executionTime / Process_SJF[t].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[t].executionTime
                        st_time = Process_SJF[t].endTime
                        Process_SJF[t].isVisited = True
                        Visited_SJF.append(Process_SJF[t])

                        Process_SJF[y+1].startTime = end_time
                        Process_SJF[y+1].endTime = st_time + Process_SJF[y+1].executionTime
                        Process_SJF[y+1].turnaroundTime = Process_SJF[y+1].endTime - Process_SJF[y+1].arrivalTime
                        Process_SJF[y+1].waitTime = Process_SJF[y+1].turnaroundTime - Process_SJF[y+1].executionTime
                        Process_SJF[y+1].utilization = round(((Process_SJF[y+1].executionTime / Process_SJF[y+1].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[y+1].executionTime
                        st_time = Process_SJF[y+1].endTime
                        Process_SJF[y+1].isVisited = True
                        Visited_SJF.append(Process_SJF[y+1])
                    else:
                        Process_SJF[t].startTime = end_time
                        Process_SJF[t].endTime = st_time + Process_SJF[t].executionTime
                        Process_SJF[t].turnaroundTime = Process_SJF[t].endTime - Process_SJF[t].arrivalTime
                        Process_SJF[t].waitTime = Process_SJF[t].turnaroundTime - Process_SJF[t].executionTime
                        Process_SJF[t].utilization = round(((Process_SJF[t].executionTime / Process_SJF[t].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[t].executionTime
                        st_time = Process_SJF[t].endTime
                        Process_SJF[t].isVisited = True
                        Visited_SJF.append(Process_SJF[t])

                        Process_SJF[y+1].startTime = end_time
                        Process_SJF[y+1].endTime = st_time + Process_SJF[y+1].executionTime
                        Process_SJF[y+1].turnaroundTime = Process_SJF[y+1].endTime - Process_SJF[y+1].arrivalTime
                        Process_SJF[y+1].waitTime = Process_SJF[y+1].turnaroundTime - Process_SJF[y+1].executionTime
                        Process_SJF[y+1].utilization = round(((Process_SJF[y+1].executionTime / Process_SJF[y+1].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[y+1].executionTime
                        st_time = Process_SJF[y+1].endTime
                        Process_SJF[y+1].isVisited = True
                        Visited_SJF.append(Process_SJF[y+1])
                        #y-=1
                elif (Process_SJF[t].executionTime > Process_SJF[y+1].executionTime and Process_SJF[y+1].isVisited == False):
                    if (Process_SJF[t].arrivalTime > Process_SJF[y+1].arrivalTime):
                        Process_SJF[y+1].startTime = end_time
                        Process_SJF[y+1].endTime = st_time + Process_SJF[y+1].executionTime
                        Process_SJF[y+1].turnaroundTime = Process_SJF[y+1].endTime - Process_SJF[y+1].arrivalTime
                        Process_SJF[y+1].waitTime = Process_SJF[y+1].turnaroundTime - Process_SJF[y+1].executionTime
                        Process_SJF[y+1].utilization = round(((Process_SJF[y+1].executionTime / Process_SJF[y+1].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[y+1].executionTime
                        st_time = Process_SJF[y+1].endTime
                        Process_SJF[y+1].isVisited = True
                        Visited_SJF.append(Process_SJF[y+1])

                        y-=1

                    elif (Process_SJF[t].arrivalTime == Process_SJF[y+1].arrivalTime):
                        Process_SJF[y+1].startTime = end_time
                        Process_SJF[y+1].endTime = st_time + Process_SJF[y+1].executionTime
                        Process_SJF[y+1].turnaroundTime = Process_SJF[y+1].endTime - Process_SJF[y+1].arrivalTime
                        Process_SJF[y+1].waitTime = Process_SJF[y+1].turnaroundTime - Process_SJF[y+1].executionTime
                        Process_SJF[y+1].utilization = round(((Process_SJF[y+1].executionTime / Process_SJF[y+1].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[y+1].executionTime
                        st_time = Process_SJF[y+1].endTime
                        Process_SJF[y+1].isVisited = True
                        Visited_SJF.append(Process_SJF[y+1])

                        #y-=1
                    elif(Process_SJF[y+1].arrivalTime <= end_time):
                        Process_SJF[y+1].startTime = end_time
                        Process_SJF[y+1].endTime = st_time + Process_SJF[y+1].executionTime
                        Process_SJF[y+1].turnaroundTime = Process_SJF[y+1].endTime - Process_SJF[y+1].arrivalTime
                        Process_SJF[y+1].waitTime = Process_SJF[y+1].turnaroundTime - Process_SJF[y+1].executionTime
                        Process_SJF[y+1].utilization = round(((Process_SJF[y+1].executionTime / Process_SJF[y+1].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[y+1].executionTime
                        st_time = Process_SJF[y+1].endTime
                        Process_SJF[y+1].isVisited = True
                        Visited_SJF.append(Process_SJF[y+1])
                        #break
                    else:
                        #print(f"{Process[t].Id}")
                        Process_SJF[t].startTime = end_time
                        Process_SJF[t].endTime = st_time + Process_SJF[t].executionTime
                        Process_SJF[t].turnaroundTime = Process_SJF[t].endTime - Process_SJF[t].arrivalTime
                        Process_SJF[t].waitTime = Process_SJF[t].turnaroundTime - Process_SJF[t].executionTime
                        Process_SJF[t].utilization = round(((Process_SJF[t].executionTime / Process_SJF[t].turnaroundTime) * 100),2)
                        end_time = st_time + Process_SJF[t].executionTime
                        st_time = Process_SJF[t].endTime
                        Process_SJF[t].isVisited = True
                        Visited_SJF.append(Process_SJF[t])
                        break
                y+=1

        if Process_SJF[t] not in Visited_SJF:
            #print("ASAD")
            if (Process_SJF[t].arrivalTime <= end_time):
                Process_SJF[t].startTime = end_time
                Process_SJF[t].endTime = st_time + Process_SJF[t].executionTime
                Process_SJF[t].turnaroundTime = Process_SJF[t].endTime - Process_SJF[t].arrivalTime
                Process_SJF[t].waitTime = Process_SJF[t].turnaroundTime - Process_SJF[t].executionTime
                Process_SJF[t].utilization = round(((Process_SJF[t].executionTime / Process_SJF[t].turnaroundTime) * 100),2)
                end_time = st_time + Process_SJF[t].executionTime
                st_time = Process_SJF[t].endTime
                Process_SJF[t].isVisited = True
                Visited_SJF.append(Process_SJF[t])
            else:
                Process_SJF[t].startTime = Process_SJF[t].arrivalTime
                Process_SJF[t].endTime = Process_SJF[t].arrivalTime + Process_SJF[t].executionTime
                Process_SJF[t].turnaroundTime = Process_SJF[t].endTime - Process_SJF[t].arrivalTime
                Process_SJF[t].waitTime = Process_SJF[t].turnaroundTime - Process_SJF[t].executionTime
                Process_SJF[t].utilization = round(((Process_SJF[t].executionTime / Process_SJF[t].turnaroundTime) * 100),2)
                end_time = Process_SJF[t].arrivalTime + Process_SJF[t].executionTime
                st_time = Process_SJF[t].endTime
                Process_SJF[t].isVisited = True
                Visited_SJF.append(Process_SJF[t])
            
        t+=1

    #for h in range (len(Visited)):
        #print(f"{Visited[h].Id}  {Visited[h].arrivalTime}  {Visited[h].executionTime}  {Visited[h].startTime}  {Visited[h].endTime}  {Visited[h].isVisited}")
        #print()
    print_table_SJF()
        
def SJF_main_func():
    take_no_of_process_SJF()
    sort_func_SJF(Process_SJF)
    ShortestJobFirst()
    
'''
print("--------------------------------------------------------------------------------------------------------------------------")
print("| Processes | Arrival time | Burst time | Wait time | Response time | Turnaround time | Completion time |    Start time  |")
print("--------------------------------------------------------------------------------------------------------------------------")

print("|   P{:d}      |     {:3d}      |    {:3d}     |   {:3d}     |       {:3d}     |      {:3d}        |      {:3d}        |      {:3}        |".format(
        i + 1, p[i]['AT'], p[i]['BT'], p[i]['WT'], response_times[i], p[i]['TAT'], p[i]['FT'], start_time))
'''

# HRRN IMPLEMENTATION

class HRRN:
    def __init__(self):
        self.Id = 0,
        self.arrivalTime = 0,
        self.executionTime = 0,
        self.startTime = 0,
        self.endTime = 0,
        self.responseRatio = 0,
        self.turnaroundTime = 0,
        self.waitTime = 0,
        self.utilization = 0,
        self.isVisited = False

Process_HRRN = []
Visited_HRRN = []

def print_func_HRRN():
    for i in range (len(Process_HRRN)):
        print(f"{Process_HRRN[i].Id}  {Process_HRRN[i].arrivalTime}  {Process_HRRN[i].executionTime}")
        print()

def print_gantt_chart_HRRN():
    print("\nGantt Chart")
    print("---------------------------------")
    #for j in range (len(Visited)):
    j = 0
    while (j < len(Visited_HRRN)):
        if (j == 0):
            if(Visited_HRRN[j].arrivalTime != 0):
                #Visited[j].isVisited == False
                print("|  Idle  ", end="")
                print(f"|  {Visited_HRRN[j].Id}  ", end="")
                #j-=1
                #continue
                #print(f"|  {Visited[j].Id}  ", end="")
            else:
                print(f"|  {Visited_HRRN[j].Id}  ", end="")
        else:
            print(f"|  {Visited_HRRN[j].Id}  ", end="")

        j+=1
    print("|")
    print("---------------------------------")
    z = 0
    #for z in Visited:
    while (z < len(Visited_HRRN)):
        if(z==0):
            if(Visited_HRRN[z].arrivalTime != 0):
                print("0         ", end="")
                print(f"{Visited_HRRN[z].startTime}    ", end="")
            else:
                print(f"{Visited_HRRN[z].startTime}    ", end="")
        else:
            print(f"{Visited_HRRN[z].startTime}    ", end="")
        z+=1
    print(f"{Visited_HRRN[-1].endTime}")

def print_table_HRRN():
    #Visited.sort(key=lambda x:x.Id)
    print("\nTable")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("| Process | Arrival Time | Execution Time | Start Time | End Time | Turnaround Time | Waiting Time | Utilization", end="")
    print(" |")
    print("--------------------------------------------------------------------------------------------------------------------")
    for u in Process_HRRN:
        print("|   P{:d}    |     {:3d}      |    {:3d}         |   {:3d}      |   {:3d}    |      {:3d}        |      {:3d}     |      {:3}  |".format(
            u.Id, u.arrivalTime, u.executionTime, u.startTime, u.endTime, u.turnaroundTime, u.waitTime, u.utilization))
        #print(f"  {u.Id}  |  {u.arrivalTime}  |  {u.executionTime}   |   {u.startTime}  |  {u.endTime}  |  {u.turnaroundTime}  |  {u.waitTime}  |  {u.utilization}")
    print("--------------------------------------------------------------------------------------------------------------------")
    print_gantt_chart_HRRN()
    
def take_no_of_process_HRRN():
    n = int(input("Enter the Number of Processes : "))
    take_arr_exe_input_HRRN(n)

def take_arr_exe_input_HRRN(n):
    for i in range (n):
        proc = HRRN()
        proc.Id = i + 1
        proc.arrivalTime = int(input(f"Enter the Arrival Time of Process {i + 1} : "))
        proc.executionTime = int(input(f"Enter the Execution Time of Process {i + 1} : "))
        Process_HRRN.append(proc)
    #sort_func(Process)

def sort_func_HRRN(Process_HRRN):
    for i in range (len(Process_HRRN)-1,0,-1):
        #j = i + 1
        for j in range (i):
            if (Process_HRRN[j].arrivalTime > Process_HRRN[j+1].arrivalTime):
                #print("ASAD")
                temp = HRRN()
                temp = Process_HRRN[j+1]
                Process_HRRN[j+1] = Process_HRRN[j]
                Process_HRRN[j] = temp
                #swap(Process[i].executionTime,Process[i+1].executionTime)
    #print_func()

def sort_func_HRRN_1(ready_queue):
    for i in range (len(ready_queue)-1,0,-1):
        #j = i + 1
        for j in range (i):
            if (ready_queue[j].responseRatio > ready_queue[j+1].responseRatio):
                #print("ASAD")
                temp = HRRN()
                temp = ready_queue[j+1]
                ready_queue[j+1] = ready_queue[j]
                ready_queue[j] = temp
                #swap(Process[i].executionTime,Process[i+1].executionTime)
    #print_func()

def Highest_Response_Ratio_Next():
    st_time = Process_HRRN[0].arrivalTime
    end_time = Process_HRRN[0].arrivalTime
    for i in range (len(Process_HRRN)):
        ready_queue = []
        for j in range(len(Process_HRRN)):
            if(Process_HRRN[j].arrivalTime <= end_time and Process_HRRN[j].isVisited == False):
                Process_HRRN[j].responseRatio = float(((end_time - Process_HRRN[j].arrivalTime) + Process_HRRN[j].executionTime) / Process_HRRN[j].executionTime)
                ready_queue.append(Process_HRRN[j])

        if (len(ready_queue) != 0):
            sort_func_HRRN_1(ready_queue)
            ready_queue[-1].startTime = end_time
            ready_queue[-1].endTime = st_time + ready_queue[-1].executionTime
            end_time = st_time + ready_queue[-1].executionTime
            st_time = ready_queue[-1].endTime
            ready_queue[-1].turnaroundTime = ready_queue[-1].endTime - ready_queue[-1].arrivalTime
            ready_queue[-1].waitTime = ready_queue[-1].turnaroundTime - ready_queue[-1].executionTime
            ready_queue[-1].utilization = round(((ready_queue[-1].executionTime / ready_queue[-1].turnaroundTime) * 100),2)
            for u in range(len(Process_HRRN)):
                if(Process_HRRN[u].Id == ready_queue[-1].Id):
                    break
            Process_HRRN[u].isVisited = True
            Visited_HRRN.append(Process_HRRN[u])

    #for h in range(len(Visited)):
        #print(f"{Visited[h].Id}  {Visited[h].arrivalTime}  {Visited[h].executionTime}  {Visited[h].isVisited}")
        #print()
    print_table_HRRN()
            
def HRRN_main_func():
    take_no_of_process_HRRN()
    sort_func_HRRN(Process_HRRN)
    Highest_Response_Ratio_Next()


# SRT IMPLEMENTED
class SRT:
    def __init__(self):
        self.Id = 0,
        self.arrivalTime = 0,
        self.executionTime = 0,
        self.ori_exec_time = 0,
        self.startTime = 0,
        self.endTime = 0,
        self.turnaroundTime = 0,
        self.waitTime = 0,
        self.utilization = 0,
        self.isVisited = False

Process_SRT = []
Visited_SRT = []
seq = []

#def print_func_SRT():
#    for i in range (len(Process_SRT)):
#        print(f"{Process_SRT[i].Id}  {Process_SRT[i].arrivalTime}  {Process_SRT[i].executionTime}")
#        print()

def print_gantt_chart_SRT():
    print("\nGantt Chart")
    print("---------------------------------------------------------------------------------------------------------------------")
    #for j in range (len(Visited)):
    j = 0
    while (j < len(seq)):
        print(f"|  {seq[j]}  ", end="")
        j+=1
    print("|")
    print("---------------------------------------------------------------------------------------------------------------------")
    z = 0
    #for z in Visited:
    while (z < len(seq)):
        if(z<10):
            print(f"{z}     ", end="")
        else:
            print(f"{z}    ", end="")
        z+=1
    print(f"{z}")

def print_table_SRT():
    #Visited.sort(key=lambda x:x.Id)
    Process_SRT.sort(key=lambda x:x.Id)
    print("\nTable")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("| Process | Arrival Time | Execution Time | Start Time | End Time | Turnaround Time | Waiting Time | Utilization", end="")
    print(" |")
    print("--------------------------------------------------------------------------------------------------------------------")
    for u in Process_SRT:
        print("|   P{:d}    |     {:3d}      |    {:3d}         |   {:3d}      |   {:3d}    |      {:3d}        |      {:3d}     |      {:3}  |".format(
            u.Id, u.arrivalTime, u.ori_exec_time, u.startTime, u.endTime, u.turnaroundTime, u.waitTime, u.utilization))
        #print(f"  {u.Id}  |  {u.arrivalTime}  |  {u.executionTime}   |   {u.startTime}  |  {u.endTime}  |  {u.turnaroundTime}  |  {u.waitTime}  |  {u.utilization}")
    print("--------------------------------------------------------------------------------------------------------------------")
    print_gantt_chart_SRT()
    
def take_no_of_process_SRT():
    n = int(input("Enter the Number of Processes : "))
    take_arr_exe_input_SRT(n)

def take_arr_exe_input_SRT(n):
    for i in range (n):
        proc = SRT()
        proc.Id = i + 1
        proc.arrivalTime = int(input(f"Enter the Arrival Time of Process {i + 1} : "))
        proc.executionTime = int(input(f"Enter the Execution Time of Process {i + 1} : "))
        proc.ori_exec_time = proc.executionTime
        Process_SRT.append(proc)
    #sort_func(Process)

def sort_func_SRT(Process_SRT):
    for i in range (len(Process_SRT)-1,0,-1):
        #j = i + 1
        for j in range (i):
            if (Process_SRT[j].arrivalTime > Process_SRT[j+1].arrivalTime):
                #print("ASAD")
                temp = SRT()
                temp = Process_SRT[j+1]
                Process_SRT[j+1] = Process_SRT[j]
                Process_SRT[j] = temp
                #swap(Process[i].executionTime,Process[i+1].executionTime)
    #print_func_SRT()

def ShortestRemainingTime():
    st_time = Process_SRT[0].arrivalTime
    end_time = Process_SRT[0].arrivalTime
    while True:
        #print("ASAD")
        ready_queue = []
        for i in range(len(Process_SRT)):
            if(Process_SRT[i].arrivalTime <= end_time and Process_SRT[i].isVisited == False):
                ready_queue.append(Process_SRT[i])

        if(len(ready_queue) == 0):
            break
        elif(len(ready_queue) != 0):
            ready_queue.sort(key=lambda x:x.executionTime)
            
            #print("ASAD")
            ready_queue[0].startTime = st_time
            ready_queue[0].endTime = end_time + 1
            end_time = st_time + 1
            st_time = ready_queue[0].endTime
            seq.append(ready_queue[0].Id)

            for k in range (len(Process_SRT)):
                if(Process_SRT[k].Id == ready_queue[0].Id):
                    break
            Process_SRT[k].executionTime = Process_SRT[k].executionTime - 1
            if(Process_SRT[k].executionTime == 0):
                Process_SRT[k].turnaroundTime = Process_SRT[k].endTime - Process_SRT[k].arrivalTime
                Process_SRT[k].waitTime = Process_SRT[k].turnaroundTime - Process_SRT[k].ori_exec_time
                Process_SRT[k].utilization = round(((Process_SRT[k].ori_exec_time / Process_SRT[k].turnaroundTime) * 100),2)
                Process_SRT[k].isVisited = True
                Visited_SRT.append(Process_SRT[k])
            
    #for h in range (len(Visited_SRT)):
        #print(f"{Visited_SRT[h].Id}  {Visited_SRT[h].arrivalTime}  {Visited_SRT[h].executionTime}  {Visited_SRT[h].startTime}  {Visited_SRT[h].endTime}  {Visited_SRT[h].isVisited}")
        #print()
    print_table_SRT()

def SRT_main_func():
    take_no_of_process_SRT()
    sort_func_SRT(Process_SRT)
    ShortestRemainingTime()


if __name__ == "__main__":
    print("Which Scheduling algorithm you want to use ?")
    print("1 for SJF, 2 for HRRN, 3 for SRT")
    print()
    inp = int(input("Enter number to use algorithm : "))

    while(inp != 1 and inp != 2 and inp != 3):
        print("Wrong Input Try Again")
        print()
        inp = int(input("Enter number to use algorithm : "))

    if(inp == 3):
        print("---------------------------------SRT Scheduling!---------------------------------")
        SRT_main_func()
    elif(inp == 2):
        print("---------------------------------HRRN Scheduling---------------------------------")
        HRRN_main_func()
    elif(inp == 1):
        print("---------------------------------SJF Scheduling---------------------------------")
        SJF_main_func()
