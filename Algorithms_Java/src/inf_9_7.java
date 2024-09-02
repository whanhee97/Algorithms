import java.util.*;
class Road implements Comparable<Road>{
    int a;
    int b;
    int cost;
    public Road(int a, int b, int cost){
        this.a = a;
        this.b = b;
        this.cost = cost;
    }

    @Override
    public int compareTo(Road t){
        return this.cost - t.cost;
    }
}

class EdgeDist implements Comparable<EdgeDist>{
    int e,d;
    public EdgeDist(int e, int d){
        this.e = e;
        this.d = d;
    }
    @Override
    public int compareTo(EdgeDist t){
        return this.d - t.d;
    }
}

public class inf_9_7 {
    static int[] parents;
    static int[] visit;
    static ArrayList<ArrayList<int[]>> graph;

    public int find(int a){
        if(parents[a] == a) return a;
        else{
            return parents[a] = find(parents[a]);
        }
    }

    public void union(int a, int b){
        int pa = find(a);
        int pb = find(b);
        if(pa != pb) {
            parents[pa] = pb;
        }
    }

    public int solution(int v, int e, List<Road> roadList){
        parents = new int[v+1];
        Collections.sort(roadList);
        for(int i=1;i<=v;i++){
            parents[i] = i;
        }
        int total = 0;
        for(Road r : roadList){
            if(find(r.a) != find(r.b)){
                union(r.a,r.b);
                total += r.cost;
            }
        }
        return total;
    }


    public int solution2(int v, int e, List<Road> roadList){
        visit = new int[v+1];
        graph = new ArrayList<>();
        for(int i=0;i<=v;i++){
            graph.add(new ArrayList<>());
        }

        for(Road r:roadList){
            graph.get(r.a).add(new int[]{r.b,r.cost});
            graph.get(r.b).add(new int[]{r.a,r.cost});
        }
        int total = 0;
        PriorityQueue<EdgeDist> pq = new PriorityQueue<>();
        pq.offer(new EdgeDist(1,0));

        while(!pq.isEmpty()){
            if(Arrays.stream(visit).sum() == v) break;
            EdgeDist cur = pq.poll();
            int a = cur.e;
            int cost = cur.d;
            if(visit[a] == 0) {
                total += cost;
                visit[a] = 1;
            }
            for(int[] tmp: graph.get(a)){
                if(visit[tmp[0]] == 0){
                    pq.offer(new EdgeDist(tmp[0],tmp[1]));
                }
            }
        }

        return total;
    }

}
