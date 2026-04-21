class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    # Safe pop operation
    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            removed_item = self.stack.pop()
            print(f"Popped: {removed_item}")
            return removed_item

    # Display stack
    def display(self):
        print("Stack:", self.stack)


s = Stack()

s.safe_pop()
s.push(10)
s.push(20)
s.push(30)

s.display()

s.safe_pop()
s.display()