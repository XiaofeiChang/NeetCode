"""
******* This question has note explanation in the folder [Notes for Questions - Queue_255] ********


******** BIlibili see 【队列模拟栈-哔哩哔哩】 https://b23.tv/vOdceUQ ******



Mirror Question: Stack 232





Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


"""


class MyStack:

    def __init__(self):
        # main queue
        self.queue1 = deque()
        # temp helper queue
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        # copy the previously pushed elements saved in queue1 to queue2 to reorder them correctly
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        # copy the entire queue2 to queue1, as queue1 is the main queue to return
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0

    # Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()