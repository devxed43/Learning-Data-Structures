# the iterative appraoch tripped me up but finally I understood that we update the value of first to move over to the second, and move second over one past the old second value to a "third"
# we keep track of 3 numbers at a time, shifting them all over by one each iteration of the loop
# finally when the loop is finished we return our third value
# it will loop starting from range of 2 to one passed our index --> index + 1
# I chose to target value at index 5,
# it adds up two values before value at index 5 as a result but it starts looping from the start
# 0 is my first base case, because index 0 is value 0 so we just return 0
# 1 is my second base case, becuase index 1 is value 1 so we just return 1
# index 2 is where the numbers begin to change

def iterative_fibonacci(index):
    first_number = 0
    second_number = 1

    if index == 0:
        return first_number

    if index == 1:
        return second_number

    for i in range(2, index + 1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return third_number


def recursive_fibonacci(n):
    if n < 2:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# fib = [0 1 1 2 3 5 8 13 21 34 55 89 144]


print('iterative fn:', iterative_fibonacci(5))
print('recursive fn:', recursive_fibonacci(7))
