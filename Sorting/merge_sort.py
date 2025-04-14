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


def merge_sort1(elements , key ,descending=False):
    size = len(elements)

    if size == 1:
        return elements
    
    left_list = merge_sort1(elements[0:size//2], key, descending)
    right_list= merge_sort1(elements[size//2:],key , elements)
    sorted_list = merge(left_list,right_list,key,descending)

    return sorted_list

def merge(left_list,right_list, key, descending=False):
    merged = []
    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    else:           
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    merged.extend(left_list)
    merged.extend(right_list)
    return merged

if __name__ == '__main__':
    # arr = [5,3,6,8,2,1,8,20,12,52,63,74,12,31,45]
    # merge_sort(arr)
    # print(arr)

    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort1(elements ,key='time_hours', descending=True)
    print(sorted_list)