while True :
    words = input()
    stack = []

    if words == "." :
        break

    for word in words :
        if word == '[' or word == '(' :
            stack.append(word)
        elif word == ']' :
            if len(stack)!=0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif word == ')' :
            if len(stack)!=0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')