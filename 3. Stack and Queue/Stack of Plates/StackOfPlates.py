"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
"""


class setofstacks(object):
    """doc"""

    maximum_stack = 5
    stacks = []
    active_stack = -1

    def push(self, ele: int) -> None:
        if self.active_stack == -1 or self.isactivefull():
            self.stacks.append([ele])
            self.active_stack += 1
        else:
            self.stacks[self.active_stack].append(ele)

    def pop(self) -> ValueError | int:
        if self.active_stack == -1:
            return ValueError("No Values in Stack.")
        ele = self.stacks[self.active_stack].pop()
        if self.isactiveempty():
            self.active_stack -= 1
        return ele

    def peek(self) -> ValueError | int:
        if self.active_stack == -1:
            return ValueError("No Values in Stack.")
        return self.stacks[self.active_stack][-1]

    def isactiveempty(self) -> bool:
        return len(self.stacks[self.active_stack]) <= 0

    def isactivefull(self) -> bool:
        return len(self.stacks[self.active_stack]) >= 5
