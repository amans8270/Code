class CountingSort:
    def __init__(self,dataset={}):
        self.dataset=dataset
        self.step_counter=0
    def sort(self,arr):
        if self.dataset=={}:
            for i in arr:
                self.step_counter+=1
                if i not in self.dataset:
                    self.dataset[i]=1
                else:
                    self.dataset[i]+=1
        RANGE_OPENING=min(self.dataset.keys())
        RANGE_CLOSING=max(self.dataset.keys())
        result=[]
        for i in range(RANGE_OPENING,RANGE_CLOSING+1):
            self.step_counter+=1
            if i in self.dataset:
                result+=[i]*self.dataset[i]
        return result
    def get_step_counter(self):
        return self.step_counter
    def reset_counter(self,value=0):
        self.step_counter=value

            
if __name__ == '__main__':
    sorting_engine=CountingSort()
    arr=list(map(int,input("Enter dataset : ").strip().split()))
    print(sorting_engine.sort(arr))
    print(f"total steps : {sorting_engine.get_step_counter()}")
    sorting_engine.reset_counter()
    