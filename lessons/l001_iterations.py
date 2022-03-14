# Given n, print a triangle like this
# * * * * * * *
#   * * * * *
#     * * *
#       *
def star_triangle(n, rotation):
    ''' For a given n
        n_rows: n
        stars: 2n-1
    '''
    max_stars = 2*n - 1
    triangle = ""

    if rotation == 0:
        for i in range(1, n+1):
            row_stars = 2*i - 1
            blanks = int((max_stars - row_stars)/2)

            row = "  "*blanks + "* "*row_stars
            triangle += "\n"+row

    else:
        for i in range(n, 0, -1):
            row_stars = 2*i - 1
            blanks = int((max_stars - row_stars)/2)

            row = "  "*blanks + "* "*row_stars
            triangle += "\n"+row
    

    return triangle

# Counting the number of digits in a given integer value
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count


# A list of the Fibonacci number not exceeding a given number n.
def get_fibonacci(n):
    fib_list = [0, 1]
    if n == 0:
        return 0
    else:
        position = 1 
        while fib_list[position] + fib_list[position-1] < n:
            fib_list.append(fib_list[position] + fib_list[position-1])
            position += 1

        return fib_list


# Return the maximum gap in the binary representation of an integer. 
# E.g 1041 = 10000010001
#     return 5
def binary_gap(N):
    n_binary = bin(N)[2:]

    b_gap = 0
    count = 0
    for i in n_binary:
        if i=='0':
            count += 1
        else:
            if count > b_gap: b_gap = count
            count = 0

    return b_gap

print(star_triangle(5, 0))