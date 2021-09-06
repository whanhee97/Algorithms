def solution2(number, k):
    stack = []

    while number:
        if len(stack) == 0:
            stack.append(number[0])
            number = number[1:]
            continue

        if int(stack[-1]) < int(number[0]):
            while stack:
                if int(stack[-1]) >= int(number[0]):
                    break
                stack.pop()
                k -= 1
                if k == 0:
                    for n in number:
                        stack.append(n)
                    number = []
                    break
        else:
            stack.append(number[0])
            number = number[1:]
    if k > 0:
        for _ in range(k):
            stack.pop()
    return ''.join(stack)


def solution(number, k):
    stack = []
    for n in number:
        while stack and n > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(n)

    if k > 0:
        for _ in range(k):
            stack.pop()
    return ''.join(stack)


print(solution("4177252841", 4))
print(solution("77777", 1))
