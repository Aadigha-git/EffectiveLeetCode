class MyQueue:
    def __init__(self):
        self.stack_enqueue = []  # Stack for enqueue operations
        self.stack_dequeue = []  # Stack for dequeue operations

    def push(self, x):
        # Move all elements from stack_dequeue to stack_enqueue
        while self.stack_dequeue:
            self.stack_enqueue.append(self.stack_dequeue.pop())
        # Push the new element to stack_enqueue
        self.stack_enqueue.append(x)

    def pop(self):
        # Move all elements from stack_enqueue to stack_dequeue
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())
        # Pop the top element from stack_dequeue (which is the oldest element)
        return self.stack_dequeue.pop()

    def peek(self):
        # Move all elements from stack_enqueue to stack_dequeue
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())
        # Return the top element from stack_dequeue (which is the oldest element)
        return self.stack_dequeue[-1]

    def empty(self):
        # Check if both stacks are empty
        return not self.stack_enqueue and not self.stack_dequeue
queue = MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek())  
print(queue.pop())  
print(queue.empty())

queue.push(3)
print(queue.pop())  
print(queue.pop())
print(queue.empty())

"""
Question13:

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""
