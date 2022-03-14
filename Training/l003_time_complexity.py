# You are given an integer n. Count the total of 1 + 2 + . . . + n.
# O(n) time and O(1) space
def count_total_v0(n): 
    result = 0
    for i in range(n):
        result += (i+1)
    return result

# O(n) time and O(1) space - FASTER
def count_total_v1(n): 
    result = 0
    for i in range((n+1)//2):
        nth_val = n - i
        result += i + 1 if (i+1) == nth_val else i + nth_val + 1

    return result

# O(1) time and space complexity - BEST SOLUTION
def count_total_v2(n):
    return n * (n+1) // 2


''' A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position 
    greater than or equal to Y. The small frog always jumps a fixed distance, D.

    Count the minimal number of jumps that the small frog must perform to reach its target.

    Write a function:

    def solution(X, Y, D)

    that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
'''
# O(n-m) time and O(1) space complexity
def num_jumps_v0(X, Y, D):
    counter = 0
    position = X
    while position < Y:
        position += D
        counter += 1

    return counter

# O(1) time and space
def num_jumps_v1(X, Y, D):
    num_count = (Y - X) // D
    
    if (Y - X) % D > 0:
        num_count += 1

    return num_count


''' An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly 
    one element is missing.

    Your goal is to find that missing element.
'''
# O(n) time and O(1) space 
def missing_num_v0(A):
    N = len(A)

    sum_A = 0
    for i in A:
        sum_A += i

    return ((N+1) * (N+2) // 2) - sum_A


# O(n) time and O(1) space -> FASTER THAN ABOVE
def missing_num_v1(A):
    N = len(A)

    sum_A = 0
    for i in range((N+1)//2):
        index_end = N - i - 1
        sum_A += A[i] if i == index_end else A[i] + A[index_end]
            
    return ((N+1) * (N+2) // 2) - sum_A

# To essentially improve on the complexity you could
# So it skips 5 times -> NOT AS FAST AS ABOVE
def missing_num_v1(A):
    N = len(A)

    sum_A = 0
    for i in range(0, N, 5):
        i0 = A[i]
        i1 = A[i+1] if i+1 < N else 0
        i2 = A[i+2] if i+2 < N else 0
        i3 = A[i+3] if i+3 < N else 0
        i4 = A[i+4] if i+4 < N else 0
        sum_A += i0 + i1 + i2 + i3 + i4
            
    return ((N+1) * (N+2) // 2) - sum_A



''' A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

    Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

    The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

    In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

    For example, consider array A such that:

        A[0] = 3
        A[1] = 1
        A[2] = 2
        A[3] = 4
        A[4] = 3
    We can split this tape in four places:

    P = 1, difference = |3 − 10| = 7
    P = 2, difference = |4 − 9| = 5
    P = 3, difference = |6 − 7| = 1
    P = 4, difference = |10 − 3| = 7
    Write a function:

    def solution(A)

    that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
'''
# O(n**2) time and O(1) space
def min_difference_v0(A):
    N = len(A)
    min_diff = float('inf')
    for i in range(1, N):
        first_sum = sum_part(A, 0, i)
        second_sum = sum_part(A, i, N)
        min_diff = abs(second_sum - first_sum) if min_diff > abs(second_sum - first_sum) else min_diff

    return min_diff

def sum_part(A, start, stop):
    result = 0
    for i in range(start, stop):
        result += A[i]
    return result

# O(n) time and O(1) space
def min_difference_v1(A):
    N = len(A)
    sum_A = 0
    for i in range((N+1)//2):
        index_end = N - i - 1
        sum_A += A[i] if i == index_end else A[i] + A[index_end]

    min_diff = float('inf')
    first_sum = 0
    for i in range(1, N):
        first_sum += A[i-1]
        second_sum = sum_A - first_sum

        min_diff = abs(second_sum - first_sum) if min_diff > abs(second_sum - first_sum) else min_diff

    return min_diff
    

# O(n) time and O(1) space
def min_difference_v2(A):
    N = len(A)
    sum_A = sum(A)
    min_diff = float('inf')
    first_sum = 0
    for i in range(1, N):
        first_sum += A[i-1]
        second_sum = sum_A - first_sum

        min_diff = abs(second_sum - first_sum) if min_diff > abs(second_sum - first_sum) else min_diff

        if min_diff == 0: break # Just to make it a bit faster since no +ve integer is lesser then 0

    return min_diff