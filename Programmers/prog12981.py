# Summer/Winter Coding(~2018) - 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    count = [0 for _ in range(n)]
    histories = set()
    for turn, word in enumerate(words):
        count[turn % n] += 1
        if turn >= 1 and words[turn-1][-1] != word[0] or word in histories:
            answer[0] = (turn % n)+1
            answer[1] = count[turn % n]
            return answer
        histories.add(word)
    answer = [0, 0]
    return answer


words = ["tank", "kick", "know", "wheel",
         "land", "dream", "mother", "robot", "tank"]
print(solution(3, words))
