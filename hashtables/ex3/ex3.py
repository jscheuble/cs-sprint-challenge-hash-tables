def intersection(arrays):
    """
    YOUR CODE HERE

    create a cache and an empty list for result
    outer loop over larger array
        inner loop over inner array
            check if the number is not in the cache
                add number to the cache, set the value to 1
            else if it is in the cache
                increment the value

    loop over the cache
        if the value is equal to the length of the outer array,
            it exists in all arrays and we append this key to the result

    return the result
    """
    # Your code here
    cache = {}
    result = []

    for arr in arrays:
        for x in arr:
            if x not in cache:
                cache[x] = 1
            else:
                cache[x] += 1

    for key in cache:
        if cache[key] == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
