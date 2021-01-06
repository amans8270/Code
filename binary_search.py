def bin_search(arr, ele):
    start=0
    end =len(arr)-1
    while start <= end:
        # print(arr[start:end])
        mid = (start + end) // 2
        if arr[mid] == ele:
            return mid + 1
        elif arr[mid] < ele:
            start = mid + 1
        elif arr[mid] > ele:
            end = mid - 1
    return "Not Found"


if __name__ == "__main__":
    print(
        'found : ',
        bin_search(list(map(int,
                            input("Enter data : ").strip().split())),
                   int(input("Enter num to search : "))))
