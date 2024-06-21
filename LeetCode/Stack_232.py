"""
******* This question has note hint in the folder [Notes for Questions - Queue_255] ********


******** BIlibili see 【队列模拟栈-哔哩哔哩】 https://b23.tv/vOdceUQ ******


Mirror Question: Queue_225


Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.


Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""


class MyQueue:

    def __init__(self):
        # initialize the two stack
        self.stack1 = []  # main
        self.stack2 = []  # temp helper

    def push(self, x: int) -> None:
        # Step1: move all elems from main to helper in order to reorder them
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Step2: push a new item to helper
        self.stack2.append(x)

        # step3: move back all the elems from main to helper to finish reorder
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        # as we have reordered the 'stack' to match a 'queue' style, we could just return the top of main stack
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


"""
In Python, basic stack operations typically involve the following fundamental operations:

Push: Adds an element to the top of the stack.
Pop: Removes and returns the element from the top of the stack.
Peek or Top: Returns the element at the top of the stack without removing it.
isEmpty: Checks if the stack is empty.
Size: Returns the number of elements currently in the stack.




In Python, a stack and an array are not the same, although they can be related depending on how they are implemented or used.

Stack:
Definition: A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed.
Operations: Basic operations on a stack include push (adds an element to the top of the stack), pop (removes and returns the top element of the stack), peek (returns the top element without removing it), is_empty (checks if the stack is empty), and size (returns the number of elements in the stack).
Implementation: Stacks can be implemented using various underlying data structures, such as arrays or linked lists. In Python, a list (list type) is commonly used to implement a stack due to its dynamic resizing and efficient append/pop operations.



Array:
Definition: An array is a collection of elements stored in contiguous memory locations, where each element is accessed by its index. Arrays in Python are provided by the array module or can be created using lists (list type).
Operations: Arrays support random access to elements using indexing, slicing operations, and various methods to manipulate and iterate through elements.
Implementation: In Python, arrays (from the array module) are fixed in size and store elements of the same data type. On the other hand, lists (list type) are dynamic arrays that can grow or shrink in size as elements are added or removed.

"""

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()