class StackMaxItem:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, x):
        self.items.append(x)

        if not self.max_items or self.max_items[-1] <= x:
            self.max_items.append(x)

    def pop(self):
        if not self.items:
            return "error"

        popped = self.items.pop()

        if self.max_items[-1] == popped:
            self.max_items.pop()

        return popped

    def get_max(self):
        if not self.max_items:
            return "None"
        return self.max_items[-1]

    def top(self):
        if not self.items:
            return "error"
        return self.items[-1]
