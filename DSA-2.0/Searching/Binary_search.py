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


if __name__ == '__main__':
    numbers_list = [12,15,17,19,21,45,67]
    number_to_find = 450

    index = binary_searh(numbers_list , number_to_find)
    print(f"Number found at index {index} using Binary search")