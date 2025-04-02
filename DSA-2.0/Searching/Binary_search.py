def linear_search(number_list , number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index

    return -1    

def binary_searh(number_list, number_to_find):
    lef_index = 0
    right_index = len(number_list)-1
    mid = 0


    while lef_index <= right_index:
        mid_index = (lef_index + right_index ) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            lef_index  = mid_index + 1
        else:
            right_index  = mid_index -1

    return -1 


def find_all_occurence(numbers, number_to_find):
    index = binary_searh(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)



def binary_recursive(number_list , number_to_find , left_index ,right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index ) // 2
    if mid_index >= len(number_list) or mid_index < 0:
        return -1
    mid_number = number_list[mid_index]
    

    if mid_number == number_to_find:
        return mid_index
    
    if mid_number < number_to_find:
        left_index = mid_index + 1

    else:
        right_index = mid_index -1

    return binary_recursive(number_list , number_to_find, left_index , right_index)        

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = find_all_occurence(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")