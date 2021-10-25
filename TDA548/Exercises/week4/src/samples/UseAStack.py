# package samples

from Stack import *


# * Using a Stack
# *
# * A Stack is very much like a list but we insert and remove from at specific
# * position called the "top" (= index 0)
# *
# * As with ArrayList, Java stacks are generic and we separate implementation and
# * interface (the specification)
# *
# * See: https:#en.wikipedia.org/wiki/Stack_(abstract_data_type)
# *
# * You don't need to learn all the methods by heart,
# * if allowed to use on exam you'll get a list.

def use_a_stack_program():
    # We could have used e.g. Collections.deque, but I want to showcase the
    # one we built in Stack.py
    stack = Stack()

    print(stack.is_empty())  # [ ]    (the empty stack)

    stack.push(1)  # [ 1 ] add on top (index 0)
    print(stack.peek())  # Just read
    stack.push(2)  # [ 2->1 ] add on top
    print(stack.peek())
    stack.push(3)  # [ 3->2->1->] add on top
    print(stack.peek())
    print(stack.size() == 3)  # true

    i: int = stack.pop()  # [ 2->1 ], remove 3 from top
    print(i == 3)
    print(stack.get_size() == 2)  # true

    stack.pop()  # [ 1 ], remove from top
    stack.pop()  # [ ], remove from top
    print(stack.is_empty())  # true

    stack.push(99)  # [ 99 ]
    stack.push(100)  # [ 100->99  ]

    stack.clear()  # [ ]
    print(stack.is_empty())  # true
