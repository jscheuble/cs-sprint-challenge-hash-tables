#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE

    create a cache and a route list full of empty slots
    iterate over list, cache all tickets. source as key, value as destination
    flight with key of None will be our starting flight
    loop over route list
        set route at index i to the value stored in our current flight variable
        set current to the cache value of current for our next destination
    """
    # Your code here
    cache = {}
    route = [None] * length

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    current = cache['NONE']

    for i in range(length):
        route[i] = current
        current = cache[current]

    return route
