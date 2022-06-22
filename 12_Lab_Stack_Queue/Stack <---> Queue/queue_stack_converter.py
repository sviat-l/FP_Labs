"""
Queue < -- > stack converter.
"""
from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def queue_to_stack(queue):
    """
    Return stack with initial queue's data
    """
    result_stack =ArrayStack()
    items = [data for data in queue]
    for i in range(len(items)-1, -1, -1):
        result_stack.push(items[i])
    return result_stack

def stack_to_queue(stack):
    """
    Return queue with initial stack's data
    """
    result_queue = ArrayQueue()
    items = [data for data in stack]
    for i in range(len(items)-1, -1, -1):
        result_queue.add(items[i])
    return result_queue
