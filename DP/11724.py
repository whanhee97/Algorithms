# 백준 11724 - 연결요소의 개수
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int, input().split()) #n,m 입력받고 n=정점수, m=간선수
visited = [False for _ in range(n+1)] #visited 정점마다 false로 초기화
count = 0

adj =[[] for _ in range(n+1)] #정점의 개수만큼 리스트를 만들고(인접한거 표현하기 위해)
for _ in range(m): #각각 점들을 입력받아서 서로의 인접 리스트에 넣는다
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
def dfs(v) : 
    visited[v] = True #방문 체크하고
    for i in adj[v]: #해당 정점의 인접리스트의 노드들을 차례로 꺼내와
        if not visited[i]: #방문 검사를 하고 방문 안했으면 
            dfs(i) # 해당 노드 함수 실행
            
# 실행문
for j in range(1,n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)