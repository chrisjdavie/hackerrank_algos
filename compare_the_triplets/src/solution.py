

def competition( a, b ):
    return int(a > b), int(b > a)

def compare_scores( a_i, b_i ):
    
    sum_a_score = 0
    sum_b_score = 0

    for a, b in zip(a_i, b_i):
        a_score, b_score = competition(a, b)
        sum_a_score += a_score
        sum_b_score += b_score
    
    return sum_a_score, sum_b_score

#a_i = [ int(a) for a in raw_input().split() ]
#b_i = [ int(b) for b in raw_input().split() ]
#
#score_a, score_b = compare_scores( a_i, b_i )
#
#print "{} {}".format( score_a, score_b )
