class QuickSort:
    def __init__(self, comparator):
        self.comparator = comparator
        self.step_counter=0
    def patrition(self, arr):
        
        pivot = 0
        left, right = 0, len(arr) - 1
        while left < right:
            while self.comparator(arr[left], arr[pivot]) < 0 and left < right:
                left += 1
                self.step_counter+=1
            while self.comparator(arr[right], arr[pivot]) > 0 and left < right:
                right -= 1
                self.step_counter+=1
            arr[right], arr[left] = arr[left], arr[right]
            
        arr[pivot], arr[left] = arr[left], arr[pivot]
        return left

    def sort(self, arr):
        self.step_counter+=1
        # print(arr, 'debug')
        if len(arr) <= 1: return arr
        center = self.patrition(arr)
        return self.sort(arr[:center]) + [arr[center]] + self.sort(
            arr[center + 1:])
    def reset_counter(self,value=0):
        self.step_counter=value


if __name__ == "__main__":
    arr = list(map(int, input('Enter dataset : ').strip().split()))
    sorting_engine = QuickSort(lambda x, y: x - y)
    print('quick sorted : ', sorting_engine.sort(arr))
    print(f"step counter value : {sorting_engine.step_counter}")