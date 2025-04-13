def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left,right,arr)

def merge_two_sorted_lists(a,b,arr):
    # sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i  < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            # sorted_list.append(a[i])
            i+=1
        else:
            arr[k] = b[j]
            # sorted_list.append(b[j])
            j +=1
        k +=1    
    while i < len_a:
        arr[k] = a[i]
        # sorted_list.append(a[i])
        i +=1
        k+=1
    while j < len_b:
        arr[k] = b[j]
        # sorted_list.append(b[j])
        j += 1
        k +=1


if __name__ == '__main__':
    arr = [5,3,6,8,2,1,8,20,12,52,63,74,12,31,45]
    merge_sort(arr)
    print(arr)