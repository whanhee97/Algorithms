# 프로그래머스 2018 KAKAO BLIND RECRUITMENT - 방금 그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    answer = ''
    answerList = []
    nMusicinfos = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace(
        'E#', 'e').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    for musicinfo in musicinfos:
        musicinfo = musicinfo.replace('C#', 'c').replace('D#', 'd').replace(
            'E#', 'e').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        nMusicinfos.append(musicinfo.split(','))
    # ["12:00","12:14","HELLO","CDEFGAB"]

    for i in range(len(nMusicinfos)):
        hour = int(nMusicinfos[i][1][0]+nMusicinfos[i][1][1]) - \
            int(nMusicinfos[i][0][0]+nMusicinfos[i][0][1])
        minute = int(nMusicinfos[i][1][3]+nMusicinfos[i][1][4]) - \
            int(nMusicinfos[i][0][3]+nMusicinfos[i][0][4])
        minute += (60*hour)
        nMusicinfos[i].append(str(minute))
        newSound = ''
        for j in range(int(nMusicinfos[i][4])):
            newSound += nMusicinfos[i][3][j % len(nMusicinfos[i][3])]
        nMusicinfos[i][3] = newSound
        nMusicinfos[i].append(str(len(nMusicinfos)-1-i))

        if m in nMusicinfos[i][3]:

            answerList.append(nMusicinfos[i][:])
    # ["12:00","12:14","HELLO","CDEFGAB","14","0"]
    # ['12:00', '12:14', 'HELLO', 'CDEFGABCDEFGAB', '14', "0"]

    if len(answerList) == 0:
        answer = '(None)'
    else:
        answerList.sort(key=lambda x: (int(x[4]), int(x[5])))
        answer = answerList[-1][2]

    return answer


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
