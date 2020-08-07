def has_negatives(a):
    """
    YOUR CODE HERE

    create a cache and empty list for result
    loop over array
        check for value in cache
            if it's not there, add it
            check if the negative value is in the cache
                if true, append the absolute value to the result
    """
    # Your code here
    cache = {}
    result = []

    for x in a:
        if x not in cache and x != 0:
            cache[x] = x
            if -x in cache:
                result.append(abs(x))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
