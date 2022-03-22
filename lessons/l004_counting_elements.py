''' We can also store the data in a slightly different way, by making an array of counters. Each number may be counted in the array by using an index that 
    corresponds to the value of the given number.
'''
def count_elements(A, m):
    '''
        A - An array of positive integers
        m - Maximun number in the array
    '''
    count_array = [0] * (m + 1)
    for i in A:
        count_array[i] += 1
    
    return count_array

''' Counting the number of negative integers can be done in two ways. 

    * The first method is to add some big number to each value: so that, all values would be greater than or equal to zero.
      That is, we shift the representation of zero by some arbitrary amount to accommodate all the negative numbers we need.

    * In the second method, we simply create a second array for counting negative numbers.

'''

''' Problem: You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 
    respectively (0 <= ai, bi <= m).
    The goal is to check whether there is a swap operation which can be performed on these arrays in such a way that the sum of elements in array A equals the sum 
    of elements in array B after the swap. By swap operation we mean picking one element from array A and one element from array B and exchanging them.
'''
def swap_element_v0(A, B, m):
    sum_A = sum(A)
    sum_B = sum(B)

    diff = sum_B - sum_A
    if diff == 0: return None

    for i in B:
        if diff > 0 and i <= diff:
            for j in A:
                if i+j == abs(diff): return (True, i, j)
        
        elif diff < 0:
            for j in A:
                if i+j == abs(diff): return (True, i, j)

    return False

# A much better approach
def swap_element_v1(A, B, m):
    sum_A = sum(A)
    sum_B = sum(B)
    diff = abs(sum_A - sum_B)

    count_A = [0] * (m + 1)
    count_B = [0] * (m + 1)

    N = len(A)

    for i in range(N):
        count_A[A[i]] += 1
        count_B[B[i]] += 1

    counter = 0
    while counter <= diff:
        if count_A[counter] > 0 and count_B[diff - counter] > 0:
            return (True, counter, diff-counter)
        
        counter += 1

    return False


''' Their method 

    TODO: try to understand this
''' 
def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a

    if d % 2 == 1:
        return False

    d //= 2
    count = count_elements(A, m)
    for i in range(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            return True

    return False


a = [1, 3, 5, 6, 7, 9, 2, 9, 1, 6]
b = [2, 5, 1, 5, 2, 6, 2, 6, 11, 0]
print(sum(a))
print(sum(b))
print(fast_solution(a, b, 11))


''' A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the 
    opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

    You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

    The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position 
    across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the 
    speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

    For example, you are given integer X = 5 and array A such that:

    A[0] = 1
    A[1] = 3
    A[2] = 1
    A[3] = 4
    A[4] = 2
    A[5] = 3
    A[6] = 5
    A[7] = 4
    In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

    Write a function:

    def solution(X, A)

    that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

    If the frog is never able to jump to the other side of the river, the function should return −1.
'''
# O(m + n) and O(n) space
def frog_river_crossing_v0(X, A): 
    N = len(A)
    positions = set()
    
    for i in range(1, X+1):
        positions.add(i)

    for i in range(N):
        if A[i] in positions:
            positions.remove(A[i])

        if len(positions) == 0:
            return i
        
    return -1

# O(n) and O(n) space -- Faster solution
def frog_river_crossing_v1(X, A):
    N = len(A)
    positions = [0] * (X+1)
    positions_sum = (X * (X+1)) // 2 

    for i in range(N):
        if A[i] <= X:
            if positions[A[i]] == 0:
                positions_sum -= A[i]
                positions[A[i]] += 1
        
        if positions_sum == 0:
            return i

    return -1


# 0(n) better
def solution(X, A):
    expected_sum = (X * (X+1)) // 2
    current_sum = 0

    counter_array = [0] * (X+1)

    earliest_crossing_time = -1

    for i, element in enumerate(A):
        if element <= X:
            if counter_array[element] == 0:
                counter_array[element] += 1
                current_sum += element

        if current_sum == expected_sum:
            earliest_crossing_time = i
            break

    return earliest_crossing_time



''' A non-empty array A consisting of N integers is given.

    A permutation is a sequence containing each element from 1 to N once, and only once.

    For example, array A such that:

        A[0] = 4
        A[1] = 1
        A[2] = 3
        A[3] = 2
    is a permutation, but array A such that:

        A[0] = 4
        A[1] = 1
        A[2] = 3
    is not a permutation, because value 2 is missing.

    The goal is to check whether array A is a permutation.

    Write a function:

    def solution(A)

    that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
'''
# O(2n) and O(n) space
def perm_check_v0(A):
    max_element = max(A) # O(n)

    element_counts = [0] * (max_element + 1)
    sum_to_max = max_element * (max_element + 1) // 2

    for i in A: # O(n)
        if element_counts[i] > 0:
            return 0

        element_counts[i] += 1
        sum_to_max -= i

    if sum_to_max == 0:
        return 1
    else: 
        return 0

# O(2n) and O(n) space -- A little memory efficient
def perm_check_v1(A):
    maxA = max(A) # O(n)
    elements = set()
    sum_to_max = maxA * (maxA + 1) // 2

    for i in A: # O(n)
        if i in elements:
            return 0

        elements.add(i)
        sum_to_max -= i

    if sum_to_max == 0:
        return 1
    else:
        return 0


# O(n) and O(n) space -- A little memory efficient and faster
def perm_check_v2(A):
    sumA = 0
    maxA = 0
    elements = set()

    for i in A:
        if i in elements:
            return 0

        elements.add(i)
        sumA += i
        if maxA < i: maxA = i

    sum_to_max = maxA * (maxA + 1) // 2
    if sum_to_max == sumA:
        return 1
    else: return 0


# Better
def solution(A):
    N = len(A)

    counter_array = [0] * (N+1)

    for element in A:
        if element <= N:
            if counter_array[element] == 0:
                counter_array[element] += 1
            elif counter_array[element] == 1:
                return 0
        else:
            return 0
        
    return 1



''' You are given N counters, initially set to 0, and you have two possible operations on them:

    increase(X) − counter X is increased by 1,
    max counter − all counters are set to the maximum value of any counter.
    A non-empty array A of M integers is given. This array represents consecutive operations:

    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
    For example, given integer N = 5 and array A such that:

        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the values of the counters after each consecutive operation will be:

        (0, 0, 1, 0, 0)
        (0, 0, 1, 1, 0)
        (0, 0, 1, 2, 0)
        (2, 2, 2, 2, 2)
        (3, 2, 2, 2, 2)
        (3, 2, 2, 3, 2)
        (3, 2, 2, 4, 2)
    The goal is to calculate the value of every counter after all operations.

    Write a function:

    def solution(N, A)

    that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

    Result array should be returned as an array of integers.
'''
def solution(N, A):
    counter_list = [0] * N
    max_value = 0

    for element in A:
        if element <= N:
            counter_list[element -1] += 1
            max_value = counter_list[element -1] if max_value < counter_list[element -1] else max_value

        else:
            counter_list = [max_value] * N

    return counter_list


# Faster
def solution(N, A):
    counter_base = 0
    counter_list = [counter_base] * N
    max_value = counter_base

    for element in A:
        if element <= N:
            if counter_list[element - 1] < counter_base:
                counter_list[element - 1] = counter_base

            counter_list[element - 1] += 1
            max_value = counter_list[element - 1] if max_value < counter_list[element - 1] else max_value

        else: 
            counter_base = max_value

    for i, counts in enumerate(counter_list):
        if counts < counter_base:
            counter_list[i] = counter_base

    return counter_list




''' Write a function:

    def solution(A)

    that, given an array A of N integers, returns the smallest positive integer (greater than 0) that 
    does not occur in A.

    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

    Given A = [1, 2, 3], the function should return 4.

    Given A = [−1, −3], the function should return 1.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def solution(A):
    max_element = max(A)
    positive_counter = [0] * (max_element+1)

    for element in A:
        if element > 0:
            positive_counter[element] += 1

    for element in range(1, max_element+1):
        if positive_counter[element] == 0:
            return element

    if max_element <= 0:
        return 1
    else:
        return max_element+1