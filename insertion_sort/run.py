from copy import copy

def run(input_arr):

    output_arr = []
    e = input_arr[-1]

    for i in range(2,len(input_arr)+1):
        if input_arr[-i] > e:
            input_arr[-(i-1)] = input_arr[-i]
            output_arr.append(copy(input_arr))
        else:
            input_arr[-(i-1)] = e
            output_arr.append(copy(input_arr))
            break
    else:
        input_arr[0] = e
        output_arr.append(copy(input_arr))

    return output_arr


