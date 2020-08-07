# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE

    create cache and result list
    loop over files
        split file by slash, store the last index as key
        check if key is in cache,
            if it's not, add it to the cache and put the full path as the value

    loop over queries:
        if query is in cache,
            append value to results
    """
    # Your code here
    cache = {}
    result = []

    for x in files:
        split_file = x.split('/')
        key = split_file[-1]
        if key not in cache:
            cache[key] = x

    for q in queries:
        if q in cache:
            result.append(cache[q])

    return result


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    # print(finder(files, queries))
    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    result = finder(files, queries)
    print(result.sort())
