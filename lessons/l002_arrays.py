# Reverse an array
def reverse_list(A):
    N = len(A)
    for i in range(N//2):
        k = N - 1 - i
        A[i], A[k] = A[k], A[i]
    return A


''' An array A consisting of N integers is given. Rotation of the array means that each element is 
    shifted right by one index, and the last element of the array is moved to the first place. 
    For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted 
    right by one index and 6 is moved to the first place).

    The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
'''
# O(n**2) time, O(1) space
def rotate_array_v0(A, k):
    N = len(A)
    if N > 0:
        for i in range(k):
            last_el = A[N-1]
            for j in range(N, 1, -1):
                A[j-1] = A[j-2]
            A[0] = last_el
    return A

# O(n) time, O(n) space
def rotate_array_v1(A, K):
    N = len(A)
    if N == 0 or N == K:
        return A
    
    if K > N: K = K % N
    if K == 0: return A

    new_arr = [0] * N
    i = K
    j = 0
    while i != K-1:
        new_arr[i] = A[j]
        i += 1
        j += 1

        if i == N: i = 0

    new_arr[i] = A[N-1]
    return new_arr

# O(n) time, O(n) space (But better than above)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        ret_str = ''
        for i in self:
            ret_str += i.value + ', '
        return ret_str.strip(', ')

    def enqueue(self, value):
        newNode = Node(value)
        if self.size == 0: 
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        
    def dequeue(self):
        value = None
        if self.size > 0:
            trash_node = self.head
            value = trash_node.value
            self.head = trash_node.next
            trash_node.next = None

            if not self.head:
                self.tail = None

            self.size -= 1

        return value

def rotate_array_v2(A, K):
    N = len(A)
    if N == 0 or N == K:
        return A
    
    if K > N: K = K % N
    if K == 0: return A

    myqueue = Queue()
    i = K
    j = 0
    while i != K-1:
        if j < K:
            myqueue.enqueue(A[i])
            A[i] = A[j]
            j += 1
        else:
            myqueue.enqueue(A[i])
            A[i] = myqueue.dequeue()

        i += 1
        if i == N: i = 0

    A[i] = myqueue.dequeue()
    return A


''' A non-empty array A consisting of N integers is given. The array contains an odd number of elements, 
    and each element of the array can be paired with another element that has the same value, except for 
    one element that is left unpaired.
    Write a function that, given an array A consisting of N integers fulfilling the above conditions, 
    returns the value of the unpaired element.
'''
def unpaired(A):
    # write your code in Python 3.6
    A_set = set()
    for i in A:
        if i in A_set:
            A_set.remove(i)
        else:
            A_set.add(i)

    return A_set.pop()