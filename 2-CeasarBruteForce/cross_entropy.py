import math

def c_entr(testo):
    eng_fr = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
             0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406,
             0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
             0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

    alpha = "abcdefghijklmnopqrstuvwxyz"
    count_list = [0] * 26

    for x in testo:
        if x.isalpha():
            x = x.casefold()  
            if x in alpha:
                count_list[alpha.index(x)] += 1

    total_count = sum(count_list)
    
    sommatoria = 0
    for i in range(26):
        if count_list[i] > 0:
            p_i = count_list[i] / total_count
            q_i = eng_fr[i]
            sommatoria += p_i * math.log(q_i)

    
    return -sommatoria

