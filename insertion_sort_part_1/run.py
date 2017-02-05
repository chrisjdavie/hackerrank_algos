from copy import copy

def run(input_arr):

    output_arr = []
    e = input_arr[-1]

    for i in range(2,len(input_arr)+1):
        
        if input_arr[-i] > e:
            input_arr[-(i-1)] = input_arr[-i]
            yield copy(input_arr)
        else:
            input_arr[-(i-1)] = e
            yield copy(input_arr)
            break
    else:
        input_arr[0] = e
        yield copy(input_arr)

if __name__ == "__main__":
    input()
    input_arr = list(map(int, input().strip().split()))
    for output_arr in run(input_arr):
        print(" ".join(map(str, output_arr)))

