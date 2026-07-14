class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([ (x[0], x[1], idx) for idx, x in enumerate(tasks) ])
        
        curr_time = 0
        min_proc_hp = []


        ans = []
        task_idx = 0

        while len(ans) != len(tasks):
            # add all tasks less than curr_time
            while task_idx < len(tasks) and tasks[task_idx][0] <= curr_time:
                heapq.heappush(
                    min_proc_hp, 
                    (tasks[task_idx][1], tasks[task_idx][2])
                )
                task_idx+=1
            
            # pop
            # update curr_time
            if  min_proc_hp:
                time, idx = heapq.heappop(min_proc_hp)                
                
            else:
                start_time, time, idx = tasks[task_idx]
                curr_time = start_time
                task_idx+=1
                
            ans.append(idx)
            curr_time += time

        return ans
            

