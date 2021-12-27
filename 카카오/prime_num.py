import math

def cnt_prime(num_targets):

    count_prime = 0

    for number in num_targets:
        divide_counter = 0
        mid = int(math.sqrt(int(number)))

        for i in range(1,mid+1):
            if int(number) % i == 0:
                divide_counter += 1
        if divide_counter < 2:
            count_prime += 1

    return count_prime


def solution(n, k):

    if n == 0 or n == 1:
        return 0

    k_transformed = ''

    while n > 0:
        n,mod = divmod(n,k)
        k_transformed += str(mod)

    k_transformed = k_transformed[::-1]

    zero_idx = [i for i,num in enumerate(k_transformed) if num == '0']

    if len(zero_idx) == 0:
        return cnt_prime([int(k_transformed)])

    else:

        num_targets = []
        if k_transformed[:min(zero_idx)] != '1' :
            num_targets.append(k_transformed[:min(zero_idx)])


        if k_transformed[max(zero_idx)+1:] != '1' and k_transformed[max(zero_idx)+1:] != '':
            num_targets.append(k_transformed[max(zero_idx)+1:])


        for i in range(len(zero_idx)-1):

            num_participant = k_transformed[zero_idx[i]+1:zero_idx[i+1]]

            if num_participant != '':
                if int(num_participant) > 1:
                    num_targets.append(num_participant)
            else:
                pass

        return cnt_prime(num_targets)


n = 1000000
k = 10
print(solution(n,k))
