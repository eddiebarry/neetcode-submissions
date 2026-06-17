class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:        
        if not tasks:
            return []

        ans = []
        tasks = sorted((x,idx) for idx, x in enumerate(tasks))
        # print(tasks)
        curr_time = tasks[0][0][0]
        # print(curr_time)
        curr_idx = 0

        tasks_on_heap = []

        # print(tasks_on_heap)

        while tasks_on_heap or curr_idx < len(tasks):            
            while curr_idx < len(tasks) and tasks[curr_idx][0][0] <= curr_time:
                heapq.heappush(
                    tasks_on_heap, (tasks[curr_idx][0][1], tasks[curr_idx][1]) 
                )
                curr_idx+=1

            if not tasks_on_heap:
                heapq.heappush(
                    tasks_on_heap, (tasks[curr_idx][0][1], tasks[curr_idx][1]) 
                )
                curr_idx+=1
                curr_time = tasks[curr_idx][0][0]

            ans.append(tasks_on_heap[0][1])
            time = tasks_on_heap[0][0]
            curr_time += time
            heapq.heappop(tasks_on_heap)

        return ans

        