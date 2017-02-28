
def mini_max_sum(nums):

    sum_nums = sum(nums)

    sum_less_i = [ sum_nums - n_i for n_i in nums ]

    return min(sum_less_i), max(sum_less_i)

#nums = [ int(n_i) for n_i in raw_input().split() ]
#mini, maxi = mini_max_sum(nums)
#
#print "{} {}".format(mini, maxi)

