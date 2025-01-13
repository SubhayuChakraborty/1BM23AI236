def is_balanced(s):
    matching_pairs = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != matching_pairs[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"
