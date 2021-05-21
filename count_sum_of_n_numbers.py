import numpy as np
import time


def sum_of_n_numbers(n):
    """Function counts the sum of N numbers

        Parameters:
        n (int): max number in range

        Returns:
            int: sum of numbers
    """
    # Generate range from 0 to N+1, because upper bound is not included in range function
    numbers = range(n+1)
    sum_numbers = np.sum(numbers)
    return sum_numbers


if __name__ == '__main__':
    N = int(input("Input a number: "))
    start_time = time.time()
    answer = sum_of_n_numbers(N)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Answer: "+str(answer))

