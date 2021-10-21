def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h_list = []
    for i in range(len(citations)):
        h = citations[i]
        left = len(citations[:i])+1
        right = len(citations[i:])
        if left >= h and right <= h:
            h_list.append(h)
    return h_list


solution([3, 0, 6, 1, 5])
