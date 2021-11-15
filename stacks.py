stack = []

def check_stack():
    return len(stack)==0


def append_elements():
    stack.append("string1")
    return stack

def pop_stack():
    stack.append("string2")
    stack.append("string1")
    stack.pop()
    return stack


output = check_stack()
print(output)

