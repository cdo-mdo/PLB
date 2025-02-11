def simplifyPath(path: str) -> str:
    stack = []
    parts = path.split("/") # split by '/'

    for part in parts:
        if part == "..":
            if stack:
                stack.pop() # go back one directory
        elif part and part != '.': # ignore empty parts (from "//") and '.'
            stack.append(part)

    return '/' + '/'.join(stack) # construct the canonical path        
