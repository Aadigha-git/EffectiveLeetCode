def process_string(s):
    stack = []
    for char in s:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return "".join(stack)

def backspaceCompare(s, t):
    processed_s = process_string(s)
    processed_t = process_string(t)

    return processed_s == processed_t

s = "ab#c"
t = "ad#c"
result = backspaceCompare(s, t)
print(result)
