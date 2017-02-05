import copy

def sort_one_index(input_arr, ind_sort):

    e = input_arr[ind_sort]

    for i in range(ind_sort-1, -1, -1):
        
        if input_arr[i] > e:
            input_arr[i+1] = input_arr[i]
        else:
            input_arr[i+1] = e
            break
    else:
        input_arr[0] = e

    return input_arr

def run(input_arr):
    
    for i in range(1, len(input_arr)):
        yield copy.copy(sort_one_index(input_arr, i))
