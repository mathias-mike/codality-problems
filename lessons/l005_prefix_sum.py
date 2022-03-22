# This is a technique that allows for fast calculation of the sum of elements of a given slice of an array
# E.g if we have an array [0, 1, 2, 3, 4, 5, 6]
# Prefix sum of the array [0, 1, 3, 6, 10, 15, 21]
#                         [a0, a0+a1, a0+a1+a2, a0+a1+a2+a3, a0+a1+a2+a3+a4, a0+a1+a2+a3+a4+a5, a0+a1+a2+a3+a4+a5+a6]

# Calculating prefix sum is O(n) 
def prefix_sum(A):
    n = len(A)
    P = [0] * n

    for i in range(1, n+1):
        P[i] = P[i-1] + A[i-1]
    
    return P


# Now witht he prefix sum, get the sum of a slice becomes easily O(1) complexity
# E.g: Say we want to find the totals of m slices from [x...y]
# We simply do {Py+1 - Px}
def total_sum_m(A, x, y):
    pref = prefix_sum(A)

    return pref[y+1] - pref[x]

A = [2, 4, 9, 3, 5, 3, 6, 7, 2, 6, 12]
prf = prefix_sum(A)
summ = total_sum_m(A, 2, 7)



''' Problem:
You are given a non-empty, zero-indexed array A of n (1 � n � 100 000) integers a0, a1, . . . , an−1 (0 � ai � 1 000). 
This array represents number of mushrooms growing on the consecutive spots along a road. You are also given integers k 
and m (0 � k, m < n). A mushroom picker is at spot number k on the road and should perform m moves. In one move she 
moves to an adjacent spot. She collects all the mushrooms growing on spots she visits. The goal is to calculate the 
maximum number of mushrooms that the mushroom picker can collect in m moves.
For example, consider array A such that:
2 3 7 5 1 3 9
0 1 2 3 4 5 6
The mushroom picker starts at spot k = 4 and should perform m = 6 moves. She might move to spots 3, 2, 3, 4, 5, 6 and 
thereby collect 1 + 5 + 7 + 3 + 9 = 25 mushrooms. This is the maximal number of mushrooms she can collect.
'''
def mushroom_picker(A, k, m):
    n = len(A)
    result = 0
    pref_sum = prefix_sum(A)

    for p in range(min(k, m) + 1):
        left_pos = k - p
        right_pos = min(n-1, k+m - 2*p)
        result = max(result, pref_sum[right_pos] - pref_sum[left_pos-1])
    for p in range(min(m+1, n-k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2*p)))
        result = max(result, pref_sum[right_pos] - pref_sum[left_pos-1])

    return result

"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""
def solution(A):
    n = len(A)
    p_sum = prefix_sum(A, n)

    pair_count = 0
    for i in range(n):
        if A[i] == 0:
            pair_count += p_sum[n-1] - p_sum[i]

    return pair_count if pair_count <= 1000000000 else -1

def prefix_sum(A, n):
    P = [0] * n

    P[0] = A[0]
    for i in range(1, n):
        P[i] = P[i-1] + A[i]

    return P


"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""
def solution(A, B, K):
    k_mod_B = B // K
    k_mod_A = A // K

    no_bet_BnA = k_mod_B - k_mod_A

    return no_bet_BnA if A%K != 0 else no_bet_BnA + 1 


"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P and Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
"""
def solution(S, P, Q):
    nu_types = {"A":1, "C":2, "G":3, "T":4}

    m = len(P)
    min_imp_fact_forq = []

    for i in range(m):
        min_imp_fact_range = nu_types[min(S[P[i]:Q[i]+1])]
        min_imp_fact_forq.append(min_imp_fact_range)

    return min_imp_fact_forq

# O(n**2) risky but worked 
def solution(S, P, Q):
    m = len(P)
    min_imp_fs = []

    for i in range(m):
        min_imp_in_range = S[P[i] : Q[i]+1]

        if "A" in min_imp_in_range:
            min_imp_fs.append(1)
        elif "C" in min_imp_in_range:
            min_imp_fs.append(2)
        elif "G" in min_imp_in_range:
            min_imp_fs.append(3)
        else:
            min_imp_fs.append(4)

    return min_imp_fs

# Optimal O(n + m)
def solution(S, P, Q):
    m = len(P)
    min_imp_fs = []

    p_sum = prefix_sum(S)

    for i in range(m):
        right = p_sum[Q[i]+1]
        left = p_sum[P[i]]

        count_a = right["A"] - left["A"]
        count_c = right["C"] - left["C"]
        count_g = right["G"] - left["G"]
        count_t = right["T"] - left["T"]

        if count_a > 0:
            min_imp_fs.append(1)
        elif count_c > 0:
            min_imp_fs.append(2)
        elif count_g > 0:
            min_imp_fs.append(3)
        elif count_t > 0:
            min_imp_fs.append(4)

    return min_imp_fs


def prefix_sum(S):
    n = len(S)

    P = [{"A":0, "C":0, "G":0, "T":0}]
    for i in range(1, n+1):
        prev_sum = P[i-1].copy()
        prev_sum[S[i-1]] += 1
        P.append(prev_sum)

    return P