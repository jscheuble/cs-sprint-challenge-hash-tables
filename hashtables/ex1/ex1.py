def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE

    create a cache
    loop through the array of weights
        if the difference between limit and weight is in the cache already,
            we have found our answer and we return (current index, cache[limit - weight] to target the other index)
        put weight/index key value pair in the cache
    otherwise, return None because the pair we're looking for does not exist.
    """
    # Your code here
    cache = {}

    for i, weight in enumerate(weights):
        if limit - weight in cache:
            return (i, cache[limit - weight])
        cache[weight] = i

    return None
