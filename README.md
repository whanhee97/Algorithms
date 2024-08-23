# Algorithms

## DFS 기본

```java
import java.util.*;

public class Main {

    static int n;
    static int[] visit;
    static int[] arr;
    static String answer = "NO";

    public void DFS(int L){
        if(answer.equals("YES")) return;
        if(L == n){
            int a=0;
            int b=0;
            for(int i=0;i<visit.length;i++){
                if(visit[i] == 1){
                    a += arr[i];
                }else{
                    b += arr[i];
                }
            }
            if(a==b){
                answer = "YES";
            }
        }else{
            visit[L] = 1;
            DFS(L+1);
            visit[L] = 0;
            DFS(L+1);
        }
    }

    public static void main(String[] args) {

        Main T = new Main();
        Scanner kb = new Scanner(System.in);

        n = kb.nextInt();
        arr = new int[n];
        visit = new int[n];

        for(int i=0;i<n;i++){
            arr[i] = kb.nextInt();
        }

        T.DFS(0);

        System.out.println(answer);
        /*for(int x : solution(s,n,arr)){
            System.out.print(x + " ");
        }*/
    }
}
```

- 기본적으로 DFS문은 if-else로 작성(if엔 끝에 다 도착했을 때 처리)
- else엔 DFS()를 양쪽으로 진행 → 이진트리라 생각 하면 됨
- 부분집합의 합을 구하는 문제로 arr에 숫자를 다 받고 숫자들의 두 부분집합의 합이 같은게 있는지 여부 판단함
- DFS(0)부터 시작해서 arr[0]이 포함되면 visit[0]에 1체크하고 DFS(1)
- arr[0]이 포함 안 되면 visit[0]에 0체크하고 DFS(1) 이런식으로 양갈래길 진행
- visit를 안 쓰고 sum을 넣어줘서 total - sum == sum 으로 판별해도됨

```java
// 이런식으로 양갈래 진행
DFS(L+1,sum+arr[L])
DFS(L+1,sum)
```

## 순열 nPr

4P2 구한다 치면 4개중 2개 (순서상관있음)

1,2,3,4 중에 2개를 뽑아 나열

(1,2) (1,3) (1,4) (2,1) (2,3) (2,4) (3,1) (3,2) (3,4) (4,1) (4,2) (4,3)

```java
public static void dfs(int level){
    if(level==r){
        for(int x:per)
            System.out.print(x + " ");
        System.out.println();
    }else{
        for(int i=1;i<=n;i++){
            if(check[i]==0){
	            per[L]=i;
				      check[i]=1;
	            dfs(L+1);
	            check[i]=0;
            }
        }
    }
}

--main--
dfs(0);
```

## 조합 nCr

4C2 구한다 치면 4개중 2개 뽑기(순서상관없이)

dfs(0,1) 1 2 3 4

dfs(1,2) 2 3 4 dfs(1,3) 3 4 dfs(1,4) 4

dfs(2,3) dfs(2,4) dfs(2,4)

```java
public static void dfs(int level, int start){
    if(level==r){
        for(int x:combi)
            System.out.print(x + " ");
        System.out.println();
    }else{
        for(int i=start;i<=n;i++){
            combi[L]=i;
            dfs(L+1,i+1);
        }

    }
}
--main--
dfs(0,1);
```

## BFS 기본

```java
import java.util.*;

public class Main {
    int[] dir = {1,-1,5};

    public int solution(int s, int e){
        int answer = 0;
        int[] visit = new int[10001];

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {s,0}); // 시작, depth 0

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0];
            int depth = cur[1];

            if(x == e){
                return depth;
            }
            for(int dx:dir){
                if(x+dx>=1 && x+dx<10001 && visit[x+dx] != 1 ){
                    visit[x+dx] = 1; // 방문체크를 여기서 해줘야 시간복잡도 감소
                    q.offer(new int[] {x+dx,depth+1});
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {

        Main T = new Main();
        Scanner kb = new Scanner(System.in);

        int s = kb.nextInt();
        int e = kb.nextInt();

        System.out.println(T.solution(s,e));
        /*for(int x : solution(s,n,arr)){
            System.out.print(x + " ");
        }*/
    }
}
```

- 큐 선언 → Queue<int[]> q = new LinkedList<>();
- 큐 배열 집어 넣는 법 → q.offer(new int[] {x+dx,depth+1});
- 방문 배열 체크하는 위치 주의 → 현재 노드가 아니라 다음 노드를 체크 해줘야 함

```jsx
//두번째 방법 Level을 queue에 같이 안 넣고 싶을때
int L = 0;
while(!q.isEmpty()){
	int len = q.size();
	for(int i=0;i<len;i++){
		int now = q.poll();
		for(){
			if(조건){
				q.offer(xx);
			}
		}
	}
	L++;
}
```

## 기타

- String 같은거 비교할때 equals() 쓰기!!!
- String 에서 인덱스 접근 → char c = s.charAt(i);
- String 으로 for문 돌릴 때 → for(char c:s.toCharArray())
- 숫자인지 → Character.isDigit(c) , 문자인지 → Character.isAlphabetic(c)
- char to int → Character.getNumericValue(c)
- int to char → Character.forDigit(val, 진수);
- String to int → Integer.parseInt(tmp);
- int to String → String.valueOf(intValue1);
- 숫자만 추출 → String sNum = str.replaceAll("[A-Za-z]","");
- String에 해당하는 char 있는지 판단 → if(answer.indexOf(c) == -1)
- char 하나만 입력 받을 때 → char input2 = kb.next().charAt(0);
- Integer.MAX_VALUE Integer.MIN_VALUE

## 배열

- 배열 입력 받을 때
  - for(){ arr[i] = kb.nextInt(); }
  - 이중 배열일 경우 이중 for문 사용.
- 배열 정렬

```java
Arrays.sort(arr);
// 단, reverseOrder를 사용하는 경우 int가 아닌 Integer 배열을 사용해야함
// Integer[] arr = {1,2,3}
// or
// int[] ints = {13, 56, 32, 123, 61, 123, 1, 6};
// Integer[] tmpInts = Arrays.stream(ints).boxed().toArray(Integer[]::new);
Arrays.sort(arr, Collections.reverseOrder());
Arrays.sort(arr, Comparator.reverseOrder());
Arrays.sort(tmpInts, (a, b) -> b - a); // 람다식 사용

int[][] ints = {{1, 3}, {10, 5}, {33, 1}, {23, 11}};

// x값 정렬 (y는 a[1] - b[1])
Arrays.sort(ints, (a, b) -> a[0] - b[0]);

// x값 정렬 내림차순
Arrays.sort(ints, (a, b) -> b[0] - a[0]);

//[x, y]에서 x값에 의한 오름차순, x값이 같은 경우는 y값에 따라 내림차순
Arrays.sort(ints, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);

// 클래스 정렬하기
Class Body implements Comparable<Body>{
	public int h,w;
	Body(int h, int w){
		this.h = h;
		this.w = w;
	}
	@Override
	public int compareTo(Body o){
		return o.h - this.h; // h를 기준으로 내림차순
	}
}
// main
ArrayList<Body> arr = new Body(h,w);
Collections.sort(arr);
```

- 배열 합계 → Arrays.stream(arr).sum();
- 배열 최대 값 → Arrays.stream(arr).max().getAsInt();
- 배열 복사 → int[] tmp = arr.clone();\
- ArrayList → array

```java
ArrayList<Integer> arrList= new ArrayList<>();

int size = arrList.size();
int[] arr= new int[size];
for(int i=0;i<size;i++){
    arr[i] = arrList.get(i);
}
```

## Stack, Queue

- Stack<Integer> st= new Stack<>();
  - st.peek(), st.push(), st.pop()
- Queue<int[]> q = new LinkedList<>();
  - q.peek(), q.offer(), q.poll()

## Priority Queue

//낮은 숫자가 우선 순위인 int 형 우선순위 큐 선언

- PriorityQueue<Integer> priorityQueueLowest = new PriorityQueue<>();

//높은 숫자가 우선 순위인 int 형 우선순위 큐 선언

- PriorityQueue<Integer> priorityQueueHighest = new PriorityQueue<>(Collections.reverseOrder());

```java

// add(value) 메서드의 경우 만약 삽입에 성공하면 true를 반환,
// 큐에 여유 공간이 없어 삽입에 실패하면 IllegalStateException을 발생
priorityQueueLowest.add(1);
priorityQueueLowest.add(10);
priorityQueueLowest.offer(100);

priorityQueueHighest.add(1);
priorityQueueHighest.add(10);
priorityQueueHighest.offer(100)

// 첫번째 값을 반환하고 제거 비어있다면 null
priorityQueueLowest.poll();

// 첫번째 값 제거 비어있다면 예외 발생
priorityQueueLowest.remove();

// 첫번째 값을 반환만 하고 제거 하지는 않는다.
// 큐가 비어있다면 null을 반환
priorityQueueLowest.peek();

// 첫번째 값을 반환만 하고 제거 하지는 않는다.
// 큐가 비어있다면 예외 발생
priorityQueueLowest.element();

// 초기화
priorityQueueLowest.clear();
```

## Set

- Set<String> set = new HashSet<String>(); → 중복x 순서x
- Set<Integer> s = new TreeSet<>(Comparator.reverseOrder()); → 중복x 순서o
  - 기본은 오름차순
  - Comparator.reverseOrder() 내림차순

## Map

- Map<Character,Integer> hm = new HashMap<>();
- hm.put(k,v), hm.remove(k);
- 키값이 있는지 확인하면서 집어 넣기
  ```java
  for(int i=0;i<s2.length()-1;i++){
  	hm.put(키,hm.getOrDefault(키,0)+1);
  }
  // 키가 있으면 하나 증가시키고 없으면 키에다 1
  // hm.getOrDefault(키,0) -> 키에 해당하는 값을 가져오거나 0으로 초기화

  ```
- hashMap for문

```java
for(Integer i : map.keySet()){ //저장된 key값 확인
    System.out.println("[Key]:" + i + " [Value]:" + map.get(i));
}

for (Map.Entry<Integer, String> entry : map.entrySet()) {
    System.out.println("[Key]:" + entry.getKey() + " [Value]:" + entry.getValue());
}
```

- hm value로 정렬(람다 이용)
  - entrySet을 ArrayList로 변환
  - Collections.sort() 이용해서 두 번째 파람에 람다식

```java
List<Map.Entry<String,Integer>> entryList = new ArrayList<>(hm.entrySet());
Collections.sort(entryList, (a,b)-> hm.get(b.getKey()) - hm.get(a.getKey()));
```

## DP - 배낭 알고리즘

https://sskl660.tistory.com/88

# SQL 코테 대비

> SELECT - DISTINCT -FROM - JOIN - ON - WHERE - GROUP BY - HAVING - ORDER BY - LIMIT - OFFSET

## WITH 예시

```sql
WITH
MEMBERS_RANK AS(
	SELECT MEMBER_ID,COUNT(MEMBER_ID) CNT, RANK() OVER(ORDER BY COUNT(MEMBER_ID) DESC) AS RANK_A
  FROM REST_REVIEW
  GROUP BY MEMBER_ID
)
BEST_MEMBER_RANK1 AS(
    SELECT * FROM(
	    SELECT MEMBER_ID,COUNT(MEMBER_ID) CNT, RANK() OVER(ORDER BY COUNT(MEMBER_ID) DESC) AS RANK_A
	    FROM REST_REVIEW
	    GROUP BY MEMBER_ID
	  )X
    WHERE X.RANK_A = 1
),
```

## 재귀구현

- RECURSIVE 명시해주고
- 초기 값 세팅 후 UNION ALL로 묶어줌

```sql
WITH RECURSIVE RECUR AS(
    -- Non-Recursive 문장( 첫번째 루프에서만 실행됨 )
    SELECT 0 AS N
    UNION ALL
    -- Recursive 문장(읽어 올 때마다 행의 위치가 기억되어 다음번 읽어 올 때 다음 행으로 이동함)
    SELECT N + 1
    FROM RECUR
    WHERE N<23
)
```

## RANK() 함수

- RANK() OVER(ORDER BY COUNT(MEMBER_ID) DESC) AS RANK_A
- RANK를 조건절에 쓰려면 한 번 더 감싸서 써야함(가장 마지막에 집계되므로)

```sql
SELECT * FROM(
  SELECT MEMBER_ID,COUNT(MEMBER_ID) CNT, RANK() OVER(ORDER BY COUNT(MEMBER_ID) DESC) AS RANK_A
  FROM REST_REVIEW
  GROUP BY MEMBER_ID
)X
WHERE X.RANK_A = 1
```
