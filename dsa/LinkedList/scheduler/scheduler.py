from queue import Queue
from cirqueue import ListBaseCircularQueue
class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum

    # def assignProcessor(self):
    #     q = ListBaseCircularQueue(self.processArrayLength)
    #     for i  in range(self.processArrayLength):
    #         data = self.processArray[i]
    #         time = data.processExecTime
    #         q.enqueue(data) 
    #     # print(q.get_item_at_index(3))
        
    #     # print(q.sized())
    #     while not q.isempty():
    #         i = 0
    #         # for i in range(q.sized()):
    #         while i < 4:
    #             print(i)
    #             item = q.get_item_at_index(i)
    #             # print('Time',type(item.processExecTime))
    #             time = item.processExecTime - self.timeQuantum
    #             item.processExecTime = time

    #             if item.processExecTime <= 0:
    #                 q.remove_at_index(i)
    #                 i-=1
                    
    #                 if item.processExecTime == 0:
    #                     print(f'Executing process {item.processName} by 5 units')
    #                     # i-=1
    #                 else:
    #                     print(f'Executing process {item.processName} by {5 - item.processExecTime} units')
    #                     # i+=1
                
    #             else:
    #                 print(f'Executing process {item.processName} by 5 units')
    #                 i+=1

    #             print(item.processExecTime)
                
    #         break
    #     # print(q.get_item_at_index(2).processExecTime)
    #     # while not q.is_empty():
    #     #     i = 0
        
    def assignProcessor(self):
        q = ListBaseCircularQueue(self.processArrayLength)
        for process in self.processArray:
            q.enqueue(process)
        
        while not q.isempty():
            current_process = q.dequeue()
            print(f"Processing {current_process.processName} for {self.timeQuantum} units of time.")
            remaining_time = current_process.processExecTime - self.timeQuantum
            if remaining_time <= 0:
                print(f"Process {current_process.processName} completed.")
            else:
                print(f"Process {current_process.processName} needs {remaining_time} units more.")
                current_process.processExecTime = remaining_time
                q.enqueue(current_process)
