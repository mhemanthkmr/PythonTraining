arr = [2,5,8,12,16,23,38,56,72,91]
n = int(input("Enter the target number to search :"))
low = 0
high = len(arr)

while (low <= high):
    mid = (low + high) // 2
    if(arr[mid] == n) :
        print("Value Found")
        print(mid)
        break
    elif (arr[mid] > n) :
        high = mid - 1;
        # print(high)
    else :
        low = mid + 1;
        # print(low)


